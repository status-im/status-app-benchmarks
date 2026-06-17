#!/usr/bin/env python3

import json
import csv
import argparse
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

import pandas as pd
import plotly.graph_objects as go
import tomli as tomllib

@dataclass
class PerformanceTest:
    test_id: str
    display_name: str
    graph_filename: str
    pattern: str
    ylabel: str = "Load Time (ms)"
    color: Optional[str] = None


def load_config(config_file: Path) -> List[PerformanceTest]:
    if not config_file.exists():
        print(f"Error: Config file not found: {config_file}")
        print(f"Expected: {DEFAULT_CONFIG}")
        sys.exit(1)
    
    try:
        with open(config_file, 'rb') as f:
            config = tomllib.load(f)
    except Exception as e:
        print(f"Error reading config file {config_file}: {e}")
        sys.exit(1)
    
    tests = []
    if 'tests' not in config:
        print(f"Error: No [[tests]] sections found in {config_file}")
        sys.exit(1)
    
    for test_config in config['tests']:
        try:
            test = PerformanceTest(
                test_id=test_config['test_id'],
                display_name=test_config['display_name'],
                graph_filename=test_config['graph_filename'],
                pattern=test_config['pattern'],
                ylabel=test_config.get('ylabel', 'Load Time (ms)'),
                color=test_config.get('color')
            )
            tests.append(test)
        except KeyError as e:
            print(f"Error: Missing required field in test config: {e}")
            sys.exit(1)
    
    if not tests:
        print(f"Error: No tests configured in {config_file}")
        sys.exit(1)
    
    return tests


DEFAULT_CONFIG = Path('scripts/tests_config.toml')

PERFORMANCE_TESTS: List[PerformanceTest] = []

DURATION_COLOR = '#54A0FF'
DURATION_FILL = 'rgba(84, 160, 255, 0.08)'
PERFORMANCE_COLORS = ['#10AC84', '#2E86DE', '#F79F1F', '#54A0FF']

CHART_WINDOW_DAYS = 30
CHART_WIDTH = 1200
CHART_HEIGHT = 500
CHART_SCALE = 1

README_PERFORMANCE_START = '<!-- performance-tests:start -->'
README_PERFORMANCE_END = '<!-- performance-tests:end -->'


def get_performance_test_patterns() -> tuple:
    return tuple(test.pattern for test in PERFORMANCE_TESTS)


def is_performance_test(test_name: str) -> bool:
    patterns = get_performance_test_patterns()
    return any(pattern in test_name for pattern in patterns)


