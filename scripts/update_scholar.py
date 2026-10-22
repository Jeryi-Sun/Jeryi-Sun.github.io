#!/usr/bin/env python3
"""Refresh the public Scholar snapshot; leave the last good data on failure."""

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urljoin, urlparse
from urllib.request import Request, urlopen


PROFILE_ID = "4n5whr0AAAAJ"
PROFILE_URL = f"https://scholar.google.com/citations?user={PROFILE_ID}&hl=en"
OUTPUT = Path(__file__).resolve().parents[1] / "_data" / "scholar.json"
RETRY_DELAYS = (20, 60)
RETRYABLE_HTTP = {403, 429, 500, 502, 503, 504}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class ScholarUnavailable(RuntimeError):
    """The public profile could not be fetched after bounded retries."""


def fetch_profile():
    request = Request(PROFILE_URL + "&pagesize=100", headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en"})
    for attempt in range(len(RETRY_DELAYS) + 1):
        retry_after = None
        try:
            with urlopen(request, timeout=30) as response:
                return response.read().decode(response.headers.get_content_charset() or "utf-8")
        except HTTPError as error:
            if error.code not in RETRYABLE_HTTP:
                raise
            reason = f"HTTP {error.code}"
            retry_after = error.headers.get("Retry-After") if error.headers else None
            error.close()
        except (URLError, TimeoutError) as error:
            reason = str(error)
        if attempt == len(RETRY_DELAYS):
            break
        delay = RETRY_DELAYS[attempt]
        if retry_after:
            try:
                wait = float(retry_after)
            except ValueError:
                try:
                    wait = (parsedate_to_datetime(retry_after) - datetime.now(timezone.utc)).total_seconds()
                except (ValueError, TypeError, OverflowError):
                    wait = 0
            if wait > max(RETRY_DELAYS):
                break
            delay = max(delay, wait)
        print(f"Scholar request {attempt + 1} unavailable ({reason}); retrying in {delay:g}s.", flush=True)
        time.sleep(delay)
    raise ScholarUnavailable(f"{reason}; profile fetch stopped after {attempt + 1} attempt(s)")


def verified_cache(output):
    try:
        snapshot = json.loads(output.read_text(encoding="utf-8"))
        updated = datetime.fromisoformat(snapshot["updated_at"])
        metrics = [snapshot[key] for key in ("citations", "h_index", "i10_index")]
        papers = snapshot["papers"]
        valid_papers = isinstance(papers, list) and papers and all(
            isinstance(paper, dict) and paper.get("id") and paper.get("title")
            and type(paper.get("citations")) is int and paper["citations"] >= 0
            for paper in papers
        )
        if (snapshot["profile_id"] != PROFILE_ID or not updated.tzinfo
                or not all(type(value) is int and value >= 0 for value in metrics)
                or metrics[0] <= 0 or not valid_papers
                or max(metrics[1:]) > len(papers)):
            return None
        return snapshot
    except (OSError, KeyError, TypeError, ValueError):
        return None


def report_result(status, message, snapshot=None):
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
            output.write(f"status={status}\n")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as summary:
            summary.write(f"## Google Scholar refresh\n\n**Result: {status}**\n\n{message}\n\n")
            if snapshot:
                summary.write(f"Last verified: `{snapshot['updated_at']}`\n\n")
                summary.write(f"{snapshot['citations']} citations; h-index {snapshot['h_index']}; {len(snapshot['papers'])} papers.\n")


@dataclass
class Element:
    tag: str
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)

    def text(self):
        return "".join(item.text() if isinstance(item, Element) else item for item in self.children).strip()

    def find_all(self, *, css_class=None, element_id=None):
        matches = []
        if (css_class and css_class in self.attrs.get("class", "").split()) or (element_id and self.attrs.get("id") == element_id):
            matches.append(self)
        for child in self.children:
            if isinstance(child, Element):
                matches.extend(child.find_all(css_class=css_class, element_id=element_id))
        return matches


class ScholarHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Element("document")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Element(tag, dict(attrs))
        self.stack[-1].children.append(node)
        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                self.stack = self.stack[:index]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def number(text):
    digits = "".join(char for char in text if char.isdecimal())
    return int(digits) if digits else 0


def parse_profile(html):
    parser = ScholarHTML()
    parser.feed(html)
    root = parser.root
    names = root.find_all(element_id="gsc_prf_in")
    metrics_tables = root.find_all(element_id="gsc_rsb_st")
    if not names or "zhongxiang" not in names[0].text().lower() or not metrics_tables:
        raise ValueError("Scholar did not return Zhongxiang Sun's public profile (possibly a block or CAPTCHA).")
    metrics = metrics_tables[0].find_all(css_class="gsc_rsb_std")
    if len(metrics) != 6 or any(not item.text().strip().isdigit() for item in metrics):
        raise ValueError("Scholar metric markup changed; keeping the last verified snapshot.")
    totals = [number(item.text()) for item in metrics]
    papers = []
    for row in root.find_all(css_class="gsc_a_tr"):
        titles = row.find_all(css_class="gsc_a_at")
        citations = row.find_all(css_class="gsc_a_ac")
        if not titles or not citations:
            raise ValueError("Incomplete Scholar publication row.")
        url = urljoin(PROFILE_URL, titles[0].attrs.get("href", ""))
        record = parse_qs(urlparse(url).query).get("citation_for_view", [""])[0]
        if not record.startswith(PROFILE_ID + ":"):
            raise ValueError("Unexpected Scholar publication identity.")
        papers.append({
            "id": record.split(":", 1)[1],
            "title": titles[0].text(),
            "citations": number(citations[0].text()),
            "url": url,
        })
    if not papers or totals[0] <= 0 or totals[2] > len(papers) or totals[4] > len(papers):
        raise ValueError("Incomplete Scholar profile; keeping the last verified snapshot.")
    more = root.find_all(element_id="gsc_bpf_more")
    if more and "disabled" not in more[0].attrs:
        raise ValueError("Profile exceeds the fetched page; increase pagesize before replacing the snapshot.")
    return {
        "profile_id": PROFILE_ID,
        "profile_url": PROFILE_URL,
        "name": names[0].text(),
        "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "citations": totals[0],
        "h_index": totals[2],
        "i10_index": totals[4],
        "papers": papers,
    }


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--input-html", type=Path, help="Parse a saved public-profile response for verification.")
    cli.add_argument("--output", type=Path, default=OUTPUT)
    cli.add_argument("--allow-stale", action="store_true", help="Report temporary fetch failures as stale only when a verified snapshot is available.")
    args = cli.parse_args()
    try:
        if args.input_html:
            raw = args.input_html.read_bytes()
            try:
                html = raw.decode("utf-8")
            except UnicodeDecodeError:
                html = raw.decode("iso-8859-1")
        else:
            try:
                html = fetch_profile()
            except ScholarUnavailable as error:
                cached = verified_cache(args.output) if args.allow_stale else None
                if cached is None:
                    raise
                print(f"Scholar remains unavailable: {error}.", file=sys.stderr)
                message = "Google Scholar was unavailable; data was not updated. The previous verified snapshot and its original timestamp were retained."
                print(f"::warning::{message}")
                report_result("stale", message, cached)
                return 0
        snapshot = parse_profile(html)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        temporary = args.output.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(args.output)
    except Exception as error:
        print(f"Scholar refresh failed: {error}. Previous data was not changed.", file=sys.stderr)
        report_result("failed", "Refresh failed. No snapshot was published; see the fetch or validation error in the log.")
        return 1
    report_result("updated", "Successfully fetched and verified the public Scholar profile.", snapshot)
    print(f"Scholar verified: {snapshot['citations']} citations, h-index {snapshot['h_index']}, {len(snapshot['papers'])} records.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
