"""Parse versioned benchmark result JSON written directly by pytest."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Tuple

from benchmark_config import BenchmarkConfig, ChartTest


SUPPORTED_SCHEMA_VERSION = 1


def _metric_values(data: dict, keyword: str) -> Dict:
    keyword = keyword.lower()
    metric = next(
        (
            candidate for candidate in data.get('metrics', [])
            if keyword in str(candidate.get('name', '')).lower()
        ),
        None,
    )
    if metric is None:
        return {}
    values = [float(value) for value in metric.get('values', [])]
    if not values:
        return {}
    return {
        'min_value': min(values),
        'max_value': max(values),
        'avg_value': sum(values) / len(values),
        'run_count': len(values),
        'all_runs': ','.join(map(str, values)),
    }


def _attachment_keyword_for_test(chart: ChartTest, test_name: str) -> str:
    for index, pattern in enumerate(chart.historical_patterns):
        if pattern not in test_name:
            continue
        if index < len(chart.historical_attachment_keywords):
            return chart.historical_attachment_keywords[index]
        break
    return chart.attachment_keyword


def parse_raw_result_json(
    json_file: Path,
    config: BenchmarkConfig,
) -> Tuple[Dict, List[Dict], List[Dict], List[Dict]]:
    data = json.loads(json_file.read_text(encoding='utf-8'))
    version = data.get('schema_version')
    if version != SUPPORTED_SCHEMA_VERSION:
        raise ValueError(
            f'Unsupported benchmark result schema {version!r} in {json_file.name}',
        )
    test_result = {
        'test_name': data.get('test_name', ''),
        'status': data.get('status', 'unknown'),
        'duration_ms': data.get('duration_ms', 0),
        'retries_count': data.get('retries_count', 0),
        'flaky': data.get('flaky', False),
    }
    test_name = test_result['test_name']
    output: dict[str, List[Dict]] = {
        'performance': [],
        'cpu': [],
        'ram': [],
    }
    for chart in config.charts:
        patterns = (chart.source_pattern or chart.pattern, *chart.historical_patterns)
        if not any(pattern in test_name for pattern in patterns):
            continue
        metric = _metric_values(data, _attachment_keyword_for_test(chart, test_name))
        if not metric:
            continue
        if chart.metrics_kind == 'performance':
            output['performance'].append({
                'test_name': chart.pattern,
                'status': test_result['status'],
                'min_time': metric['min_value'],
                'max_time': metric['max_value'],
                'avg_time': metric['avg_value'],
                'run_count': metric['run_count'],
                'all_runs': metric['all_runs'],
            })
        else:
            output[chart.metrics_kind].append({
                'test_name': chart.pattern,
                'metric_id': chart.test_id,
                'status': test_result['status'],
                **metric,
            })
    return test_result, output['performance'], output['cpu'], output['ram']
