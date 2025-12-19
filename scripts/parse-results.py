#!/usr/bin/env python3
"""
Parse Allure test results and Prometheus metrics into CSV files for benchmarking.
Generates only summary_metrics.csv and performance_metrics.csv.
"""

import json
import csv
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import argparse


def parse_performance_attachment(attachment_file: Path) -> Dict:
    """Parse performance test attachment file and extract timing metrics."""
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
    """Find the attachment source filename that contains performance timing data."""
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


def parse_test_case_json(json_file: Path, benchmark_dir: Path) -> tuple:
    """Parse individual test case JSON file and extract test result."""
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
    
    if 'test_swap_loading_time' in test_name or 'test_wallet_loading_time' in test_name:
        attachment_source = find_performance_attachment_source(data)
        
        if attachment_source:
            attachment_path = benchmark_dir / 'attachments' / attachment_source
            perf_data = parse_performance_attachment(attachment_path)
            
            if perf_data:
                performance_metrics = {
                    'test_name': test_name,
                    'status': test_result['status'],
                    **perf_data
                }
    
    return test_result, performance_metrics


def process_benchmark_run(benchmark_dir: Path, data_dir: Path, commit_hash: str, date: str):
    """Process a single benchmark run directory and generate CSV files."""
    print(f"\nProcessing benchmark: {benchmark_dir}")
    
    test_cases_dir = benchmark_dir / 'test-cases'
    if not test_cases_dir.exists():
        print(f"Error: test-cases directory not found in {benchmark_dir}")
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
            
            if performance_metrics:
                performance_results.append(performance_metrics)
            
            aggregate['total_tests'] += 1
            aggregate[test_result['status']] = aggregate.get(test_result['status'], 0) + 1
            aggregate['total_duration_ms'] += test_result['duration_ms']
            aggregate['min_duration_ms'] = min(aggregate['min_duration_ms'], test_result['duration_ms'])
            aggregate['max_duration_ms'] = max(aggregate['max_duration_ms'], test_result['duration_ms'])
            aggregate['total_retries'] += test_result['retries_count']
            if test_result['flaky']:
                aggregate['flaky_tests'] += 1
                
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


def main():
    parser = argparse.ArgumentParser(
        description='Parse Allure test results into CSV files for benchmarking'
    )
    parser.add_argument(
        'benchmark_dir',
        type=Path,
        help='Path to benchmark directory containing test-cases/ and attachments/'
    )
    parser.add_argument(
        '--commit-hash',
        required=True,
        help='Git commit hash (e.g., a1b2c3d)'
    )
    parser.add_argument(
        '--date',
        required=True,
        help='Benchmark datetime in YYYY-MM-DDTHH:MM:SS format (e.g., 2024-12-19T14:30:45)'
    )
    parser.add_argument(
        '--data-dir',
        type=Path,
        default=Path('data'),
        help='Path to data directory where CSV files will be stored (default: data/)'
    )
    
    args = parser.parse_args()
    
    try:
        datetime.strptime(args.date, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        print(f"Error: Date must be in YYYY-MM-DDTHH:MM:SS format, got: {args.date}")
        return
    
    process_benchmark_run(args.benchmark_dir, args.data_dir, args.commit_hash, args.date)
    print(f"\nCSV files updated in {args.data_dir.absolute()}")
    print(f"Generated: summary_metrics.csv, performance_metrics.csv")


if __name__ == '__main__':
    main()