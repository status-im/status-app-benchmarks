import sys
import tempfile
import unittest
from pathlib import Path

TESTS = Path(__file__).resolve().parent
SCRIPTS = TESTS.parents[0] / 'scripts'
sys.path.insert(0, str(TESTS))
sys.path.insert(0, str(SCRIPTS))

from site_fixtures import PAGE  # noqa: E402
from site_generator import write_site  # noqa: E402


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
        self.assertIn('href="wallet-fresh.html"', html)
        self.assertIn('href="index.html">← Dashboard</a>', html)
        self.assertIn('User profiles', html)

    def test_profile_page_back_link_and_collapsed_scenarios(self):
        html = self._read('wallet-fresh.html')
        self.assertIn('href="profiles.html">← User profiles</a>', html)
        self.assertNotIn('<details class="scenario-charts" open', html)

    def test_legacy_summary_redirects_to_index(self):
        html = self._read('summary.html')
        self.assertIn('url=index.html', html)
        self.assertIn('href="index.html"', html)


if __name__ == '__main__':
    unittest.main()
