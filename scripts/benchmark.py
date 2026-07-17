#!/usr/bin/env python3

import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from allure_parser import parse_test_case_json
from benchmark_config import DEFAULT_CONFIG, BenchmarkConfig, ChartEntry, load_benchmark_config
from chart_builder import cleanup_stale_charts, render_chart
from environment_parser import load_run_environment, record_run_environment
from regression_report import collect_scenario_summaries, write_regression_report
from site_generator import write_docs_root_index, write_site

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


def _append_csv_rows(data_dir: Path, filename: str, fieldnames: List[str], rows: List[Dict]) -> None:
    if not rows:
        return
    csv_path = data_dir / filename
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
    return pd.read_csv(path, parse_dates=['date']).sort_values('date')


def load_metrics(data_dir: Path) -> Dict[str, Optional[pd.DataFrame]]:
    return {
        kind: _read_metrics_csv(data_dir, csv_name)
        for kind, (csv_name, _) in METRICS_CSV.items()
    }


def process_benchmark_run(
    benchmark_dir: Path,
    data_dir: Path,
    commit_hash: str,
    date: str,
    *,
    machine_info_file: Optional[Path] = None,
):
    print(f'\nProcessing benchmark: {benchmark_dir}')

    test_cases_dir = benchmark_dir / 'test-cases'
    if not test_cases_dir.exists():
        test_cases_dir = benchmark_dir / 'data' / 'test-cases'
    if not test_cases_dir.exists():
        print('Error: test-cases directory not found')
        return

    json_files = list(test_cases_dir.glob('*.json'))
    if not json_files:
        print(f'Error: No JSON files found in {test_cases_dir}')
        return

    print(f'Found {len(json_files)} test case files')

    performance_results: List[Dict] = []
    cpu_results: List[Dict] = []
    ram_results: List[Dict] = []
    aggregate = {
        'total_tests': 0, 'passed': 0, 'failed': 0, 'broken': 0,
        'skipped': 0, 'unknown': 0, 'total_duration_ms': 0,
        'min_duration_ms': float('inf'), 'max_duration_ms': 0,
        'total_retries': 0, 'flaky_tests': 0,
    }

    for json_file in json_files:
        try:
            test_result, performance_metrics, cpu_metrics, ram_metrics = parse_test_case_json(
                json_file, benchmark_dir, CONFIG,
            )
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

    if aggregate['total_tests'] == 0:
        print('Error: No test results found')
        return

    aggregate['pass_rate'] = round((aggregate.get('passed', 0) / aggregate['total_tests']) * 100, 2)
    aggregate['avg_duration_ms'] = round(aggregate['total_duration_ms'] / aggregate['total_tests'], 2)
    if aggregate['min_duration_ms'] == float('inf'):
        aggregate['min_duration_ms'] = 0
    for status in ['passed', 'failed', 'broken', 'skipped', 'unknown']:
        aggregate.setdefault(status, 0)

    data_dir.mkdir(parents=True, exist_ok=True)

    summary_csv = data_dir / 'summary_metrics.csv'
    file_exists = summary_csv.exists()
    with open(summary_csv, 'a', newline='', encoding='utf-8') as handle:
        fieldnames = [
            'commit_hash', 'date', 'total_tests', 'passed', 'failed', 'broken',
            'skipped', 'unknown', 'pass_rate', 'total_duration_ms', 'avg_duration_ms',
            'min_duration_ms', 'max_duration_ms', 'total_retries', 'flaky_tests',
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'commit_hash': commit_hash, 'date': date, **aggregate})

    _append_csv_rows(data_dir, 'performance_metrics.csv', [
        'commit_hash', 'date', 'test_name', 'status',
        'min_time', 'max_time', 'avg_time', 'run_count', 'all_runs',
    ], [{
        'commit_hash': commit_hash,
        'date': date,
        **{key: row[key] for key in (
            'test_name', 'status', 'min_time', 'max_time', 'avg_time', 'run_count', 'all_runs',
        )},
    } for row in performance_results])

    for results, kind in ((cpu_results, 'cpu'), (ram_results, 'ram')):
        csv_name, column_map = METRICS_CSV[kind]
        _append_csv_rows(data_dir, csv_name, [
            'commit_hash', 'date', 'test_name', 'metric_id', 'status',
            *column_map.keys(), 'run_count', 'all_runs',
        ], [{
            'commit_hash': commit_hash,
            'date': date,
            'test_name': row['test_name'],
            'metric_id': row['metric_id'],
            'status': row['status'],
            **{csv_col: row[metric_key] for csv_col, metric_key in column_map.items()},
            'run_count': row['run_count'],
            'all_runs': row['all_runs'],
        } for row in results])

    record_run_environment(
        data_dir, commit_hash, date, machine_info_file=machine_info_file,
    )

    print(f"Processed {aggregate['total_tests']} tests")
    if performance_results:
        print(f'Processed {len(performance_results)} load time results')
    if cpu_results:
        print(f'Processed {len(cpu_results)} CPU results')
    if ram_results:
        print(f'Processed {len(ram_results)} RAM results')
    print(f"Pass rate: {aggregate['pass_rate']}%")
    print(f"Total duration: {aggregate['total_duration_ms']}ms")


