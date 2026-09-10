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
from benchmark_config import load_benchmark_config  # noqa: E402


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
        self.assertNotIn('href="data-usage.html"', html)
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


class DataUsagePageTests(unittest.TestCase):
    def test_data_usage_pages_have_total_waku_and_app_charts(self):
        config = load_benchmark_config(SCRIPTS / 'tests_config.toml')
        net_charts = [chart for chart in config.charts if chart.metrics_kind == 'net']
        self.assertEqual(len(net_charts), 8)
        slugs = {page.slug for page in config.pages}
        self.assertIn('data-usage-fresh', slugs)
        self.assertIn('data-usage-wallet-load-alex', slugs)
        self.assertNotIn('data-usage-wallet-load', slugs)
        self.assertNotIn('data-usage-community-member', slugs)
        by_id = {chart.test_id: chart for chart in net_charts}
        self.assertIn('test_data_usage_total_fresh', by_id)
        self.assertIn('test_data_usage_waku_fresh', by_id)
        self.assertIn('test_data_usage_https_fresh', by_id)
        self.assertIn('test_data_usage_other_fresh', by_id)
        total = by_id['test_data_usage_total_fresh']
        self.assertEqual(
            total.overlay_test_ids,
            (
                'test_data_usage_waku_fresh',
                'test_data_usage_https_fresh',
                'test_data_usage_other_fresh',
            ),
        )
        self.assertIn('Total = Waku + HTTPS + Other', total.description)
        self.assertIn('DiscV5 UDP peer discovery', total.description)
        self.assertIn('5 min window', total.footnote)
        self.assertIn('libp2p', by_id['test_data_usage_waku_fresh'].description)
        self.assertIn('status-go HTTP', by_id['test_data_usage_https_fresh'].description)
        self.assertIn('leftover after Waku and HTTPS: mostly DiscV5 UDP peer discovery', by_id['test_data_usage_other_fresh'].description)
        fresh_page = next(page for page in config.pages if page.slug == 'data-usage-fresh')
        self.assertEqual(fresh_page.test_ids, ('test_data_usage_total_fresh',))
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            write_site(output, config.pages, {}, chart_tests=config.charts)
            html = (output / 'data-usage-fresh.html').read_text(encoding='utf-8')
            index = (output / 'index.html').read_text(encoding='utf-8')
            profiles = (output / 'profiles.html').read_text(encoding='utf-8')
            usage = (output / 'data-usage.html').read_text(encoding='utf-8')
        self.assertIn('<h2>Data usage</h2>', html)
        self.assertIn('href="data-usage.html">← Data usage</a>', html)
        self.assertIn('href="data-usage.html">Data usage →</a>', index)
        self.assertIn('<h2 class="summary-heading">Data usage</h2>', index)
        self.assertIn('Data usage', html)
        self.assertNotIn('<h2>Total</h2>', html)
        self.assertNotIn('<h2>Waku</h2>', html)
        self.assertNotIn('<h2>Status app</h2>', html)
        self.assertNotIn('<section class="area-group"><h2>Wallet</h2>', html)
        self.assertNotIn('<section class="area-group"><h2>Messenger</h2>', html)
        self.assertNotIn('<section class="area-group"><h2>Communities</h2>', html)
        self.assertNotIn('<section class="area-group"><h2>Browser</h2>', html)
        self.assertNotIn('class="profile-detail-section stat-messenger"', html)
        self.assertNotIn('class="profile-detail-section stat-communities"', html)
        self.assertNotIn('Wallet landing data usage', html)
        self.assertNotIn('Collectibles landing data usage', html)
        self.assertNotIn('Messenger landing data usage', html)
        self.assertNotIn('Discover landing data usage', html)
        self.assertNotIn('Status community data usage', html)
        self.assertNotIn('Home landing data usage', html)
        self.assertNotIn('Session total data usage', html)
        self.assertIn('From login through 5 min after Wallet', html)
        self.assertIn('DiscV5 UDP peer discovery', html)
        self.assertIn('class="chart-footnote"', html)
        self.assertIn('Data usage (new user)', html)
        self.assertIn('Data usage (new user)', index)
        self.assertIn('Data usage (heavy account from Alex)', index)
        self.assertNotIn('Data usage (semi-heavy wallet)', index)
        self.assertNotIn('Data usage (Status community member)', index)
        self.assertNotIn('href="data-usage-fresh.html"', profiles)
        self.assertNotIn('href="data-usage-wallet-load-alex.html"', profiles)
        self.assertIn('href="data-usage-fresh.html"', usage)
        self.assertIn('href="data-usage-wallet-load-alex.html"', usage)
        self.assertNotIn('href="data-usage-wallet-load.html"', usage)
        self.assertNotIn('href="data-usage-community-member.html"', usage)

    def test_data_usage_page_renders_hosts_table(self):
        config = load_benchmark_config(SCRIPTS / 'tests_config.toml')
        hosts = {
            'test_data_usage_total_fresh': {
                'https': [{'host': 'prod.market.status.im', 'mb': 12.5}],
            },
        }
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            write_site(
                output, config.pages, {},
                chart_tests=config.charts,
                hosts_by_test_id=hosts,
            )
            html = (output / 'data-usage-fresh.html').read_text(encoding='utf-8')
        self.assertIn('Latest run hosts', html)
        self.assertIn('prod.market.status.im', html)
        self.assertIn('12.50 MB', html)


if __name__ == '__main__':
    unittest.main()
