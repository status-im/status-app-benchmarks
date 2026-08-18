"""Run metadata, channel routing, and release baseline promotion."""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Optional

import pandas as pd


CHANNELS = ('nightly', 'pr', 'release')
MANIFEST_CSV = 'runs.csv'
NIGHTLY_BASELINE_CSV = 'nightly_baseline.csv'
NIGHTLY_BASELINE_FIELDS = ('run_id', 'commit_hash', 'date', 'pr_run_id')
BASELINE_REGISTRY_CSV = 'registry.csv'
METRIC_FILES = (
    'performance_metrics.csv',
    'cpu_metrics.csv',
    'ram_metrics.csv',
    'summary_metrics.csv',
    'run_environment.csv',
)
_SAFE_SEGMENT = re.compile(r'^[A-Za-z0-9][A-Za-z0-9._-]*$')
_RELEASE_SERIES = re.compile(r'^(\d+\.\d+)')


def safe_segment(value: str, field: str) -> str:
    value = value.strip()
    if not value or not _SAFE_SEGMENT.fullmatch(value) or value in {'.', '..'}:
        raise ValueError(f'Invalid {field}: {value!r}')
    return value


def release_series_from_version(version: str) -> str:
    match = _RELEASE_SERIES.match(version.strip())
    if not match:
        raise ValueError(f'Cannot derive release series from {version!r}')
    return match.group(1)


@dataclass(frozen=True)
class RunContext:
    run_id: str
    channel: str
    commit_hash: str
    date: str
    build_label: str = ''
    source_ref: str = ''
    build_source: str = ''
    pr_number: str = ''
    release_series: str = ''
    release_version: str = ''

    def validate(self) -> None:
        safe_segment(self.run_id, 'run_id')
        if self.channel not in CHANNELS:
            raise ValueError(f'Invalid channel {self.channel!r}; expected one of {CHANNELS}')
        safe_segment(self.commit_hash, 'commit_hash')
        if self.channel == 'pr':
            safe_segment(self.pr_number, 'pr_number')
            if not self.pr_number.isdigit():
                raise ValueError('pr_number must contain digits only')
        if self.channel == 'release':
            series = self.release_series or release_series_from_version(self.release_version)
            safe_segment(series, 'release_series')
            safe_segment(self.release_version, 'release_version')

    def as_row(self) -> dict[str, str]:
        return {
            'run_id': self.run_id,
            'channel': self.channel,
            'commit_hash': self.commit_hash,
            'date': self.date,
            'build_label': self.build_label,
            'source_ref': self.source_ref,
            'build_source': self.build_source,
            'pr_number': self.pr_number,
            'release_series': self.release_series,
            'release_version': self.release_version,
        }

    def with_defaults(self) -> 'RunContext':
        if self.channel == 'release' and not self.release_series:
            return replace(self, release_series=release_series_from_version(self.release_version))
        return self


def channel_data_dir(root: Path, context: RunContext) -> Path:
    """Return a physically isolated data directory for a run."""
    context = context.with_defaults()
    context.validate()
    if context.channel == 'nightly':
        # Keep the existing history in place; other channels are isolated below desktop/.
        return root
    if context.channel == 'pr':
        return root / 'desktop' / 'pr' / context.pr_number
    if context.channel == 'release':
        return root / 'desktop' / 'releases' / context.release_series
    raise ValueError(f'Unsupported channel {context.channel!r}')


def ensure_new_run(data_dir: Path, run_id: str) -> None:
    manifest = data_dir / MANIFEST_CSV
    if not manifest.exists():
        return
    with open(manifest, newline='', encoding='utf-8') as handle:
        if any(row.get('run_id') == run_id for row in csv.DictReader(handle)):
            raise ValueError(f'Run {run_id!r} is already present in {manifest}')


