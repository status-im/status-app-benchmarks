#!/usr/bin/env python3

import argparse
import csv
import sys
from dataclasses import replace
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))


def _configure_stdio() -> None:
    """Avoid UnicodeEncodeError on Windows consoles (cp1252) when printing reports."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, 'reconfigure', None)
        if reconfigure is None:
            continue
        try:
            reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass


_configure_stdio()

from allure_parser import parse_test_case_json
from benchmark_config import DEFAULT_CONFIG, BenchmarkConfig, ChartEntry, load_benchmark_config
from chart_builder import cleanup_stale_charts, render_chart
from environment_parser import record_run_environment
from regression_report import (
    collect_scenario_summaries,
    collect_violations,
    filter_metrics_to_stamp,
    resolve_nightly_baseline,
    with_nightly_comparisons,
    write_regression_report,
)
from raw_result_parser import parse_raw_result_json
from run_context import (
    RunContext,
    append_run_manifest,
    channel_data_dir,
    ensure_new_run,
    load_baseline_registry,
    load_nightly_baseline,
    load_run_manifest,
    promote_release_baseline,
    save_nightly_baseline,
)
from site_generator import (
    NightlyBaseline,
    nightly_comparison_header,
    resolve_pr_title,
    write_desktop_landing,
    write_docs_root_index,
    write_site,
)

CONFIG: BenchmarkConfig

METRICS_CSV = {
    'performance': ('performance_metrics.csv', {
        'min_time': 'min_value', 'max_time': 'max_value', 'avg_time': 'avg_value',
    }),
    'cpu': ('cpu_metrics.csv', {
        'min_cpu': 'min_value', 'max_cpu': 'max_value', 'avg_cpu': 'avg_value',
    }),
    'ram': ('ram_metrics.csv', {
        'min_ram_mb': 'min_value', 'max_ram_mb': 'max_value', 'avg_ram_mb': 'avg_value',
    }),
}


def _ensure_csv_schema(csv_path: Path, fieldnames: List[str]) -> None:
    if not csv_path.exists():
        return
    with open(csv_path, newline='', encoding='utf-8') as handle:
        reader = csv.DictReader(handle)
        current = list(reader.fieldnames or [])
        if current == fieldnames:
            return
        rows = list(reader)
    unknown = [field for field in current if field not in fieldnames]
    if unknown:
        raise ValueError(f'Cannot migrate {csv_path}: unexpected columns {unknown}')
    temp_path = csv_path.with_suffix(f'{csv_path.suffix}.tmp')
    with open(temp_path, 'w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    temp_path.replace(csv_path)


def _append_csv_rows(data_dir: Path, filename: str, fieldnames: List[str], rows: List[Dict]) -> None:
    if not rows:
        return
    csv_path = data_dir / filename
    _ensure_csv_schema(csv_path, fieldnames)
    file_exists = csv_path.exists()
    with open(csv_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerows(rows)


def _read_metrics_csv(data_dir: Path, filename: str) -> Optional[pd.DataFrame]:
    path = data_dir / filename
    if not path.exists():
        return None
    frame = pd.read_csv(path, parse_dates=['date']).sort_values('date')
    if 'run_id' not in frame:
        frame['run_id'] = frame['commit_hash'].astype(str)
    else:
        frame['run_id'] = frame['run_id'].fillna('').astype(str)
        missing_run_id = frame['run_id'].str.strip() == ''
        frame.loc[missing_run_id, 'run_id'] = frame.loc[missing_run_id, 'commit_hash'].astype(str)
    if 'build_label' not in frame:
        frame['build_label'] = ''
    else:
        frame['build_label'] = frame['build_label'].fillna('')
    return frame


def load_metrics(data_dir: Path) -> Dict[str, Optional[pd.DataFrame]]:
    return {
        kind: _read_metrics_csv(data_dir, csv_name)
        for kind, (csv_name, _) in METRICS_CSV.items()
    }


def process_benchmark_run(
    benchmark_dir: Path,
    data_dir: Path,
    context: RunContext,
    *,
    machine_info_file: Optional[Path] = None,
):
    context.validate()
    ensure_new_run(data_dir, context.run_id)
    print(f'\nProcessing benchmark: {benchmark_dir}')

    test_cases_dir = benchmark_dir / 'test-cases'
    if not test_cases_dir.exists():
        test_cases_dir = benchmark_dir / 'data' / 'test-cases'
    if test_cases_dir.exists():
        json_files = list(test_cases_dir.glob('*.json'))
        result_format = 'Allure'
    else:
        json_files = list(benchmark_dir.glob('*.json'))
        result_format = 'raw benchmark JSON'
    if not json_files:
        raise ValueError(f'No supported JSON files found in {benchmark_dir}')

    print(f'Found {len(json_files)} {result_format} test case files')

    performance_results: List[Dict] = []
    cpu_results: List[Dict] = []
    ram_results: List[Dict] = []
    parse_errors: List[str] = []
    aggregate = {
        'total_tests': 0, 'passed': 0, 'failed': 0, 'broken': 0,
        'skipped': 0, 'unknown': 0, 'total_duration_ms': 0,
        'min_duration_ms': float('inf'), 'max_duration_ms': 0,
        'total_retries': 0, 'flaky_tests': 0,
    }

    for json_file in json_files:
        try:
            if result_format == 'Allure':
                parsed = parse_test_case_json(json_file, benchmark_dir, CONFIG)
            else:
                parsed = parse_raw_result_json(json_file, CONFIG)
            test_result, performance_metrics, cpu_metrics, ram_metrics = parsed
            aggregate['total_tests'] += 1
            aggregate[test_result['status']] = aggregate.get(test_result['status'], 0) + 1
            aggregate['total_duration_ms'] += test_result['duration_ms']
            aggregate['min_duration_ms'] = min(aggregate['min_duration_ms'], test_result['duration_ms'])
            aggregate['max_duration_ms'] = max(aggregate['max_duration_ms'], test_result['duration_ms'])
            aggregate['total_retries'] += test_result['retries_count']
            if test_result['flaky']:
                aggregate['flaky_tests'] += 1
            performance_results.extend(performance_metrics)
            cpu_results.extend(cpu_metrics)
            ram_results.extend(ram_metrics)
        except Exception as error:
            print(f'Error parsing {json_file.name}: {error}')
            parse_errors.append(f'{json_file.name}: {error}')

    if parse_errors:
        raise ValueError(
            f'Failed to parse {len(parse_errors)} result file(s): {"; ".join(parse_errors[:3])}',
        )
    if aggregate['total_tests'] == 0:
        raise ValueError('No test results found')

    aggregate['pass_rate'] = round((aggregate.get('passed', 0) / aggregate['total_tests']) * 100, 2)
    aggregate['avg_duration_ms'] = round(aggregate['total_duration_ms'] / aggregate['total_tests'], 2)
    if aggregate['min_duration_ms'] == float('inf'):
        aggregate['min_duration_ms'] = 0
    for status in ['passed', 'failed', 'broken', 'skipped', 'unknown']:
        aggregate.setdefault(status, 0)

    data_dir.mkdir(parents=True, exist_ok=True)

    summary_csv = data_dir / 'summary_metrics.csv'
    summary_fields = [
        'run_id', 'commit_hash', 'date', 'build_label',
        'total_tests', 'passed', 'failed', 'broken',
        'skipped', 'unknown', 'pass_rate', 'total_duration_ms', 'avg_duration_ms',
        'min_duration_ms', 'max_duration_ms', 'total_retries', 'flaky_tests',
    ]
    _ensure_csv_schema(summary_csv, summary_fields)
    file_exists = summary_csv.exists()
    with open(summary_csv, 'a', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=summary_fields)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'run_id': context.run_id,
            'commit_hash': context.commit_hash,
            'date': context.date,
            'build_label': context.build_label,
            **aggregate,
        })

    _append_csv_rows(data_dir, 'performance_metrics.csv', [
        'run_id', 'commit_hash', 'date', 'build_label', 'test_name', 'status',
        'min_time', 'max_time', 'avg_time', 'run_count', 'all_runs',
    ], [{
        'run_id': context.run_id,
        'commit_hash': context.commit_hash,
        'date': context.date,
        'build_label': context.build_label,
        **{key: row[key] for key in (
            'test_name', 'status', 'min_time', 'max_time', 'avg_time', 'run_count', 'all_runs',
        )},
    } for row in performance_results])

    for results, kind in ((cpu_results, 'cpu'), (ram_results, 'ram')):
        csv_name, column_map = METRICS_CSV[kind]
        _append_csv_rows(data_dir, csv_name, [
            'run_id', 'commit_hash', 'date', 'build_label', 'test_name', 'metric_id', 'status',
            *column_map.keys(), 'run_count', 'all_runs',
        ], [{
            'run_id': context.run_id,
            'commit_hash': context.commit_hash,
            'date': context.date,
            'build_label': context.build_label,
            'test_name': row['test_name'],
            'metric_id': row['metric_id'],
            'status': row['status'],
            **{csv_col: row[metric_key] for csv_col, metric_key in column_map.items()},
            'run_count': row['run_count'],
            'all_runs': row['all_runs'],
        } for row in results])

    record_run_environment(
        data_dir, context.commit_hash, context.date,
        run_id=context.run_id, build_label=context.build_label,
        machine_info_file=machine_info_file,
    )
    append_run_manifest(data_dir, context)

    print(f"Processed {aggregate['total_tests']} tests")
    if performance_results:
        print(f'Processed {len(performance_results)} load time results')
    if cpu_results:
        print(f'Processed {len(cpu_results)} CPU results')
    if ram_results:
        print(f'Processed {len(ram_results)} RAM results')
    print(f"Pass rate: {aggregate['pass_rate']}%")
    print(f"Total duration: {aggregate['total_duration_ms']}ms")


def _config_with_promoted_baselines(
    config: BenchmarkConfig,
    registry: list[dict[str, str]],
) -> BenchmarkConfig:
    promoted = [row.get('commit_hash', '') for row in registry if row.get('commit_hash')]
    if not promoted:
        return config
    baseline_hashes = tuple(dict.fromkeys([*config.defaults.baselines, *promoted]))
    reference = promoted[-1]
    defaults = replace(
        config.defaults, baselines=baseline_hashes, reference_build=reference,
    )
    charts = tuple(
        replace(
            chart,
            baselines=tuple(dict.fromkeys([*chart.baselines, *promoted])),
            reference_build=reference,
        )
        if chart.inherit_reference_build else chart
        for chart in config.charts
    )
    return replace(config, defaults=defaults, charts=charts)


def _merge_baseline_metrics(
    metrics: Dict[str, Optional[pd.DataFrame]],
    baseline_dir: Optional[Path],
    registry: list[dict[str, str]],
) -> Dict[str, Optional[pd.DataFrame]]:
    if baseline_dir is None or not baseline_dir.exists() or not registry:
        return metrics
    baseline_metrics = load_metrics(baseline_dir)
    allowed_run_ids = {row.get('run_id', '') for row in registry}
    merged = dict(metrics)
    for kind, baseline_frame in baseline_metrics.items():
        if baseline_frame is None or baseline_frame.empty:
            continue
        baseline_frame = baseline_frame[
            baseline_frame['run_id'].astype(str).isin(allowed_run_ids)
        ]
        if baseline_frame.empty:
            continue
        current = merged.get(kind)
        merged[kind] = (
            baseline_frame.copy()
            if current is None or current.empty
            else pd.concat([current, baseline_frame], ignore_index=True).sort_values('date')
        )
    return merged


def _merge_reference_metrics(
    metrics: Dict[str, Optional[pd.DataFrame]],
    source_dir: Path,
    reference_commit: str,
) -> Dict[str, Optional[pd.DataFrame]]:
    """Merge reference-build rows from nightly data into isolated channel metrics."""
    source_metrics = load_metrics(source_dir)
    merged = dict(metrics)
    for kind, source_frame in source_metrics.items():
        if source_frame is None or source_frame.empty:
            continue
        reference_rows = source_frame[
            source_frame['commit_hash'].astype(str) == reference_commit
        ]
        if reference_rows.empty:
            continue
        group_cols = ['test_name']
        if 'metric_id' in reference_rows.columns:
            group_cols.append('metric_id')
        reference_rows = (
            reference_rows.sort_values('date')
            .groupby(group_cols, as_index=False)
            .tail(1)
        )
        current = merged.get(kind)
        if current is None or current.empty:
            merged[kind] = reference_rows.copy()
        else:
            existing_run_ids = set(current['run_id'].astype(str))
            new_rows = reference_rows[
                ~reference_rows['run_id'].astype(str).isin(existing_run_ids)
            ]
            if not new_rows.empty:
                merged[kind] = (
                    pd.concat([current, new_rows], ignore_index=True).sort_values('date')
                )
    return merged


def _nightly_data_dir(data_dir: Path, channel: str) -> Path:
    if channel == 'nightly':
        return data_dir
    return data_dir.parent.parent.parent


def generate_graphs(
    data_dir: Path,
    output_dir: Path,
    *,
    channel: str = 'nightly',
    baseline_dir: Optional[Path] = None,
    pr_title: str = '',
):
    global CONFIG
    registry = load_baseline_registry(baseline_dir) if baseline_dir else []
    if channel == 'release':
        # Keep this release's final build in its RC -> final trend. It becomes a
        # pinned baseline only for nightly and subsequent release series.
        registry = [
            row for row in registry
            if row.get('release_series') != output_dir.name
        ]
    CONFIG = _config_with_promoted_baselines(CONFIG, registry)
    build_labels = {
        row['commit_hash']: row.get('label', '')
        for row in registry if row.get('commit_hash')
    }
    window_days = None if channel in {'release', 'pr'} else 30
    graph_filenames = [chart.graph_filename for chart in CONFIG.charts]
    output_dir.mkdir(parents=True, exist_ok=True)
    cleanup_stale_charts(output_dir, graph_filenames)

    print(f'\nLoading data from {data_dir}...')
    metrics = _merge_baseline_metrics(load_metrics(data_dir), baseline_dir, registry)
    if channel in {'pr', 'release'}:
        nightly_dir = _nightly_data_dir(data_dir, channel)
        reference_commit = CONFIG.defaults.reference_build
        if nightly_dir.exists() and reference_commit:
            metrics = _merge_reference_metrics(metrics, nightly_dir, reference_commit)
    runs = load_run_manifest(data_dir)

    charts_by_test_id: Dict[str, ChartEntry] = {}

    print(f'\nGenerating charts in {output_dir}...')
    for chart in CONFIG.charts:
        frame = metrics.get(chart.metrics_kind)
        if frame is None or frame.empty:
            continue
        try:
            entry = render_chart(
                chart, frame, output_dir, CONFIG.defaults,
                window_days=window_days, build_labels=build_labels,
            )
            if entry is not None:
                charts_by_test_id[chart.test_id] = entry
        except Exception as error:
            print(f'Error generating chart for {chart.test_id}: {error}')

    print('\nGenerating GitHub Pages site...')
    summaries = collect_scenario_summaries(metrics, CONFIG, window_days=window_days)
    nightly = NightlyBaseline()
    resolved_pr_title = ''
    if channel == 'pr':
        nightly_dir = _nightly_data_dir(data_dir, channel)
        if nightly_dir.exists():
            nightly_metrics = load_metrics(nightly_dir)
            stamp = resolve_nightly_baseline(
                cached=load_nightly_baseline(data_dir),
                nightly_runs=load_run_manifest(nightly_dir),
                pr_runs=runs,
                nightly_metrics=nightly_metrics,
                pr_metrics=metrics,
            )
            if stamp:
                save_nightly_baseline(data_dir, stamp)
                nightly_metrics = filter_metrics_to_stamp(nightly_metrics, stamp)
                summaries = with_nightly_comparisons(
                    summaries, nightly_metrics, CONFIG, window_days=None,
                )
                nightly = NightlyBaseline.for_pr(*nightly_comparison_header(
                    pd.DataFrame([stamp]),
                    nightly_metrics,
                ))
        pr_number = output_dir.name if output_dir.name.isdigit() else ''
        resolved_pr_title = resolve_pr_title(
            pr_number, data_dir=data_dir, pr_title=pr_title,
        )
    performance = metrics.get('performance')
    violations = []
    if performance is not None and not performance.empty:
        violations = collect_violations(performance, CONFIG, window_days=window_days)
    write_site(
        output_dir, CONFIG.pages, charts_by_test_id,
        chart_tests=CONFIG.charts,
        summaries=summaries,
        runs=runs,
        violations=violations,
        flag_tickets=CONFIG.flag_tickets,
        channel=channel,
        release_series=output_dir.name if channel == 'release' else '',
        nightly_baseline_label=nightly.label,
        nightly_baseline_title=nightly.title,
        nightly_baseline_name=nightly.name,
        pr_title=resolved_pr_title,
    )
    if channel in {'pr', 'release'}:
        desktop_dir = output_dir.parent.parent
    else:
        desktop_dir = output_dir.parent
    write_desktop_landing(desktop_dir)
    write_docs_root_index(desktop_dir.parent)

    report_path = output_dir / 'regression_report.md'
    if performance is not None and not performance.empty:
        write_regression_report(performance, CONFIG, report_path, violations=violations)

    print(f'\nDone: {output_dir.absolute()}')


def cmd_parse(args):
    try:
        datetime.strptime(args.date, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        print(f'Error: Date must be YYYY-MM-DDTHH:MM:SS, got: {args.date}')
        sys.exit(1)
    try:
        context = RunContext(
            run_id=args.run_id,
            channel=args.channel,
            commit_hash=args.commit_hash,
            date=args.date,
            build_label=args.build_label,
            source_ref=args.source_ref,
            build_source=args.build_source,
            pr_number=args.pr_number,
            release_series=args.release_series,
            release_version=args.release_version,
        ).with_defaults()
        data_dir = channel_data_dir(args.data_dir, context)
        process_benchmark_run(
            args.benchmark_dir, data_dir, context,
            machine_info_file=args.machine_info,
        )
    except ValueError as error:
        print(f'Error: {error}')
        sys.exit(1)
    print(f'\nCSV files updated in {data_dir.absolute()}')


def cmd_graphs(args):
    generate_graphs(
        args.data_dir, args.output_dir,
        channel=args.channel, baseline_dir=args.baseline_dir,
        pr_title=args.pr_title,
    )


def cmd_promote_baseline(args):
    try:
        commit_hash = promote_release_baseline(
            args.release_data_dir,
            args.baseline_dir,
            run_id=args.run_id,
        )
    except ValueError as error:
        print(f'Error: {error}')
        sys.exit(1)
    print(f'Promoted final build {commit_hash} as a baseline')


def cmd_report(args):
    metrics = load_metrics(args.data_dir)
    performance = metrics.get('performance')
    if performance is None or performance.empty:
        print('Error: no performance metrics found')
        sys.exit(1)
    write_regression_report(performance, CONFIG, args.output)


def cmd_list_tests(_args):
    if CONFIG.pages:
        print('\nScenario pages:')
        for page in CONFIG.pages:
            print(f'  {page.slug}: {page.title} ({", ".join(page.test_ids)})')
    print('\nCharts:')
    for chart in CONFIG.charts:
        print(f'  [{chart.metrics_kind}] {chart.test_id} -> {chart.graph_filename}')


def main():
    parser = argparse.ArgumentParser(
        description='Parse structured or Allure benchmark results and publish GitHub Pages charts',
    )
    parser.add_argument('--config', type=Path, default=DEFAULT_CONFIG, help=f'Config file (default: {DEFAULT_CONFIG})')
    subparsers = parser.add_subparsers(dest='command')

    parse_parser = subparsers.add_parser(
        'parse', help='Parse structured benchmark JSON (or legacy Allure results) into CSV',
    )
    parse_parser.add_argument('benchmark_dir', type=Path)
    parse_parser.add_argument('--run-id', required=True)
    parse_parser.add_argument('--channel', choices=('nightly', 'pr', 'release'), default='nightly')
    parse_parser.add_argument('--commit-hash', required=True)
    parse_parser.add_argument('--date', required=True)
    parse_parser.add_argument('--build-label', default='')
    parse_parser.add_argument('--source-ref', default='')
    parse_parser.add_argument('--build-source', default='')
    parse_parser.add_argument('--pr-number', default='')
    parse_parser.add_argument('--release-series', default='')
    parse_parser.add_argument('--release-version', default='')
    parse_parser.add_argument('--data-dir', type=Path, default=Path('data'))
    parse_parser.add_argument(
        '--machine-info', type=Path,
        help='JSON file with system metadata (hostname, windows_version, os_build, cpu, ram_gb)',
    )
    parse_parser.set_defaults(func=cmd_parse)

    graphs_parser = subparsers.add_parser('graphs', help='Generate charts and GitHub Pages site')
    graphs_parser.add_argument('--data-dir', type=Path, default=Path('data'))
    graphs_parser.add_argument('--output-dir', type=Path, default=Path('docs/desktop/nightly'))
    graphs_parser.add_argument('--channel', choices=('nightly', 'pr', 'release'), default='nightly')
    graphs_parser.add_argument('--baseline-dir', type=Path)
    graphs_parser.add_argument('--pr-title', default='', help='PR title to show on the dashboard heading')
    graphs_parser.set_defaults(func=cmd_graphs)

    report_parser = subparsers.add_parser('report', help='Write regression report from CSV data')
    report_parser.add_argument('--data-dir', type=Path, default=Path('data'))
    report_parser.add_argument('--output', type=Path, default=Path('docs/desktop/regression_report.md'))
    report_parser.set_defaults(func=cmd_report)

    promote_parser = subparsers.add_parser(
        'promote-baseline', help='Promote a final release run into the shared baseline store',
    )
    promote_parser.add_argument('--release-data-dir', type=Path, required=True)
    promote_parser.add_argument('--baseline-dir', type=Path, default=Path('data/desktop/baselines'))
    promote_parser.add_argument('--run-id', required=True)
    promote_parser.set_defaults(func=cmd_promote_baseline)

    subparsers.add_parser('list-tests', help='List configured charts and pages').set_defaults(func=cmd_list_tests)

    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
        sys.exit(1)

    global CONFIG
    try:
        CONFIG = load_benchmark_config(args.config)
    except (FileNotFoundError, ValueError) as error:
        print(f'Error: {error}')
        sys.exit(1)

    args.func(args)


if __name__ == '__main__':
    main()
