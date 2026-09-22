import sys
import unittest
from pathlib import Path

import pandas as pd


SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))

from benchmark_config import ChartDefaults, ChartTest  # noqa: E402
from chart_builder import (  # noqa: E402
    aggregate_by_build,
    build_chart_figure,
    metrics_in_chart_window,
)


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


def _send_style_chart() -> ChartTest:
    return ChartTest(
        test_id='test_demo_time',
        display_name='Demo',
        graph_filename='demo.png',
        pattern='test_demo',
        ylabel='seconds',
        value_column='avg_time',
        metrics_kind='performance',
        attachment_keyword='load time',
        area='messenger',
        show_rolling_average=True,
        show_speed_zones=True,
        description='Lower is better.',
    )


def _metrics(values: list[float]) -> pd.DataFrame:
    return pd.DataFrame([
        {
            'run_id': f'run-{index}',
            'commit_hash': f'abc{index:04d}',
            'date': pd.Timestamp('2026-09-01') + pd.Timedelta(days=index),
            'test_name': 'test_demo',
            'avg_time': value,
        }
        for index, value in enumerate(values)
    ])


class RollingAverageTests(unittest.TestCase):
    def _figure(self, values: list[float]):
        return build_chart_figure(
            _send_style_chart(),
            _metrics(values),
            ChartDefaults(rolling_window=5),
            build_labels={},
            window_days=None,
        )

    def test_two_builds_draw_partial_window_average(self):
        fig = self._figure([1.0, 3.0])
        names = [trace.name for trace in fig.data]
        self.assertEqual(names, ['per build', '5-build average'])
        self.assertEqual(list(fig.data[1].y), [1.0, 2.0])
        self.assertTrue(fig.layout.showlegend)

    def test_five_build_window_uses_trailing_mean(self):
        fig = self._figure([1.0, 2.0, 3.0, 4.0, 5.0])
        self.assertEqual(list(fig.data[1].y), [1.0, 1.5, 2.0, 2.5, 3.0])

    def test_single_build_has_no_average_line(self):
        fig = self._figure([1.0])
        self.assertEqual([trace.name for trace in fig.data], ['per build'])
        self.assertFalse(fig.layout.showlegend)


if __name__ == '__main__':
    unittest.main()
