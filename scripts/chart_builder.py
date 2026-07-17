"""Build Plotly charts and write PNG + interactive HTML assets."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, List, Optional

import numpy as np
import pandas as pd
import plotly.graph_objects as go

from benchmark_config import (
    CHART_WINDOW_DAYS,
    ChartDefaults,
    ChartEntry,
    ChartTest,
    load_desktop_build_labels,
)

PERFORMANCE_COLORS = ['#10AC84', '#2E86DE', '#F79F1F', '#54A0FF']
PRIMARY_LOAD_TIME_COLOR = '#10AC84'
ROLLING_AVG_COLOR = '#34495e'

# Reference levels for pinned release baselines (hash -> line/label color).
BASELINE_REFERENCE_COLORS = {
    '760417': '#2E86DE',  # 2.37.1
    '5f66de': '#1e8449',  # 2.38.0 (GA)
}
BASELINE_REFERENCE_COLOR_FALLBACK = ['#2E86DE', '#1e8449', '#F79F1F', '#9b59b6']

CHART_WIDTH = 1200
CHART_HEIGHT = 600
CHART_SCALE = 1
MAX_RECENT_BUILDS = 28

# Share of figure height reserved below the plot (tilted ticks + footer lines).
BOTTOM_RESERVE_RATIO = 0.34

ZONE_FAST_COLOR = 'rgba(39, 174, 96, 0.14)'
ZONE_OK_COLOR = 'rgba(241, 196, 15, 0.18)'
ZONE_SLOW_COLOR = 'rgba(192, 57, 43, 0.14)'


def filter_recent(df: pd.DataFrame, days: int = CHART_WINDOW_DAYS) -> pd.DataFrame:
    cutoff = pd.Timestamp.now().normalize() - pd.Timedelta(days=days)
    return df[df['date'] >= cutoff].copy()


def aggregate_by_build(
    df: pd.DataFrame,
    value_col: str,
    group_cols: Optional[List[str]] = None,
) -> pd.DataFrame:
    """One point per commit_hash (latest run), ordered by date — avoids same-day overlap."""
    keys = ['commit_hash', *(group_cols or [])]
    aggregated = (
        df.groupby(keys, as_index=False)
        .agg(**{value_col: (value_col, 'mean'), 'date': ('date', 'max')})
        .sort_values('date')
        .reset_index(drop=True)
    )
    aggregated['x_index'] = range(len(aggregated))
    aggregated['tick_label'] = aggregated.apply(
        lambda row: f"{row['date'].strftime('%b %d')}\n{str(row['commit_hash'])[:7]}",
        axis=1,
    )
    return aggregated


def _select_x_ticks(points: pd.DataFrame, max_ticks: int = 14) -> pd.DataFrame:
    if len(points) <= max_ticks:
        return points
    step = max(1, (len(points) - 1) // (max_ticks - 1))
    indices = list(range(0, len(points), step))
    if indices[-1] != len(points) - 1:
        indices.append(len(points) - 1)
    return points.iloc[indices]


def _format_point_label(value: float, metrics_kind: str) -> str:
    if metrics_kind == 'performance':
        return f'{value:.2f}s'
    if metrics_kind == 'cpu':
        return f'{value:.1f}%'
    return f'{value:.1f} MB'


def _hover_value_format(metrics_kind: str) -> str:
    return '.2f' if metrics_kind == 'performance' else '.1f'


def _point_label_texts(
    values: List[float],
    metrics_kind: str,
    *,
    n_baselines: int = 0,
    ref_levels: Optional[List[float]] = None,
) -> tuple[List[str], List[str]]:
    """Alternate label positions; thin out text when many builds."""
    count = len(values)
    if count <= 16:
        stride = 1
    elif count <= 28:
        stride = 2
    else:
        stride = 3
    ref_levels = ref_levels or []
    y_tol = 0.04 if metrics_kind == 'performance' else 0.5
    texts = []
    for index, value in enumerate(values):
        if index < n_baselines:
            texts.append('')
            continue
        near_ref = any(abs(value - level) < y_tol for level in ref_levels)
        if near_ref:
            texts.append('')
        elif index % stride == 0 or index == count - 1:
            texts.append(_format_point_label(value, metrics_kind))
        else:
            texts.append('')
    positions = [
        'top center' if index % 2 == 0 else 'bottom center'
        for index in range(count)
    ]
    return texts, positions


def match_test_pattern(series: pd.Series, pattern: str) -> pd.Series:
    escaped = re.escape(pattern)
    return series.str.contains(rf'{escaped}(?:\[|$)', regex=True, na=False)


def match_chart_patterns(series: pd.Series, chart: ChartTest) -> pd.Series:
    matches = match_test_pattern(series, chart.pattern)
    for pattern in chart.historical_patterns:
        matches |= match_test_pattern(series, pattern)
    return matches


def variant_name(test_name: str) -> str:
    if '[' in test_name and ']' in test_name:
        return test_name.split('[')[1].split(']')[0]
    return 'default'


def _version_from_label(label: str) -> str:
    """Extract release version from a CSV label (date|version · hash)."""
    if '|' not in label:
        return label.strip()
    return label.split('|', 1)[1].split('·')[0].strip()


def _baseline_tick_label(build_labels: dict[str, str], commit_hash: str) -> str:
    raw = build_labels.get(commit_hash, '')
    version = _version_from_label(raw) if raw else commit_hash[:7]
    return f'{version}\nbaseline'


def series_for_chart(
    metrics: pd.DataFrame,
    chart: ChartTest,
    build_labels: Optional[dict[str, str]] = None,
) -> Optional[tuple[pd.DataFrame, int]]:
    """Filter metrics to one chart pattern and aggregate to one point per build.

    Returns (series, n_baselines). n_baselines is 0 when pinning is inactive.
    """
    filtered = filter_recent(metrics)
    test_data = filtered[match_chart_patterns(filtered['test_name'], chart)].copy()
    if test_data.empty:
        return None
    test_data['test_name'] = chart.pattern
    aggregated = aggregate_by_build(test_data, chart.value_column, ['test_name'])
    if aggregated.empty:
        return None

    labels = build_labels if build_labels is not None else {}
    n_baselines = 0
    if chart.baselines:
        present = set(aggregated['commit_hash'].astype(str))
        base_order = [h for h in chart.baselines if h in present]
        if base_order:
            baseline_set = set(base_order)
            recent = (
                aggregated[~aggregated['commit_hash'].astype(str).isin(baseline_set)]
                .sort_values('date')
                .tail(MAX_RECENT_BUILDS)
            )
            order_hashes = base_order + recent['commit_hash'].astype(str).tolist()
            aggregated = aggregated[aggregated['commit_hash'].astype(str).isin(order_hashes)].copy()
            order_map = {h: index for index, h in enumerate(order_hashes)}
            aggregated['_sort'] = aggregated['commit_hash'].astype(str).map(order_map)
            aggregated = (
                aggregated.sort_values('_sort')
                .drop(columns='_sort')
                .reset_index(drop=True)
            )
            aggregated['x_index'] = range(len(aggregated))
            n_baselines = len(base_order)

            def tick_label(row: pd.Series) -> str:
                commit_hash = str(row['commit_hash'])
                if int(row['x_index']) < n_baselines:
                    return _baseline_tick_label(labels, commit_hash)
                return f"{row['date'].strftime('%b %d')}\n{commit_hash[:7]}"

            aggregated['tick_label'] = aggregated.apply(tick_label, axis=1)

    return aggregated, n_baselines


def _rolling_mean(values: List[float], window: int) -> List[float]:
    result = []
    for index in range(len(values)):
        chunk = values[max(0, index - window + 1):index + 1]
        result.append(sum(chunk) / len(chunk))
    return result


def _hover_template(trace_name: str, ylabel: str, *, value_format: str = '.3f') -> str:
    return (
        f'<b>{trace_name}</b><br>'
        'Commit: %{customdata[0]}<br>'
        'Date: %{customdata[1]}<br>'
        f'{ylabel}: %{{y:{value_format}}}'
        '<extra></extra>'
    )


def _trace_customdata(points: pd.DataFrame) -> list:
    return np.column_stack([
        points['commit_hash'].astype(str),
        points['date'].dt.strftime('%b %d, %Y %H:%M'),
    ]).tolist()


def _axis_ticks(axis_points: pd.DataFrame, n_baselines: int = 0) -> pd.DataFrame:
    if 'x_index' in axis_points.columns:
        sorted_pts = axis_points.sort_values('x_index')
        selected = _select_x_ticks(sorted_pts)
        if n_baselines > 0:
            baseline_ticks = sorted_pts[sorted_pts['x_index'] < n_baselines]
            selected = pd.concat([
                baseline_ticks,
                selected[~selected['x_index'].isin(baseline_ticks['x_index'])],
            ]).drop_duplicates('x_index').sort_values('x_index')
        return selected
    ticks = axis_points.sort_values('date').copy()
    ticks['day'] = ticks['date'].dt.normalize()
    return ticks.drop_duplicates('day', keep='last')


def compose_chart_footnote(chart: ChartTest) -> str:
    """Return chart footnote (account type + aggregation; runner info lives on the dashboard)."""
    return chart.footnote.strip()


def _build_title(chart: ChartTest) -> str:
    parts = [f'<b>{chart.display_name}</b>']
    if chart.description:
        parts.append(
            f'<br><span style="font-size:12px;color:#656d76;">{chart.description}</span>'
        )
    return ''.join(parts)


def _add_chart_footer(
    fig: go.Figure,
    *,
    show_zones: bool,
    normal_range_label: str,
    footnote: str,
    plot_height_px: float,
) -> None:
    """Place zone legend and account footnote below tilted x-axis tick labels."""
    # Paper y is relative to plot height; tilted two-line ticks need ~0.45× plot height.
    tick_clearance = 0.46
    line_gap = 18 / max(plot_height_px, 1)
    zones_y = -(tick_clearance)
    if show_zones:
        fig.add_annotation(
            xref='paper', yref='paper', x=0.5, y=zones_y,
            text=(
                'zones: &lt;0.5s fast · 0.5–0.9s ok · '
                '0.9–1.0s ok near slow · &gt;1.0s slow'
            ),
            showarrow=False, xanchor='center', yanchor='top',
            font=dict(size=9, color='#888888'),
        )
    next_y = zones_y - line_gap if show_zones else zones_y
    if normal_range_label:
        fig.add_annotation(
            xref='paper', yref='paper', x=0.5, y=next_y,
            text=f'dotted = {normal_range_label} normal range',
            showarrow=False, xanchor='center', yanchor='top',
            font=dict(size=9, color='#888888'),
        )
        next_y -= line_gap
    if footnote:
        fig.add_annotation(
            xref='paper', yref='paper', x=0.5,
            y=next_y,
            text=footnote,
            showarrow=False, xanchor='center', yanchor='top',
            font=dict(size=9, color='#888888'),
        )


def _add_speed_zones(
    fig: go.Figure,
    *,
    ymax: float,
    fast_threshold: float,
    slow_threshold: float,
):
    fig.add_hrect(y0=0, y1=min(fast_threshold, ymax), fillcolor=ZONE_FAST_COLOR, line_width=0, layer='below')
    if ymax > fast_threshold:
        fig.add_hrect(
            y0=fast_threshold, y1=min(slow_threshold, ymax),
            fillcolor=ZONE_OK_COLOR, line_width=0, layer='below',
        )
        fig.add_hline(y=fast_threshold, line_dash='dash', line_color='#1e8449', line_width=1, opacity=0.5)
        fig.add_annotation(
            x=1, y=fast_threshold, xref='paper', yref='y',
            text=f' {fast_threshold:.1f}s · fast', showarrow=False,
            xanchor='right', yanchor='bottom', font=dict(size=10, color='#1e8449'),
        )
    if ymax > slow_threshold:
        fig.add_hrect(y0=slow_threshold, y1=ymax, fillcolor=ZONE_SLOW_COLOR, line_width=0, layer='below')
        fig.add_hline(y=slow_threshold, line_dash='dash', line_color='#c0392b', line_width=1, opacity=0.5)
        fig.add_annotation(
            x=1, y=slow_threshold, xref='paper', yref='y',
            text=f' {slow_threshold:.1f}s · slow', showarrow=False,
            xanchor='right', yanchor='bottom', font=dict(size=10, color='#c0392b'),
        )


def _bottom_margin(*, show_zones: bool, normal_range_label: str, footnote: str) -> int:
    reserve = int(CHART_HEIGHT * BOTTOM_RESERVE_RATIO)
    if show_zones:
        reserve += 14
    if normal_range_label:
        reserve += 14
    if footnote.strip():
        reserve += 14
    return reserve


def _reference_builds_for_chart(chart: ChartTest) -> tuple[str, ...]:
    if chart.baselines:
        return chart.baselines
    if chart.reference_build:
        return (chart.reference_build,)
    return ()


def _reference_line_color(commit_hash: str, index: int) -> str:
    return BASELINE_REFERENCE_COLORS.get(
        commit_hash,
        BASELINE_REFERENCE_COLOR_FALLBACK[index % len(BASELINE_REFERENCE_COLOR_FALLBACK)],
    )


def _reference_label_text(level: float, version: str, metrics_kind: str) -> str:
    return f'{version} ({_format_point_label(level, metrics_kind)})'


def _add_reference_lines(
    fig: go.Figure,
    points: pd.DataFrame,
    value_col: str,
    reference_builds: tuple[str, ...],
    build_labels: Optional[dict[str, str]] = None,
    *,
    ymax: float,
    metrics_kind: str = 'performance',
):
    labels = build_labels or {}
    refs: list[tuple[float, str, str, int]] = []
    for index, commit_hash in enumerate(reference_builds):
        ref_rows = points[points['commit_hash'].astype(str) == commit_hash]
        if ref_rows.empty:
            continue
        level = float(ref_rows[value_col].iloc[0])
        label = (
            _version_from_label(labels[commit_hash])
            if commit_hash in labels
            else commit_hash[:8]
        )
        color = _reference_line_color(commit_hash, index)
        x_pos = int(ref_rows['x_index'].iloc[0])
        refs.append((level, label, color, x_pos))

    min_label_gap = ymax * 0.06
    close_labels = (
        len(refs) > 1
        and abs(refs[0][0] - refs[1][0]) < min_label_gap
    )
    higher_idx = (
        0 if refs[0][0] >= refs[1][0] else 1
    ) if close_labels else 0
    label_offset_px = 4
    for index, (level, label, color, x_pos) in enumerate(refs):
        fig.add_shape(
            type='line',
            xref='paper', x0=0, x1=1,
            yref='y', y0=level, y1=level,
            line=dict(color=color, width=1.2),
            layer='below',
        )
        if close_labels:
            if index == higher_idx:
                yanchor, yshift = 'bottom', label_offset_px
            else:
                yanchor, yshift = 'top', -label_offset_px
        else:
            yanchor, yshift = 'bottom', label_offset_px
        fig.add_annotation(
            x=x_pos, y=level, xref='x', yref='y',
            text=f' {_reference_label_text(level, label, metrics_kind)}',
            showarrow=False,
            xanchor='center',
            yanchor=yanchor,
            yshift=yshift,
            font=dict(size=9, color=color),
        )


def _add_normal_range(
    fig: go.Figure,
    points: pd.DataFrame,
    chart: ChartTest,
    defaults: ChartDefaults,
    build_labels: dict[str, str],
) -> str:
    if chart.metrics_kind != 'performance':
        return ''
    reference_build = chart.reference_build or defaults.reference_build
    if not reference_build:
        return ''
    reference_rows = points[points['commit_hash'].astype(str) == reference_build]
    if reference_rows.empty:
        return ''

    reference_value = float(reference_rows[chart.value_column].iloc[0])
    for level in (
        reference_value * (1 - defaults.regression_pct),
        reference_value * (1 + defaults.regression_pct),
    ):
        fig.add_hline(
            y=level,
            line_dash='dot',
            line_color='#555555',
            line_width=0.9,
            opacity=0.55,
            layer='below',
        )
    raw_label = build_labels.get(reference_build, '')
    version = _version_from_label(raw_label) if raw_label else reference_build[:8]
    return f'{version} ±{defaults.regression_pct:.0%}'


def _add_baseline_separator(fig: go.Figure, n_baselines: int, n_points: int) -> None:
    if not (0 < n_baselines < n_points):
        return
    fig.add_vline(
        x=n_baselines - 0.5,
        line_color='#bbbbbb',
        line_width=1,
        opacity=0.9,
    )
    fig.add_annotation(
        xref='x', yref='paper',
        x=n_baselines - 0.5, y=1.0,
        text='baselines | trend',
        showarrow=False,
        xanchor='center', yanchor='bottom',
        font=dict(size=7, color='#999999'),
    )


def _apply_layout(
    fig: go.Figure,
    chart: ChartTest,
    ylabel: str,
    axis_points: pd.DataFrame,
    *,
    show_legend: bool,
    ymax: float,
    show_zones: bool,
    normal_range_label: str = '',
    footnote: str = '',
    chart_width: int = CHART_WIDTH,
    n_baselines: int = 0,
):
    ticks = _axis_ticks(axis_points, n_baselines=n_baselines)
    uses_build_index = 'x_index' in axis_points.columns
    top_margin = 95 if chart.description else 80
    bottom = _bottom_margin(
        show_zones=show_zones,
        normal_range_label=normal_range_label,
        footnote=footnote,
    )
    plot_height_px = CHART_HEIGHT - top_margin - bottom
    title_pad = dict(b=12)

    layout = dict(
        template='plotly_white',
        title=dict(
            text=_build_title(chart),
            x=0.05, xanchor='left', pad=title_pad,
        ),
        xaxis_title='',
        yaxis_title=ylabel,
        width=chart_width,
        height=CHART_HEIGHT,
        margin=dict(l=60, r=60, t=top_margin, b=bottom),
        hovermode='closest',
        showlegend=show_legend,
        yaxis=dict(range=[0, ymax], showgrid=True, gridcolor='#E8ECF0', gridwidth=1),
    )
    if show_legend:
        layout['legend'] = dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    fig.update_layout(**layout)

    if len(ticks) > 0 and uses_build_index:
        fig.update_xaxes(
            type='linear',
            tickmode='array',
            tickvals=ticks['x_index'].tolist(),
            ticktext=ticks['tick_label'].tolist(),
            tickangle=-40,
            tickfont=dict(size=9),
            ticklabelposition='outside',
            automargin=False,
            showgrid=True,
            gridcolor='#F0F2F5',
            gridwidth=1,
        )
    elif len(ticks) > 0:
        fig.update_xaxes(
            type='date',
            tickmode='array',
            tickvals=ticks['date'],
            ticktext=ticks['tick_label'].tolist(),
            tickangle=-40,
            tickfont=dict(size=10),
            showgrid=False,
        )
    else:
        fig.update_xaxes(type='linear', showgrid=False)

    _add_chart_footer(
        fig,
        show_zones=show_zones,
        normal_range_label=normal_range_label,
        footnote=footnote,
        plot_height_px=plot_height_px,
    )


def _disconnected_trace_series(
    points: pd.DataFrame,
    value_col: str,
    *,
    n_baselines: int = 0,
) -> tuple[list, list]:
    """Break lines between pinned baseline columns and before trend."""
    x_out: list = []
    y_out: list = []
    rows = points.reset_index(drop=True)
    for pos in range(len(rows)):
        row = rows.iloc[pos]
        if x_out and n_baselines > 0:
            prev_x = int(rows.iloc[pos - 1]['x_index'])
            curr_x = int(row['x_index'])
            if prev_x < n_baselines or curr_x < n_baselines:
                x_out.append(None)
                y_out.append(None)
        x_out.append(int(row['x_index']))
        y_out.append(row[value_col])
    return x_out, y_out


def _add_build_trace(
    fig: go.Figure,
    points: pd.DataFrame,
    value_col: str,
    *,
    name: str,
    ylabel: str,
    color: str,
    value_format: str = '.3f',
    show_point_labels: bool = False,
    metrics_kind: str = 'performance',
    n_baselines: int = 0,
    ref_levels: Optional[List[float]] = None,
):
    x_col = 'x_index' if 'x_index' in points.columns else 'date'
    values = points[value_col].tolist()
    if x_col == 'x_index' and n_baselines > 0:
        x_values, y_values = _disconnected_trace_series(
            points.reset_index(drop=True), value_col, n_baselines=n_baselines,
        )
        full_cd = _trace_customdata(points)
        customdata: list = []
        value_idx = 0
        for x in x_values:
            if x is None:
                customdata.append(['', ''])
            else:
                customdata.append(full_cd[value_idx])
                value_idx += 1
        # Map disconnected indices back to text labels (skip None slots).
        if show_point_labels:
            full_text, full_pos = _point_label_texts(
                values, metrics_kind, n_baselines=n_baselines, ref_levels=ref_levels,
            )
            text, textposition = [], []
            value_idx = 0
            for x in x_values:
                if x is None:
                    text.append('')
                    textposition.append('top center')
                else:
                    text.append(full_text[value_idx])
                    textposition.append(full_pos[value_idx])
                    value_idx += 1
            mode = 'lines+markers+text'
        else:
            text, textposition = None, None
            mode = 'lines+markers'
    else:
        x_values = points[x_col].tolist()
        y_values = values
        customdata = _trace_customdata(points)
        if show_point_labels:
            text, textposition = _point_label_texts(
                values, metrics_kind, n_baselines=n_baselines, ref_levels=ref_levels,
            )
            mode = 'lines+markers+text'
        else:
            text, textposition = None, None
            mode = 'lines+markers'
    marker_size = 6 if len(points) > 24 else 7
    trace_kwargs = dict(
        x=x_values,
        y=y_values,
        mode=mode,
        name=name,
        line=dict(color=color, width=2.5),
        marker=dict(size=marker_size, color=color),
        customdata=customdata,
        hovertemplate=_hover_template(name, ylabel, value_format=value_format),
        text=text,
        textposition=textposition,
        textfont=dict(size=8, color=color),
        cliponaxis=False,
        connectgaps=False,
    )
    fig.add_trace(go.Scatter(**trace_kwargs))


def _add_rolling_average_trace(
    fig: go.Figure,
    points: pd.DataFrame,
    value_col: str,
    *,
    window: int,
    ylabel: str,
    value_format: str = '.2f',
):
    values = points[value_col].tolist()
    if len(values) < 4:
        return
    rolling = _rolling_mean(values, window)
    x_col = 'x_index' if 'x_index' in points.columns else 'date'
    fig.add_trace(go.Scatter(
        x=points[x_col],
        y=rolling,
        mode='lines',
        name=f'{window}-build average',
        line=dict(color=ROLLING_AVG_COLOR, width=1.8),
        opacity=0.65,
        customdata=_trace_customdata(points),
        hovertemplate=_hover_template(f'{window}-build average', ylabel, value_format=value_format),
    ))


def _add_rolling_average_trace_trend_only(
    fig: go.Figure,
    points: pd.DataFrame,
    value_col: str,
    *,
    n_baselines: int,
    window: int,
    ylabel: str,
    value_format: str = '.2f',
):
    trend = points[points['x_index'] >= n_baselines] if n_baselines > 0 else points
    _add_rolling_average_trace(
        fig, trend, value_col,
        window=window, ylabel=ylabel, value_format=value_format,
    )


def save_chart_assets(fig: go.Figure, output_dir: Path, graph_filename: str) -> str:
    charts_dir = output_dir / 'charts'
    charts_dir.mkdir(parents=True, exist_ok=True)
    html_filename = Path(graph_filename).with_suffix('.html').name
    fig.write_image(output_dir / graph_filename, scale=CHART_SCALE)
    html_figure = go.Figure(fig)
    html_figure.update_layout(width=None, height=None, autosize=True)
    html_path = charts_dir / html_filename
    html_figure.write_html(
        html_path,
        include_plotlyjs='directory',
        full_html=True,
        config={'responsive': True},
        default_width='100%',
        default_height='100%',
    )
    html = html_path.read_text(encoding='utf-8')
    html = html.replace(
        '<head>',
        '<head><style>'
        'html,body,.plotly-graph-div{width:100%;height:100%;margin:0;overflow:hidden;}'
        '</style>',
        1,
    )
    html_path.write_text(html, encoding='utf-8')
    print(f'Generated {graph_filename} and charts/{html_filename}')
    return html_filename


def build_chart_figure(
    chart: ChartTest,
    metrics: pd.DataFrame,
    defaults: ChartDefaults,
    *,
    footnote: str = '',
    build_labels: Optional[dict[str, str]] = None,
) -> Optional[go.Figure]:
    labels = build_labels if build_labels is not None else load_desktop_build_labels()
    result = series_for_chart(metrics, chart, labels)
    if result is None:
        print(f'Warning: No data for {chart.test_id} in the last {CHART_WINDOW_DAYS} days')
        return None
    series, n_baselines = result

    fig = go.Figure()
    value_format = _hover_value_format(chart.metrics_kind)
    show_point_labels = True
    color = chart.color or (
        PRIMARY_LOAD_TIME_COLOR if chart.metrics_kind == 'performance'
        else PERFORMANCE_COLORS[0]
    )
    show_legend = bool(chart.show_rolling_average)

    ref_builds = _reference_builds_for_chart(chart)
    ref_levels = [
        float(series.loc[series['commit_hash'].astype(str) == h, chart.value_column].iloc[0])
        for h in ref_builds
        if not series.loc[series['commit_hash'].astype(str) == h].empty
    ]

    _add_build_trace(
        fig, series, chart.value_column, name='per build', ylabel=chart.ylabel,
        color=color, value_format=value_format, show_point_labels=show_point_labels,
        metrics_kind=chart.metrics_kind, n_baselines=n_baselines, ref_levels=ref_levels,
    )
    if chart.show_rolling_average:
        _add_rolling_average_trace_trend_only(
            fig, series, chart.value_column,
            n_baselines=n_baselines,
            window=defaults.rolling_window, ylabel=chart.ylabel, value_format=value_format,
        )
        trend_len = len(series) - n_baselines if n_baselines > 0 else len(series)
        if trend_len >= 4:
            show_legend = True

    ymax = series[chart.value_column].max() * 1.35
    show_zones = chart.show_speed_zones and chart.metrics_kind == 'performance'
    if show_zones:
        ymax = max(ymax, defaults.slow_threshold_s * 1.1)
        _add_speed_zones(
            fig, ymax=ymax,
            fast_threshold=defaults.fast_threshold_s,
            slow_threshold=defaults.slow_threshold_s,
        )

    _add_reference_lines(
        fig, series, chart.value_column, ref_builds, labels,
        ymax=ymax, metrics_kind=chart.metrics_kind,
    )
    normal_range_label = _add_normal_range(fig, series, chart, defaults, labels)
    _add_baseline_separator(fig, n_baselines, len(series))

    n_points = len(series)
    chart_width = max(CHART_WIDTH, min(2000, 800 + n_points * 24))

    _apply_layout(
        fig, chart, chart.ylabel, series,
        show_legend=show_legend, ymax=ymax, show_zones=show_zones,
        normal_range_label=normal_range_label, footnote=footnote,
        chart_width=chart_width, n_baselines=n_baselines,
    )
    return fig


def render_chart(
    chart: ChartTest,
    metrics: pd.DataFrame,
    output_dir: Path,
    defaults: ChartDefaults,
) -> Optional[ChartEntry]:
    footnote = compose_chart_footnote(chart)
    fig = build_chart_figure(chart, metrics, defaults, footnote=footnote)
    if fig is None:
        return None
    html_filename = save_chart_assets(fig, output_dir, chart.graph_filename)
    return ChartEntry(
        display_name=chart.display_name,
        html_filename=html_filename,
        footnote=footnote,
    )


def cleanup_stale_charts(output_dir: Path, graph_filenames: Iterable[str]):
    expected_png = set(graph_filenames)
    for png in output_dir.glob('*.png'):
        if png.name not in expected_png:
            png.unlink()
            print(f'Removed stale chart: {png.name}')

    charts_dir = output_dir / 'charts'
    if not charts_dir.exists():
        return
    expected_html = {Path(name).with_suffix('.html').name for name in expected_png}
    for html_file in charts_dir.glob('*.html'):
        if html_file.name not in expected_html:
            html_file.unlink()
            print(f'Removed stale chart: charts/{html_file.name}')
