import sys
import unittest
from pathlib import Path

import pandas as pd

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))

from site_generator import (  # noqa: E402
    _last_run_markdown,
    _last_run_panel,
    _machine_info_markdown,
    _machine_info_panel,
)


FULL_COMMIT = '27614460fb0482179e72efd1d4bc18d816fffae5'


def _frame(commit_hash: str = FULL_COMMIT) -> pd.DataFrame:
    return pd.DataFrame([
        {
            'commit_hash': commit_hash,
            'date': pd.Timestamp('2026-08-17T12:00:00'),
            'hostname': 'WINDOWS-NODE-01',
            'windows_version': 'Windows Server 2022 Standard 21H2',
            'os_build': '20348.1487',
            'cpu': 'AMD Ryzen 7 PRO 8700GE',
            'ram_gb': '63',
        },
    ])


class SitePanelTests(unittest.TestCase):
    def test_host_panel_has_specs_not_commit(self):
        html = _machine_info_panel(_frame())
        self.assertIn('WINDOWS-NODE-01', html)
        self.assertIn('Windows e2e benchmark runner', html)
        self.assertIn('AMD Ryzen 7 PRO 8700GE', html)
        self.assertNotIn('27614460f', html)
        self.assertNotIn('Last run', html)

    def test_last_run_panel_has_date_and_commit_link(self):
        html = _last_run_panel(_frame())
        self.assertIn('Last run', html)
        self.assertIn('Aug 17, 2026', html)
        self.assertIn('27614460f', html)
        self.assertIn(
            f'https://github.com/status-im/status-app/commit/{FULL_COMMIT}',
            html,
        )
        self.assertIn('target="_blank"', html)
        self.assertNotIn('noreferrer', html)
        self.assertNotIn('WINDOWS-NODE-01', html)
        self.assertNotIn('AMD Ryzen', html)

    def test_short_commit_href_expands_to_full_sha(self):
        from unittest.mock import patch

        from site_generator import _commit_github_href, _expanded_commit_shas

        _expanded_commit_shas.clear()
        with patch(
            'site_generator._fetch_full_commit_sha',
            return_value=FULL_COMMIT,
        ) as fetch:
            href = _commit_github_href('27614460fb')
        self.assertEqual(
            href,
            f'https://github.com/status-im/status-app/commit/{FULL_COMMIT}',
        )
        fetch.assert_called_once_with('27614460fb')

    def test_markdown_splits_the_same_way(self):
        host = '\n'.join(_machine_info_markdown(_frame()))
        last = '\n'.join(_last_run_markdown(_frame()))
        self.assertIn('WINDOWS-NODE-01', host)
        self.assertNotIn('27614460f', host)
        self.assertIn('Last run', last)
        self.assertIn(
            f'https://github.com/status-im/status-app/commit/{FULL_COMMIT}',
            last,
        )
        self.assertNotIn('WINDOWS-NODE-01', last)


if __name__ == '__main__':
    unittest.main()
