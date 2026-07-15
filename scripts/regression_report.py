"""Evaluate performance regression rules and write a markdown report."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional

import pandas as pd

from benchmark_config import BenchmarkConfig, ChartDefaults, ChartTest
from chart_builder import series_for_chart, variant_name


@dataclass(frozen=True)
class Violation:
    rule: str
    test_id: str
    variant: str
    value: float
    commit_hash: str
    date: str
    detail: str


def _check_regression(
    series: pd.DataFrame,
    chart: ChartTest,
    defaults: ChartDefaults,
) -> Optional[Violation]:
    values = series[chart.value_column].tolist()
    commits = series['commit_hash'].astype(str).tolist()
    dates = series['date'].dt.strftime('%Y-%m-%d %H:%M').tolist()
    test_name = series['test_name'].iloc[0]
    needed = defaults.regression_consecutive
    if len(values) < needed + 1:
        return None
    threshold = 1.0 + defaults.regression_pct
    end = len(values) - 1
    ok = True
    for offset in range(needed):
        idx = end - needed + 1 + offset
        if values[idx] < values[idx - 1] * threshold:
            ok = False
            break
    if not ok:
        return None
    return Violation(
        rule='2.1 Regression',
        test_id=chart.test_id,
        variant=variant_name(test_name),
        value=values[end],
        commit_hash=commits[end],
        date=dates[end],
        detail=(
            f'{needed} consecutive builds each ≥{defaults.regression_pct:.0%} above previous '
            f'({values[end - needed]:.3f}s → {values[end]:.3f}s)'
        ),
    )


def _check_slow_latest(series: pd.DataFrame, chart: ChartTest, defaults: ChartDefaults) -> Optional[Violation]:
    latest = series.iloc[-1]
    value = float(latest[chart.value_column])
    if value <= defaults.slow_threshold_s:
        return None
    test_name = latest['test_name']
    return Violation(
        rule='2.2 Slow build',
        test_id=chart.test_id,
        variant=variant_name(test_name),
        value=value,
        commit_hash=str(latest['commit_hash']),
        date=latest['date'].strftime('%Y-%m-%d %H:%M'),
        detail=f'Latest value {value:.3f}s exceeds {defaults.slow_threshold_s}s slow threshold',
    )


def _check_backlog(series: pd.DataFrame, chart: ChartTest, defaults: ChartDefaults) -> Optional[Violation]:
    n = defaults.backlog_slow_of_last_n
    min_slow = defaults.backlog_slow_min_count
    tail = series.tail(n)
    if len(tail) < min_slow:
        return None
    slow_count = int((tail[chart.value_column] > defaults.slow_threshold_s).sum())
    if slow_count < min_slow:
        return None
    latest = series.iloc[-1]
    test_name = latest['test_name']
    return Violation(
        rule='2.3 Backlog candidate',
        test_id=chart.test_id,
        variant=variant_name(test_name),
        value=float(latest[chart.value_column]),
        commit_hash=str(latest['commit_hash']),
        date=latest['date'].strftime('%Y-%m-%d %H:%M'),
        detail=(
            f'Slow (>{defaults.slow_threshold_s}s) in {slow_count} of last {len(tail)} builds — '
            'consider a backlog ticket'
        ),
    )


def collect_violations(metrics: pd.DataFrame, config: BenchmarkConfig) -> List[Violation]:
    violations: List[Violation] = []
    defaults = config.defaults
    performance_charts = [c for c in config.charts if c.metrics_kind == 'performance']

    for chart in performance_charts:
        series = series_for_chart(metrics, chart)
        if series is None:
            continue
        regression = _check_regression(series, chart, defaults)
        if regression:
            violations.append(regression)
        slow = _check_slow_latest(series, chart, defaults)
        if slow:
            violations.append(slow)
        backlog = _check_backlog(series, chart, defaults)
        if backlog and not any(
            v.rule == '2.2 Slow build' and v.test_id == chart.test_id
            and v.variant == backlog.variant for v in violations
        ):
            violations.append(backlog)
    return violations


def _format_section(title: str, items: List[Violation]) -> List[str]:
    lines = [f'## {title}', '']
    if not items:
        lines.append('_No violations._')
        lines.append('')
        return lines
    lines.extend([
        '| Test | Variant | Value | Commit | Date | Detail |',
        '|------|---------|-------|--------|------|--------|',
    ])
    for item in items:
        lines.append(
            f'| {item.test_id} | {item.variant} | {item.value:.3f}s '
            f'| `{item.commit_hash[:10]}` | {item.date} | {item.detail} |'
        )
    lines.append('')
    return lines


def write_regression_report(
    metrics: pd.DataFrame,
    config: BenchmarkConfig,
    output_path: Path,
) -> List[Violation]:
    violations = collect_violations(metrics, config)
    by_rule = {
        '2.1 Regression': [v for v in violations if v.rule == '2.1 Regression'],
        '2.2 Slow build': [v for v in violations if v.rule == '2.2 Slow build'],
        '2.3 Backlog candidate': [v for v in violations if v.rule == '2.3 Backlog candidate'],
    }

    lines = [
        '# Desktop benchmark regression report',
        '',
        f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}',
        '',
        f'**Total flags:** {len(violations)}',
        '',
    ]
    for rule_title, items in by_rule.items():
        lines.extend(_format_section(rule_title, items))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Wrote regression report: {output_path} ({len(violations)} flags)')

    if violations:
        print('\nRegression summary:')
        for item in violations:
            print(f'  [{item.rule}] {item.test_id} ({item.variant}): {item.detail}')
    else:
        print('No regression violations detected.')

    return violations
