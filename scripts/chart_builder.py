"""Build Plotly charts and write PNG + interactive HTML assets."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

import pandas as pd
import plotly.graph_objects as go

from benchmark_config import CHART_WINDOW_DAYS, ChartEntry, ChartTest

DURATION_COLOR = '#54A0FF'
DURATION_FILL = 'rgba(84, 160, 255, 0.08)'
PERFORMANCE_COLORS = ['#10AC84', '#2E86DE', '#F79F1F', '#54A0FF']

SPREAD_COLUMNS = {
    'performance': ('avg_time', 'min_time', 'max_time'),
    'cpu': ('avg_cpu', 'min_cpu', 'max_cpu'),
    'ram': ('avg_ram_mb', 'min_ram_mb', 'max_ram_mb'),
}

CHART_WIDTH = 1200
CHART_HEIGHT = 500
CHART_SCALE = 1


def filter_recent(df: pd.DataFrame, days: int = CHART_WINDOW_DAYS) -> pd.DataFrame:
    cutoff = pd.Timestamp.now().normalize() - pd.Timedelta(days=days)
    return df[df['date'] >= cutoff].copy()


def _join_runs(series: pd.Series) -> str:
    values = []
    for item in series.dropna():
        values.extend(str(item).split(','))
    return ', '.join(values)


def aggregate_by_build(
    df: pd.DataFrame,
    value_col: str,
    group_cols: Optional[List[str]] = None,
    *,
    spread_cols: Optional[Tuple[str, str]] = None,
) -> pd.DataFrame:
    keys = ['commit_hash', 'date', *(group_cols or [])]
    if spread_cols:
        min_col, max_col = spread_cols
        aggregated = df.groupby(keys, as_index=False).agg(
            **{
                value_col: (value_col, 'mean'),
                min_col: (min_col, 'min'),
                max_col: (max_col, 'max'),
                'all_runs': ('all_runs', _join_runs),
                'run_count': ('run_count', 'max'),
            }
        )
    else:
        aggregated = df.groupby(keys, as_index=False)[value_col].mean()
    aggregated = aggregated.sort_values('date')
    aggregated['tick_label'] = aggregated['date'].dt.strftime('%b %d')
    return aggregated


def _hex_to_rgba(hex_color: str, alpha: float) -> str:
    color = hex_color.lstrip('#')
    if len(color) != 6:
        return f'rgba(46, 134, 222, {alpha})'
    red, green, blue = (int(color[index:index + 2], 16) for index in (0, 2, 4))
    return f'rgba({red}, {green}, {blue}, {alpha})'


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


def _spread_hover_template(ylabel: str, value_format: str) -> str:
    return (
        f'<b>%{{fullData.name}}</b><br>'
        'Date: %{x|%b %d, %Y %H:%M}<br>'
        'Commit: %{customdata[0]}<br>'
        f'Average {ylabel}: %{{y:{value_format}}}<br>'
        f'Min {ylabel}: %{{customdata[1]:{value_format}}}<br>'
        f'Max {ylabel}: %{{customdata[2]:{value_format}}}<br>'
        'Runs (%{customdata[3]}): %{customdata[4]}'
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
    spread_cols: Optional[Tuple[str, str]] = None,
):
    if spread_cols:
        min_col, max_col = spread_cols
        fill_color = _hex_to_rgba(color, 0.18)
        fig.add_trace(go.Scatter(
            x=points['date'], y=points[max_col], mode='lines', line=dict(width=0),
            showlegend=False, hoverinfo='skip',
        ))
        fig.add_trace(go.Scatter(
            x=points['date'], y=points[min_col], mode='lines', line=dict(width=0),
            fill='tonexty', fillcolor=fill_color, showlegend=False, hoverinfo='skip',
        ))
        customdata = list(zip(
            points['commit_hash'].astype(str),
            points[min_col],
            points[max_col],
            points['run_count'].fillna(0).astype(int),
            points['all_runs'].fillna('').astype(str),
        ))
        hovertemplate = _spread_hover_template(ylabel, value_format)
    else:
        customdata = points['commit_hash'].astype(str)
        hovertemplate = _hover_template(name, ylabel, value_format=value_format)

    trace_kwargs = dict(
        x=points['date'],
        y=points[value_col],
        mode='lines+markers',
        name=name,
        line=dict(color=color, width=2.5),
        marker=dict(size=6, color=color),
        customdata=customdata,
        hovertemplate=hovertemplate,
    )
    if fill:
        trace_kwargs['fill'] = 'tozeroy'
        trace_kwargs['fillcolor'] = DURATION_FILL
    fig.add_trace(go.Scatter(**trace_kwargs))


def save_chart_assets(fig: go.Figure, output_dir: Path, graph_filename: str) -> str:
    charts_dir = output_dir / 'charts'
    charts_dir.mkdir(parents=True, exist_ok=True)
    html_filename = Path(graph_filename).with_suffix('.html').name
    fig.write_image(output_dir / graph_filename, scale=CHART_SCALE)

    html_fig = go.Figure(fig)
    html_fig.update_layout(autosize=True, width=None, height=CHART_HEIGHT)
    html_fig.write_html(
        charts_dir / html_filename,
        include_plotlyjs='directory',
        full_html=True,
        config={'responsive': True},
        default_width='100%',
        default_height='100%',
    )
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

    spread_cols = None
    value_col = chart.value_column
    if chart.show_run_spread:
        columns = SPREAD_COLUMNS.get(chart.metrics_kind)
        if columns:
            value_col, min_col, max_col = columns
            spread_cols = (min_col, max_col)

    fig = go.Figure()
    axis_points = []
    test_names = test_data['test_name'].unique()
    value_format = '.2f' if chart.metrics_kind == 'performance' else '.3f'

    for index, test_name in enumerate(test_names):
        variant_data = test_data[test_data['test_name'] == test_name]
        param_name = test_name.split('[')[1].split(']')[0] if '[' in test_name else 'default'
        color = (
            chart.color if chart.color and len(test_names) == 1
            else PERFORMANCE_COLORS[index % len(PERFORMANCE_COLORS)]
        )
        variant = aggregate_by_build(variant_data, value_col, ['test_name'], spread_cols=spread_cols)
        axis_points.append(variant)
        _add_build_trace(
            fig, variant, value_col, name=param_name, ylabel=chart.ylabel,
            color=color, value_format=value_format, spread_cols=spread_cols,
        )

    _apply_layout(
        fig, chart.display_name, chart.ylabel, pd.concat(axis_points, ignore_index=True),
        show_legend=len(test_names) > 1,
    )
    return fig


def render_chart(chart: ChartTest, metrics: pd.DataFrame, output_dir: Path) -> Optional[ChartEntry]:
    fig = build_chart_figure(chart, metrics)
    if fig is None:
        return None
    html_filename = save_chart_assets(fig, output_dir, chart.graph_filename)
    return ChartEntry(
        display_name=chart.display_name,
        html_filename=html_filename,
        footnote=chart.footnote,
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