def parse_performance_attachment(attachment_file: Path) -> Dict:
    if not attachment_file.exists():
        return {}
    
    try:
        with open(attachment_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        run_times = []
        for line in content.split('\n'):
            if 'load time:' in line.lower() and 'average' not in line.lower():
                parts = line.split('load time:')
                if len(parts) > 1:
                    time_str = parts[1].strip().split()[0]
                    try:
                        run_times.append(float(time_str))
                    except ValueError:
                        continue
        
        avg_time = None
        for line in content.split('\n'):
            if 'average' in line.lower() and 'load time' in line.lower():
                parts = line.split(':')
                if len(parts) > 1:
                    time_str = parts[1].strip().split()[0]
                    try:
                        avg_time = float(time_str)
                    except ValueError:
                        pass
        
        if run_times:
            return {
                'min_time': min(run_times),
                'max_time': max(run_times),
                'avg_time': avg_time if avg_time is not None else (sum(run_times) / len(run_times)),
                'run_count': len(run_times),
                'all_runs': ','.join(map(str, run_times))
            }
        
        return {}
    except Exception as e:
        print(f"Warning: Failed to parse performance attachment {attachment_file}: {e}")
        return {}


def find_performance_attachment_source(test_data: Dict) -> Optional[str]:
    test_stage = test_data.get('testStage', {})
    
    attachments = test_stage.get('attachments', [])
    for attachment in attachments:
        name = attachment.get('name', '').lower()
        if 'load time' in name:
            source = attachment.get('source', '')
            if source:
                return source
    
    steps = test_stage.get('steps', [])
    for step in steps:
        step_attachments = step.get('attachments', [])
        for attachment in step_attachments:
            name = attachment.get('name', '').lower()
            if 'load time' in name:
                source = attachment.get('source', '')
                if source:
                    return source
    
    return None


def parse_test_case_json(json_file: Path, benchmark_dir: Path) -> Tuple[Dict, Optional[Dict]]:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    test_result = {
        'test_name': data.get('name', ''),
        'status': data.get('status', 'unknown'),
        'duration_ms': data.get('time', {}).get('duration', 0),
        'retries_count': data.get('retriesCount', 0),
        'flaky': data.get('flaky', False)
    }
    
    test_name = test_result['test_name']
    performance_metrics = None
    
    if is_performance_test(test_name):
        attachment_source = find_performance_attachment_source(data)
        
        if attachment_source:
            attachment_path = benchmark_dir / 'attachments' / attachment_source
            if not attachment_path.exists():
                attachment_path = benchmark_dir / 'data' / 'attachments' / attachment_source
            
            perf_data = parse_performance_attachment(attachment_path)
            
            if perf_data:
                performance_metrics = {
                    'test_name': test_name,
                    'status': test_result['status'],
                    **perf_data
                }
    
    return test_result, performance_metrics


def process_benchmark_run(benchmark_dir: Path, data_dir: Path, commit_hash: str, date: str):
    print(f"\nProcessing benchmark: {benchmark_dir}")
    
    test_cases_dir = benchmark_dir / 'test-cases'
    if not test_cases_dir.exists():
        test_cases_dir = benchmark_dir / 'data' / 'test-cases'
    
    if not test_cases_dir.exists():
        print(f"Error: test-cases directory not found in:")
        print(f"  {benchmark_dir / 'test-cases'} or")
        print(f"  {benchmark_dir / 'data' / 'test-cases'}")
        return
    
    json_files = list(test_cases_dir.glob('*.json'))
    if not json_files:
        print(f"Error: No JSON files found in {test_cases_dir}")
        return
    
    print(f"Found {len(json_files)} test case files")
    
    performance_results = []
    aggregate = {
        'total_tests': 0, 'passed': 0, 'failed': 0, 'broken': 0,
        'skipped': 0, 'unknown': 0, 'total_duration_ms': 0,
        'min_duration_ms': float('inf'), 'max_duration_ms': 0,
        'total_retries': 0, 'flaky_tests': 0
    }
    
    for json_file in json_files:
        try:
            test_result, performance_metrics = parse_test_case_json(json_file, benchmark_dir)
            
            aggregate['total_tests'] += 1
            aggregate[test_result['status']] = aggregate.get(test_result['status'], 0) + 1
            aggregate['total_duration_ms'] += test_result['duration_ms']
            aggregate['min_duration_ms'] = min(aggregate['min_duration_ms'], test_result['duration_ms'])
            aggregate['max_duration_ms'] = max(aggregate['max_duration_ms'], test_result['duration_ms'])
            aggregate['total_retries'] += test_result['retries_count']
            if test_result['flaky']:
                aggregate['flaky_tests'] += 1
            
            if performance_metrics:
                performance_results.append(performance_metrics)
                
        except Exception as e:
            print(f"Error parsing {json_file.name}: {e}")
            continue
    
    if aggregate['total_tests'] == 0:
        print("Error: No test results found")
        return
    
    aggregate['pass_rate'] = round(
        (aggregate.get('passed', 0) / aggregate['total_tests']) * 100, 2
    )
    aggregate['avg_duration_ms'] = round(
        aggregate['total_duration_ms'] / aggregate['total_tests'], 2
    )
    
    if aggregate['min_duration_ms'] == float('inf'):
        aggregate['min_duration_ms'] = 0
    
    for status in ['passed', 'failed', 'broken', 'skipped', 'unknown']:
        if status not in aggregate:
            aggregate[status] = 0
    
    data_dir.mkdir(parents=True, exist_ok=True)
    
    summary_csv = data_dir / 'summary_metrics.csv'
    file_exists = summary_csv.exists()
    
    with open(summary_csv, 'a', newline='', encoding='utf-8') as f:
        fieldnames = [
            'commit_hash', 'date', 'total_tests', 'passed', 'failed', 'broken',
            'skipped', 'unknown', 'pass_rate', 'total_duration_ms', 'avg_duration_ms',
            'min_duration_ms', 'max_duration_ms', 'total_retries', 'flaky_tests'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow({
            'commit_hash': commit_hash,
            'date': date,
            'total_tests': aggregate['total_tests'],
            'passed': aggregate['passed'],
            'failed': aggregate['failed'],
            'broken': aggregate['broken'],
            'skipped': aggregate['skipped'],
            'unknown': aggregate['unknown'],
            'pass_rate': aggregate['pass_rate'],
            'total_duration_ms': aggregate['total_duration_ms'],
            'avg_duration_ms': aggregate['avg_duration_ms'],
            'min_duration_ms': aggregate['min_duration_ms'],
            'max_duration_ms': aggregate['max_duration_ms'],
            'total_retries': aggregate['total_retries'],
            'flaky_tests': aggregate['flaky_tests']
        })
    
    if performance_results:
        performance_csv = data_dir / 'performance_metrics.csv'
        file_exists = performance_csv.exists()
        
        with open(performance_csv, 'a', newline='', encoding='utf-8') as f:
            fieldnames = [
                'commit_hash', 'date', 'test_name', 'status', 'min_time', 
                'max_time', 'avg_time', 'run_count', 'all_runs'
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()
            
            for perf in performance_results:
                writer.writerow({
                    'commit_hash': commit_hash,
                    'date': date,
                    'test_name': perf['test_name'],
                    'status': perf['status'],
                    'min_time': perf['min_time'],
                    'max_time': perf['max_time'],
                    'avg_time': perf['avg_time'],
                    'run_count': perf['run_count'],
                    'all_runs': perf['all_runs']
                })
    
    print(f"Processed {aggregate['total_tests']} tests")
    if performance_results:
        print(f"Processed {len(performance_results)} performance tests")
    print(f"Pass rate: {aggregate['pass_rate']}%")
    print(f"Total duration: {aggregate['total_duration_ms']}ms")

def load_data(data_dir: Path) -> tuple:
    summary_file = data_dir / 'summary_metrics.csv'
    performance_file = data_dir / 'performance_metrics.csv'
    
    if not summary_file.exists():
        print(f"Error: {summary_file} not found")
        sys.exit(1)
    
    summary = pd.read_csv(summary_file, parse_dates=['date'])
    summary = summary.sort_values('date')
    
    performance = None
    if performance_file.exists():
        performance = pd.read_csv(performance_file, parse_dates=['date'])
        performance = performance.sort_values('date')
    
    return summary, performance


def filter_recent(df: pd.DataFrame, days: int = CHART_WINDOW_DAYS,
                  date_col: str = 'date') -> pd.DataFrame:
    cutoff = pd.Timestamp.now().normalize() - pd.Timedelta(days=days)
    return df[df[date_col] >= cutoff].copy()


def aggregate_daily(df: pd.DataFrame, value_col: str,
                    group_cols: Optional[List[str]] = None) -> pd.DataFrame:
    grouped = df.copy()
    grouped['_day'] = grouped['date'].dt.normalize()
    keys = ['_day'] + (group_cols or [])
    aggregated = grouped.groupby(keys, as_index=False)[value_col].mean()
    return aggregated.rename(columns={'_day': 'date'}).sort_values('date')


def format_date_range(dates: pd.Series, days: int = CHART_WINDOW_DAYS) -> str:
    start = dates.min().strftime('%b %d')
    end = dates.max().strftime('%b %d, %Y')
    return f"{start} – {end} (last {days} days)"


def apply_chart_layout(fig: go.Figure, title: str, ylabel: str, dates: pd.Series,
                       days: int = CHART_WINDOW_DAYS, show_legend: bool = True):
    layout = dict(
        template='plotly_white',
        title=dict(text=f"{title}<br><sup>{format_date_range(dates, days)}</sup>",
                   x=0.05, xanchor='left'),
        xaxis_title='Date',
        yaxis_title=ylabel,
        width=CHART_WIDTH,
        height=CHART_HEIGHT,
        margin=dict(l=60, r=40, t=80, b=60),
        hovermode='x unified',
        showlegend=show_legend,
    )
    if show_legend:
        layout['legend'] = dict(orientation='h', yanchor='bottom', y=1.02,
                                xanchor='right', x=1)
    fig.update_layout(**layout)
    fig.update_xaxes(type='date', tickformat='%b %d', showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='#E8ECF0', gridwidth=1)


def match_test_pattern(series: pd.Series, pattern: str) -> pd.Series:
    escaped = re.escape(pattern)
    return series.str.contains(rf'{escaped}(?:\[|$)', regex=True, na=False)


def save_chart(fig: go.Figure, output_dir: Path, filename: str):
    fig.write_image(output_dir / filename, scale=CHART_SCALE)
    print(f"Generated {filename}")


def plot_metric(summary: pd.DataFrame, output_dir: Path, column: str,
                ylabel: str, title: str, filename: str, color: str,
                transform=None):
    filtered = filter_recent(summary)
    if filtered.empty:
        print(f"Warning: No data for {filename} in the last {CHART_WINDOW_DAYS} days")
        return

    daily = aggregate_daily(filtered, column)
    data = daily[column] if transform is None else transform(daily[column])

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=daily['date'],
        y=data,
        mode='lines+markers',
        line=dict(color=color, width=2.5),
        marker=dict(size=6, color=color),
        fill='tozeroy',
        fillcolor=DURATION_FILL,
        showlegend=False,
    ))

    apply_chart_layout(fig, title, ylabel, daily['date'], show_legend=False)
    save_chart(fig, output_dir, filename)


def plot_performance(performance: pd.DataFrame, test_config: PerformanceTest,
                     output_dir: Path):
    filtered = filter_recent(performance)
    test_data = filtered[match_test_pattern(filtered['test_name'], test_config.pattern)].copy()

    if test_data.empty:
        print(f"Warning: No data for {test_config.pattern} in the last {CHART_WINDOW_DAYS} days")
        return

    fig = go.Figure()
    test_names = test_data['test_name'].unique()
    for idx, test_name in enumerate(test_names):
        variant_data = aggregate_daily(
            test_data[test_data['test_name'] == test_name], 'avg_time', ['test_name']
        )
        if test_config.color and len(test_names) == 1:
            color = test_config.color
        else:
            color = PERFORMANCE_COLORS[idx % len(PERFORMANCE_COLORS)]
        param_name = test_name.split('[')[1].split(']')[0] if '[' in test_name else 'default'
        avg_ms = variant_data['avg_time'] * 1000

        fig.add_trace(go.Scatter(
            x=variant_data['date'],
            y=avg_ms,
            mode='lines+markers',
            name=param_name,
            line=dict(color=color, width=2.5),
            marker=dict(size=6, color=color),
        ))

    apply_chart_layout(fig, test_config.display_name, test_config.ylabel, test_data['date'])
    save_chart(fig, output_dir, test_config.graph_filename)


def cleanup_stale_charts(output_dir: Path):
    expected = {'total_duration.png'} | {t.graph_filename for t in PERFORMANCE_TESTS}
    for png in output_dir.glob('*.png'):
        if png.name not in expected:
            png.unlink()
            print(f"Removed stale chart: {png.name}")


def generate_performance_readme_section(tests: List[PerformanceTest]) -> str:
    blocks = []
    for test in tests:
        blocks.append(
            f'<details>\n'
            f'<summary><b>{test.display_name}</b></summary>\n\n'
            f'![{test.display_name}](./docs/{test.graph_filename})\n'
            f'</details>'
        )
    return '\n\n'.join(blocks) + '\n'


def update_readme_performance_section(readme_path: Path, tests: List[PerformanceTest]):
    if not readme_path.exists():
        print(f"Warning: README not found at {readme_path}, skipping update")
        return

    content = readme_path.read_text(encoding='utf-8')
    if README_PERFORMANCE_START not in content or README_PERFORMANCE_END not in content:
        print(f"Warning: README markers not found, skipping update")
        return

    start = content.index(README_PERFORMANCE_START) + len(README_PERFORMANCE_START)
    end = content.index(README_PERFORMANCE_END)
    new_section = generate_performance_readme_section(tests)
    readme_path.write_text(
        content[:start] + '\n\n' + new_section + content[end:],
        encoding='utf-8',
    )
    print(f"Updated performance tests section in {readme_path}")


def generate_graphs(data_dir: Path, output_dir: Path, readme_path: Optional[Path] = None):
    output_dir.mkdir(parents=True, exist_ok=True)
    cleanup_stale_charts(output_dir)
    
    print(f"\nLoading data from {data_dir}...")
    summary, performance = load_data(data_dir)
    print(f"Loaded {len(summary)} benchmark runs")
    if performance is not None and not performance.empty:
        print(f"Loaded {len(performance)} performance results")
    
    print(f"\nGenerating graphs in {output_dir}...")
    
    plot_metric(summary, output_dir, 'total_duration_ms', 'Duration (minutes)',
                'Total Test Suite Duration', 'total_duration.png', DURATION_COLOR,
                transform=lambda x: x / 1000 / 60)
    
    if performance is not None and not performance.empty:
        print("\nGenerating performance metrics graphs...")
        
        for test_config in PERFORMANCE_TESTS:
            try:
                plot_performance(performance, test_config, output_dir)
            except Exception as e:
                print(f"Error generating graph for {test_config.test_id}: {e}")
                continue

    if readme_path is not None:
        update_readme_performance_section(readme_path, PERFORMANCE_TESTS)
    
    print(f"\nAll graphs generated in {output_dir.absolute()}")


def cmd_parse(args):
    try:
        datetime.strptime(args.date, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        print(f"Error: Date must be in YYYY-MM-DDTHH:MM:SS format, got: {args.date}")
        sys.exit(1)
    
    process_benchmark_run(args.benchmark_dir, args.data_dir, args.commit_hash, args.date)
    print(f"\nCSV files updated in {args.data_dir.absolute()}")
    print(f"Generated: summary_metrics.csv, performance_metrics.csv")


def cmd_graphs(args):
    readme_path = None if args.no_update_readme else args.readme
    generate_graphs(args.data_dir, args.output_dir, readme_path)


def cmd_list_tests(args):
    print("\nConfigured performance tests:")
    for i, test in enumerate(PERFORMANCE_TESTS, 1):
        print(f"\n{i}. {test.test_id}")
        print(f"   Display name: {test.display_name}")
        print(f"   Graph file:   {test.graph_filename}")
        print(f"   Pattern:      {test.pattern}")


def main():
    main_parser = argparse.ArgumentParser(
        description='Unified benchmark tool: Parse Allure results and generate performance graphs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Parse Allure results (uses default config: scripts/tests_config.toml)
  python benchmark.py parse /path/to/allure-results \\
      --commit-hash abc123 \\
      --date 2026-03-18T10:30:00

  # Parse with custom config file
  python benchmark.py --config my_config.toml parse /path/to/allure-results \\
      --commit-hash abc123 \\
      --date 2026-03-18T10:30:00

  # Generate graphs and update README (as run by Jenkins on schedule)
  python benchmark.py graphs --data-dir data/ --output-dir docs/

  # List configured tests
  python benchmark.py list-tests
        """
    )
    
    main_parser.add_argument(
        '--config',
        type=Path,
        default=DEFAULT_CONFIG,
        help=f'Path to benchmark config file (default: {DEFAULT_CONFIG})'
    )
    
    subparsers = main_parser.add_subparsers(dest='command', help='Available commands')
    
    parse_parser = subparsers.add_parser('parse', help='Parse Allure test results')
    parse_parser.add_argument(
        'benchmark_dir',
        type=Path,
        help='Path to Allure report directory (can contain test-cases/ or data/test-cases/)'
    )
    parse_parser.add_argument(
        '--commit-hash',
        required=True,
        help='Git commit hash (e.g., a1b2c3d)'
    )
    parse_parser.add_argument(
        '--date',
        required=True,
        help='Benchmark datetime in YYYY-MM-DDTHH:MM:SS format'
    )
    parse_parser.add_argument(
        '--data-dir',
        type=Path,
        default=Path('data'),
        help='Path to data directory for CSV files (default: data/)'
    )
    parse_parser.set_defaults(func=cmd_parse)
    
    graphs_parser = subparsers.add_parser('graphs', help='Generate benchmark graphs')
    graphs_parser.add_argument(
        '--data-dir',
        type=Path,
        default=Path('data'),
        help='Path to data directory with CSV files (default: data/)'
    )
    graphs_parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('docs'),
        help='Path to output directory for graphs (default: docs/)'
    )
    graphs_parser.add_argument(
        '--readme',
        type=Path,
        default=Path('README.md'),
        help='Path to README to update with performance test sections (default: README.md)'
    )
    graphs_parser.add_argument(
        '--no-update-readme',
        action='store_true',
        help='Skip auto-updating the Performance Tests section in README'
    )
    graphs_parser.set_defaults(func=cmd_graphs)
    
    list_parser = subparsers.add_parser('list-tests', help='List configured performance tests')
    list_parser.set_defaults(func=cmd_list_tests)
    
    args = main_parser.parse_args()
    
    if not hasattr(args, 'func'):
        main_parser.print_help()
        sys.exit(1)
    
    global PERFORMANCE_TESTS
    PERFORMANCE_TESTS = load_config(args.config)
    
    args.func(args)


if __name__ == '__main__':
    main()