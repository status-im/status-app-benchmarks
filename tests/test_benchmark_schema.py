import csv
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))

from benchmark import _ensure_csv_schema, _read_metrics_csv  # noqa: E402


class CsvSchemaTests(unittest.TestCase):
    def test_legacy_csv_is_extended_without_losing_rows(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'performance_metrics.csv'
            with open(path, 'w', newline='', encoding='utf-8') as handle:
                writer = csv.writer(handle)
                writer.writerow(['commit_hash', 'date', 'test_name'])
                writer.writerow(['abc123', '2026-08-13T12:00:00', 'wallet_open'])

            fields = ['run_id', 'commit_hash', 'date', 'build_label', 'test_name']
            _ensure_csv_schema(path, fields)

            with open(path, newline='', encoding='utf-8') as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(rows[0]['commit_hash'], 'abc123')
            self.assertEqual(rows[0]['run_id'], '')
            self.assertEqual(rows[0]['build_label'], '')
            frame = _read_metrics_csv(path.parent, path.name)
            self.assertEqual(frame.iloc[0]['run_id'], 'abc123')


if __name__ == '__main__':
    unittest.main()
