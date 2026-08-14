"""Static HTML site generator for GitHub Pages benchmark dashboard."""

from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Optional

import pandas as pd

from benchmark_config import (
    CHART_WINDOW_DAYS,
    BenchmarkPage,
    ChartEntry,
    ChartTest,
    FlagTicket,
)
from environment_parser import RUN_ENVIRONMENT_FIELDS
from regression_report import ScenarioSummary, Violation

CHARTS_DIR = 'charts'
SITE_TITLE = 'Status App Benchmarks'
STATUS_APP_REPO = 'https://github.com/status-im/status-app'
CHANNEL_BADGE = {
    'nightly': ('Nightly', 'channel-badge-nightly'),
    'pr': ('Pull request', 'channel-badge-pr'),
    'release': ('Release', 'channel-badge-release'),
}
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
FLAG_BADGE_BY_RULE = {
    '2.1 Regression': ('slow', '↗ Regression'),
    '2.2 Slow build': ('ok-warn', '⏱ Slow'),
    '2.3 Backlog candidate': ('backlog', 'Backlog'),
}
FLAG_BADGE_BY_SECTION = {
    'Regression': ('slow', '↗ Regression'),
    'Slow builds': ('ok-warn', '⏱ Slow'),
    'Backlog candidates': ('backlog', 'Backlog'),
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
      --accent-data: #57606a;
      --accent-data-bg: #eaeef2;
      --accent-wallet: #6e40c9;
      --accent-wallet-bg: #f3f0ff;
      --accent-messenger: #1a7f37;
      --accent-messenger-bg: #dafbe1;
      --accent-communities: #bc4c00;
      --accent-communities-bg: #fff1e5;
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
        --accent-data: #8b949e;
        --accent-data-bg: #21262d;
        --accent-wallet: #a371f7;
        --accent-wallet-bg: #2b1f47;
        --accent-messenger: #3fb950;
        --accent-messenger-bg: #12261e;
        --accent-communities: #f0883e;
        --accent-communities-bg: #2d1f14;
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
    .page-heading {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.65rem 0.85rem;
      margin: 0 0 0.25rem;
    }
    .page-heading h1 { margin: 0; }
    .channel-badge {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      padding: 0.22rem 0.6rem;
      border-radius: 999px;
      line-height: 1.2;
      white-space: nowrap;
    }
    .channel-badge-nightly {
      background: #ddf4ff;
      color: #0969da;
    }
    .channel-badge-pr {
      background: #dafbe1;
      color: #1a7f37;
    }
    .channel-badge-release {
      background: #fff1e5;
      color: #bc4c00;
    }
    @media (prefers-color-scheme: dark) {
      .channel-badge-nightly {
        background: #12263a;
        color: #58a6ff;
      }
      .channel-badge-pr {
        background: #12261e;
        color: #3fb950;
      }
      .channel-badge-release {
        background: #2d1f14;
        color: #f0883e;
      }
    }
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
    .listing-card {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
    .listing-card:hover { border-color: var(--link); }
    .listing-card .listing-main {
      text-decoration: none;
      color: inherit;
      flex: 1;
    }
    .listing-card .listing-main h2 { margin: 0 0 0.4rem; font-size: 1.1rem; }
    .listing-card .listing-meta {
      margin: 0;
      color: var(--muted);
      font-size: 0.9rem;
    }
    .listing-card .listing-meta + .listing-meta { margin-top: 0.2rem; }
    .listing-card .listing-extra {
      font-size: 0.85rem;
      color: var(--link);
      text-decoration: none;
    }
    .listing-card .listing-extra:hover { text-decoration: underline; }
    .listing-history {
      list-style: none;
      margin: 0.65rem 0 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }
    .listing-history li {
      display: flex;
      flex-wrap: wrap;
      gap: 0.35rem 0.75rem;
      font-size: 0.85rem;
      color: var(--muted);
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }
    .listing-history .commit {
      color: var(--text);
      font-weight: 600;
    }
    .profile-fact-groups {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      margin-top: 0.85rem;
    }
    .stat-group {
      display: flex;
      flex-wrap: wrap;
      gap: 0.35rem;
      align-items: center;
    }
    .stat-group-label {
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      min-width: 5.5rem;
    }
    .stat-chip {
      display: inline-flex;
      align-items: baseline;
      gap: 0.2rem;
      border-radius: 999px;
      padding: 0.15rem 0.55rem;
      font-size: 0.76rem;
      font-weight: 500;
      line-height: 1.35;
    }
    .stat-chip strong { font-weight: 700; }
    .stat-chip.stat-zero { opacity: 0.55; }
    .stat-data {
      align-self: flex-start;
      background: var(--accent-data-bg);
      color: var(--accent-data);
      font-weight: 600;
    }
    .stat-wallet .stat-group-label { color: var(--accent-wallet); }
    .stat-wallet .stat-chip {
      background: var(--accent-wallet-bg);
      color: var(--accent-wallet);
    }
    .stat-messenger .stat-group-label { color: var(--accent-messenger); }
    .stat-messenger .stat-chip {
      background: var(--accent-messenger-bg);
      color: var(--accent-messenger);
    }
    .stat-communities .stat-group-label { color: var(--accent-communities); }
    .stat-communities .stat-chip {
      background: var(--accent-communities-bg);
      color: var(--accent-communities);
    }
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
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1rem;
    }
    .profile-detail-section {
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.75rem 0.85rem;
    }
    .profile-detail-section h3 {
      margin: 0 0 0.5rem;
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .profile-detail-section.stat-wallet {
      border-color: color-mix(in srgb, var(--accent-wallet) 35%, var(--border));
    }
    .profile-detail-section.stat-wallet h3 { color: var(--accent-wallet); }
    .profile-detail-section.stat-messenger {
      border-color: color-mix(in srgb, var(--accent-messenger) 35%, var(--border));
    }
    .profile-detail-section.stat-messenger h3 { color: var(--accent-messenger); }
    .profile-detail-section.stat-communities {
      border-color: color-mix(in srgb, var(--accent-communities) 35%, var(--border));
    }
    .profile-detail-section.stat-communities h3 { color: var(--accent-communities); }
    .profile-detail-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 0.35rem;
    }
    .area-group { margin-top: 2rem; }
    .area-group > h2 { margin-bottom: 0.75rem; }
    .scenario-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
    details.scenario-charts {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
    }
    details.scenario-charts[open] { border-color: var(--link); }
    details.scenario-charts > summary {
      cursor: pointer;
      padding: 0.9rem 1.1rem;
      font-weight: 600;
    }
    details.scenario-charts > summary:hover {
      background: var(--accent-data-bg);
    }
    details.scenario-charts > summary:focus-visible {
      outline: 2px solid var(--link);
      outline-offset: -2px;
    }
    .scenario-summary-content {
      display: inline-flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 1rem;
      width: calc(100% - 1.5rem);
      margin-left: 0.25rem;
      vertical-align: middle;
    }
    .scenario-chart-count {
      color: var(--muted);
      font-size: 0.8rem;
      font-weight: 500;
      white-space: nowrap;
    }
    .scenario-charts-body {
      border-top: 1px solid var(--border);
      padding: 1rem;
    }
    .scenario-charts-body section.chart:last-child { margin-bottom: 0; }
    .area-empty {
      border: 1px dashed var(--border);
      border-radius: 8px;
      padding: 1rem 1.25rem;
      color: var(--muted);
    }
    .summary-links {
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      margin-top: 1rem;
    }
    .summary-link {
      display: inline-block;
      color: var(--link);
      text-decoration: none;
      font-weight: 600;
    }
    .summary-link:hover { text-decoration: underline; }
    .summary-badge {
      display: inline-block;
      margin-left: 0.35rem;
      padding: 0.1rem 0.45rem;
      border-radius: 999px;
      font-size: 0.8rem;
      font-weight: 600;
      background: #cf222e;
      color: #fff;
    }
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
    .summary-table .measured-column {
      min-width: 6.5rem;
    }
    .measured-cell {
      display: flex;
      flex-direction: column;
      gap: 0.15rem;
      line-height: 1.2;
    }
    .measured-build {
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 0.82rem;
    }
    .measured-date {
      color: var(--muted);
      font-size: 0.78rem;
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
    .status-fast {
      color: #1a7f37;
      border-color: #1a7f37;
      background: #dafbe1;
    }
    .status-ok {
      color: var(--link);
      border-color: var(--link);
      background: #ddf4ff;
    }
    .status-ok-warn {
      color: #9a6700;
      border-color: #9a6700;
      background: #fff8c5;
    }
    .status-slow {
      color: #cf222e;
      border-color: #cf222e;
      background: #ffebe9;
    }
    .status-backlog {
      color: var(--accent-wallet);
      border-color: var(--accent-wallet);
      background: var(--accent-wallet-bg);
    }
    .status-neutral,
    .status-no-data,
    .status-not-tested {
      color: var(--muted);
      background: var(--accent-data-bg);
    }
    @media (prefers-color-scheme: dark) {
      .status-fast { background: var(--accent-messenger-bg); }
      .status-ok { background: #0c2d6b; color: #58a6ff; border-color: #58a6ff; }
      .status-ok-warn { background: #3d2e00; color: #d4a72c; border-color: #d4a72c; }
      .status-slow { background: #3d1418; }
      .status-backlog { background: var(--accent-wallet-bg); }
    }
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
    .regression-legend {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      margin-top: 0.5rem;
    }
    .regression-legend-item {
      display: flex;
      align-items: baseline;
      flex-wrap: wrap;
      gap: 0.35rem;
    }
    .section-heading {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.4rem;
    }
    .section-heading .summary-badge { margin-left: 0; }
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
      scroll-margin-top: 1rem;
    }
    .chart-permalink {
      display: flex;
      justify-content: flex-end;
      margin-bottom: 0.25rem;
      font-size: 0.8rem;
    }
    .chart-permalink a {
      color: var(--link);
      text-decoration: none;
    }
    .chart-permalink a:hover { text-decoration: underline; }
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


def _channel_badge_html(channel: str) -> str:
    label, css_class = CHANNEL_BADGE.get(channel, (channel.title(), 'channel-badge-nightly'))
    return f'<span class="channel-badge {css_class}">{escape(label)}</span>'


def _heading_with_badge(heading: str, channel: str) -> str:
    return (
        f'<div class="page-heading">{_channel_badge_html(channel)}'
        f'<h1>{escape(heading)}</h1></div>'
    )


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


def _chart_permalink(test_id: str) -> str:
    anchor = escape(test_id, quote=True)
    return (
        '<div class="chart-permalink">'
        f'<a href="#{anchor}" aria-label="Permalink to this chart">Permalink</a>'
        '</div>'
    )


def _placeholder_section(test_id: str, title: str) -> str:
    anchor = escape(test_id, quote=True)
    return (
        f'<section class="chart chart-placeholder" id="{anchor}">'
        f'{_chart_permalink(test_id)}'
        f'<h2>{escape(title)}</h2>'
        '<p class="placeholder-note">'
        'No data yet — chart will appear after the next nightly benchmark run.'
        '</p>'
        '</section>'
    )


def _chart_section(test_id: str, chart: ChartEntry) -> str:
    anchor = escape(test_id, quote=True)
    chart_path = f'{CHARTS_DIR}/{chart.html_filename}'
    return (
        f'<section class="chart" id="{anchor}">'
        f'{_chart_permalink(test_id)}'
        f'{_chart_iframe(chart_path, chart.display_name)}'
        '</section>'
    )


def _scenario_charts_section(
    group: dict[str, ChartTest],
    charts_by_test_id: dict[str, ChartEntry],
) -> str:
    scenario = _scenario_chart(group)
    sections = []
    for metrics_kind in ('performance', 'cpu', 'ram'):
        chart_test = group.get(metrics_kind)
        if chart_test is None:
            continue
        chart = charts_by_test_id.get(chart_test.test_id)
        if chart is not None:
            sections.append(_chart_section(chart_test.test_id, chart))
        else:
            sections.append(_placeholder_section(
                chart_test.test_id, chart_test.display_name,
            ))

    chart_count = len(sections)
    chart_label = 'chart' if chart_count == 1 else 'charts'
    return (
        '<details class="scenario-charts">'
        '<summary><span class="scenario-summary-content">'
        f'<span>{escape(scenario.display_name)}</span>'
        f'<span class="scenario-chart-count">{chart_count} {chart_label}</span>'
        '</span></summary>'
        f'<div class="scenario-charts-body">{"".join(sections)}</div>'
        '</details>'
    )


def _chart_hash_script() -> str:
    return """
<script>
  (() => {
    const revealChart = () => {
      const anchor = window.location.hash.slice(1);
      if (!anchor) return;
      const target = document.getElementById(anchor);
      if (!target) return;
      const group = target.closest('details.scenario-charts');
      if (group) group.open = true;
      window.requestAnimationFrame(() => target.scrollIntoView({block: 'start'}));
    };
    window.addEventListener('hashchange', revealChart);
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', revealChart);
    } else {
      revealChart();
    }
  })();
</script>
"""


def _is_zero_stat(value: str) -> bool:
    normalized = value.strip().lower()
    return normalized in ('0', 'tbd', '—', '-', '')


def _stat_chip(label: str, value: str, category: str) -> str:
    zero_class = ' stat-zero' if _is_zero_stat(value) else ''
    return (
        f'<span class="stat-chip stat-{category}{zero_class}">'
        f'<strong>{escape(value)}</strong> {escape(label)}'
        '</span>'
    )


def _stat_group(title: str, category: str, chips: str) -> str:
    return (
        f'<div class="stat-group stat-{category}">'
        f'<span class="stat-group-label">{escape(title)}</span>'
        f'{chips}'
        '</div>'
    )


def _user_data_chip(user_data_size: str) -> str:
    label = user_data_size
    if 'data' not in user_data_size.lower():
        label = f'{user_data_size} user data'
    return f'<span class="stat-chip stat-data">{escape(label)}</span>'


def _profile_detail_section(title: str, category: str, chips: str) -> str:
    return (
        f'<div class="profile-detail-section stat-{category}">'
        f'<h3>{escape(title)}</h3>'
        f'<div class="profile-detail-chips">{chips}</div>'
        '</div>'
    )


def _profile_facts(page: BenchmarkPage) -> str:
    wallet_chips = ''.join([
        _stat_chip('accounts', page.wallet_accounts, 'wallet'),
        _stat_chip('tokens', page.wallet_tokens, 'wallet'),
        _stat_chip('NFTs', page.wallet_nfts, 'wallet'),
        _stat_chip('txs', page.wallet_transactions, 'wallet'),
    ])
    messenger_chips = ''.join([
        _stat_chip('DMs', page.messenger_direct_chats, 'messenger'),
        _stat_chip('groups', page.messenger_group_chats, 'messenger'),
    ])
    community_chips = ''.join([
        _stat_chip('joined', page.communities_joined, 'communities'),
        _stat_chip('spectated', page.communities_spectated, 'communities'),
    ])
    return (
        '<div class="profile-fact-groups">'
        f'{_user_data_chip(page.user_data_size)}'
        f'{_stat_group("Wallet", "wallet", wallet_chips)}'
        f'{_stat_group("Messenger", "messenger", messenger_chips)}'
        f'{_stat_group("Communities", "communities", community_chips)}'
        '</div>'
    )


def _profile_details(page: BenchmarkPage) -> str:
    wallet_chips = ''.join([
        _stat_chip('accounts', page.wallet_accounts, 'wallet'),
        _stat_chip('tokens with balance > 0', page.wallet_tokens, 'wallet'),
        _stat_chip('NFTs', page.wallet_nfts, 'wallet'),
        _stat_chip('transactions', page.wallet_transactions, 'wallet'),
    ])
    messenger_chips = ''.join([
        _stat_chip('1-on-1 chats', page.messenger_direct_chats, 'messenger'),
        _stat_chip('group chats', page.messenger_group_chats, 'messenger'),
    ])
    community_chips = ''.join([
        _stat_chip('joined', page.communities_joined, 'communities'),
        _stat_chip('spectated', page.communities_spectated, 'communities'),
    ])
    return (
        '<section class="profile-details">'
        '<h2>User data profile</h2>'
        f'<p class="subtitle">Stored data: {escape(page.user_data_size)}</p>'
        '<div class="profile-details-grid">'
        f'{_profile_detail_section("Wallet", "wallet", wallet_chips)}'
        f'{_profile_detail_section("Messenger", "messenger", messenger_chips)}'
        f'{_profile_detail_section("Communities", "communities", community_chips)}'
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


def _page_slugs_by_test_id(
    pages: tuple[BenchmarkPage, ...],
) -> dict[str, str]:
    return {
        test_id: page.slug
        for page in pages
        for test_id in page.test_ids
    }


def _chart_href(page_slug: str, test_id: str) -> str:
    return escape(f'{page_slug}.html#{test_id}', quote=True)


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


def _measured_cell_html(build: str, date: str) -> str:
    if build == '—' and date == '—':
        return '—'
    return (
        '<div class="measured-cell">'
        f'<span class="measured-build">{escape(build)}</span>'
        f'<span class="measured-date">{escape(date)}</span>'
        '</div>'
    )


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
    page_slug: str,
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
    scenario_link = (
        f'<a href="{_chart_href(page_slug, scenario.test_id)}">'
        f'{escape(scenario.display_name)}</a>'
    )

    return (
        '<tr>'
        f'<td data-label="Area">{escape(area_label)}</td>'
        f'<td data-label="Scenario">{scenario_link}</td>'
        f'<td data-label="Load time / Speed">{load_time}</td>'
        f'<td class="reference-column" data-label="vs 2.38.0">'
        f'{_reference_html(vs_reference)}</td>'
        f'<td data-label="CPU">{escape(cpu_value)}</td>'
        f'<td data-label="RAM">{escape(ram_value)}</td>'
        f'<td class="measured-column" data-label="Measured">'
        f'{_measured_cell_html(build, date)}</td>'
        '</tr>'
    )


def _summary_sort_key(
    group: dict[str, ChartTest] | None,
    summaries: dict[str, ScenarioSummary],
) -> float:
    if group is None:
        return -1.0
    _chart, performance = _scenario_summary(group, summaries, 'performance')
    if performance is None or performance.value is None:
        return -1.0
    return float(performance.value)


def _summary_page(
    pages: tuple[BenchmarkPage, ...],
    charts_by_id: dict[str, ChartTest],
    summaries: dict[str, ScenarioSummary],
    *,
    channel: str = 'nightly',
) -> str:
    sections = []
    for page in pages:
        keyed_rows: list[tuple[float, str]] = []
        for area, area_label in PRODUCT_AREAS:
            groups = _scenario_groups(page, charts_by_id, area)
            if groups:
                for group in groups:
                    keyed_rows.append((
                        _summary_sort_key(group, summaries),
                        _summary_row(area_label, group, summaries, page.slug),
                    ))
            else:
                keyed_rows.append((
                    _summary_sort_key(None, summaries),
                    _summary_row(area_label, None, summaries, page.slug),
                ))
        keyed_rows.sort(key=lambda item: item[0], reverse=True)
        rows = ''.join(html for _key, html in keyed_rows)
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
            '<th class="measured-column" '
            'title="Build and date of the latest scenario result">Measured</th>'
            f'</tr></thead><tbody>{rows}</tbody></table>'
            '</section>'
        )
    return (
        '<nav class="back"><a href="index.html">← Dashboard</a></nav>'
        f'{_heading_with_badge("Scenario summary", channel)}'
        '<p class="subtitle">Latest result for every tested scenario. '
        'Speed categories:<br>'
        '<span class="speed-legend">'
        '<span class="speed-fast">&lt;0.5s Fast</span>'
        '<span class="speed-ok">0.5–0.9s Ok</span>'
        '<span class="speed-ok-warn">0.9–1.0s Ok near slow</span>'
        '<span class="speed-slow">&gt;1.0s Slow</span>'
        '</span><br>'
        'Reference parity (where shown) means the latest value is within ±15% of 2.38.0. '
        'Wallet tab scenarios omit the 2.38.0 comparison because the e2e methodology '
        'changed in Jul 2026.</p>'
        f'{"".join(sections)}'
    )


def _flag_badge(status: str, label: str) -> str:
    return (
        f'<span class="status status-{escape(status)}">'
        f'{escape(label)}</span>'
    )


def _flag_badge_for_rule(rule: str) -> str:
    status, label = FLAG_BADGE_BY_RULE.get(rule, ('neutral', rule))
    return _flag_badge(status, label)


def _section_heading(title: str, count: int) -> str:
    status, label = FLAG_BADGE_BY_SECTION.get(title, ('neutral', title))
    count_badge = (
        f'<span class="summary-badge">{count}</span>' if count else ''
    )
    return (
        f'<h2 class="section-heading">{escape(title)}'
        f'{count_badge}{_flag_badge(status, label)}</h2>'
    )


def _ticket_cell_html(
    item: Violation,
    flag_tickets: dict[str, FlagTicket],
) -> str:
    ticket = flag_tickets.get(item.test_id)
    if ticket is None:
        return '—'
    return (
        f'<a href="{escape(ticket.url, quote=True)}" '
        'target="_blank" rel="noopener">'
        f'#{ticket.issue}</a>'
    )


def _regression_violation_row(
    item: Violation,
    flag_tickets: dict[str, FlagTicket],
    page_slugs_by_test_id: dict[str, str],
) -> str:
    commit = escape(item.commit_hash[:10])
    page_slug = page_slugs_by_test_id.get(item.test_id)
    test_cell = escape(item.test_id)
    if page_slug is not None:
        test_cell = (
            f'<a href="{_chart_href(page_slug, item.test_id)}">'
            f'{test_cell}</a>'
        )
    value_cell = (
        '<div class="load-time-cell">'
        f'<span class="metric-value">{item.value:.3f}s</span>'
        f'{_flag_badge_for_rule(item.rule)}'
        '</div>'
    )
    return (
        '<tr>'
        f'<td data-label="Test">{test_cell}</td>'
        f'<td data-label="Variant">{escape(item.variant)}</td>'
        f'<td data-label="Value">{value_cell}</td>'
        f'<td data-label="Commit"><code>{commit}</code></td>'
        f'<td data-label="Date">{escape(item.date)}</td>'
        f'<td data-label="Detail">{escape(item.detail)}</td>'
        f'<td data-label="Ticket">{_ticket_cell_html(item, flag_tickets)}</td>'
        '</tr>'
    )


def _regression_section(
    title: str,
    items: list[Violation],
    flag_tickets: dict[str, FlagTicket],
    page_slugs_by_test_id: dict[str, str],
) -> str:
    heading = _section_heading(title, len(items))
    if not items:
        return (
            f'<section class="summary-profile">{heading}'
            '<p class="subtitle">No violations.</p></section>'
        )
    sorted_items = sorted(items, key=lambda item: item.value, reverse=True)
    rows = ''.join(
        _regression_violation_row(item, flag_tickets, page_slugs_by_test_id)
        for item in sorted_items
    )
    return (
        f'<section class="summary-profile">{heading}'
        '<table class="summary-table"><thead><tr>'
        '<th>Test</th><th>Variant</th><th>Value</th><th>Commit</th>'
        '<th>Date</th><th>Detail</th><th>Ticket</th>'
        f'</tr></thead><tbody>{rows}</tbody></table></section>'
    )


def _regression_page(
    violations: list[Violation],
    flag_tickets: dict[str, FlagTicket] | None = None,
    page_slugs_by_test_id: dict[str, str] | None = None,
    *,
    channel: str = 'nightly',
) -> str:
    tickets = flag_tickets or {}
    page_slugs = page_slugs_by_test_id or {}
    by_rule = {
        'Regression': [v for v in violations if v.rule == '2.1 Regression'],
        'Slow builds': [v for v in violations if v.rule == '2.2 Slow build'],
        'Backlog candidates': [v for v in violations if v.rule == '2.3 Backlog candidate'],
    }
    sections = ''.join(
        _regression_section(title, items, tickets, page_slugs)
        for title, items in by_rule.items()
    )
    return (
        '<nav class="back"><a href="index.html">← Dashboard</a></nav>'
        f'{_heading_with_badge("Flags", channel)}'
        '<p class="subtitle">Automated flags from nightly performance data.</p>'
        '<p class="subtitle regression-legend">'
        '<span class="regression-legend-item">'
        f'{_flag_badge("slow", "↗ Regression")}'
        '3 consecutive builds each ≥15% slower than the previous.</span>'
        '<span class="regression-legend-item">'
        f'{_flag_badge("ok-warn", "⏱ Slow")}'
        'latest value exceeds 1.0s slow threshold (and not yet a backlog candidate).</span>'
        '<span class="regression-legend-item">'
        f'{_flag_badge("backlog", "Backlog")}'
        'slow in 3 of the last 5 builds (listed here instead of Slow).</span>'
        '</p>'
        f'<p class="subtitle"><strong>Total flags:</strong> {len(violations)}</p>'
        f'{sections}'
    )


def _summary_links_html(violations: list[Violation]) -> str:
    badge = ''
    if violations:
        badge = f'<span class="summary-badge">{len(violations)}</span>'
    return (
        '<div class="summary-links">'
        '<a class="summary-link" href="summary.html">View scenario summary →</a>'
        f'<a class="summary-link" href="regression_report.html">View flags{badge} →</a>'
        '</div>'
    )


def write_site(
    output_dir: Path,
    pages: tuple[BenchmarkPage, ...],
    charts_by_test_id: dict[str, ChartEntry],
    *,
    chart_tests: tuple[ChartTest, ...] = (),
    summaries: dict[str, ScenarioSummary] | None = None,
    run_environment: pd.DataFrame | None = None,
    violations: list[Violation] | None = None,
    flag_tickets: dict[str, FlagTicket] | None = None,
    channel: str = 'nightly',
    release_series: str = '',
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    env_frame = run_environment if run_environment is not None else pd.DataFrame()
    machine_panel = _machine_info_panel(env_frame)
    charts_by_id = {chart.test_id: chart for chart in chart_tests}
    scenario_summaries = summaries or {}
    regression_violations = violations or []
    tickets = flag_tickets or {}
    page_slugs_by_test_id = _page_slugs_by_test_id(pages)

    cards = ''.join(
        f'<a class="card" href="{escape(page.slug)}.html">'
        f'<h2>{escape(page.title)}</h2>'
        f'<p>{escape(page.description)}</p>'
        f'{_profile_facts(page)}</a>'
        for page in pages
    )
    if channel == 'release':
        heading = f'Windows {release_series} Release Benchmarks'
        subtitle = (
            f'Performance history for {release_series} release candidates through the final build. '
            'Each point is one RC or final benchmark run; the complete release series stays visible.'
        )
    elif channel == 'pr':
        heading = 'Windows Pull Request Benchmarks'
        subtitle = (
            'Performance history for this pull request. Each point is one requested benchmark run; '
            'release baselines are pinned separately for comparison.'
        )
    else:
        heading = 'Windows Nightly Benchmark Dashboard'
        subtitle = (
            f'Performance metrics from the last {CHART_WINDOW_DAYS} days. '
            'Each point is one nightly run; release baselines are pinned separately.'
        )
    index_body = (
        f'<nav class="back"><a href="{_channel_root_href(channel)}">← All Windows benchmarks</a></nav>'
        f'{_heading_with_badge(heading, channel)}'
        f'<p class="subtitle">{escape(subtitle)} '
        'Load-time charts plot the average of samples per run.</p>'
        f'{machine_panel}'
        f'{_summary_links_html(regression_violations)}'
        '<h2 style="margin-top:2rem">User profiles</h2>'
        f'<div class="grid">{cards}</div>'
        '<p class="note">Raw CSV history lives in the repository <code>data/</code> folder. '
        'PNG charts on GitHub: '
        f'<a href="{_github_readme_href(output_dir)}">{escape(_github_readme_rel(output_dir))}</a>.</p>'
    )
    (output_dir / 'index.html').write_text(_layout('Dashboard', index_body), encoding='utf-8')
    print('Generated index.html')

    (output_dir / 'summary.html').write_text(
        _layout(
            'Scenario summary',
            _summary_page(pages, charts_by_id, scenario_summaries, channel=channel),
        ),
        encoding='utf-8',
    )
    print('Generated summary.html')

    (output_dir / 'regression_report.html').write_text(
        _layout(
            'Flags',
            _regression_page(
                regression_violations,
                tickets,
                page_slugs_by_test_id,
                channel=channel,
            ),
        ),
        encoding='utf-8',
    )
    print('Generated regression_report.html')

    expected_pages = {f'{page.slug}.html' for page in pages} | {'summary.html', 'regression_report.html'}
    for page in pages:
        area_sections = []
        for area, area_label in PRODUCT_AREAS:
            groups = _scenario_groups(page, charts_by_id, area)
            if not groups:
                content = '<div class="area-empty">Not tested for this user profile.</div>'
            else:
                sections = ''.join(
                    _scenario_charts_section(group, charts_by_test_id)
                    for group in groups
                )
                content = f'<div class="scenario-list">{sections}</div>'
            area_sections.append(
                f'<section class="area-group"><h2>{escape(area_label)}</h2>{content}</section>'
            )
        page_body = (
            '<nav class="back"><a href="index.html">← Dashboard</a></nav>'
            f'{_heading_with_badge(page.title, channel)}'
            f'<p class="subtitle">{escape(page.description)}</p>'
            f'{_profile_details(page)}'
            f'{"".join(area_sections)}'
            f'{_chart_hash_script()}'
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
        channel=channel,
    )


def _channel_root_href(channel: str) -> str:
    if channel in {'release', 'pr'}:
        return '../../'
    return '../'


def _github_readme_rel(output_dir: Path) -> str:
    parts = output_dir.as_posix().replace('\\', '/')
    if 'docs/' in parts:
        return f'{parts[parts.index("docs/"):].rstrip("/")}/README.md'
    return f'docs/desktop/{output_dir.name}/README.md'


def _github_readme_href(output_dir: Path) -> str:
    return (
        'https://github.com/status-im/status-app-benchmarks/blob/master/'
        f'{_github_readme_rel(output_dir)}'
    )


def channel_listing_sort_key(name: str) -> tuple:
    """Sort PR numbers and dotted versions numerically, newest first when reversed."""
    if name.isdigit():
        return (0, int(name))
    parts = name.split('.')
    if parts and all(part.isdigit() for part in parts):
        return (1, tuple(int(part) for part in parts))
    return (2, name)


MANIFEST_CSV_NAME = 'runs.csv'


def _desktop_data_dir(desktop_dir: Path) -> Path:
    """Map docs/desktop -> <repo>/data/desktop."""
    return desktop_dir.parent.parent / 'data' / 'desktop'


def _format_run_date(value: object) -> str:
    text = _field_text(value)
    if not text:
        return ''
    try:
        parsed = pd.to_datetime(text, utc=True)
    except (TypeError, ValueError):
        return text
    if pd.isna(parsed):
        return text
    return parsed.strftime('%Y-%m-%d %H:%M UTC')


LISTING_HISTORY_LIMIT = 8


def _load_runs_frame(runs_csv: Path) -> pd.DataFrame | None:
    if not runs_csv.exists():
        return None
    try:
        frame = pd.read_csv(runs_csv)
    except (OSError, pd.errors.EmptyDataError, pd.errors.ParserError):
        return None
    if frame.empty:
        return None
    ordered = frame.copy()
    ordered['_sort_date'] = pd.to_datetime(
        ordered['date'] if 'date' in ordered.columns else pd.NaT,
        errors='coerce',
        utc=True,
    )
    return ordered.sort_values('_sort_date', ascending=False, na_position='last')


def _run_history_entries(frame: pd.DataFrame) -> list[dict[str, object]]:
    """Newest-first run rows for listing cards (commit + date per publish)."""
    entries: list[dict[str, object]] = []
    for _, row in frame.head(LISTING_HISTORY_LIMIT).iterrows():
        entries.append({
            'commit': _field_text(row.get('commit_hash')) or 'unknown',
            'date': _format_run_date(row.get('date')),
            'version': _field_text(row.get('release_version')),
        })
    return entries


def _unique_commit_count(frame: pd.DataFrame) -> int:
    if 'commit_hash' not in frame.columns:
        return 0
    commits = {_field_text(value) for value in frame['commit_hash'] if _field_text(value)}
    return len(commits)


def _history_list_html(entries: list[dict[str, object]]) -> str:
    if not entries:
        return ''
    items = []
    for entry in entries:
        commit = str(entry.get('commit') or '')
        date_text = str(entry.get('date') or '')
        version = str(entry.get('version') or '')
        left = escape(commit)
        if version:
            left = f'{escape(version)} · {escape(commit)}'
        items.append(
            '<li>'
            f'<span class="commit">{left}</span>'
            f'<span>{escape(date_text)}</span>'
            '</li>'
        )
    return f'<ul class="listing-history">{"".join(items)}</ul>'


def _listing_card(
    *,
    href: str,
    title: str,
    meta_lines: list[str],
    history_html: str = '',
    extra_href: str = '',
    extra_label: str = '',
) -> str:
    meta_html = ''.join(
        f'<p class="listing-meta">{escape(line)}</p>' for line in meta_lines if line
    )
    extra = ''
    if extra_href and extra_label:
        extra = (
            f'<a class="listing-extra" href="{escape(extra_href, quote=True)}" '
            f'target="_blank" rel="noopener">{escape(extra_label)}</a>'
        )
    return (
        f'<article class="card listing-card">'
        f'<a class="listing-main" href="{escape(href, quote=True)}">'
        f'<h2>{escape(title)}</h2>{meta_html}{history_html}</a>{extra}</article>'
    )


def _pr_listing_card(path: Path, data_root: Path) -> str:
    runs_csv = data_root / 'pr' / path.name / MANIFEST_CSV_NAME
    frame = _load_runs_frame(runs_csv)
    title = f'PR #{path.name}'
    meta_lines: list[str] = []
    history_html = ''
    if frame is None or frame.empty:
        meta_lines.append('No run metadata yet.')
    else:
        run_count = len(frame)
        commit_count = _unique_commit_count(frame)
        latest_date = _format_run_date(frame.iloc[0].get('date'))
        parts = []
        if run_count:
            parts.append(f'{run_count} run{"s" if run_count != 1 else ""}')
        if commit_count:
            parts.append(f'{commit_count} commit{"s" if commit_count != 1 else ""}')
        if latest_date:
            parts.append(f'last {latest_date}')
        if parts:
            meta_lines.append(' · '.join(parts))
        history_html = _history_list_html(_run_history_entries(frame))
        remaining = run_count - min(run_count, LISTING_HISTORY_LIMIT)
        if remaining > 0:
            history_html += (
                f'<p class="listing-meta">+{remaining} earlier run'
                f'{"s" if remaining != 1 else ""}</p>'
            )
    return _listing_card(
        href=f'{path.name}/',
        title=title,
        meta_lines=meta_lines,
        history_html=history_html,
        extra_href=f'{STATUS_APP_REPO}/pull/{path.name}',
        extra_label='View on GitHub →',
    )


def _release_listing_card(path: Path, data_root: Path) -> str:
    runs_csv = data_root / 'releases' / path.name / MANIFEST_CSV_NAME
    frame = _load_runs_frame(runs_csv)
    title = f'Release {path.name}'
    meta_lines: list[str] = []
    history_html = ''
    if frame is None or frame.empty:
        meta_lines.append('No run metadata yet.')
    else:
        run_count = len(frame)
        latest_date = _format_run_date(frame.iloc[0].get('date'))
        parts = []
        if run_count:
            parts.append(f'{run_count} run{"s" if run_count != 1 else ""}')
        if latest_date:
            parts.append(f'last {latest_date}')
        if parts:
            meta_lines.append(' · '.join(parts))
        history_html = _history_list_html(_run_history_entries(frame))
        remaining = run_count - min(run_count, LISTING_HISTORY_LIMIT)
        if remaining > 0:
            history_html += (
                f'<p class="listing-meta">+{remaining} earlier run'
                f'{"s" if remaining != 1 else ""}</p>'
            )
    return _listing_card(
        href=f'{path.name}/',
        title=title,
        meta_lines=meta_lines,
        history_html=history_html,
    )


def _channel_directory_cards(
    parent: Path,
    data_root: Path,
    *,
    kind: str,
) -> str:
    if not parent.exists():
        return '<p class="note">No published runs yet.</p>'
    entries = [
        path for path in parent.iterdir()
        if path.is_dir() and (path / 'index.html').exists()
    ]
    entries.sort(key=lambda item: channel_listing_sort_key(item.name), reverse=True)
    if not entries:
        return '<p class="note">No published runs yet.</p>'
    if kind == 'pr':
        cards = ''.join(_pr_listing_card(path, data_root) for path in entries)
    else:
        cards = ''.join(_release_listing_card(path, data_root) for path in entries)
    return f'<div class="grid">{cards}</div>'


def _write_nightly_stub(nightly_dir: Path) -> None:
    """Placeholder until the first nightly graphs publish lands in docs/desktop/nightly/."""
    if (nightly_dir / 'index.html').exists():
        return
    nightly_dir.mkdir(parents=True, exist_ok=True)
    body = (
        '<nav class="back"><a href="../">← All Windows benchmarks</a></nav>'
        f'{_heading_with_badge("Windows Nightly Benchmark Dashboard", "nightly")}'
        '<p class="subtitle">Nightly charts have not been published to this path yet.</p>'
        '<p class="note">After the next successful nightly publish, this page is replaced '
        'with the full rolling dashboard. Older charts may still appear under '
        '<a href="../">docs/desktop/</a> until that cleanup.</p>'
    )
    (nightly_dir / 'index.html').write_text(
        _layout('Nightly benchmarks', body), encoding='utf-8',
    )
    print(f'Generated nightly stub {nightly_dir / "index.html"}')


def write_desktop_landing(desktop_dir: Path) -> None:
    """Write the channel picker and discovered PR/release-series links."""
    desktop_dir.mkdir(parents=True, exist_ok=True)
    data_root = _desktop_data_dir(desktop_dir)

    releases_dir = desktop_dir / 'releases'
    prs_dir = desktop_dir / 'pr'
    nightly_dir = desktop_dir / 'nightly'
    releases_dir.mkdir(parents=True, exist_ok=True)
    prs_dir.mkdir(parents=True, exist_ok=True)
    _write_nightly_stub(nightly_dir)

    (releases_dir / 'index.html').write_text(
        _layout(
            'Release benchmarks',
            '<nav class="back"><a href="../">← All Windows benchmarks</a></nav>'
            f'{_heading_with_badge("Release benchmarks", "release")}'
            '<p class="subtitle">RC-to-final performance history, isolated by release series.</p>'
            f'{_channel_directory_cards(releases_dir, data_root, kind="release")}',
        ),
        encoding='utf-8',
    )
    (prs_dir / 'index.html').write_text(
        _layout(
            'Pull request benchmarks',
            '<nav class="back"><a href="../">← All Windows benchmarks</a></nav>'
            f'{_heading_with_badge("Pull request benchmarks", "pr")}'
            '<p class="subtitle">Persistent benchmark history for explicitly tested pull requests.</p>'
            f'{_channel_directory_cards(prs_dir, data_root, kind="pr")}',
        ),
        encoding='utf-8',
    )

    body = (
        '<h1>Windows Benchmark Dashboard</h1>'
        '<p class="subtitle">Nightly, pull request, and release results are stored '
        'and charted independently.</p>'
        '<div class="grid">'
        '<a class="card" href="nightly/"><h2>Nightly</h2>'
        '<p>Rolling master performance trend and promoted release baselines.</p></a>'
        '<a class="card" href="releases/"><h2>Releases</h2>'
        '<p>RC-to-final trend charts, with a separate page for every release.</p></a>'
        '<a class="card" href="pr/"><h2>Pull requests</h2>'
        '<p>On-demand PR benchmark runs and comparisons with release baselines.</p></a>'
        '</div>'
    )
    (desktop_dir / 'index.html').write_text(
        _layout('Windows benchmarks', body), encoding='utf-8',
    )
    (desktop_dir / 'README.md').write_text(
        '\n'.join([
            '# Windows benchmarks',
            '',
            'Nightly, pull request, and release charts are stored separately:',
            '',
            '- [Nightly](nightly/README.md)',
            '- [Releases](releases/)',
            '- [Pull requests](pr/)',
            '',
            'Interactive dashboard: '
            '[docs/desktop/](https://status-im.github.io/status-app-benchmarks/desktop/).',
            '',
        ]),
        encoding='utf-8',
    )
    print(f'Generated {desktop_dir / "index.html"}')


def _profile_data_markdown(page: BenchmarkPage) -> list[str]:
    return [
        '### User data profile',
        '',
        f'- **Stored data:** {page.user_data_size}',
        (
            f'- **Wallet:** {page.wallet_accounts} wallet accounts · '
            f'{page.wallet_tokens} tokens with balance > 0 · '
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
        'Reference parity (where shown) means the latest value '
        'is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** '
        'because the e2e test now waits for tab content (Jul 2026).',
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
                measured_cell = (
                    f'{build}<br>{date}'
                    if build != '—' or date != '—' else '—'
                )
                lines.append(
                    f'| {page.title} | {area_label} | {scenario.display_name} '
                    f'| {load_time} | {_reference_markdown(vs_reference)} '
                    f'| {cpu_value} | {ram_value} '
                    f'| {measured_cell} |'
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
    channel: str = 'nightly',
) -> None:
    """GitHub-rendered fallback dashboard (PNG embeds) until GitHub Pages is enabled."""
    if channel == 'release':
        window_line = (
            'Charts show the full RC-to-final history for this release. '
            'Each point is one requested benchmark run.'
        )
    elif channel == 'pr':
        window_line = (
            'Charts show every requested run for this pull request. '
            'Each point is one benchmark run.'
        )
    else:
        window_line = (
            f'Charts show data from the last {CHART_WINDOW_DAYS} days — '
            'each point is one nightly run.'
        )
    lines = [
        '# Windows — performance benchmarks',
        '',
        'Automated test suite performance tracking for the Windows desktop app.',
        window_line,
        'Load-time charts plot the average of runs per build. Lower is better.',
        '',
        '> **Viewing charts:** This README renders inline PNG images on GitHub — works without',
        '> GitHub Pages. For interactive charts (hover tooltips, zoom), use the',
        '> [interactive dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) once GitHub Pages is enabled.',
        '',
        f'Full CSV history: [`data/`](../../data/).',
        '',
        '> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — '
        'benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab '
        'tests now wait for tab content. Nightly trend continues; non-tab scenarios still '
        'compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new '
        'baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).',
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
