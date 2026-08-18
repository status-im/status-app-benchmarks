"""Evaluate performance regression rules and write a markdown report."""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime
from pathlib import Path
from typing import List, Optional

import pandas as pd

from benchmark_config import (
    CHART_WINDOW_DAYS,
    BenchmarkConfig,
    ChartDefaults,
    ChartTest,
    effective_reference_build,
)
from chart_builder import series_for_chart, variant_name
from run_context import latest_run_row, run_stamp, utc_dates


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
    vs_nightly: str = '—'


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
            f'{needed} consecutive builds each >={defaults.regression_pct:.0%} above previous '
            f'({values[end - needed]:.3f}s -> {values[end]:.3f}s)'
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
            f'Slow (>{defaults.slow_threshold_s}s) in {slow_count} of last {len(tail)} builds -- '
            'consider a backlog ticket'
        ),
    )


def _trend_only(series: pd.DataFrame, chart: ChartTest) -> pd.DataFrame:
    if not chart.baselines:
        return series
    filtered = series[~series['commit_hash'].astype(str).isin(chart.baselines)]
    return filtered.reset_index(drop=True)


def collect_violations(
    metrics: pd.DataFrame,
    config: BenchmarkConfig,
    *,
    window_days: Optional[int] = CHART_WINDOW_DAYS,
) -> List[Violation]:
    violations: List[Violation] = []
    defaults = config.defaults
    performance_charts = [c for c in config.charts if c.metrics_kind == 'performance']

    for chart in performance_charts:
        result = series_for_chart(metrics, chart, window_days=window_days)
        if result is None:
            continue
        series, _n_baselines = result
        series = _trend_only(series, chart)
        if series.empty:
            continue
        regression = _check_regression(series, chart, defaults)
        if regression:
            violations.append(regression)
        # Escalate: chronic slowdowns go to Backlog only; one-off latest
        # slowdowns stay under Slow builds.
        backlog = _check_backlog(series, chart, defaults)
        if backlog:
            violations.append(backlog)
        else:
            slow = _check_slow_latest(series, chart, defaults)
            if slow:
                violations.append(slow)
    return violations


def comparison_label(
    value: float,
    reference_value: float,
    regression_pct: float,
) -> str:
    """Return 'parity' when the delta is within ±regression_pct, else +0.123s / -0.123s."""
    delta = value - reference_value
    if abs(delta) <= abs(reference_value) * regression_pct:
        return 'parity'
    return f'{delta:+.3f}s'


def latest_trend_value(
    metrics: dict[str, pd.DataFrame],
    chart: ChartTest,
    *,
    window_days: Optional[int] = CHART_WINDOW_DAYS,
) -> Optional[float]:
    frame = metrics.get(chart.metrics_kind)
    if frame is None or frame.empty:
        return None
    result = series_for_chart(frame, chart, window_days=window_days)
    if result is None:
        return None
    series, _n_baselines = result
    trend = _trend_only(series, chart)
    if trend.empty:
        return None
    return float(trend.iloc[-1][chart.value_column])


def with_nightly_comparisons(
    summaries: dict[str, ScenarioSummary],
    nightly_metrics: dict[str, pd.DataFrame],
    config: BenchmarkConfig,
    *,
    window_days: Optional[int] = CHART_WINDOW_DAYS,
) -> dict[str, ScenarioSummary]:
    """Attach vs-latest-nightly deltas. Does not change vs_reference (release)."""
    nightly_values = {
        chart.test_id: latest_trend_value(
            nightly_metrics, chart, window_days=window_days,
        )
        for chart in config.charts
        if chart.metrics_kind == 'performance'
    }
    pct = config.defaults.regression_pct
    updated: dict[str, ScenarioSummary] = {}
    for test_id, summary in summaries.items():
        nightly_value = nightly_values.get(test_id)
        if summary.value is None or nightly_value is None:
            updated[test_id] = replace(summary, vs_nightly='—')
            continue
        updated[test_id] = replace(
            summary,
            vs_nightly=comparison_label(summary.value, nightly_value, pct),
        )
    return updated


def _stamp_on_or_before(frame: pd.DataFrame, cutoff: pd.Timestamp) -> dict[str, str]:
    return run_stamp(latest_run_row(frame, until=cutoff))


