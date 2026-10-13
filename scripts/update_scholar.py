#!/usr/bin/env python3
"""Refresh the public Scholar snapshot; leave the last good data on failure."""

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urljoin, urlparse
from urllib.request import Request, urlopen


PROFILE_ID = "4n5whr0AAAAJ"
PROFILE_URL = f"https://scholar.google.com/citations?user={PROFILE_ID}&hl=en"
OUTPUT = Path(__file__).resolve().parents[1] / "_data" / "scholar.json"
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


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
    args = cli.parse_args()
    try:
        if args.input_html:
            raw = args.input_html.read_bytes()
            try:
                html = raw.decode("utf-8")
            except UnicodeDecodeError:
                html = raw.decode("iso-8859-1")
        else:
            request = Request(PROFILE_URL + "&pagesize=100", headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en"})
            with urlopen(request, timeout=30) as response:
                html = response.read().decode(response.headers.get_content_charset() or "utf-8")
        snapshot = parse_profile(html)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        temporary = args.output.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(args.output)
    except Exception as error:
        print(f"Scholar refresh failed: {error}. Previous data was not changed.", file=sys.stderr)
        return 1
    print(f"Scholar verified: {snapshot['citations']} citations, h-index {snapshot['h_index']}, {len(snapshot['papers'])} records.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
