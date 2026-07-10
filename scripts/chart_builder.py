"""Build Plotly charts and write PNG + interactive HTML assets."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, List, Optional

import pandas as pd
import plotly.graph_objects as go

from benchmark_config import CHART_WINDOW_DAYS, ChartEntry, ChartTest

DURATION_COLOR = '#54A0FF'
DURATION_FILL = 'rgba(84, 160, 255, 0.08)'
PERFORMANCE_COLORS = ['#10AC84', '#2E86DE', '#F79F1F', '#54A0FF']

CHART_WIDTH = 1200
CHART_HEIGHT = 500
CHART_SCALE = 1


def filter_recent(df: pd.DataFrame, days: int = CHART_WINDOW_DAYS) -> pd.DataFrame:
    cutoff = pd.Timestamp.now().normalize() - pd.Timedelta(days=days)
    return df[df['date'] >= cutoff].copy()


def aggregate_by_build(
    df: pd.DataFrame,
    value_col: str,
    group_cols: Optional[List[str]] = None,
) -> pd.DataFrame:
    keys = ['commit_hash', 'date', *(group_cols or [])]
    aggregated = df.groupby(keys, as_index=False)[value_col].mean().sort_values('date')
    aggregated['tick_label'] = aggregated['date'].dt.strftime('%b %d')
    return aggregated


def match_test_pattern(series: pd.Series, pattern: str) -> pd.Series:
    escaped = re.escape(pattern)
    return series.str.contains(rf'{escaped}(?:\[|$)', regex=True, na=False)


def _hover_template(trace_name: str, ylabel: str, *, value_format: str = '.3f') -> str:
    return (
        f'<b>{trace_name}</b><br>'
        'Date: %{x|%b %d, %Y %H:%M}<br>'
        'Commit: %{customdata}<br>'
        f'{ylabel}: %{{y:{value_format}}}'
        '<extra></extra>'
    )


def _axis_ticks(axis_points: pd.DataFrame) -> pd.DataFrame:
    """One x-axis tick per calendar day (dates only — commit hash is on hover)."""
    ticks = axis_points.sort_values('date').copy()
    ticks['day'] = ticks['date'].dt.normalize()
    return ticks.drop_duplicates('day', keep='last')


def _format_date_range(dates: pd.Series) -> str:
    return f"{dates.min().strftime('%b %d')} – {dates.max().strftime('%b %d, %Y')} (last {CHART_WINDOW_DAYS} days)"


def _apply_layout(fig: go.Figure, title: str, ylabel: str, axis_points: pd.DataFrame, *, show_legend: bool):
    dates = axis_points['date']
    ticks = _axis_ticks(axis_points)
    layout = dict(
        template='plotly_white',
        title=dict(text=f'{title}<br><sup>{_format_date_range(dates)}</sup>', x=0.05, xanchor='left'),
        xaxis_title='Build date',
        yaxis_title=ylabel,
        width=CHART_WIDTH,
        height=CHART_HEIGHT,
        margin=dict(l=60, r=40, t=80, b=max(70, min(120, 50 + len(ticks) * 3))),
        hovermode='closest',
        showlegend=show_legend,
    )
    if show_legend:
        layout['legend'] = dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    fig.update_layout(**layout)
    if len(ticks) > 0:
        fig.update_xaxes(
            type='date',
            tickmode='array',
            tickvals=ticks['date'],
            ticktext=ticks['tick_label'].tolist(),
            tickangle=-45,
            showgrid=False,
        )
    else:
        fig.update_xaxes(type='date', tickformat='%b %d', showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='#E8ECF0', gridwidth=1)


def _add_build_trace(
    fig: go.Figure,
    points: pd.DataFrame,
    value_col: str,
    *,
    name: str,
    ylabel: str,
    color: str,
    value_format: str = '.3f',
    fill: bool = False,
):
    trace_kwargs = dict(
        x=points['date'],
        y=points[value_col],
        mode='lines+markers',
        name=name,
        line=dict(color=color, width=2.5),
        marker=dict(size=6, color=color),
        customdata=points['commit_hash'].astype(str),
        hovertemplate=_hover_template(name, ylabel, value_format=value_format),
    )
    if fill:
        trace_kwargs['fill'] = 'tozeroy'
        trace_kwargs['fillcolor'] = DURATION_FILL
        trace_kwargs['showlegend'] = False
    fig.add_trace(go.Scatter(**trace_kwargs))


def save_chart_assets(fig: go.Figure, output_dir: Path, graph_filename: str) -> str:
    charts_dir = output_dir / 'charts'
    charts_dir.mkdir(parents=True, exist_ok=True)
    html_filename = Path(graph_filename).with_suffix('.html').name
    fig.write_image(output_dir / graph_filename, scale=CHART_SCALE)
    fig.write_html(charts_dir / html_filename, include_plotlyjs='directory', full_html=True)
    print(f'Generated {graph_filename} and charts/{html_filename}')
    return html_filename


def build_duration_figure(summary: pd.DataFrame) -> Optional[go.Figure]:
    filtered = filter_recent(summary)
    if filtered.empty:
        return None

    points = aggregate_by_build(filtered, 'total_duration_ms')
    points = points.assign(minutes=points['total_duration_ms'] / 1000 / 60)

    fig = go.Figure()
    _add_build_trace(
        fig, points, 'minutes', name='Test suite', ylabel='Duration (minutes)',
        color=DURATION_COLOR, value_format='.2f', fill=True,
    )
    _apply_layout(fig, 'Total Test Suite Duration', 'Duration (minutes)', points, show_legend=False)
    return fig


def build_chart_figure(chart: ChartTest, metrics: pd.DataFrame) -> Optional[go.Figure]:
    filtered = filter_recent(metrics)
    test_data = filtered[match_test_pattern(filtered['test_name'], chart.pattern)].copy()
    if test_data.empty:
        print(f'Warning: No data for {chart.test_id} in the last {CHART_WINDOW_DAYS} days')
        return None

    fig = go.Figure()
    test_names = test_data['test_name'].unique()
    axis_points = []
    for index, test_name in enumerate(test_names):
        variant = aggregate_by_build(
            test_data[test_data['test_name'] == test_name],
            chart.value_column,
            ['test_name'],
        )
        axis_points.append(variant)
        param_name = test_name.split('[')[1].split(']')[0] if '[' in test_name else 'default'
        color = (
            chart.color if chart.color and len(test_names) == 1
            else PERFORMANCE_COLORS[index % len(PERFORMANCE_COLORS)]
        )
        _add_build_trace(fig, variant, chart.value_column, name=param_name, ylabel=chart.ylabel, color=color)

    _apply_layout(fig, chart.display_name, chart.ylabel, pd.concat(axis_points, ignore_index=True), show_legend=True)
    return fig


def render_chart(chart: ChartTest, metrics: pd.DataFrame, output_dir: Path) -> Optional[ChartEntry]:
    fig = build_chart_figure(chart, metrics)
    if fig is None:
        return None
    html_filename = save_chart_assets(fig, output_dir, chart.graph_filename)
    return ChartEntry(display_name=chart.display_name, html_filename=html_filename)


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