def resolve_nightly_baseline(
    *,
    cached: dict[str, str] | None,
    nightly_runs: pd.DataFrame,
    pr_runs: pd.DataFrame,
    nightly_metrics: dict[str, pd.DataFrame] | None = None,
    pr_metrics: dict[str, pd.DataFrame] | None = None,
) -> dict[str, str]:
    """Pick the newest nightly at or before the latest PR run, and reuse a cache
    while that PR run stays the newest.
    """
    pr_row = latest_run_row(pr_runs)
    if pr_row is None and pr_metrics:
        pr_row = latest_run_row(pr_metrics.get('performance'))
    pr_run_id = str(pr_row.get('run_id') or '').strip() if pr_row is not None else ''
    cached = cached or {}
    if (
        pr_run_id
        and cached.get('pr_run_id') == pr_run_id
        and (cached.get('commit_hash') or cached.get('date'))
    ):
        return cached
    cutoff = (
        pd.to_datetime(pr_row.get('date'), utc=True, errors='coerce')
        if pr_row is not None else pd.NaT
    )
    if pd.isna(cutoff):
        return {}
    stamp = _stamp_on_or_before(nightly_runs, cutoff)
    if not stamp.get('commit_hash') and nightly_metrics:
        performance = nightly_metrics.get('performance')
        stamp = _stamp_on_or_before(
            performance if performance is not None else pd.DataFrame(), cutoff,
        )
    if stamp:
        stamp['pr_run_id'] = pr_run_id
    return stamp


def _commits_match(left: str, right: str) -> bool:
    if not left or not right:
        return False
    size = min(len(left), len(right))
    return size >= 6 and left[:size] == right[:size]


def filter_metrics_to_stamp(
    metrics: dict[str, pd.DataFrame],
    stamp: dict[str, str],
) -> dict[str, pd.DataFrame]:
    run_id = (stamp.get('run_id') or '').strip()
    commit = (stamp.get('commit_hash') or '').strip()
    date = (stamp.get('date') or '').strip()
    target_date = pd.to_datetime(date, utc=True, errors='coerce') if date else pd.NaT
    filtered: dict[str, pd.DataFrame] = {}
    for kind, frame in metrics.items():
        if frame is None or frame.empty:
            continue
        subset = frame
        if run_id and 'run_id' in subset.columns:
            by_id = subset[subset['run_id'].astype(str) == run_id]
            if not by_id.empty:
                filtered[kind] = by_id
                continue
        mask = pd.Series(True, index=subset.index)
        if commit and 'commit_hash' in subset.columns:
            hashes = subset['commit_hash'].astype(str)
            mask &= hashes.map(lambda value: _commits_match(str(value), commit))
        if not pd.isna(target_date) and 'date' in subset.columns:
            mask &= utc_dates(subset) == target_date
        filtered[kind] = subset[mask]
    return filtered


def collect_scenario_summaries(
    metrics: dict[str, pd.DataFrame],
    config: BenchmarkConfig,
    *,
    window_days: Optional[int] = CHART_WINDOW_DAYS,
) -> dict[str, ScenarioSummary]:
    summaries: dict[str, ScenarioSummary] = {}
    defaults = config.defaults
    for chart in config.charts:
        frame = metrics.get(chart.metrics_kind)
        result = (
            series_for_chart(frame, chart, window_days=window_days)
            if frame is not None and not frame.empty else None
        )
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

            reference_build = effective_reference_build(chart, defaults)
            if not chart.inherit_reference_build and reference_build is None:
                vs_reference = 'no baseline'
                reference_detail = (
                    '2.38.0 baseline not comparable for this scenario '
                    '(test methodology changed Jul 2026).'
                )
            else:
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
                    vs_reference = comparison_label(
                        value, reference_value, defaults.regression_pct,
                    )
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


def _ticket_markdown(item: Violation, config: BenchmarkConfig) -> str:
    ticket = config.flag_tickets.get(item.test_id)
    if ticket is None:
        return '—'
    return f'[#{ticket.issue}]({ticket.url})'


def _format_section(
    title: str,
    items: List[Violation],
    config: BenchmarkConfig,
) -> List[str]:
    lines = [f'## {title}', '']
    if not items:
        lines.append('_No violations._')
        lines.append('')
        return lines
    lines.extend([
        '| Test | Variant | Value | Commit | Date | Detail | Ticket |',
        '|------|---------|-------|--------|------|--------|--------|',
    ])
    for item in sorted(items, key=lambda entry: entry.value, reverse=True):
        lines.append(
            f'| {item.test_id} | {item.variant} | {item.value:.3f}s '
            f'| `{item.commit_hash[:10]}` | {item.date} | {item.detail} '
            f'| {_ticket_markdown(item, config)} |'
        )
    lines.append('')
    return lines


def write_regression_report(
    metrics: pd.DataFrame,
    config: BenchmarkConfig,
    output_path: Path,
    *,
    violations: Optional[List[Violation]] = None,
) -> List[Violation]:
    if violations is None:
        violations = collect_violations(metrics, config)
    by_rule = {
        'Regression': [v for v in violations if v.rule == '2.1 Regression'],
        'Slow builds': [v for v in violations if v.rule == '2.2 Slow build'],
        'Backlog candidates': [v for v in violations if v.rule == '2.3 Backlog candidate'],
    }

    lines = [
        '# Desktop benchmark flags',
        '',
        f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}',
        '',
        f'**Total flags:** {len(violations)}',
        '',
    ]
    for rule_title, items in by_rule.items():
        lines.extend(_format_section(rule_title, items, config))

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
