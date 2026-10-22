import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, call, patch
from urllib.error import HTTPError, URLError

import update_scholar as scholar


PROFILE_HTML = f"""
<div id="gsc_prf_in">Zhongxiang Sun</div>
<table id="gsc_rsb_st"><tr>
  <td class="gsc_rsb_std">100</td><td class="gsc_rsb_std">90</td>
  <td class="gsc_rsb_std">2</td><td class="gsc_rsb_std">2</td>
  <td class="gsc_rsb_std">2</td><td class="gsc_rsb_std">2</td>
</tr></table>
<table><tr class="gsc_a_tr">
  <td><a class="gsc_a_at" href="/citations?citation_for_view={scholar.PROFILE_ID}:paper1">First test paper</a></td>
  <td><a class="gsc_a_ac">80</a></td>
</tr><tr class="gsc_a_tr">
  <td><a class="gsc_a_at" href="/citations?citation_for_view={scholar.PROFILE_ID}:paper2">Second test paper</a></td>
  <td><a class="gsc_a_ac">20</a></td>
</tr></table>
<button id="gsc_bpf_more" disabled>More</button>
"""


def http_error(code=403, headers=None):
    return HTTPError(scholar.PROFILE_URL, code, "Test HTTP error", headers or {}, None)


def response(html=PROFILE_HTML):
    result = Mock()
    result.__enter__ = Mock(return_value=result)
    result.__exit__ = Mock(return_value=False)
    result.headers.get_content_charset.return_value = "utf-8"
    result.read.return_value = html.encode()
    return result


class ScholarRefreshTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.output = self.root / "scholar.json"
        self.summary = self.root / "summary.md"
        self.outputs = self.root / "outputs.txt"
        self.snapshot = scholar.parse_profile(PROFILE_HTML)
        self.snapshot["updated_at"] = "2026-10-01T00:00:00+00:00"
        self.original = json.dumps(self.snapshot).encode()
        self.output.write_bytes(self.original)
        self.environment = patch.dict(os.environ, {
            "GITHUB_OUTPUT": str(self.outputs),
            "GITHUB_STEP_SUMMARY": str(self.summary),
        })
        self.environment.start()
        self.addCleanup(self.environment.stop)

    def run_cli(self, *args):
        with patch("sys.argv", ["update_scholar.py", "--output", str(self.output), *args]):
            with patch("sys.stdout", new_callable=io.StringIO), patch("sys.stderr", new_callable=io.StringIO):
                return scholar.main()

    @patch("time.sleep")
    @patch.object(scholar, "urlopen")
    def test_retries_403_before_failing_in_strict_mode(self, request, sleep):
        request.side_effect = [http_error(), http_error(), http_error()]
        self.assertEqual(self.run_cli(), 1)
        self.assertEqual(request.call_count, 3)
        self.assertEqual(sleep.call_args_list, [call(20), call(60)])
        self.assertEqual(self.output.read_bytes(), self.original)

    @patch("time.sleep")
    @patch.object(scholar, "urlopen")
    def test_blocked_refresh_reports_stale_without_rewriting_data(self, request, sleep):
        request.side_effect = [http_error(), http_error(), http_error()]
        self.assertEqual(self.run_cli("--allow-stale"), 0)
        self.assertEqual(self.output.read_bytes(), self.original)
        self.assertIn("status=stale\n", self.outputs.read_text())
        self.assertIn(self.snapshot["updated_at"], self.summary.read_text())
        self.assertIn("not updated", self.summary.read_text())
        self.assertFalse(self.output.with_suffix(".json.tmp").exists())

    @patch("time.sleep")
    @patch.object(scholar, "urlopen")
    def test_retry_recovers_and_publishes_verified_data(self, request, sleep):
        request.side_effect = [http_error(), response()]
        self.assertEqual(self.run_cli("--allow-stale"), 0)
        self.assertEqual(request.call_count, 2)
        updated = json.loads(self.output.read_text())
        self.assertEqual(updated["citations"], 100)
        self.assertEqual(len(updated["papers"]), 2)
        self.assertNotEqual(updated["updated_at"], self.snapshot["updated_at"])
        self.assertIn("status=updated\n", self.outputs.read_text())

    @patch("time.sleep")
    @patch.object(scholar, "urlopen")
    def test_non_retryable_http_errors_still_fail(self, request, sleep):
        request.side_effect = http_error(404)
        self.assertEqual(self.run_cli("--allow-stale"), 1)
        self.assertEqual(request.call_count, 1)
        sleep.assert_not_called()
        self.assertEqual(self.output.read_bytes(), self.original)

    @patch.object(scholar, "urlopen")
    def test_invalid_html_is_not_treated_as_a_successful_fallback(self, request):
        request.return_value = response("<html>Unexpected response or CAPTCHA</html>")
        self.assertEqual(self.run_cli("--allow-stale"), 1)
        self.assertIn("status=failed\n", self.outputs.read_text())
        self.assertEqual(self.output.read_bytes(), self.original)

    @patch("time.sleep")
    @patch.object(scholar, "urlopen")
    def test_unavailable_without_a_valid_snapshot_still_fails(self, request, sleep):
        for contents in (None, b"invalid json", b'{"profile_id":"somebody-else"}'):
            with self.subTest(contents=contents):
                if contents is None:
                    self.output.unlink(missing_ok=True)
                else:
                    self.output.write_bytes(contents)
                request.side_effect = [http_error(), http_error(), http_error()]
                self.assertEqual(self.run_cli("--allow-stale"), 1)
                if contents is None:
                    self.assertFalse(self.output.exists())
                else:
                    self.assertEqual(self.output.read_bytes(), contents)

    @patch("time.sleep")
    @patch.object(scholar, "urlopen")
    def test_network_errors_use_the_same_bounded_fallback(self, request, sleep):
        request.side_effect = URLError("temporary network failure")
        self.assertEqual(self.run_cli("--allow-stale"), 0)
        self.assertEqual(request.call_count, 3)
        self.assertEqual(self.output.read_bytes(), self.original)

    @patch("time.sleep")
    @patch.object(scholar, "urlopen")
    def test_long_retry_after_is_respected_without_excessive_requests(self, request, sleep):
        request.side_effect = http_error(429, {"Retry-After": "3600"})
        self.assertEqual(self.run_cli("--allow-stale"), 0)
        self.assertEqual(request.call_count, 1)
        sleep.assert_not_called()
        self.assertEqual(self.output.read_bytes(), self.original)

    @patch.object(scholar, "urlopen")
    def test_saved_html_can_still_be_verified_offline(self, request):
        source = self.root / "profile.html"
        source.write_text(PROFILE_HTML)
        self.assertEqual(self.run_cli("--input-html", str(source)), 0)
        request.assert_not_called()
        self.assertIn("status=updated\n", self.outputs.read_text())


if __name__ == "__main__":
    unittest.main()
