"""Static HTML site generator for GitHub Pages benchmark dashboard."""

from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Optional

import pandas as pd

from benchmark_config import CHART_WINDOW_DAYS, BenchmarkPage, ChartEntry, ChartTest
from environment_parser import RUN_ENVIRONMENT_FIELDS
from regression_report import ScenarioSummary

CHARTS_DIR = 'charts'
SITE_TITLE = 'Status App Benchmarks'
MACHINE_FIELD_LABELS = {
    'hostname': 'Host',
    'windows_version': 'Windows',
    'os_build': 'OS build',
    'cpu': 'CPU',
    'ram_gb': 'RAM',
}
PRODUCT_AREAS = (
    ('wallet', 'Wallet'),
    ('messenger', 'Messenger'),
    ('communities', 'Communities'),
    ('browser', 'Browser'),
)
STATUS_LABELS = {
    'fast': 'Fast',
    'ok': 'Ok',
    'ok-warn': 'Ok',
    'slow': 'Slow',
    'neutral': 'No time threshold',
    'no-data': 'No data',
    'not-tested': 'Not tested',
}


def _page_styles() -> str:
    return """
    :root {
      color-scheme: light dark;
      --bg: #f6f8fa;
      --card: #ffffff;
      --text: #1f2328;
      --muted: #656d76;
      --border: #d0d7de;
      --link: #0969da;
      --header-bg: #24292f;
      --header-text: #ffffff;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #0d1117;
        --card: #161b22;
        --text: #e6edf3;
        --muted: #8b949e;
        --border: #30363d;
        --link: #58a6ff;
        --header-bg: #010409;
        --header-text: #e6edf3;
      }
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
    }
    header {
      background: var(--header-bg);
      color: var(--header-text);
      padding: 1.25rem 1.5rem;
    }
    header a { color: var(--header-text); text-decoration: none; }
    header a:hover { text-decoration: underline; }
    main { max-width: 1200px; margin: 0 auto; padding: 1.5rem; }
    h1 { margin: 0 0 0.25rem; font-size: 1.5rem; }
    .subtitle { color: var(--muted); margin: 0; }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }
    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem 1.25rem;
      text-decoration: none;
      color: inherit;
      transition: border-color 0.15s;
    }
    .card:hover { border-color: var(--link); }
    .card h2 { margin: 0 0 0.5rem; font-size: 1.1rem; }
    .card p { margin: 0; color: var(--muted); font-size: 0.9rem; }
    .profile-facts {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 0.35rem 0.75rem;
      margin-top: 0.85rem;
      color: var(--muted);
      font-size: 0.78rem;
    }
    .profile-facts span:first-child { grid-column: 1 / -1; }
    .profile-details {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem 1.25rem;
      margin: 1rem 0 1.5rem;
    }
    .profile-details h2 { margin: 0 0 0.75rem; font-size: 1.05rem; }
    .profile-details-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
    }
    .profile-details h3 { margin: 0 0 0.35rem; font-size: 0.9rem; }
    .profile-details dl { margin: 0; }
    .profile-details dt { color: var(--muted); font-size: 0.78rem; }
    .profile-details dd { margin: 0 0 0.3rem; font-weight: 500; }
    .area-group { margin-top: 2rem; }
    .area-group > h2 { margin-bottom: 0.75rem; }
    .area-empty {
      border: 1px dashed var(--border);
      border-radius: 8px;
      padding: 1rem 1.25rem;
      color: var(--muted);
    }
    .summary-link {
      display: inline-block;
      margin-top: 1rem;
      color: var(--link);
      text-decoration: none;
      font-weight: 600;
    }
    .summary-link:hover { text-decoration: underline; }
    .summary-profile { margin: 2rem 0; }
    .summary-profile h2 { margin-bottom: 0.25rem; }
    .summary-table {
      width: 100%;
      border-collapse: collapse;
      background: var(--card);
      border: 1px solid var(--border);
      margin-top: 0.75rem;
      font-size: 0.88rem;
    }
    .summary-table th,
    .summary-table td {
      padding: 0.65rem 0.75rem;
      border-bottom: 1px solid var(--border);
      text-align: left;
      vertical-align: top;
    }
    .summary-table th { color: var(--muted); font-size: 0.78rem; }
    .summary-table .load-time-column {
      min-width: 145px;
      white-space: nowrap;
    }
    .summary-table .reference-column {
      min-width: 105px;
      white-space: nowrap;
    }
    .summary-table tr:last-child td { border-bottom: 0; }
    .load-time-cell {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.4rem;
    }
    .metric-value { white-space: nowrap; font-weight: 600; }
    .status {
      display: inline-block;
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 0.1rem 0.45rem;
      margin: 0 0.2rem 0.2rem 0;
      white-space: nowrap;
      font-size: 0.75rem;
      font-weight: 600;
    }
    .status-fast { color: #1a7f37; border-color: #1a7f37; }
    .status-ok { color: var(--link); border-color: var(--link); }
    .status-ok-warn { color: #9a6700; border-color: #9a6700; }
    .status-slow { color: #cf222e; border-color: #cf222e; }
    .status-neutral,
    .status-no-data,
    .status-not-tested { color: var(--muted); }
    .speed-legend {
      display: inline-flex;
      flex-wrap: wrap;
      gap: 0.25rem 0.75rem;
      margin-top: 0.2rem;
    }
    .speed-fast { color: #1a7f37; font-weight: 600; }
    .speed-ok { color: var(--link); font-weight: 600; }
    .speed-ok-warn { color: #9a6700; font-weight: 600; }
    .speed-slow { color: #cf222e; font-weight: 600; }
    .reference-value { font-weight: 600; white-space: nowrap; }
    .reference-parity,
    .reference-improvement { color: #1a7f37; }
    .reference-regression { color: #cf222e; }
    .reference-neutral { color: var(--muted); }
    section.chart {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem 1.25rem 1.25rem;
      margin-bottom: 1.5rem;
    }
    section.chart iframe {
      width: 100%;
      height: 600px;
      border: 0;
      border-radius: 4px;
      background: #fff;
      display: block;
    }
    .chart-footnote {
      color: var(--muted);
      font-size: 0.85rem;
      margin: 0.5rem 0 0;
    }
    section.chart-placeholder {
      border-style: dashed;
      background: transparent;
    }
    .placeholder-note {
      color: var(--muted);
      font-size: 0.9rem;
      margin: 0;
      font-style: italic;
    }
    .note { color: var(--muted); font-size: 0.9rem; margin: 1rem 0 0; }
    nav.back { margin-bottom: 1rem; }
    nav.back a { color: var(--link); text-decoration: none; }
    nav.back a:hover { text-decoration: underline; }
    section.machine-info {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem 1.25rem;
      margin: 1rem 0 1.5rem;
      font-size: 0.95rem;
    }
    section.machine-info h2 {
      margin: 0 0 0.5rem;
      font-size: 1.05rem;
    }
    section.machine-info dl {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 0.5rem 1.5rem;
      margin: 0;
    }
    section.machine-info dt {
      margin: 0;
      color: var(--muted);
      font-size: 0.85rem;
    }
    section.machine-info dd {
      margin: 0.1rem 0 0;
      font-weight: 500;
    }
    @media (max-width: 700px) {
      main { padding: 1rem; }
      .summary-table,
      .summary-table tbody,
      .summary-table tr,
      .summary-table td { display: block; width: 100%; }
      .summary-table thead { display: none; }
      .summary-table tr { padding: 0.45rem 0; border-bottom: 1px solid var(--border); }
      .summary-table tr:last-child { border-bottom: 0; }
      .summary-table td { border: 0; padding: 0.25rem 0.75rem; }
      .summary-table td::before {
        content: attr(data-label) ": ";
        color: var(--muted);
        font-weight: 600;
      }
    }
    """


