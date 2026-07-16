"""Build Plotly charts and write PNG + interactive HTML assets."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, List, Optional

import numpy as np
import pandas as pd
import plotly.graph_objects as go

from benchmark_config import CHART_WINDOW_DAYS, ChartDefaults, ChartEntry, ChartTest

PERFORMANCE_COLORS = ['#10AC84', '#2E86DE', '#F79F1F', '#54A0FF']
PRIMARY_LOAD_TIME_COLOR = '#10AC84'
ROLLING_AVG_COLOR = '#34495e'

CHART_WIDTH = 1200
CHART_HEIGHT = 600
CHART_SCALE = 1

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


def _point_label_texts(values: List[float], metrics_kind: str) -> tuple[List[str], List[str]]:
    """Alternate label positions; thin out text when many builds."""
    count = len(values)
    if count <= 16:
        stride = 1
    elif count <= 28:
        stride = 2
    else:
        stride = 3
    texts = [
        _format_point_label(value, metrics_kind) if index % stride == 0 or index == count - 1 else ''
        for index, value in enumerate(values)
    ]
    positions = [
        'top center' if index % 2 == 0 else 'bottom center'
        for index in range(count)
    ]
    return texts, positions


def match_test_pattern(series: pd.Series, pattern: str) -> pd.Series:
    escaped = re.escape(pattern)
    return series.str.contains(rf'{escaped}(?:\[|$)', regex=True, na=False)


def variant_name(test_name: str) -> str:
    if '[' in test_name and ']' in test_name:
        return test_name.split('[')[1].split(']')[0]
    return 'default'


def series_for_chart(metrics: pd.DataFrame, chart: ChartTest) -> Optional[pd.DataFrame]:
    """Filter metrics to one chart pattern and aggregate to one point per build."""
    filtered = filter_recent(metrics)
    test_data = filtered[match_test_pattern(filtered['test_name'], chart.pattern)].copy()
    if test_data.empty:
        return None
    aggregated = aggregate_by_build(test_data, chart.value_column, ['test_name'])
    return aggregated if not aggregated.empty else None


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


def _axis_ticks(axis_points: pd.DataFrame) -> pd.DataFrame:
    if 'x_index' in axis_points.columns:
        return _select_x_ticks(axis_points.sort_values('x_index'))
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
            text='zones: &lt;0.5s fast · 0.5–1.0s ok · &gt;1.0s slow',
            showarrow=False, xanchor='center', yanchor='top',
            font=dict(size=9, color='#888888'),
        )
    if footnote:
        fig.add_annotation(
            xref='paper', yref='paper', x=0.5,
            y=zones_y - line_gap if show_zones else zones_y,
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


def _bottom_margin(*, show_zones: bool, footnote: str) -> int:
    reserve = int(CHART_HEIGHT * BOTTOM_RESERVE_RATIO)
    if show_zones:
        reserve += 14
    if footnote.strip():
        reserve += 14
    return reserve


def _add_reference_line(
    fig: go.Figure,
    points: pd.DataFrame,
    value_col: str,
    reference_build: Optional[str],
    label: str = '',
):
    if not reference_build:
        return
    ref_rows = points[points['commit_hash'] == reference_build]
    if ref_rows.empty:
        return
    level = float(ref_rows[value_col].iloc[0])
    fig.add_hline(y=level, line_color='#333333', line_width=1.1, opacity=0.85)
    fig.add_annotation(
        x=1, y=level, xref='paper', yref='y',
        text=f' {label or reference_build[:8]}', showarrow=False,
        xanchor='right', yanchor='bottom', font=dict(size=9, color='#333333'),
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
    footnote: str = '',
    chart_width: int = CHART_WIDTH,
):
    ticks = _axis_ticks(axis_points)
    uses_build_index = 'x_index' in axis_points.columns
    top_margin = 95 if chart.description else 80
    bottom = _bottom_margin(show_zones=show_zones, footnote=footnote)
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
        fig, show_zones=show_zones, footnote=footnote, plot_height_px=plot_height_px,
    )


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
):
    x_col = 'x_index' if 'x_index' in points.columns else 'date'
    values = points[value_col].tolist()
    if show_point_labels:
        text, textposition = _point_label_texts(values, metrics_kind)
        mode = 'lines+markers+text'
    else:
        text, textposition = None, None
        mode = 'lines+markers'
    marker_size = 6 if len(points) > 24 else 7
    trace_kwargs = dict(
        x=points[x_col],
        y=points[value_col],
        mode=mode,
        name=name,
        line=dict(color=color, width=2.5),
        marker=dict(size=marker_size, color=color),
        customdata=_trace_customdata(points),
        hovertemplate=_hover_template(name, ylabel, value_format=value_format),
        text=text,
        textposition=textposition,
        textfont=dict(size=8, color=color),
        cliponaxis=False,
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


def save_chart_assets(fig: go.Figure, output_dir: Path, graph_filename: str) -> str:
    charts_dir = output_dir / 'charts'
    charts_dir.mkdir(parents=True, exist_ok=True)
    html_filename = Path(graph_filename).with_suffix('.html').name
    fig.write_image(output_dir / graph_filename, scale=CHART_SCALE)
    fig.write_html(charts_dir / html_filename, include_plotlyjs='directory', full_html=True)
    print(f'Generated {graph_filename} and charts/{html_filename}')
    return html_filename


def build_chart_figure(
    chart: ChartTest,
    metrics: pd.DataFrame,
    defaults: ChartDefaults,
    *,
    footnote: str = '',
) -> Optional[go.Figure]:
    series = series_for_chart(metrics, chart)
    if series is None:
        print(f'Warning: No data for {chart.test_id} in the last {CHART_WINDOW_DAYS} days')
        return None

    fig = go.Figure()
    value_format = _hover_value_format(chart.metrics_kind)
    show_point_labels = True
    color = chart.color or (
        PRIMARY_LOAD_TIME_COLOR if chart.metrics_kind == 'performance'
        else PERFORMANCE_COLORS[0]
    )
    show_legend = bool(chart.show_rolling_average)

    _add_build_trace(
        fig, series, chart.value_column, name='per build', ylabel=chart.ylabel,
        color=color, value_format=value_format, show_point_labels=show_point_labels,
        metrics_kind=chart.metrics_kind,
    )
    if chart.show_rolling_average:
        _add_rolling_average_trace(
            fig, series, chart.value_column,
            window=defaults.rolling_window, ylabel=chart.ylabel, value_format=value_format,
        )
        if len(series) >= 4:
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

    _add_reference_line(fig, series, chart.value_column, chart.reference_build)

    n_points = len(series)
    chart_width = max(CHART_WIDTH, min(2000, 800 + n_points * 24))

    _apply_layout(
        fig, chart, chart.ylabel, series,
        show_legend=show_legend, ymax=ymax, show_zones=show_zones,
        footnote=footnote, chart_width=chart_width,
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