def append_run_manifest(data_dir: Path, context: RunContext) -> None:
    context = context.with_defaults()
    context.validate()
    data_dir.mkdir(parents=True, exist_ok=True)
    path = data_dir / MANIFEST_CSV
    fields = list(context.as_row())
    exists = path.exists()
    with open(path, 'a', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        if not exists:
            writer.writeheader()
        writer.writerow(context.as_row())


def load_nightly_baseline(data_dir: Path) -> dict[str, str]:
    path = data_dir / NIGHTLY_BASELINE_CSV
    if not path.exists():
        return {}
    with open(path, newline='', encoding='utf-8') as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return {}
    row = rows[0]
    return {
        field: (row.get(field) or '').strip()
        for field in NIGHTLY_BASELINE_FIELDS
    }


def save_nightly_baseline(data_dir: Path, stamp: dict[str, str]) -> None:
    if not (stamp.get('commit_hash') or stamp.get('date')):
        return
    data_dir.mkdir(parents=True, exist_ok=True)
    with open(data_dir / NIGHTLY_BASELINE_CSV, 'w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(NIGHTLY_BASELINE_FIELDS))
        writer.writeheader()
        writer.writerow({
            field: (stamp.get(field) or '').strip()
            for field in NIGHTLY_BASELINE_FIELDS
        })


def load_run_manifest(path: Path) -> pd.DataFrame:
    """Read runs.csv from a data directory or from the CSV path itself."""
    csv_path = path if path.suffix.lower() == '.csv' else path / MANIFEST_CSV
    if not csv_path.exists():
        return pd.DataFrame()
    try:
        frame = pd.read_csv(csv_path)
    except (OSError, pd.errors.EmptyDataError, pd.errors.ParserError):
        return pd.DataFrame()
    return frame if frame is not None else pd.DataFrame()


def utc_dates(frame: pd.DataFrame, column: str = 'date') -> pd.Series:
    if frame is None or frame.empty or column not in frame.columns:
        index = getattr(frame, 'index', None)
        return pd.Series(dtype='datetime64[ns, UTC]', index=index)
    return pd.to_datetime(frame[column], utc=True, errors='coerce')


def latest_run_row(
    frame: pd.DataFrame | None,
    *,
    until: Optional[pd.Timestamp] = None,
) -> Optional[pd.Series]:
    if frame is None or frame.empty or 'date' not in frame.columns:
        return None
    ordered = frame.assign(_sort=utc_dates(frame))
    ordered = ordered[ordered['_sort'].notna()]
    if until is not None and not pd.isna(until):
        ordered = ordered[ordered['_sort'] <= until]
    if ordered.empty:
        return None
    return ordered.sort_values('_sort').iloc[-1].drop(labels='_sort', errors='ignore')


def run_stamp(row: object | None) -> dict[str, str]:
    if row is None:
        return {}
    getter = row.get if hasattr(row, 'get') else lambda _key, default='': default
    date = getter('date')
    if date is None or (not isinstance(date, str) and pd.isna(date)):
        date_text = ''
    elif hasattr(date, 'strftime'):
        date_text = pd.Timestamp(date).strftime('%Y-%m-%dT%H:%M:%S')
    else:
        date_text = str(date).strip()
    return {
        'run_id': str(getter('run_id') or '').strip(),
        'commit_hash': str(getter('commit_hash') or '').strip(),
        'date': date_text,
    }


def load_baseline_registry(baseline_dir: Path) -> list[dict[str, str]]:
    path = baseline_dir / BASELINE_REGISTRY_CSV
    if not path.exists():
        return []
    with open(path, newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def _select_run_rows(source: Path, run_id: str) -> tuple[list[str], list[dict[str, str]]]:
    if not source.exists():
        return [], []
    with open(source, newline='', encoding='utf-8') as handle:
        reader = csv.DictReader(handle)
        rows = [
            row for row in reader
            if row.get('run_id', row.get('commit_hash', '')) == run_id
        ]
        return list(reader.fieldnames or []), rows


def _append_unique_rows(
    destination: Path,
    fieldnames: Iterable[str],
    rows: list[dict[str, str]],
) -> None:
    fields = list(fieldnames)
    destination.parent.mkdir(parents=True, exist_ok=True)
    exists = destination.exists()
    with open(destination, 'a', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        if not exists:
            writer.writeheader()
        writer.writerows(rows)


def promote_release_baseline(
    release_data_dir: Path,
    baseline_dir: Path,
    *,
    run_id: str,
    release_series: str = '',
    promoted_at: str = '',
) -> str:
    """Copy one validated final release run into the immutable baseline store."""
    safe_segment(run_id, 'run_id')
    manifests, matches = _select_run_rows(release_data_dir / MANIFEST_CSV, run_id)
    if len(matches) != 1:
        raise ValueError(f'Expected one manifest row for {run_id!r}, found {len(matches)}')
    manifest = matches[0]
    if manifest.get('channel') != 'release':
        raise ValueError(f'Run {run_id!r} is not a release run')
    series = release_series or manifest.get('release_series') or release_series_from_version(
        manifest.get('release_version', ''),
    )
    safe_segment(series, 'release_series')
    if manifest.get('release_series') and manifest.get('release_series') != series:
        raise ValueError(f'Run {run_id!r} does not belong to release {series}')
    release_version = manifest.get('release_version', '')
    if not promoted_at:
        promoted_at = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
    if not release_version or 'rc' in release_version.lower():
        raise ValueError('Only a final release version can be promoted')

    registry = load_baseline_registry(baseline_dir)
    if any(row.get('release_series') == series for row in registry):
        raise ValueError(f'Release {series!r} already has a promoted baseline')

    _summary_fields, summary_rows = _select_run_rows(
        release_data_dir / 'summary_metrics.csv', run_id,
    )
    if len(summary_rows) != 1:
        raise ValueError(f'Expected one summary row for final run {run_id!r}')
    summary = summary_rows[0]
    total = int(float(summary.get('total_tests') or 0))
    passed = int(float(summary.get('passed') or 0))
    if total == 0 or passed != total:
        raise ValueError('Only a complete, fully passed final run can be promoted')

    copied = 0
    for filename in METRIC_FILES:
        fields, rows = _select_run_rows(release_data_dir / filename, run_id)
        if not rows:
            if filename in {'performance_metrics.csv', 'summary_metrics.csv'}:
                raise ValueError(f'Required final-run data is missing from {filename}')
            continue
        _append_unique_rows(baseline_dir / filename, fields, rows)
        copied += len(rows)

    if copied == 0:
        raise ValueError(f'No metric rows found for final run {run_id!r}')

    baseline_dir.mkdir(parents=True, exist_ok=True)
    registry_path = baseline_dir / BASELINE_REGISTRY_CSV
    fields = ['run_id', 'commit_hash', 'release_series', 'release_version', 'label', 'promoted_at']
    exists = registry_path.exists()
    with open(registry_path, 'a', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        if not exists:
            writer.writeheader()
        writer.writerow({
            'run_id': run_id,
            'commit_hash': manifest.get('commit_hash', ''),
            'release_series': series,
            'release_version': release_version,
            'label': manifest.get('build_label') or release_version,
            'promoted_at': promoted_at,
        })
    return manifest.get('commit_hash', '')