def _layout(title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} — {SITE_TITLE}</title>
  <style>{_page_styles()}</style>
</head>
<body>
  <header><a href="index.html">{SITE_TITLE}</a></header>
  <main>{body}</main>
</body>
</html>
"""


def _chart_iframe(chart_path: str, title: str) -> str:
    return (
        f'<iframe src="{escape(chart_path)}" '
        f'title="{escape(title, quote=True)}" loading="lazy" scrolling="no"></iframe>'
    )


def _field_text(value: object) -> str:
    if value is None:
        return ''
    try:
        if pd.isna(value):
            return ''
    except (TypeError, ValueError):
        pass
    text = str(value).strip()
    return '' if text.lower() == 'nan' else text


def _display_field_value(field: str, value: str) -> str:
    if field == 'ram_gb' and not value.lower().endswith('gb'):
        return f'{value} GB'
    return value


def _machine_info_rows(latest: dict) -> list[tuple[str, str]]:
    rows = []
    for field, label in MACHINE_FIELD_LABELS.items():
        value = _field_text(latest.get(field))
        if not value:
            continue
        rows.append((label, _display_field_value(field, value)))
    return rows


def _latest_run_environment(run_environment: pd.DataFrame) -> Optional[dict]:
    if run_environment.empty:
        return None
    latest = run_environment.iloc[-1]
    if not any(_field_text(latest.get(field)) for field in RUN_ENVIRONMENT_FIELDS):
        return None
    return latest.to_dict()


def _machine_info_panel(run_environment: pd.DataFrame) -> str:
    latest = _latest_run_environment(run_environment)
    if latest is None:
        return ''

    rows = _machine_info_rows(latest)
    if not rows:
        return ''

    items = [
        f'<div><dt>{escape(label)}</dt><dd>{escape(display)}</dd></div>'
        for label, display in rows
    ]

    commit = _field_text(latest.get('commit_hash'))
    date = latest.get('date')
    recorded = date.strftime('%b %d, %Y') if hasattr(date, 'strftime') else ''
    meta = ' · '.join(part for part in (recorded, f'commit {commit[:9]}' if commit else '') if part)

    return (
        '<section class="machine-info">'
        '<h2>System info</h2>'
        f'<p class="subtitle">Latest recorded environment{(" · " + escape(meta)) if meta else ""}</p>'
        f'<dl>{"".join(items)}</dl>'
        '</section>'
    )


def _machine_info_markdown(run_environment: pd.DataFrame) -> list[str]:
    latest = _latest_run_environment(run_environment)
    if latest is None:
        return []

    rows = _machine_info_rows(latest)
    if not rows:
        return []

    parts = [f'**{label}:** {display}' for label, display in rows]
    return ['## System info', '', ' · '.join(parts), '']


def _placeholder_section(title: str) -> str:
    return (
        '<section class="chart chart-placeholder">'
        f'<h2>{escape(title)}</h2>'
        '<p class="placeholder-note">'
        'No data yet — chart will appear after the next nightly benchmark run.'
        '</p>'
        '</section>'
    )


def _chart_section(chart: ChartEntry) -> str:
    chart_path = f'{CHARTS_DIR}/{chart.html_filename}'
    return (
        '<section class="chart">'
        f'{_chart_iframe(chart_path, chart.display_name)}'
        '</section>'
    )


def _profile_facts(page: BenchmarkPage) -> str:
    return (
        '<div class="profile-facts">'
        f'<span>User data: {escape(page.user_data_size)}</span>'
        f'<span>Tokens: {escape(page.wallet_tokens)}</span>'
        f'<span>NFTs: {escape(page.wallet_nfts)}</span>'
        f'<span>Transactions: {escape(page.wallet_transactions)}</span>'
        f'<span>1-on-1 chats: {escape(page.messenger_direct_chats)}</span>'
        f'<span>Group chats: {escape(page.messenger_group_chats)}</span>'
        f'<span>Joined communities: {escape(page.communities_joined)}</span>'
        f'<span>Spectated communities: {escape(page.communities_spectated)}</span>'
        '</div>'
    )


def _profile_details(page: BenchmarkPage) -> str:
    return (
        '<section class="profile-details">'
        '<h2>User data profile</h2>'
        f'<p class="subtitle">Stored data: {escape(page.user_data_size)}</p>'
        '<div class="profile-details-grid">'
        '<div><h3>Wallet</h3><dl>'
        f'<dt>Tokens with balance &gt; 0</dt><dd>{escape(page.wallet_tokens)}</dd>'
        f'<dt>NFTs</dt><dd>{escape(page.wallet_nfts)}</dd>'
        f'<dt>Transaction history</dt><dd>{escape(page.wallet_transactions)}</dd>'
        '</dl></div>'
        '<div><h3>Messenger</h3><dl>'
        f'<dt>1-on-1 chats</dt><dd>{escape(page.messenger_direct_chats)}</dd>'
        f'<dt>Group chats</dt><dd>{escape(page.messenger_group_chats)}</dd>'
        '</dl></div>'
        '<div><h3>Communities</h3><dl>'
        f'<dt>Joined communities</dt><dd>{escape(page.communities_joined)}</dd>'
        f'<dt>Spectated communities</dt><dd>{escape(page.communities_spectated)}</dd>'
        '</dl></div>'
        '</div></section>'
    )


def _metric_value(chart: ChartTest, summary: ScenarioSummary | None) -> str:
    if summary is None or summary.value is None:
        return '—'
    if chart.metrics_kind == 'performance':
        return f'{summary.value:.3f}s'
    if chart.metrics_kind == 'cpu':
        return f'{summary.value:.1f}%'
    return f'{summary.value:.1f} MB'


def _status_badges(summary: ScenarioSummary | None) -> str:
    status = summary.speed_status if summary is not None else 'no-data'
    detail = escape(summary.detail, quote=True) if summary is not None else ''
    return (
        f'<span class="status status-{escape(status)}" title="{detail}">'
        f'{escape(STATUS_LABELS[status])}</span>'
    )


def _scenario_groups(
    page: BenchmarkPage,
    charts_by_id: dict[str, ChartTest],
    area: str,
) -> list[dict[str, ChartTest]]:
    groups: dict[str, dict[str, ChartTest]] = {}
    for test_id in page.test_ids:
        chart = charts_by_id.get(test_id)
        if chart is None or chart.area != area:
            continue
        groups.setdefault(chart.pattern, {})[chart.metrics_kind] = chart
    return list(groups.values())


def _scenario_chart(group: dict[str, ChartTest]) -> ChartTest:
    return group.get('performance') or next(iter(group.values()))


def _scenario_summary(
    group: dict[str, ChartTest],
    summaries: dict[str, ScenarioSummary],
    metrics_kind: str,
) -> tuple[ChartTest | None, ScenarioSummary | None]:
    chart = group.get(metrics_kind)
    return chart, summaries.get(chart.test_id) if chart is not None else None


def _measured_summary(
    group: dict[str, ChartTest],
    summaries: dict[str, ScenarioSummary],
) -> ScenarioSummary | None:
    for metrics_kind in ('performance', 'cpu', 'ram'):
        chart = group.get(metrics_kind)
        if chart is not None:
            summary = summaries.get(chart.test_id)
            if summary is not None and summary.commit_hash:
                return summary
    return None


def _reference_style(value: str) -> tuple[str, str]:
    if value == 'parity':
        return 'reference-parity', 'Within ±15% of 2.38.0'
    if value.startswith('+'):
        return 'reference-regression', 'Slower than 2.38.0'
    if value.startswith('-'):
        return 'reference-improvement', 'Faster than 2.38.0'
    return 'reference-neutral', 'No reference comparison available'


def _reference_html(value: str) -> str:
    css_class, title = _reference_style(value)
    return (
        f'<span class="reference-value {css_class}" '
        f'title="{escape(title, quote=True)}">{escape(value)}</span>'
    )


def _reference_markdown(value: str) -> str:
    if value.startswith('+'):
        return f'{value} slower'
    if value.startswith('-'):
        return f'{value} faster'
    return value


def _summary_row(
    area_label: str,
    group: dict[str, ChartTest] | None,
    summaries: dict[str, ScenarioSummary],
) -> str:
    if group is None:
        not_tested = _status_badges(None).replace(
            'status-no-data', 'status-not-tested'
        ).replace('No data', 'Not tested')
        return (
            '<tr>'
            f'<td data-label="Area">{escape(area_label)}</td>'
            '<td data-label="Scenario">Not tested</td>'
            f'<td data-label="Load time / Speed">{not_tested}</td>'
            f'<td class="reference-column" data-label="vs 2.38.0">{_reference_html("—")}</td>'
            '<td data-label="CPU">—</td>'
            '<td data-label="RAM">—</td>'
            '<td data-label="Measured">—</td>'
            '</tr>'
        )

    scenario = _scenario_chart(group)
    performance_chart, performance = _scenario_summary(group, summaries, 'performance')
    cpu_chart, cpu = _scenario_summary(group, summaries, 'cpu')
    ram_chart, ram = _scenario_summary(group, summaries, 'ram')
    measured = _measured_summary(group, summaries)

    if performance_chart is None:
        load_time = '—'
        vs_reference = '—'
    else:
        load_time = (
            '<div class="load-time-cell">'
            f'<span class="metric-value">{escape(_metric_value(performance_chart, performance))}</span>'
            f'{_status_badges(performance)}'
            '</div>'
        )
        vs_reference = performance.vs_reference if performance is not None else '—'
    cpu_value = _metric_value(cpu_chart, cpu) if cpu_chart is not None else '—'
    ram_value = _metric_value(ram_chart, ram) if ram_chart is not None else '—'
    build = measured.commit_hash[:9] if measured is not None and measured.commit_hash else '—'
    date = measured.date if measured is not None and measured.date else '—'

    return (
        '<tr>'
        f'<td data-label="Area">{escape(area_label)}</td>'
        f'<td data-label="Scenario">{escape(scenario.display_name)}</td>'
        f'<td data-label="Load time / Speed">{load_time}</td>'
        f'<td class="reference-column" data-label="vs 2.38.0">'
        f'{_reference_html(vs_reference)}</td>'
        f'<td data-label="CPU">{escape(cpu_value)}</td>'
        f'<td data-label="RAM">{escape(ram_value)}</td>'
        f'<td data-label="Measured">{escape(build)} · {escape(date)}</td>'
        '</tr>'
    )


def _summary_page(
    pages: tuple[BenchmarkPage, ...],
    charts_by_id: dict[str, ChartTest],
    summaries: dict[str, ScenarioSummary],
) -> str:
    sections = []
    for page in pages:
        rows = []
        for area, area_label in PRODUCT_AREAS:
            groups = _scenario_groups(page, charts_by_id, area)
            if groups:
                rows.extend(
                    _summary_row(area_label, group, summaries)
                    for group in groups
                )
            else:
                rows.append(_summary_row(area_label, None, summaries))
        sections.append(
            '<section class="summary-profile">'
            f'<h2><a href="{escape(page.slug)}.html">{escape(page.title)}</a></h2>'
            f'<p class="subtitle">{escape(page.description)}</p>'
            '<table class="summary-table"><thead><tr>'
            '<th>Area</th><th>Scenario</th>'
            '<th class="load-time-column" '
            'title="Latest measured loading time and mobile-style speed category">'
            'Load time / Speed</th>'
            '<th class="reference-column" '
            'title="Difference from the 2.38.0 reference build">vs 2.38.0</th>'
            '<th title="Average CPU usage during the scenario">CPU</th>'
            '<th title="Average RAM usage during the scenario">RAM</th>'
            '<th title="Build and date of the latest scenario result">Measured</th>'
            f'</tr></thead><tbody>{"".join(rows)}</tbody></table>'
            '</section>'
        )
    return (
        '<nav class="back"><a href="index.html">← Dashboard</a></nav>'
        '<h1>Scenario summary</h1>'
        '<p class="subtitle">Latest result for every tested scenario. '
        'Speed categories:<br>'
        '<span class="speed-legend">'
        '<span class="speed-fast">&lt;0.5s Fast</span>'
        '<span class="speed-ok">0.5–0.9s Ok</span>'
        '<span class="speed-ok-warn">0.9–1.0s Ok near slow</span>'
        '<span class="speed-slow">&gt;1.0s Slow</span>'
        '</span><br>'
        'Reference parity means the latest value is within ±15% of 2.38.0.</p>'
        f'{"".join(sections)}'
    )


def write_site(
    output_dir: Path,
    pages: tuple[BenchmarkPage, ...],
    charts_by_test_id: dict[str, ChartEntry],
    *,
    chart_tests: tuple[ChartTest, ...] = (),
    summaries: dict[str, ScenarioSummary] | None = None,
    run_environment: pd.DataFrame | None = None,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    env_frame = run_environment if run_environment is not None else pd.DataFrame()
    machine_panel = _machine_info_panel(env_frame)
    charts_by_id = {chart.test_id: chart for chart in chart_tests}
    scenario_summaries = summaries or {}

    cards = ''.join(
        f'<a class="card" href="{escape(page.slug)}.html">'
        f'<h2>{escape(page.title)}</h2>'
        f'<p>{escape(page.description)}</p>'
        f'{_profile_facts(page)}</a>'
        for page in pages
    )
    index_body = (
        '<h1>Windows Benchmark Dashboard</h1>'
        f'<p class="subtitle">Performance metrics from the last {CHART_WINDOW_DAYS} days. '
        'Each point is one nightly run — x-axis shows build date; hover a point for commit hash. '
        'Load-time charts plot the average of runs per build.</p>'
        f'{machine_panel}'
        '<a class="summary-link" href="summary.html">View scenario summary →</a>'
        '<h2 style="margin-top:2rem">User profiles</h2>'
        f'<div class="grid">{cards}</div>'
        '<p class="note">Raw CSV history lives in the repository <code>data/</code> folder. '
        'PNG charts on GitHub: '
        '<a href="https://github.com/status-im/status-app-benchmarks/blob/master/docs/desktop/README.md">'
        'docs/desktop/README.md</a>.</p>'
    )
    (output_dir / 'index.html').write_text(_layout('Dashboard', index_body), encoding='utf-8')
    print('Generated index.html')

    (output_dir / 'summary.html').write_text(
        _layout('Scenario summary', _summary_page(pages, charts_by_id, scenario_summaries)),
        encoding='utf-8',
    )
    print('Generated summary.html')

    expected_pages = {f'{page.slug}.html' for page in pages} | {'summary.html'}
    for page in pages:
        area_sections = []
        for area, area_label in PRODUCT_AREAS:
            test_ids = [
                test_id for test_id in page.test_ids
                if test_id in charts_by_id and charts_by_id[test_id].area == area
            ]
            if not test_ids:
                content = '<div class="area-empty">Not tested for this user profile.</div>'
            else:
                sections = []
                for test_id in test_ids:
                    chart = charts_by_test_id.get(test_id)
                    if chart is not None:
                        sections.append(_chart_section(chart))
                    else:
                        sections.append(_placeholder_section(charts_by_id[test_id].display_name))
                content = ''.join(sections)
            area_sections.append(
                f'<section class="area-group"><h2>{escape(area_label)}</h2>{content}</section>'
            )
        page_body = (
            '<nav class="back"><a href="index.html">← Dashboard</a></nav>'
            f'<h1>{escape(page.title)}</h1>'
            f'<p class="subtitle">{escape(page.description)}</p>'
            f'{_profile_details(page)}'
            f'{"".join(area_sections)}'
        )
        (output_dir / f'{page.slug}.html').write_text(
            _layout(page.title, page_body),
            encoding='utf-8',
        )
        print(f'Generated {page.slug}.html')

    for stale_page in output_dir.glob('*.html'):
        if stale_page.name != 'index.html' and stale_page.name not in expected_pages:
            stale_page.unlink()
            print(f'Removed stale page: {stale_page.name}')

    write_github_readme(
        output_dir, pages, charts_by_test_id,
        chart_tests=chart_tests,
        summaries=scenario_summaries,
        run_environment=env_frame,
    )


def _profile_data_markdown(page: BenchmarkPage) -> list[str]:
    return [
        '### User data profile',
        '',
        f'- **Stored data:** {page.user_data_size}',
        (
            f'- **Wallet:** {page.wallet_tokens} tokens with balance > 0 · '
            f'{page.wallet_nfts} NFTs · {page.wallet_transactions} transactions'
        ),
        (
            f'- **Messenger:** {page.messenger_direct_chats} 1-on-1 chats · '
            f'{page.messenger_group_chats} group chats'
        ),
        (
            f'- **Communities:** {page.communities_joined} joined communities · '
            f'{page.communities_spectated} spectated communities'
        ),
        '',
    ]


def _github_summary_markdown(
    pages: tuple[BenchmarkPage, ...],
    charts_by_id: dict[str, ChartTest],
    summaries: dict[str, ScenarioSummary],
) -> list[str]:
    lines = [
        '## Scenario summary',
        '',
        'Latest result for every tested scenario. Speed categories:',
        '',
        '**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Ok near slow** · **>1.0s Slow**',
        '',
        'Reference parity means the latest value '
        'is within ±15% of 2.38.0.',
        '',
        '| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |',
        '|--------------|------|----------|-------------------|-----------|-----|-----|----------|',
    ]
    for page in pages:
        for area, area_label in PRODUCT_AREAS:
            groups = _scenario_groups(page, charts_by_id, area)
            if not groups:
                lines.append(
                    f'| {page.title} | {area_label} | Not tested | Not tested '
                    '| — | — | — | — |'
                )
                continue
            for group in groups:
                scenario = _scenario_chart(group)
                performance_chart, performance = _scenario_summary(
                    group, summaries, 'performance'
                )
                cpu_chart, cpu = _scenario_summary(group, summaries, 'cpu')
                ram_chart, ram = _scenario_summary(group, summaries, 'ram')
                measured = _measured_summary(group, summaries)

                if performance_chart is None:
                    load_time = '—'
                    vs_reference = '—'
                else:
                    status = performance.speed_status if performance is not None else 'no-data'
                    load_time = (
                        f'{_metric_value(performance_chart, performance)} · '
                        f'{STATUS_LABELS[status]}'
                    )
                    vs_reference = (
                        performance.vs_reference if performance is not None else '—'
                    )
                cpu_value = _metric_value(cpu_chart, cpu) if cpu_chart is not None else '—'
                ram_value = _metric_value(ram_chart, ram) if ram_chart is not None else '—'
                build = (
                    measured.commit_hash[:9]
                    if measured is not None and measured.commit_hash else '—'
                )
                date = measured.date if measured is not None and measured.date else '—'
                lines.append(
                    f'| {page.title} | {area_label} | {scenario.display_name} '
                    f'| {load_time} | {_reference_markdown(vs_reference)} '
                    f'| {cpu_value} | {ram_value} '
                    f'| {build} · {date} |'
                )
    lines.append('')
    return lines


def write_github_readme(
    output_dir: Path,
    pages: tuple[BenchmarkPage, ...],
    charts_by_test_id: dict[str, ChartEntry],
    *,
    chart_tests: tuple[ChartTest, ...] = (),
    summaries: dict[str, ScenarioSummary] | None = None,
    run_environment: pd.DataFrame | None = None,
) -> None:
    """GitHub-rendered fallback dashboard (PNG embeds) until GitHub Pages is enabled."""
    lines = [
        '# Windows — performance benchmarks',
        '',
        'Automated test suite performance tracking for the Windows desktop app.',
        f'Charts show data from the last {CHART_WINDOW_DAYS} days — each point is one nightly run.',
        'Load-time charts plot the average of runs per build. Lower is better.',
        '',
        '> **Viewing charts:** This README renders inline PNG images on GitHub — works without',
        '> GitHub Pages. For interactive charts (hover tooltips, zoom), use the',
        '> [interactive dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) once GitHub Pages is enabled.',
        '',
        f'Full CSV history: [`data/`](../../data/).',
        '',
    ]

    env_frame = run_environment if run_environment is not None else pd.DataFrame()
    lines.extend(_machine_info_markdown(env_frame))
    charts_by_id = {chart.test_id: chart for chart in chart_tests}
    scenario_summaries = summaries or {}
    lines.extend(_github_summary_markdown(pages, charts_by_id, scenario_summaries))

    for page in pages:
        lines.extend([f'## {page.title}', '', page.description, ''])
        lines.extend(_profile_data_markdown(page))
        for area, area_label in PRODUCT_AREAS:
            test_ids = [
                test_id for test_id in page.test_ids
                if test_id in charts_by_id and charts_by_id[test_id].area == area
            ]
            lines.extend([f'### {area_label}', ''])
            if not test_ids:
                lines.extend(['_Not tested for this user profile._', ''])
                continue
            for test_id in test_ids:
                chart = charts_by_test_id.get(test_id)
                if chart is None:
                    chart_test = charts_by_id[test_id]
                    lines.extend([
                        f'**{chart_test.display_name}**',
                        '',
                        '_No data yet — chart will appear after the next nightly benchmark run._',
                        '',
                    ])
                    continue
                png_name = Path(chart.html_filename).with_suffix('.png').name
                lines.extend([f'![{chart.display_name}](./{png_name})', ''])

    lines.extend([
        '---',
        '',
        'Generated by `scripts/benchmark.py graphs` from `data/`. Refreshed nightly by Jenkins.',
        '',
    ])
    readme_path = output_dir / 'README.md'
    readme_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Generated {readme_path.name}')


def write_docs_root_index(docs_dir: Path) -> None:
    """Redirect docs/ site root to the desktop dashboard."""
    (docs_dir / '.nojekyll').touch()
    index_body = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        '  <meta charset="utf-8">\n'
        '  <meta http-equiv="refresh" content="0; url=desktop/">\n'
        '  <link rel="canonical" href="desktop/">\n'
        '  <title>Status App Benchmarks</title>\n</head>\n<body>\n'
        '  <p><a href="desktop/">Windows benchmarks</a></p>\n</body>\n</html>\n'
    )
    (docs_dir / 'index.html').write_text(index_body, encoding='utf-8')
    print(f'Generated {docs_dir / "index.html"}')
