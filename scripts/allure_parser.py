"""Parse Allure test-case JSON and metric attachments."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from benchmark_config import BenchmarkConfig, ChartTest


def attachment_path(benchmark_dir: Path, source: str) -> Path:
    path = benchmark_dir / 'attachments' / source
    if not path.exists():
        path = benchmark_dir / 'data' / 'attachments' / source
    return path


def parse_metric_attachment(attachment_file: Path, metric_keyword: str) -> Dict:
    if not attachment_file.exists():
        return {}

    keyword = metric_keyword.lower()
    try:
        run_values = []
        avg_value = None
        for line in attachment_file.read_text(encoding='utf-8').split('\n'):
            line_lower = line.lower()
            if keyword not in line_lower:
                continue
            parts = line.split(':')
            if len(parts) <= 1:
                continue
            try:
                value = float(parts[1].strip().split()[0])
            except ValueError:
                continue
            if 'average' in line_lower:
                avg_value = value
            else:
                run_values.append(value)

        if not run_values:
            return {}

        return {
            'min_value': min(run_values),
            'max_value': max(run_values),
            'avg_value': avg_value if avg_value is not None else sum(run_values) / len(run_values),
            'run_count': len(run_values),
            'all_runs': ','.join(map(str, run_values)),
        }
    except Exception as error:
        print(f'Warning: Failed to parse {metric_keyword} attachment {attachment_file}: {error}')
        return {}


def find_attachment_source(test_data: Dict, keyword: str) -> Optional[str]:
    keyword = keyword.lower()

    def find_in_stage(stage: Dict) -> Optional[str]:
        for attachment in stage.get('attachments', []):
            if keyword in attachment.get('name', '').lower():
                source = attachment.get('source', '')
                if source:
                    return source

        for step in stage.get('steps', []):
            source = find_in_stage(step)
            if source:
                return source

        return None

    return find_in_stage(test_data.get('testStage', {}))


def _load_time_row(test_name: str, status: str, metric_data: Dict) -> Dict:
    return {
        'test_name': test_name,
        'status': status,
        'min_time': metric_data['min_value'],
        'max_time': metric_data['max_value'],
        'avg_time': metric_data['avg_value'],
        'run_count': metric_data['run_count'],
        'all_runs': metric_data['all_runs'],
    }


def _resource_row(chart: ChartTest, test_name: str, status: str, metric_data: Dict) -> Dict:
    return {
        'test_name': test_name,
        'status': status,
        'metric_id': chart.test_id,
        **metric_data,
    }


def _attachment_keyword_for_test(chart: ChartTest, test_name: str) -> str:
    for index, pattern in enumerate(chart.historical_patterns):
        if pattern not in test_name:
            continue
        if index < len(chart.historical_attachment_keywords):
            return chart.historical_attachment_keywords[index]
        break
    return chart.attachment_keyword


def parse_test_case_json(
    json_file: Path,
    benchmark_dir: Path,
    config: BenchmarkConfig,
) -> Tuple[Dict, List[Dict], List[Dict], List[Dict]]:
    data = json.loads(json_file.read_text(encoding='utf-8'))

    test_result = {
        'test_name': data.get('name', ''),
        'status': data.get('status', 'unknown'),
        'duration_ms': data.get('time', {}).get('duration', 0),
        'retries_count': data.get('retriesCount', 0),
        'flaky': data.get('flaky', False),
    }
    test_name = test_result['test_name']
    performance_results: List[Dict] = []
    cpu_results: List[Dict] = []
    ram_results: List[Dict] = []

    for chart in config.charts:
        patterns = (
            chart.source_pattern or chart.pattern,
            *chart.historical_patterns,
        )
        if not any(pattern in test_name for pattern in patterns):
            continue
        attachment_keyword = _attachment_keyword_for_test(chart, test_name)
        attachment_source = find_attachment_source(data, attachment_keyword)
        if not attachment_source:
            continue
        metric_data = parse_metric_attachment(
            attachment_path(benchmark_dir, attachment_source),
            attachment_keyword,
        )
        if not metric_data:
            continue

        if chart.metrics_kind == 'performance':
            performance_results.append(
                _load_time_row(chart.pattern, test_result['status'], metric_data)
            )
        elif chart.metrics_kind == 'cpu':
            cpu_results.append(
                _resource_row(chart, chart.pattern, test_result['status'], metric_data)
            )
        else:
            ram_results.append(
                _resource_row(chart, chart.pattern, test_result['status'], metric_data)
            )

    return test_result, performance_results, cpu_results, ram_results
