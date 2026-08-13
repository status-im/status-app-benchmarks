import sys
import unittest
from pathlib import Path

import pandas as pd


SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))

from chart_builder import aggregate_by_build, metrics_in_chart_window  # noqa: E402


class ChartRunTests(unittest.TestCase):
    def test_repeated_commit_runs_remain_separate_points(self):
        frame = pd.DataFrame([
            {
                'run_id': 'release-rc2-first',
                'commit_hash': 'abc123',
                'build_label': '2.39.0-rc.2 run 1',
                'date': pd.Timestamp('2026-08-13T10:00:00'),
                'test_name': 'wallet_open',
                'avg_time': 0.5,
            },
            {
                'run_id': 'release-rc2-second',
                'commit_hash': 'abc123',
                'build_label': '2.39.0-rc.2 run 2',
                'date': pd.Timestamp('2026-08-13T11:00:00'),
                'test_name': 'wallet_open',
                'avg_time': 0.6,
            },
        ])
        points = aggregate_by_build(frame, 'avg_time', ['test_name'])
        self.assertEqual(len(points), 2)
        self.assertEqual(
            points['tick_label'].tolist(),
            ['2.39.0-rc.2 run 1', '2.39.0-rc.2 run 2'],
        )

    def test_release_window_keeps_old_release_candidates(self):
        frame = pd.DataFrame([
            {'commit_hash': 'old', 'test_name': 'wallet_open', 'date': pd.Timestamp('2025-01-01')},
            {'commit_hash': 'new', 'test_name': 'wallet_open', 'date': pd.Timestamp('2026-08-13')},
        ])
        self.assertEqual(len(metrics_in_chart_window(frame, days=None)), 2)


if __name__ == '__main__':
    unittest.main()
