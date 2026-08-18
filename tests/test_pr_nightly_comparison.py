import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

TESTS = Path(__file__).resolve().parent
SCRIPTS = TESTS.parents[0] / 'scripts'
sys.path.insert(0, str(TESTS))
sys.path.insert(0, str(SCRIPTS))

from regression_report import comparison_label  # noqa: E402
from site_fixtures import PAGE  # noqa: E402
from site_generator import (  # noqa: E402
    nightly_comparison_header,
    pr_page_heading,
    resolve_pr_title,
    write_site,
)


class NightlyComparisonTests(unittest.TestCase):
    def test_parity_within_fifteen_percent(self):
        self.assertEqual(comparison_label(1.0, 1.0, 0.15), 'parity')
        self.assertEqual(comparison_label(1.10, 1.0, 0.15), 'parity')
        self.assertEqual(comparison_label(1.15, 1.0, 0.15), 'parity')

    def test_slower_and_faster_deltas(self):
        self.assertEqual(comparison_label(1.20, 1.0, 0.15), '+0.200s')
        self.assertEqual(comparison_label(0.80, 1.0, 0.15), '-0.200s')

    def test_nightly_page_omits_vs_nightly_column(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            write_site(output, (PAGE,), {}, channel='nightly')
            html = (output / 'index.html').read_text(encoding='utf-8')
            self.assertIn('vs 2.38.0', html)
            self.assertNotIn('vs nightly', html)

    def test_pr_page_includes_vs_nightly_column(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            write_site(output, (PAGE,), {}, channel='pr')
            html = (output / 'index.html').read_text(encoding='utf-8')
            self.assertIn('vs 2.38.0', html)
            self.assertIn('vs nightly', html)
            self.assertIn('at the time this PR was measured', html)
            self.assertNotIn('updates when nightly republishes', html)

    def test_pr_page_shows_which_nightly_by_date(self):
        label, title, name = nightly_comparison_header(pd.DataFrame([{
            'date': '2026-08-17T04:00:00',
            'commit_hash': '27614460fabcdef',
        }]))
        self.assertEqual(label, 'vs nightly · Aug 17, 2026')
        self.assertIn('Aug 17, 2026', title)
        self.assertIn('27614460f', title)
        self.assertEqual(name, 'nightly Aug 17, 2026')
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            write_site(
                output, (PAGE,), {}, channel='pr',
                nightly_baseline_label=label,
                nightly_baseline_title=title,
                nightly_baseline_name=name,
            )
            html = (output / 'index.html').read_text(encoding='utf-8')
            self.assertIn('vs nightly · Aug 17, 2026', html)
            self.assertIn('class="column-date">Aug 17, 2026</span>', html)
            self.assertIn('nightly-column', html)
            self.assertIn('Difference from nightly Aug 17, 2026', html)
            readme = (output / 'README.md').read_text(encoding='utf-8')
            self.assertIn('vs nightly · Aug 17, 2026', readme)

    def test_pr_heading_uses_number_and_title(self):
        self.assertEqual(
            pr_page_heading('21890', 'Enable loading skeletons'),
            '#21890 Enable loading skeletons',
        )
        self.assertEqual(pr_page_heading('21890'), '#21890')
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / '21890'
            write_site(
                output, (PAGE,), {}, channel='pr',
                pr_title='Enable loading skeletons',
            )
            html = (output / 'index.html').read_text(encoding='utf-8')
            self.assertIn('class="pr-title"', html)
            self.assertIn('Enable loading skeletons', html)
            self.assertIn(
                'https://github.com/status-im/status-app/pull/21890',
                html,
            )
            self.assertNotIn('Windows Pull Request Benchmarks', html)
            profiles = (output / 'profiles.html').read_text(encoding='utf-8')
            self.assertIn('class="pr-title"', profiles)
            self.assertIn('Enable loading skeletons', profiles)
            self.assertIn(
                'https://github.com/status-im/status-app/pull/21890',
                profiles,
            )
            self.assertNotIn('<h1>User profiles</h1>', profiles)
            profile_page = (output / 'wallet-fresh.html').read_text(encoding='utf-8')
            self.assertIn('class="pr-title"', profile_page)
            self.assertIn('Enable loading skeletons', profile_page)
            self.assertIn(
                'https://github.com/status-im/status-app/pull/21890',
                profile_page,
            )
            self.assertIn('class="profile-page-name">New user profile</h2>', profile_page)
            self.assertNotIn('<h1>User profiles</h1>', profile_page)
            readme = (output / 'README.md').read_text(encoding='utf-8')
            self.assertIn(
                '# [#21890](https://github.com/status-im/status-app/pull/21890)',
                readme,
            )
            self.assertIn('Enable loading skeletons', readme)

    def test_pr_heading_fetches_title_when_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / '21980'
            with patch(
                'site_generator._fetch_pr_title',
                return_value='Wallet cache',
            ) as fetch:
                write_site(output, (PAGE,), {}, channel='pr')
            fetch.assert_called_once_with('21980')
            html = (output / 'index.html').read_text(encoding='utf-8')
            self.assertIn('#21980', html)
            self.assertIn('Wallet cache', html)

    def test_pr_title_uses_cached_file_without_github(self):
        with tempfile.TemporaryDirectory() as tmp:
            data_dir = Path(tmp)
            (data_dir / 'pr_title.txt').write_text('Perf/loading skeletons\n')
            with patch('site_generator._fetch_pr_title') as fetch:
                title = resolve_pr_title('21890', data_dir=data_dir)
            fetch.assert_not_called()
            self.assertEqual(title, 'Perf/loading skeletons')


if __name__ == '__main__':
    unittest.main()
