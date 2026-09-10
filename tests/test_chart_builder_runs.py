import sys
import unittest
from pathlib import Path

import pandas as pd


SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))

from chart_builder import (  # noqa: E402
    _format_point_label,
    aggregate_by_build,
    build_chart_figure,
    metrics_in_chart_window,
    series_for_chart,
)
from benchmark_config import ChartDefaults, load_benchmark_config  # noqa: E402


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

    def test_net_metric_ids_from_the_same_test_stay_separate(self):
        config = load_benchmark_config(SCRIPTS / 'tests_config.toml')
        total = next(
            chart for chart in config.charts
            if chart.test_id == 'test_data_usage_total_fresh'
        )
        alex = next(
            chart for chart in config.charts
            if chart.test_id == 'test_data_usage_total_wallet_load_alex'
        )
        waku = next(
            chart for chart in config.charts
            if chart.test_id == 'test_data_usage_waku_fresh'
        )
        frame = pd.DataFrame([
            {
                'run_id': 'nightly-1',
                'commit_hash': 'abc123',
                'date': pd.Timestamp('2026-09-08'),
                'test_name': 'test_data_usage_first_open[fresh_user]',
                'metric_id': 'test_data_usage_total_fresh',
                'avg_net_mb': 103.4,
                'avg_settle_sec': 301.8,
            },
            {
                'run_id': 'nightly-1',
                'commit_hash': 'abc123',
                'date': pd.Timestamp('2026-09-08'),
                'test_name': 'test_data_usage_first_open[wallet_load_alex_user]',
                'metric_id': 'test_data_usage_total_wallet_load_alex',
                'avg_net_mb': 207.9,
                'avg_settle_sec': 301.6,
            },
            {
                'run_id': 'nightly-1',
                'commit_hash': 'abc123',
                'date': pd.Timestamp('2026-09-08'),
                'test_name': 'test_data_usage_first_open[fresh_user]',
                'metric_id': 'test_data_usage_waku_fresh',
                'avg_net_mb': 80.0,
                'avg_settle_sec': 301.8,
            },
        ])
        total_series, _ = series_for_chart(frame, total, window_days=None)
        alex_series, _ = series_for_chart(frame, alex, window_days=None)
        waku_series, _ = series_for_chart(frame, waku, window_days=None)
        self.assertEqual(len(total_series), 1)
        self.assertEqual(len(alex_series), 1)
        self.assertEqual(len(waku_series), 1)
        self.assertAlmostEqual(float(total_series.iloc[0]['avg_net_mb']), 103.4)
        self.assertAlmostEqual(float(total_series.iloc[0]['avg_settle_sec']), 301.8)
        self.assertAlmostEqual(float(alex_series.iloc[0]['avg_net_mb']), 207.9)
        self.assertAlmostEqual(float(waku_series.iloc[0]['avg_net_mb']), 80.0)

    def test_net_point_label_includes_settle_time(self):
        self.assertEqual(_format_point_label(1.523, 'net', settle_sec=30.7), '1.52 MB · 30.7s')
        self.assertEqual(_format_point_label(21.575, 'net', settle_sec=220.4), '21.57 MB · 220s')
        self.assertEqual(_format_point_label(1.5, 'net'), '1.50 MB')

    def test_net_charts_explain_five_minute_window(self):
        config = load_benchmark_config(SCRIPTS / 'tests_config.toml')
        total = next(
            chart for chart in config.charts
            if chart.test_id == 'test_data_usage_total_fresh'
        )
        self.assertIn('Total = Waku + HTTPS + Other', total.description)
        self.assertIn('DiscV5 UDP peer discovery', total.description)
        self.assertIn('5 min window', total.footnote)

    def test_metric_id_rows_survive_baseline_dedupe(self):
        frame = pd.DataFrame([
            {
                'commit_hash': '5f66de',
                'test_name': 'test_data_usage_first_open[fresh_user]',
                'metric_id': 'test_data_usage_total_fresh',
                'date': pd.Timestamp('2025-01-01'),
                'avg_net_mb': 1.0,
            },
            {
                'commit_hash': '5f66de',
                'test_name': 'test_data_usage_first_open[wallet_load_alex_user]',
                'metric_id': 'test_data_usage_total_wallet_load_alex',
                'date': pd.Timestamp('2025-01-01'),
                'avg_net_mb': 20.0,
            },
            {
                'commit_hash': 'new',
                'test_name': 'test_data_usage_first_open[fresh_user]',
                'metric_id': 'test_data_usage_total_fresh',
                'date': pd.Timestamp('2026-09-08'),
                'avg_net_mb': 103.4,
            },
        ])
        windowed = metrics_in_chart_window(frame, baselines=['5f66de'], days=30)
        self.assertEqual(len(windowed), 3)

    def test_combined_net_chart_draws_total_waku_and_app_traces(self):
        config = load_benchmark_config(SCRIPTS / 'tests_config.toml')
        charts_by_id = {chart.test_id: chart for chart in config.charts}
        total = charts_by_id['test_data_usage_total_fresh']
        frame = pd.DataFrame([
            {
                'run_id': 'nightly-1',
                'commit_hash': 'abc123',
                'date': pd.Timestamp('2026-09-09'),
                'test_name': 'test_data_usage_first_open[fresh_user]',
                'metric_id': 'test_data_usage_total_fresh',
                'avg_net_mb': 99.4,
                'avg_settle_sec': 301.6,
            },
            {
                'run_id': 'nightly-1',
                'commit_hash': 'abc123',
                'date': pd.Timestamp('2026-09-09'),
                'test_name': 'test_data_usage_first_open[fresh_user]',
                'metric_id': 'test_data_usage_waku_fresh',
                'avg_net_mb': 23.6,
                'avg_settle_sec': 301.6,
            },
            {
                'run_id': 'nightly-1',
                'commit_hash': 'abc123',
                'date': pd.Timestamp('2026-09-09'),
                'test_name': 'test_data_usage_first_open[fresh_user]',
                'metric_id': 'test_data_usage_https_fresh',
                'avg_net_mb': 50.0,
                'avg_settle_sec': 301.6,
            },
            {
                'run_id': 'nightly-1',
                'commit_hash': 'abc123',
                'date': pd.Timestamp('2026-09-09'),
                'test_name': 'test_data_usage_first_open[fresh_user]',
                'metric_id': 'test_data_usage_other_fresh',
                'avg_net_mb': 10.8,
                'avg_settle_sec': 301.6,
            },
        ])
        fig = build_chart_figure(
            total, frame, ChartDefaults(),
            window_days=None, charts_by_id=charts_by_id,
        )
        self.assertIsNotNone(fig)
        names = [trace.name for trace in fig.data]
        self.assertEqual(names, ['Total', 'Waku', 'HTTPS', 'Other'])
        self.assertEqual(fig.layout.hovermode, 'x unified')
        self.assertEqual(fig.layout.hoverlabel.font.size, 15)
        for trace in fig.data:
            self.assertNotIn('Window', trace.hovertemplate)
            self.assertIn(trace.name, trace.hovertemplate)
            self.assertIn('MB', trace.hovertemplate)
        self.assertIn('Commit:', fig.data[0].hovertemplate)
        for overlay in fig.data[1:]:
            self.assertNotIn('Commit:', overlay.hovertemplate)


if __name__ == '__main__':
    unittest.main()
