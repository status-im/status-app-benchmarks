import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'scripts'
sys.path.insert(0, str(SCRIPTS))

from benchmark_config import load_benchmark_config  # noqa: E402
from raw_result_parser import parse_raw_result_json  # noqa: E402


class RawResultParserTests(unittest.TestCase):
    def test_structured_pytest_result_produces_dashboard_rows(self):
        result = {
            'schema_version': 1,
            'test_name': 'test_wallet_first_open_loading_time[fresh_user]',
            'status': 'passed',
            'duration_ms': 1234,
            'retries_count': 0,
            'flaky': False,
            'metrics': [
                {
                    'name': 'Wallet first open load times',
                    'unit': 'seconds',
                    'values': [0.5, 0.7],
                },
                {
                    'name': 'Wallet first open CPU usage',
                    'unit': 'percent',
                    'values': [10.0, 12.0],
                },
                {
                    'name': 'Wallet first open RAM usage',
                    'unit': 'MB',
                    'values': [200.0, 220.0],
                },
            ],
        }
        config = load_benchmark_config(SCRIPTS / 'tests_config.toml')
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'result.json'
            path.write_text(json.dumps(result), encoding='utf-8')
            test, performance, cpu, ram, net = parse_raw_result_json(path, config)

        self.assertEqual(test['status'], 'passed')
        self.assertEqual(len(performance), 1)
        self.assertAlmostEqual(performance[0]['avg_time'], 0.6)
        self.assertEqual(len(cpu), 1)
        self.assertEqual(len(ram), 1)
        self.assertEqual(net, [])

    def test_one_data_usage_test_yields_total_waku_and_app_rows(self):
        result = {
            'schema_version': 1,
            'test_name': 'test_data_usage_first_open[fresh_user]',
            'status': 'passed',
            'duration_ms': 320000,
            'retries_count': 0,
            'flaky': False,
            'metrics': [
                {'name': 'Total data usage', 'unit': 'MB', 'values': [103.4], 'durations_sec': [301.8]},
                {'name': 'Waku data usage', 'unit': 'MB', 'values': [80.0], 'durations_sec': [301.8]},
                {'name': 'HTTPS data usage', 'unit': 'MB', 'values': [15.0], 'durations_sec': [301.8]},
                {'name': 'Other data usage', 'unit': 'MB', 'values': [3.4], 'durations_sec': [301.8]},
            ],
        }
        config = load_benchmark_config(SCRIPTS / 'tests_config.toml')
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'result.json'
            path.write_text(json.dumps(result), encoding='utf-8')
            test, performance, cpu, ram, net = parse_raw_result_json(path, config)

        self.assertEqual(test['status'], 'passed')
        self.assertEqual(performance, [])
        by_id = {row['metric_id']: row for row in net}
        self.assertEqual(set(by_id), {
            'test_data_usage_total_fresh',
            'test_data_usage_waku_fresh',
            'test_data_usage_https_fresh',
            'test_data_usage_other_fresh',
        })
        self.assertAlmostEqual(by_id['test_data_usage_total_fresh']['avg_value'], 103.4)
        self.assertAlmostEqual(by_id['test_data_usage_waku_fresh']['avg_value'], 80.0)
        self.assertAlmostEqual(by_id['test_data_usage_https_fresh']['avg_value'], 15.0)
        self.assertAlmostEqual(by_id['test_data_usage_other_fresh']['avg_value'], 3.4)
        self.assertAlmostEqual(by_id['test_data_usage_total_fresh']['avg_settle_sec'], 301.8)

    def test_data_usage_hosts_attach_to_total_row(self):
        result = {
            'schema_version': 1,
            'test_name': 'test_data_usage_first_open[fresh_user]',
            'status': 'passed',
            'duration_ms': 320000,
            'retries_count': 0,
            'flaky': False,
            'metrics': [
                {'name': 'Total data usage', 'unit': 'MB', 'values': [103.4], 'durations_sec': [301.8]},
                {'name': 'Waku data usage', 'unit': 'MB', 'values': [80.0], 'durations_sec': [301.8]},
                {'name': 'HTTPS data usage', 'unit': 'MB', 'values': [15.0], 'durations_sec': [301.8]},
                {'name': 'Other data usage', 'unit': 'MB', 'values': [3.4], 'durations_sec': [301.8]},
            ],
            'hosts': {
                'https': [{'host': 'prod.market.status.im', 'mb': 12.0}],
            },
        }
        config = load_benchmark_config(SCRIPTS / 'tests_config.toml')
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'result.json'
            path.write_text(json.dumps(result), encoding='utf-8')
            _test, _performance, _cpu, _ram, net = parse_raw_result_json(path, config)
        by_id = {row['metric_id']: row for row in net}
        self.assertEqual(
            by_id['test_data_usage_total_fresh']['hosts']['https'][0]['host'],
            'prod.market.status.im',
        )
        self.assertNotIn('hosts', by_id['test_data_usage_waku_fresh'])

    def test_data_usage_profile_param_maps_to_its_own_charts(self):
        result = {
            'schema_version': 1,
            'test_name': 'test_data_usage_first_open[wallet_load_alex_user]',
            'status': 'passed',
            'duration_ms': 320000,
            'retries_count': 0,
            'flaky': False,
            'metrics': [
                {'name': 'Total data usage', 'unit': 'MB', 'values': [207.9], 'durations_sec': [301.6]},
                {'name': 'Waku data usage', 'unit': 'MB', 'values': [150.0], 'durations_sec': [301.6]},
                {'name': 'HTTPS data usage', 'unit': 'MB', 'values': [40.0], 'durations_sec': [301.6]},
                {'name': 'Other data usage', 'unit': 'MB', 'values': [7.9], 'durations_sec': [301.6]},
            ],
        }
        config = load_benchmark_config(SCRIPTS / 'tests_config.toml')
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'result.json'
            path.write_text(json.dumps(result), encoding='utf-8')
            _test, performance, cpu, ram, net = parse_raw_result_json(path, config)

        by_id = {row['metric_id']: row for row in net}
        self.assertEqual(performance, [])
        self.assertNotIn('test_data_usage_total_fresh', by_id)
        self.assertAlmostEqual(by_id['test_data_usage_total_wallet_load_alex']['avg_value'], 207.9)
        self.assertAlmostEqual(by_id['test_data_usage_waku_wallet_load_alex']['avg_value'], 150.0)
        self.assertAlmostEqual(by_id['test_data_usage_https_wallet_load_alex']['avg_value'], 40.0)


class AllureSettleParseTests(unittest.TestCase):
    def test_attachment_line_with_in_seconds(self):
        from allure_parser import parse_metric_attachment

        text = (
            '[1/1] Wallet landing data usage: 1.523 MB in 30.7s\n'
            'Average Wallet landing data usage over 1 runs: 1.523 MB in 30.7s\n'
        )
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'wallet.txt'
            path.write_text(text, encoding='utf-8')
            parsed = parse_metric_attachment(path, 'Wallet landing data usage')
        self.assertAlmostEqual(parsed['avg_value'], 1.523)
        self.assertAlmostEqual(parsed['avg_settle_sec'], 30.7)

    def test_attachment_without_settle_still_parses_mb(self):
        from allure_parser import parse_metric_attachment

        text = (
            '[1/1] Wallet landing data usage: 1.523 MB\n'
            'Average Wallet landing data usage over 1 runs: 1.523 MB\n'
        )
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'wallet.txt'
            path.write_text(text, encoding='utf-8')
            parsed = parse_metric_attachment(path, 'Wallet landing data usage')
        self.assertAlmostEqual(parsed['avg_value'], 1.523)
        self.assertNotIn('avg_settle_sec', parsed)


if __name__ == '__main__':
    unittest.main()
