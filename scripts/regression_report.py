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


@dataclass(frozen=True)
class ScenarioSummary:
    test_id: str
    value: Optional[float]
    commit_hash: str
    date: str
    speed_status: str
    vs_reference: str
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


def _trend_only(series: pd.DataFrame, chart: ChartTest) -> pd.DataFrame:
    if not chart.baselines:
        return series
    filtered = series[~series['commit_hash'].astype(str).isin(chart.baselines)]
    return filtered.reset_index(drop=True)


def collect_violations(metrics: pd.DataFrame, config: BenchmarkConfig) -> List[Violation]:
    violations: List[Violation] = []
    defaults = config.defaults
    performance_charts = [c for c in config.charts if c.metrics_kind == 'performance']

    for chart in performance_charts:
        result = series_for_chart(metrics, chart)
        if result is None:
            continue
        series, _n_baselines = result
        series = _trend_only(series, chart)
        if series.empty:
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


def collect_scenario_summaries(
    metrics: dict[str, pd.DataFrame],
    config: BenchmarkConfig,
) -> dict[str, ScenarioSummary]:
    summaries: dict[str, ScenarioSummary] = {}
    defaults = config.defaults
    for chart in config.charts:
        frame = metrics.get(chart.metrics_kind)
        result = series_for_chart(frame, chart) if frame is not None and not frame.empty else None
        if result is None:
            summaries[chart.test_id] = ScenarioSummary(
                test_id=chart.test_id,
                value=None,
                commit_hash='',
                date='',
                speed_status='no-data',
                vs_reference='—',
                detail='No data in the current chart window.',
            )
            continue

        full_series, _n_baselines = result
        trend = _trend_only(full_series, chart)
        if trend.empty:
            summaries[chart.test_id] = ScenarioSummary(
                test_id=chart.test_id,
                value=None,
                commit_hash='',
                date='',
                speed_status='no-data',
                vs_reference='—',
                detail='No trend data in the current chart window.',
            )
            continue

        latest = trend.iloc[-1]
        value = float(latest[chart.value_column])
        if chart.metrics_kind == 'performance':
            ok_warn_threshold = (
                defaults.slow_threshold_s * (1 - defaults.ok_near_slow_ratio)
            )
            if value < defaults.fast_threshold_s:
                speed_status = 'fast'
            elif value > defaults.slow_threshold_s:
                speed_status = 'slow'
            elif value >= ok_warn_threshold:
                speed_status = 'ok-warn'
            else:
                speed_status = 'ok'

            reference_build = chart.reference_build or defaults.reference_build
            reference_rows = (
                full_series[full_series['commit_hash'].astype(str) == reference_build]
                if reference_build else pd.DataFrame()
            )
            if reference_rows.empty:
                vs_reference = 'no baseline'
                reference_detail = 'No reference-build result is available.'
            else:
                reference_value = float(reference_rows[chart.value_column].iloc[0])
                delta = value - reference_value
                if abs(delta) <= reference_value * defaults.regression_pct:
                    vs_reference = 'parity'
                else:
                    vs_reference = f'{delta:+.3f}s'
                reference_detail = (
                    f'Latest {value:.3f}s vs reference {reference_value:.3f}s '
                    f'({delta:+.3f}s); parity is within ±{defaults.regression_pct:.0%}.'
                )
            detail = (
                f'Speed: {speed_status}; fast <{defaults.fast_threshold_s}s, '
                f'ok {defaults.fast_threshold_s}–{ok_warn_threshold:.1f}s, '
                f'ok near slow {ok_warn_threshold:.1f}–{defaults.slow_threshold_s}s, '
                f'slow >{defaults.slow_threshold_s}s. {reference_detail}'
            )
        else:
            speed_status = 'neutral'
            vs_reference = '—'
            detail = 'Time-based thresholds do not apply to this metric.'
        summaries[chart.test_id] = ScenarioSummary(
            test_id=chart.test_id,
            value=value,
            commit_hash=str(latest['commit_hash']),
            date=latest['date'].strftime('%Y-%m-%d'),
            speed_status=speed_status,
            vs_reference=vs_reference,
            detail=detail,
        )
    return summaries


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
        'Regression': [v for v in violations if v.rule == '2.1 Regression'],
        'Slow builds': [v for v in violations if v.rule == '2.2 Slow build'],
        'Backlog candidates': [v for v in violations if v.rule == '2.3 Backlog candidate'],
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
