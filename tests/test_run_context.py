import csv
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))

from run_context import (  # noqa: E402
    RunContext,
    append_run_manifest,
    channel_data_dir,
    ensure_new_run,
    promote_release_baseline,
    release_series_from_version,
)


class RunContextTests(unittest.TestCase):
    def test_release_series_is_derived_from_version(self):
        self.assertEqual(release_series_from_version('2.39.0-rc.1'), '2.39')
        self.assertEqual(release_series_from_version('2.39.0'), '2.39')
        with self.assertRaisesRegex(ValueError, 'Cannot derive'):
            release_series_from_version('rc-only')

    def test_release_data_dir_fills_series_from_version(self):
        context = RunContext(
            run_id='release-abc-1',
            channel='release',
            commit_hash='abc123',
            date='2026-08-13T12:00:00',
            release_version='2.39.0-rc.1',
        )
        self.assertEqual(
            channel_data_dir(Path('data'), context),
            Path('data/desktop/releases/2.39'),
        )

    def test_channels_are_physically_isolated(self):
        root = Path('data')
        release = RunContext(
            run_id='release-abc-1',
            channel='release',
            commit_hash='abc123',
            date='2026-08-13T12:00:00',
            release_series='2.39',
            release_version='2.39.0-rc.1',
        )
        pr = RunContext(
            run_id='pr-123-1',
            channel='pr',
            commit_hash='def456',
            date='2026-08-13T12:00:00',
            pr_number='123',
        )
        self.assertEqual(
            channel_data_dir(root, release),
            Path('data/desktop/releases/2.39'),
        )
        self.assertEqual(channel_data_dir(root, pr), Path('data/desktop/pr/123'))

    def test_duplicate_run_id_is_rejected(self):
        context = RunContext(
            run_id='nightly-abc-1',
            channel='nightly',
            commit_hash='abc123',
            date='2026-08-13T12:00:00',
        )
        with tempfile.TemporaryDirectory() as temp:
            data_dir = Path(temp)
            append_run_manifest(data_dir, context)
            with self.assertRaisesRegex(ValueError, 'already present'):
                ensure_new_run(data_dir, context.run_id)

    def test_final_release_can_be_promoted_once(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            release_dir = root / 'releases' / '2.39'
            baseline_dir = root / 'baselines'
            release_dir.mkdir(parents=True)
            context = RunContext(
                run_id='release-final-1',
                channel='release',
                commit_hash='abc123',
                date='2026-08-13T12:00:00',
                build_label='2.39.0',
                release_series='2.39',
                release_version='2.39.0',
            )
            append_run_manifest(release_dir, context)
            self._write_csv(
                release_dir / 'summary_metrics.csv',
                ['run_id', 'commit_hash', 'total_tests', 'passed', 'failed', 'broken'],
                [['release-final-1', 'abc123', '1', '1', '0', '0']],
            )
            self._write_csv(
                release_dir / 'performance_metrics.csv',
                ['run_id', 'commit_hash', 'date', 'test_name', 'avg_time'],
                [['release-final-1', 'abc123', context.date, 'wallet_open', '0.5']],
            )

            promoted = promote_release_baseline(
                release_dir,
                baseline_dir,
                run_id=context.run_id,
            )
            self.assertEqual(promoted, 'abc123')
            with self.assertRaisesRegex(ValueError, 'already has'):
                promote_release_baseline(
                    release_dir,
                    baseline_dir,
                    run_id=context.run_id,
                )

    @staticmethod
    def _write_csv(path: Path, fields: list[str], rows: list[list[str]]) -> None:
        with open(path, 'w', newline='', encoding='utf-8') as handle:
            writer = csv.writer(handle)
            writer.writerow(fields)
            writer.writerows(rows)


if __name__ == '__main__':
    unittest.main()