def generate_graphs(data_dir: Path, output_dir: Path):
    graph_filenames = [chart.graph_filename for chart in CONFIG.charts]
    output_dir.mkdir(parents=True, exist_ok=True)
    cleanup_stale_charts(output_dir, graph_filenames)

    print(f'\nLoading data from {data_dir}...')
    metrics = load_metrics(data_dir)
    run_environment = load_run_environment(data_dir)

    charts_by_test_id: Dict[str, ChartEntry] = {}

    print(f'\nGenerating charts in {output_dir}...')
    for chart in CONFIG.charts:
        frame = metrics.get(chart.metrics_kind)
        if frame is None or frame.empty:
            continue
        try:
            entry = render_chart(chart, frame, output_dir, CONFIG.defaults)
            if entry is not None:
                charts_by_test_id[chart.test_id] = entry
        except Exception as error:
            print(f'Error generating chart for {chart.test_id}: {error}')

    print('\nGenerating GitHub Pages site...')
    summaries = collect_scenario_summaries(metrics, CONFIG)
    write_site(
        output_dir, CONFIG.pages, charts_by_test_id,
        chart_tests=CONFIG.charts,
        summaries=summaries,
        run_environment=run_environment,
    )
    write_docs_root_index(output_dir.parent)

    report_path = output_dir / 'regression_report.md'
    performance = metrics.get('performance')
    if performance is not None and not performance.empty:
        write_regression_report(performance, CONFIG, report_path)

    print(f'\nDone: {output_dir.absolute()}')


def cmd_parse(args):
    try:
        datetime.strptime(args.date, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        print(f'Error: Date must be YYYY-MM-DDTHH:MM:SS, got: {args.date}')
        sys.exit(1)
    process_benchmark_run(
        args.benchmark_dir, args.data_dir, args.commit_hash, args.date,
        machine_info_file=args.machine_info,
    )
    print(f'\nCSV files updated in {args.data_dir.absolute()}')


def cmd_graphs(args):
    generate_graphs(args.data_dir, args.output_dir)


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
    parser = argparse.ArgumentParser(description='Parse Allure benchmark results and publish charts to GitHub Pages')
    parser.add_argument('--config', type=Path, default=DEFAULT_CONFIG, help=f'Config file (default: {DEFAULT_CONFIG})')
    subparsers = parser.add_subparsers(dest='command')

    parse_parser = subparsers.add_parser('parse', help='Parse Allure results into CSV')
    parse_parser.add_argument('benchmark_dir', type=Path)
    parse_parser.add_argument('--commit-hash', required=True)
    parse_parser.add_argument('--date', required=True)
    parse_parser.add_argument('--data-dir', type=Path, default=Path('data'))
    parse_parser.add_argument(
        '--machine-info', type=Path,
        help='JSON file with system metadata (hostname, windows_version, os_build, cpu, ram_gb)',
    )
    parse_parser.set_defaults(func=cmd_parse)

    graphs_parser = subparsers.add_parser('graphs', help='Generate charts and GitHub Pages site')
    graphs_parser.add_argument('--data-dir', type=Path, default=Path('data'))
    graphs_parser.add_argument('--output-dir', type=Path, default=Path('docs/desktop'))
    graphs_parser.set_defaults(func=cmd_graphs)

    report_parser = subparsers.add_parser('report', help='Write regression report from CSV data')
    report_parser.add_argument('--data-dir', type=Path, default=Path('data'))
    report_parser.add_argument('--output', type=Path, default=Path('docs/desktop/regression_report.md'))
    report_parser.set_defaults(func=cmd_report)

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
