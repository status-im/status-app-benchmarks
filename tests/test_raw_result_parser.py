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
            test, performance, cpu, ram = parse_raw_result_json(path, config)

        self.assertEqual(test['status'], 'passed')
        self.assertEqual(len(performance), 1)
        self.assertAlmostEqual(performance[0]['avg_time'], 0.6)
        self.assertEqual(len(cpu), 1)
        self.assertEqual(len(ram), 1)


if __name__ == '__main__':
    unittest.main()
