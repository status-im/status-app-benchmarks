import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

TESTS = Path(__file__).resolve().parent
SCRIPTS = TESTS.parents[0] / 'scripts'
sys.path.insert(0, str(TESTS))
sys.path.insert(0, str(SCRIPTS))

from site_fixtures import PAGE  # noqa: E402
from site_generator import write_site  # noqa: E402
from benchmark_config import ChartTest  # noqa: E402
from regression_report import ScenarioSummary  # noqa: E402


class SiteNavigationTests(unittest.TestCase):
    def setUp(self):
        self._temp = tempfile.TemporaryDirectory()
        self.output = Path(self._temp.name)
        write_site(self.output, (PAGE,), {})

    def tearDown(self):
        self._temp.cleanup()

    def _read(self, name: str) -> str:
        return (self.output / name).read_text(encoding='utf-8')

    def test_index_links_to_profiles_not_summary(self):
        html = self._read('index.html')
        self.assertIn('href="profiles.html">User profiles →</a>', html)
        self.assertIn('href="send-timing.html">Send timing →</a>', html)
        self.assertIn('<h2 class="summary-heading">Test scenarios</h2>', html)
        self.assertIn('class="summary-legend"', html)
        self.assertIn('Near ok · 0.9–1.0s', html)
        self.assertIn('compares the latest load time with the 2.38.0 release', html)
        self.assertNotIn('Wallet tab scenarios skip', html)
        self.assertNotIn('href="summary.html">View scenario summary', html)
        self.assertNotIn('class="card"', html)
        self.assertNotIn('vs nightly', html)

    def test_index_scenarios_are_collapsed(self):
        html = self._read('index.html')
        self.assertIn('<details class="summary-profile">', html)
        self.assertNotIn('<details class="summary-profile" open', html)
        self.assertIn('New user profile', html)

    def test_profiles_page_has_cards(self):
        html = self._read('profiles.html')
        self.assertIn('class="card"', html)
        self.assertIn('href="fresh-profile.html"', html)
        self.assertIn('href="index.html">← Dashboard</a>', html)
        self.assertIn('User profiles', html)

    def test_profile_page_back_link_and_collapsed_scenarios(self):
        html = self._read('fresh-profile.html')
        self.assertIn('href="profiles.html">← User profiles</a>', html)
        self.assertNotIn('<details class="scenario-charts" open', html)

    def test_send_timing_page_empty_without_charts(self):
        html = self._read('send-timing.html')
        self.assertIn('href="index.html">← Dashboard</a>', html)
        self.assertIn('Send timing', html)
        self.assertIn('No send-timing results in the current chart window.', html)

    def test_send_timing_table_uses_latest_summaries(self):
        sent = ChartTest(
            test_id='test_group_chat_plain_text_sent_time',
            display_name='Time to Sent after sending 1000-character text in a 3-person group',
            graph_filename='group_chat_plain_text_sent_time.png',
            pattern='test_group_chat_plain_text_sent',
            ylabel='seconds',
            value_column='avg_time',
            metrics_kind='performance',
            attachment_keyword='load time',
            area='messenger',
            source_pattern='test_group_chat_send_message_timing',
        )
        delivered = ChartTest(
            test_id='test_group_chat_plain_text_delivered_time',
            display_name='Time to Delivered after sending 1000-character text in a 3-person group',
            graph_filename='group_chat_plain_text_delivered_time.png',
            pattern='test_group_chat_plain_text_delivered',
            ylabel='seconds',
            value_column='avg_time',
            metrics_kind='performance',
            attachment_keyword='load time',
            area='messenger',
            source_pattern='test_group_chat_send_message_timing',
        )
        page = replace(PAGE, test_ids=(sent.test_id, delivered.test_id))
        write_site(
            self.output,
            (page,),
            {},
            chart_tests=(sent, delivered),
            summaries={
                sent.test_id: ScenarioSummary(
                    test_id=sent.test_id,
                    value=1.089,
                    commit_hash='39901f54d',
                    date='2026-09-21 10:40',
                    speed_status='slow',
                    vs_reference='—',
                    detail='Latest value',
                ),
                delivered.test_id: ScenarioSummary(
                    test_id=delivered.test_id,
                    value=3.368,
                    commit_hash='39901f54d',
                    date='2026-09-21 10:40',
                    speed_status='slow',
                    vs_reference='—',
                    detail='Latest value',
                ),
            },
        )
        html = self._read('send-timing.html')
        self.assertIn('Group chat', html)
        self.assertIn('1000-character text in a 3-person group', html)
        self.assertIn('1.089s', html)
        self.assertIn('3.368s', html)
        self.assertIn('39901f54d', html)
        self.assertIn('2026-09-21 10:40', html)
        self.assertIn('href="fresh-profile.html#test_group_chat_plain_text_sent_time"', html)
        readme = self._read('README.md')
        self.assertIn('## Send timing', readme)
        self.assertIn('[send-timing.html](send-timing.html)', readme)

    def test_legacy_summary_redirects_to_index(self):
        html = self._read('summary.html')
        self.assertIn('url=index.html', html)
        self.assertIn('href="index.html"', html)


if __name__ == '__main__':
    unittest.main()
