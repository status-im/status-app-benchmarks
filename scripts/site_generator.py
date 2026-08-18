"""Static HTML site generator for GitHub Pages benchmark dashboard."""

from __future__ import annotations

from dataclasses import dataclass
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
from environment_parser import RUN_ENVIRONMENT_FIELDS, load_run_environment
from regression_report import ScenarioSummary, Violation
from run_context import latest_run_row, load_run_manifest, utc_dates

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
    'ok-warn': 'Near ok',
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


@dataclass(frozen=True)
class NightlyBaseline:
    label: str = ''
    title: str = ''
    name: str = ''

    @classmethod
    def for_pr(
        cls,
        label: str = '',
        title: str = '',
        name: str = '',
    ) -> 'NightlyBaseline':
        return cls(
            label=label or 'vs nightly',
            title=title or (
                'Difference from the latest nightly at the time this PR was measured'
            ),
            name=name or 'latest nightly',
        )


@dataclass(frozen=True)
class _ScenarioSnapshot:
    scenario: ChartTest
    performance_chart: ChartTest | None
    performance: ScenarioSummary | None
    cpu_chart: ChartTest | None
    cpu: ScenarioSummary | None
    ram_chart: ChartTest | None
    ram: ScenarioSummary | None
    measured: ScenarioSummary | None
    vs_reference: str
    vs_nightly: str


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
    .page-heading h1 a { color: inherit; text-decoration: none; }
    .page-heading h1 a:hover { text-decoration: underline; }
    .page-heading h1 .pr-title { font-weight: 600; }
    .profile-page-name {
      margin: 0.85rem 0 0.25rem;
      font-size: 1.2rem;
    }
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
    .summary-heading {
      margin: 2rem 0 0.55rem;
      font-size: 1.35rem;
      text-align: center;
    }
    .summary-legend {
      margin: 0 0 1.5rem;
      text-align: center;
    }
    .summary-legend-note {
      margin: 0.7rem auto 0;
      max-width: 38rem;
      color: var(--text);
      font-size: 0.88rem;
      line-height: 1.45;
    }
    details.summary-profile {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
      margin: 0.75rem 0;
    }
    details.summary-profile[open] { border-color: var(--link); }
    details.summary-profile > summary {
      cursor: pointer;
      padding: 0.9rem 1.1rem;
      font-weight: 600;
    }
    details.summary-profile > summary:hover {
      background: var(--accent-data-bg);
    }
    details.summary-profile > summary:focus-visible {
      outline: 2px solid var(--link);
      outline-offset: -2px;
    }
    .summary-profile-body {
      border-top: 1px solid var(--border);
      padding: 0.25rem 1rem 1rem;
    }
    .summary-profile-body .subtitle { margin: 0.75rem 0 0; }
    section.summary-profile { margin: 2rem 0; }
    section.summary-profile h2 { margin-bottom: 0.25rem; }
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
    .summary-table th.nightly-column {
      white-space: normal;
      min-width: 6.75rem;
    }
    .summary-table th .column-date {
      display: block;
      margin-top: 0.12rem;
      font-weight: 500;
      font-size: 0.72rem;
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
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.45rem 0.6rem;
    }
    .speed-legend .status { margin: 0; }
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
    section.last-run {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
      gap: 0.45rem 0.9rem;
      background: var(--accent-data-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.8rem 1.15rem;
      margin: 1rem 0;
    }
    .last-run-label {
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--muted);
    }
    .last-run-date {
      font-size: 1.05rem;
      font-weight: 600;
    }
    a.last-run-commit {
      display: inline-flex;
      align-items: center;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.92rem;
      font-weight: 600;
      color: var(--link);
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 0.2rem 0.55rem;
      text-decoration: none;
    }
    a.last-run-commit:hover {
      border-color: var(--link);
      text-decoration: underline;
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
  <meta http-equiv="Cache-Control" content="no-store">
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


def _heading_with_badge(heading: str, channel: str, *, heading_html: str = '') -> str:
    title_html = heading_html or f'<h1>{escape(heading)}</h1>'
    return (
        f'<div class="page-heading">{_channel_badge_html(channel)}'
        f'{title_html}</div>'
    )


def _back_nav(href: str, label: str) -> str:
    return f'<nav class="back"><a href="{escape(href)}">← {escape(label)}</a></nav>'


def _channel_subheading(channel: str, text: str) -> str:
    if channel != 'pr':
        return ''
    return f'<h2 class="profile-page-name">{escape(text)}</h2>'


def _count_label(count: int, singular: str) -> str:
    return f'{count} {singular}' if count == 1 else f'{count} {singular}s'


def _pr_url(pr_number: str) -> str:
    return f'{STATUS_APP_REPO}/pull/{pr_number}'


def _channel_page_title(
    channel: str,
    heading: str,
    heading_html: str,
    fallback: str,
) -> tuple[str, str]:
    if channel == 'pr':
        return heading, heading_html
    return fallback, ''


def _write_page(output_dir: Path, filename: str, title: str, body: str) -> None:
    (output_dir / filename).write_text(_layout(title, body), encoding='utf-8')
    print(f'Generated {filename}')


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
    row = latest_run_row(run_environment)
    if row is None:
        return None
    latest = row.to_dict()
    if not any(_field_text(latest.get(field)) for field in RUN_ENVIRONMENT_FIELDS):
        return None
    return latest


def _run_date_label(value: object) -> str:
    if hasattr(value, 'strftime'):
        try:
            if pd.isna(value):
                return ''
        except (TypeError, ValueError):
            pass
        return value.strftime('%b %d, %Y')
    text = _field_text(value)
    if not text:
        return ''
    try:
        parsed = pd.to_datetime(text)
    except (TypeError, ValueError):
        return text
    if pd.isna(parsed):
        return text
    return parsed.strftime('%b %d, %Y')


def _sha_from_local_git(commit: str) -> str:
    """Resolve a prefix to a full SHA from a local status-app checkout, if present."""
    import os
    import subprocess

    candidates: list[Path] = []
    env_dir = os.environ.get('STATUS_APP_GIT_DIR', '').strip()
    if env_dir:
        candidates.append(Path(env_dir))
    candidates.append(Path(__file__).resolve().parents[1].parent / 'status-app')
    for git_dir in candidates:
        git_meta = git_dir / '.git'
        if not git_dir.exists() or not (git_meta.exists() or git_dir.is_dir()):
            continue
        try:
            result = subprocess.run(
                ['git', '-C', str(git_dir), 'rev-parse', '--verify', f'{commit}^{{commit}}'],
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired):
            continue
        sha = (result.stdout or '').strip()
        if result.returncode == 0 and len(sha) >= 40:
            return sha
    return ''


def _github_api_json(resource: str) -> dict:
    import json
    import os
    from urllib.error import URLError
    from urllib.request import Request, urlopen

    repo = STATUS_APP_REPO.removeprefix('https://github.com/')
    headers = {
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'status-app-benchmarks',
    }
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
    if token:
        headers['Authorization'] = f'Bearer {token}'
    request = Request(
        f'https://api.github.com/repos/{repo}/{resource}',
        headers=headers,
    )
    try:
        with urlopen(request, timeout=8) as response:
            payload = json.loads(response.read().decode('utf-8'))
    except (URLError, TimeoutError, ValueError, OSError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _fetch_full_commit_sha(commit: str) -> str:
    """Resolve a short prefix to the full 40-char SHA."""
    local = _sha_from_local_git(commit)
    if local:
        return local
    sha = str(_github_api_json(f'commits/{commit}').get('sha') or '').strip()
    return sha if len(sha) >= 40 else ''


_pr_titles: dict[str, str] = {}
PR_TITLE_FILENAME = 'pr_title.txt'


def _pr_title_cache_path(data_dir: Path) -> Path:
    return data_dir / PR_TITLE_FILENAME


def load_pr_title(data_dir: Path) -> str:
    path = _pr_title_cache_path(data_dir)
    if not path.exists():
        return ''
    return path.read_text(encoding='utf-8').strip()


def save_pr_title(data_dir: Path, title: str) -> None:
    title = title.strip()
    if not title:
        return
    data_dir.mkdir(parents=True, exist_ok=True)
    path = _pr_title_cache_path(data_dir)
    current = load_pr_title(data_dir)
    if current == title:
        return
    path.write_text(title + '\n', encoding='utf-8')


def _pr_title_from_runs(data_dir: Path) -> str:
    row = latest_run_row(load_run_manifest(data_dir))
    if row is None:
        return ''
    ref = _field_text(row.get('source_ref'))
    return ref.replace('-', ' ') if ref else ''


def _inferred_pr_data_dir(output_dir: Path) -> Path | None:
    if not output_dir.name.isdigit() or output_dir.parent.name != 'pr':
        return None
    data_dir = _desktop_data_dir(output_dir.parent.parent) / 'pr' / output_dir.name
    return data_dir if data_dir.exists() else None


def _fetch_pr_title(pr_number: str) -> str:
    if not pr_number.isdigit():
        return ''
    cached = _pr_titles.get(pr_number)
    if cached:
        return cached
    title = str(_github_api_json(f'pulls/{pr_number}').get('title') or '').strip()
    if title:
        _pr_titles[pr_number] = title
    return title


def resolve_pr_title(
    pr_number: str,
    *,
    data_dir: Path | None = None,
    pr_title: str = '',
) -> str:
    title = pr_title.strip()
    if not title and data_dir is not None:
        title = load_pr_title(data_dir)
    if not title and pr_number:
        title = _fetch_pr_title(pr_number)
    if not title and data_dir is not None:
        title = _pr_title_from_runs(data_dir)
    if title and data_dir is not None:
        save_pr_title(data_dir, title)
    return title


def pr_page_heading(pr_number: str, pr_title: str = '') -> str:
    if pr_number and pr_title:
        return f'#{pr_number} {pr_title}'
    if pr_number:
        return f'#{pr_number}'
    return 'Windows Pull Request Benchmarks'


def _pr_heading_html(pr_number: str, pr_title: str) -> str:
    if not pr_number:
        return f'<h1>{escape(pr_page_heading(pr_number, pr_title))}</h1>'
    href = _pr_url(pr_number)
    number = (
        f'<a href="{href}" title="{href}" target="_blank">'
        f'#{escape(pr_number)}</a>'
    )
    title = (
        f'<span class="pr-title"> {escape(pr_title)}</span>' if pr_title else ''
    )
    return f'<h1>{number}{title}</h1>'


def _pr_heading_markdown(pr_number: str, pr_title: str) -> str:
    if not pr_number:
        return pr_page_heading(pr_number, pr_title)
    return f'[#{pr_number}]({_pr_url(pr_number)}) {pr_title}'.strip()


def _resolve_pr_identity(
    output_dir: Path,
    pr_number: str = '',
    pr_title: str = '',
) -> tuple[str, str]:
    number = pr_number.strip() or (output_dir.name if output_dir.name.isdigit() else '')
    data_dir = _inferred_pr_data_dir(output_dir)
    title = resolve_pr_title(number, data_dir=data_dir, pr_title=pr_title)
    return number, title


_expanded_commit_shas: dict[str, str] = {}


def _expand_commit_sha(commit: str) -> str:
    if len(commit) >= 40:
        return commit[:40]
    cached = _expanded_commit_shas.get(commit)
    if cached:
        return cached
    sha = _fetch_full_commit_sha(commit)
    if sha:
        _expanded_commit_shas[commit] = sha
        return sha
    return commit


def _commit_github_href(commit: str) -> str:
    return f'{STATUS_APP_REPO}/commit/{_expand_commit_sha(commit)}'


def _commit_link_html(commit: str) -> str:
    sha = _expand_commit_sha(commit).lower()
    short = escape((sha or commit)[:9])
    if len(sha) != 40 or any(char not in '0123456789abcdef' for char in sha):
        return f'<span class="last-run-commit">{short}</span>'
    href = f'{STATUS_APP_REPO}/commit/{sha}'
    return (
        f'<a class="last-run-commit" href="{href}" title="{href}" '
        f'target="_blank">{short}</a>'
    )


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
    return (
        '<section class="machine-info">'
        '<h2>System info</h2>'
        '<p class="subtitle">Windows e2e benchmark runner</p>'
        f'<dl>{"".join(items)}</dl>'
        '</section>'
    )


def _last_run_stamp(frame: pd.DataFrame) -> tuple[str, str]:
    row = latest_run_row(frame)
    if row is None:
        return '', ''
    return _row_stamp(row)


def _last_run_panel(run_environment: pd.DataFrame) -> str:
    date, commit = _last_run_stamp(run_environment)
    if not date and not commit:
        return ''
    date_html = (
        f'<span class="last-run-date">{escape(date)}</span>' if date else ''
    )
    commit_html = _commit_link_html(commit) if commit else ''
    return (
        '<section class="last-run">'
        '<span class="last-run-label">Last run</span>'
        f'{date_html}{commit_html}'
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
    return ['## System info', '', 'Windows e2e benchmark runner.', '', ' · '.join(parts), '']


def _last_run_markdown(run_environment: pd.DataFrame) -> list[str]:
    date, commit = _last_run_stamp(run_environment)
    parts = ['**Last run**']
    if date:
        parts.append(date)
    if commit:
        parts.append(f'[`{commit[:9]}`]({_commit_github_href(commit)})')
    if len(parts) == 1:
        return []
    return [' · '.join(parts), '']


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


def _measured_parts(measured: ScenarioSummary | None) -> tuple[str, str]:
    build = measured.commit_hash[:9] if measured is not None and measured.commit_hash else '—'
    date = measured.date if measured is not None and measured.date else '—'
    return build, date


def _metric_or_dash(chart: ChartTest | None, summary: ScenarioSummary | None) -> str:
    return _metric_value(chart, summary) if chart is not None else '—'


def _measured_cell_html(build: str, date: str) -> str:
    if build == '—' and date == '—':
        return '—'
    return (
        '<div class="measured-cell">'
        f'<span class="measured-build">{escape(build)}</span>'
        f'<span class="measured-date">{escape(date)}</span>'
        '</div>'
    )


def _reference_style(value: str, *, baseline: str = '2.38.0') -> tuple[str, str]:
    if value == 'parity':
        return 'reference-parity', f'Within ±15% of {baseline}'
    if value.startswith('+'):
        return 'reference-regression', f'Slower than {baseline}'
    if value.startswith('-'):
        return 'reference-improvement', f'Faster than {baseline}'
    return 'reference-neutral', 'No reference comparison available'


def _reference_html(value: str, *, baseline: str = '2.38.0') -> str:
    css_class, title = _reference_style(value, baseline=baseline)
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


def _row_stamp(row: object) -> tuple[str, str]:
    date = _run_date_label(row.get('date') if hasattr(row, 'get') else None)
    commit_value = row.get('commit_hash') if hasattr(row, 'get') else ''
    return date, _field_text(commit_value)


def _nightly_stamp(
    run_environment: pd.DataFrame | None = None,
    metrics: dict[str, pd.DataFrame] | None = None,
) -> tuple[str, str]:
    row = latest_run_row(run_environment)
    if row is None and metrics:
        row = latest_run_row(metrics.get('performance'))
    if row is None:
        return '', ''
    return _row_stamp(row)


def nightly_comparison_header(
    run_environment: pd.DataFrame | None = None,
    metrics: dict[str, pd.DataFrame] | None = None,
) -> tuple[str, str, str]:
    """Column label, tooltip, and cell baseline name for vs nightly."""
    date, commit = _nightly_stamp(run_environment, metrics)
    label = f'vs nightly · {date}' if date else 'vs nightly'
    name = f'nightly {date}' if date else 'latest nightly'
    if date and commit:
        title = f'Difference from nightly {date} · commit {commit[:9]}'
    elif date:
        title = f'Difference from nightly {date}'
    else:
        title = 'Difference from the latest nightly at the time this PR was measured'
    return label, title, name


def _nightly_header_html(label: str, title: str) -> str:
    main, _sep, date = label.partition(' · ')
    if date:
        inner = f'{escape(main)}<span class="column-date">{escape(date)}</span>'
    else:
        inner = escape(label)
    return (
        f'<th class="reference-column nightly-column" '
        f'title="{escape(title, quote=True)}">{inner}</th>'
    )


def _nightly_cell_html(value: str, *, label: str, name: str) -> str:
    return (
        f'<td class="reference-column" data-label="{escape(label, quote=True)}">'
        f'{_reference_html(value, baseline=name)}</td>'
    )


def _optional_nightly_cell(value: str, nightly: NightlyBaseline) -> str:
    if not nightly.label:
        return ''
    return _nightly_cell_html(value, label=nightly.label, name=nightly.name)


def _comparison_values(
    performance_chart: ChartTest | None,
    performance: ScenarioSummary | None,
) -> tuple[str, str]:
    if performance_chart is None or performance is None:
        return '—', '—'
    return performance.vs_reference, performance.vs_nightly


def _scenario_snapshot(
    group: dict[str, ChartTest],
    summaries: dict[str, ScenarioSummary],
) -> _ScenarioSnapshot:
    performance_chart, performance = _scenario_summary(group, summaries, 'performance')
    cpu_chart, cpu = _scenario_summary(group, summaries, 'cpu')
    ram_chart, ram = _scenario_summary(group, summaries, 'ram')
    vs_reference, vs_nightly = _comparison_values(performance_chart, performance)
    return _ScenarioSnapshot(
        scenario=_scenario_chart(group),
        performance_chart=performance_chart,
        performance=performance,
        cpu_chart=cpu_chart,
        cpu=cpu,
        ram_chart=ram_chart,
        ram=ram,
        measured=_measured_summary(group, summaries),
        vs_reference=vs_reference,
        vs_nightly=vs_nightly,
    )


def _load_time_html(snapshot: _ScenarioSnapshot) -> str:
    if snapshot.performance_chart is None:
        return '—'
    return (
        '<div class="load-time-cell">'
        f'<span class="metric-value">'
        f'{escape(_metric_value(snapshot.performance_chart, snapshot.performance))}'
        f'</span>{_status_badges(snapshot.performance)}</div>'
    )


def _load_time_markdown(snapshot: _ScenarioSnapshot) -> str:
    if snapshot.performance_chart is None:
        return '—'
    status = (
        snapshot.performance.speed_status
        if snapshot.performance is not None else 'no-data'
    )
    return (
        f'{_metric_value(snapshot.performance_chart, snapshot.performance)} · '
        f'{STATUS_LABELS[status]}'
    )


def _summary_row(
    area_label: str,
    group: dict[str, ChartTest] | None,
    summaries: dict[str, ScenarioSummary],
    page_slug: str,
    *,
    nightly: NightlyBaseline = NightlyBaseline(),
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
            f'{_optional_nightly_cell("—", nightly)}'
            '<td data-label="CPU">—</td>'
            '<td data-label="RAM">—</td>'
            '<td data-label="Measured">—</td>'
            '</tr>'
        )

    snapshot = _scenario_snapshot(group, summaries)
    build, date = _measured_parts(snapshot.measured)
    scenario_link = (
        f'<a href="{_chart_href(page_slug, snapshot.scenario.test_id)}">'
        f'{escape(snapshot.scenario.display_name)}</a>'
    )
    return (
        '<tr>'
        f'<td data-label="Area">{escape(area_label)}</td>'
        f'<td data-label="Scenario">{scenario_link}</td>'
        f'<td data-label="Load time / Speed">{_load_time_html(snapshot)}</td>'
        f'<td class="reference-column" data-label="vs 2.38.0">'
        f'{_reference_html(snapshot.vs_reference)}</td>'
        f'{_optional_nightly_cell(snapshot.vs_nightly, nightly)}'
        f'<td data-label="CPU">{escape(_metric_or_dash(snapshot.cpu_chart, snapshot.cpu))}</td>'
        f'<td data-label="RAM">{escape(_metric_or_dash(snapshot.ram_chart, snapshot.ram))}</td>'
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


def _summary_intro(*, nightly_column: str = '') -> str:
    nightly_note = ''
    if nightly_column:
        nightly_note = (
            f' <strong>{escape(nightly_column)}</strong> compares the same load time '
            'with that nightly run — the latest nightly at the time this PR was measured.'
        )
    return (
        '<h2 class="summary-heading">Test scenarios</h2>'
        '<div class="summary-legend">'
        '<div class="speed-legend">'
        '<span class="status status-fast">Fast · &lt;0.5s</span>'
        '<span class="status status-ok">Ok · 0.5–0.9s</span>'
        '<span class="status status-ok-warn">Near ok · 0.9–1.0s</span>'
        '<span class="status status-slow">Slow · &gt;1.0s</span>'
        '</div>'
        '<p class="summary-legend-note">'
        'The <strong>vs 2.38.0</strong> column compares the latest load time with the '
        '2.38.0 release. A difference within ±15% is shown as parity.'
        f'{nightly_note}'
        '</p>'
        '</div>'
    )


def _summary_profile_section(
    page: BenchmarkPage,
    charts_by_id: dict[str, ChartTest],
    summaries: dict[str, ScenarioSummary],
    *,
    nightly: NightlyBaseline = NightlyBaseline(),
) -> str:
    keyed_rows: list[tuple[float, str]] = []
    scenario_count = 0
    for area, area_label in PRODUCT_AREAS:
        groups = _scenario_groups(page, charts_by_id, area) or [None]
        if groups[0] is not None:
            scenario_count += len(groups)
        for group in groups:
            keyed_rows.append((
                _summary_sort_key(group, summaries),
                _summary_row(
                    area_label, group, summaries, page.slug, nightly=nightly,
                ),
            ))
    keyed_rows.sort(key=lambda item: item[0], reverse=True)
    rows = ''.join(html for _key, html in keyed_rows)
    count_label = _count_label(scenario_count, 'scenario')
    nightly_header = (
        _nightly_header_html(nightly.label, nightly.title) if nightly.label else ''
    )
    return (
        '<details class="summary-profile">'
        '<summary><span class="scenario-summary-content">'
        f'<span>{escape(page.title)}</span>'
        f'<span class="scenario-chart-count">{count_label}</span>'
        '</span></summary>'
        '<div class="summary-profile-body">'
        f'<p class="subtitle">{escape(page.description)} '
        f'<a href="{escape(page.slug)}.html">Open profile →</a></p>'
        '<table class="summary-table"><thead><tr>'
        '<th>Area</th><th>Scenario</th>'
        '<th class="load-time-column" '
        'title="Latest measured loading time and mobile-style speed category">'
        'Load time / Speed</th>'
        '<th class="reference-column" '
        'title="Difference from the 2.38.0 reference build">vs 2.38.0</th>'
        f'{nightly_header}'
        '<th title="Average CPU usage during the scenario">CPU</th>'
        '<th title="Average RAM usage during the scenario">RAM</th>'
        '<th class="measured-column" '
        'title="Build and date of the latest scenario result">Measured</th>'
        f'</tr></thead><tbody>{rows}</tbody></table>'
        '</div></details>'
    )


def _summary_sections(
    pages: tuple[BenchmarkPage, ...],
    charts_by_id: dict[str, ChartTest],
    summaries: dict[str, ScenarioSummary],
    *,
    nightly: NightlyBaseline = NightlyBaseline(),
) -> str:
    return ''.join(
        _summary_profile_section(page, charts_by_id, summaries, nightly=nightly)
        for page in pages
    )


def _profile_cards_html(pages: tuple[BenchmarkPage, ...]) -> str:
    return ''.join(
        f'<a class="card" href="{escape(page.slug)}.html">'
        f'<h2>{escape(page.title)}</h2>'
        f'<p>{escape(page.description)}</p>'
        f'{_profile_facts(page)}</a>'
        for page in pages
    )


def _profiles_page(
    pages: tuple[BenchmarkPage, ...],
    *,
    channel: str = 'nightly',
    heading: str = 'User profiles',
    heading_html: str = '',
) -> str:
    return (
        f'{_back_nav("index.html", "Dashboard")}'
        f'{_heading_with_badge(heading, channel, heading_html=heading_html)}'
        '<p class="subtitle">Choose a user profile to open its scenario charts.</p>'
        f'<div class="grid">{_profile_cards_html(pages)}</div>'
    )


def _redirect_page(href: str, label: str) -> str:
    return (
        '<!DOCTYPE html><html lang="en"><head>'
        '<meta charset="utf-8">'
        f'<meta http-equiv="refresh" content="0;url={escape(href)}">'
        f'<link rel="canonical" href="{escape(href)}">'
        f'<title>Redirecting</title></head><body>'
        f'<p><a href="{escape(href)}">{escape(label)}</a></p>'
        '</body></html>'
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
    heading: str = 'Flags',
    heading_html: str = '',
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
    flags_title = _channel_subheading(channel, 'Flags')
    return (
        f'{_back_nav("index.html", "Dashboard")}'
        f'{_heading_with_badge(heading, channel, heading_html=heading_html)}'
        f'{flags_title}'
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
        '<a class="summary-link" href="profiles.html">User profiles →</a>'
        f'<a class="summary-link" href="regression_report.html">View flags{badge} →</a>'
        '</div>'
    )


def _channel_copy(
    channel: str,
    *,
    release_series: str = '',
    nightly: NightlyBaseline = NightlyBaseline(),
    pr_number: str = '',
    pr_title: str = '',
) -> tuple[str, str, str]:
    if channel == 'release':
        heading = f'Windows {release_series} Release Benchmarks'
        subtitle = (
            f'Performance history for {release_series} release candidates through the final build. '
            'Each point is one RC or final benchmark run; the complete release series stays visible.'
        )
        return heading, '', subtitle
    if channel == 'pr':
        heading = pr_page_heading(pr_number, pr_title)
        subtitle = (
            'Performance history for this pull request. Each point is one requested benchmark run. '
            f'vs 2.38.0 is the last release; {nightly.label} is the latest master nightly '
            'at measurement time.'
        )
        return heading, _pr_heading_html(pr_number, pr_title), subtitle
    return (
        'Windows Nightly Benchmark Dashboard',
        '',
        f'Performance metrics from the last {CHART_WINDOW_DAYS} days. '
        'Each point is one nightly run; release baselines are pinned separately.',
    )


def _profile_areas_html(
    page: BenchmarkPage,
    charts_by_id: dict[str, ChartTest],
    charts_by_test_id: dict[str, ChartEntry],
) -> str:
    sections = []
    for area, area_label in PRODUCT_AREAS:
        groups = _scenario_groups(page, charts_by_id, area)
        if not groups:
            content = '<div class="area-empty">Not tested for this user profile.</div>'
        else:
            content = (
                '<div class="scenario-list">'
                + ''.join(
                    _scenario_charts_section(group, charts_by_test_id)
                    for group in groups
                )
                + '</div>'
            )
        sections.append(
            f'<section class="area-group"><h2>{escape(area_label)}</h2>{content}</section>'
        )
    return ''.join(sections)


def write_site(
    output_dir: Path,
    pages: tuple[BenchmarkPage, ...],
    charts_by_test_id: dict[str, ChartEntry],
    *,
    chart_tests: tuple[ChartTest, ...] = (),
    summaries: dict[str, ScenarioSummary] | None = None,
    runs: pd.DataFrame | None = None,
    violations: list[Violation] | None = None,
    flag_tickets: dict[str, FlagTicket] | None = None,
    channel: str = 'nightly',
    release_series: str = '',
    nightly_baseline_label: str = '',
    nightly_baseline_title: str = '',
    nightly_baseline_name: str = '',
    pr_number: str = '',
    pr_title: str = '',
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    runs_frame = runs if runs is not None else pd.DataFrame()
    machine_panel = _last_run_panel(runs_frame)
    charts_by_id = {chart.test_id: chart for chart in chart_tests}
    scenario_summaries = summaries or {}
    regression_violations = violations or []
    tickets = flag_tickets or {}
    page_slugs_by_test_id = _page_slugs_by_test_id(pages)

    nightly = NightlyBaseline()
    resolved_pr_number = ''
    resolved_pr_title = ''
    if channel == 'pr':
        nightly = NightlyBaseline.for_pr(
            nightly_baseline_label,
            nightly_baseline_title,
            nightly_baseline_name,
        )
        resolved_pr_number, resolved_pr_title = _resolve_pr_identity(
            output_dir, pr_number, pr_title,
        )
    heading, heading_html, subtitle = _channel_copy(
        channel,
        release_series=release_series,
        nightly=nightly,
        pr_number=resolved_pr_number,
        pr_title=resolved_pr_title,
    )
    index_body = (
        f'{_back_nav(_channel_root_href(channel), "All Windows benchmarks")}'
        f'{_heading_with_badge(heading, channel, heading_html=heading_html)}'
        f'<p class="subtitle">{escape(subtitle)} '
        'Load-time charts plot the average of samples per run.</p>'
        f'{machine_panel}'
        f'{_summary_links_html(regression_violations)}'
        f'{_summary_intro(nightly_column=nightly.label)}'
        f'{_summary_sections(pages, charts_by_id, scenario_summaries, nightly=nightly)}'
        '<p class="note">Raw CSV history lives in the repository <code>data/</code> folder. '
        'PNG charts on GitHub: '
        f'<a href="{_github_readme_href(output_dir)}">{escape(_github_readme_rel(output_dir))}</a>.</p>'
    )
    _write_page(output_dir, 'index.html', heading, index_body)

    profiles_title, profiles_html = _channel_page_title(
        channel, heading, heading_html, 'User profiles',
    )
    _write_page(
        output_dir, 'profiles.html', profiles_title,
        _profiles_page(
            pages, channel=channel,
            heading=profiles_title, heading_html=profiles_html,
        ),
    )

    (output_dir / 'summary.html').write_text(
        _redirect_page('index.html', 'View scenario summary'),
        encoding='utf-8',
    )
    print('Generated summary.html')

    flags_title, flags_html = _channel_page_title(
        channel, heading, heading_html, 'Flags',
    )
    _write_page(
        output_dir, 'regression_report.html', flags_title,
        _regression_page(
            regression_violations,
            tickets,
            page_slugs_by_test_id,
            channel=channel,
            heading=flags_title,
            heading_html=flags_html,
        ),
    )

    expected_pages = {
        f'{page.slug}.html' for page in pages
    } | {'summary.html', 'profiles.html', 'regression_report.html'}
    for page in pages:
        page_title, page_html = _channel_page_title(
            channel, heading, heading_html, page.title,
        )
        back_label = heading if channel == 'pr' else 'User profiles'
        page_body = (
            f'{_back_nav("profiles.html", back_label)}'
            f'{_heading_with_badge(page_title, channel, heading_html=page_html)}'
            f'{_channel_subheading(channel, page.title)}'
            f'<p class="subtitle">{escape(page.description)}</p>'
            f'{_profile_details(page)}'
            f'{_profile_areas_html(page, charts_by_id, charts_by_test_id)}'
            f'{_chart_hash_script()}'
        )
        _write_page(output_dir, f'{page.slug}.html', page_title, page_body)

    for stale_page in output_dir.glob('*.html'):
        if stale_page.name != 'index.html' and stale_page.name not in expected_pages:
            stale_page.unlink()
            print(f'Removed stale page: {stale_page.name}')

    write_github_readme(
        output_dir, pages, charts_by_test_id,
        chart_tests=chart_tests,
        summaries=scenario_summaries,
        runs=runs_frame,
        channel=channel,
        nightly_baseline_label=nightly.label,
        pr_number=resolved_pr_number,
        pr_title=resolved_pr_title,
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
    frame = load_run_manifest(runs_csv)
    if frame.empty:
        return None
    return frame.assign(_sort_date=utc_dates(frame)).sort_values(
        '_sort_date', ascending=False, na_position='last',
    )


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


def _listing_history(
    frame: pd.DataFrame | None,
    *,
    include_commits: bool = False,
) -> tuple[list[str], str]:
    if frame is None or frame.empty:
        return ['No run metadata yet.'], ''
    run_count = len(frame)
    parts: list[str] = []
    if run_count:
        parts.append(_count_label(run_count, 'run'))
    if include_commits:
        commit_count = _unique_commit_count(frame)
        if commit_count:
            parts.append(_count_label(commit_count, 'commit'))
    latest_date = _format_run_date(frame.iloc[0].get('date'))
    if latest_date:
        parts.append(f'last {latest_date}')
    history_html = _history_list_html(_run_history_entries(frame))
    remaining = run_count - min(run_count, LISTING_HISTORY_LIMIT)
    if remaining > 0:
        history_html += (
            f'<p class="listing-meta">+{_count_label(remaining, "earlier run")}</p>'
        )
    return ([' · '.join(parts)] if parts else []), history_html


def _pr_listing_card(path: Path, data_root: Path) -> str:
    data_dir = data_root / 'pr' / path.name
    frame = _load_runs_frame(data_dir)
    meta_lines, history_html = _listing_history(frame, include_commits=True)
    return _listing_card(
        href=f'{path.name}/',
        title=pr_page_heading(path.name, resolve_pr_title(path.name, data_dir=data_dir)),
        meta_lines=meta_lines,
        history_html=history_html,
        extra_href=_pr_url(path.name),
        extra_label='View on GitHub →',
    )


def _release_listing_card(path: Path, data_root: Path) -> str:
    frame = _load_runs_frame(data_root / 'releases' / path.name)
    meta_lines, history_html = _listing_history(frame)
    return _listing_card(
        href=f'{path.name}/',
        title=f'Release {path.name}',
        meta_lines=meta_lines,
        history_html=history_html,
    )


def _channel_directory_cards(
    parent: Path,
    data_root: Path,
    *,
    kind: str,
) -> str:
    empty = '<p class="note">No published runs yet.</p>'
    if not parent.exists():
        return empty
    entries = [
        path for path in parent.iterdir()
        if path.is_dir() and (path / 'index.html').exists()
    ]
    entries.sort(key=lambda item: channel_listing_sort_key(item.name), reverse=True)
    if not entries:
        return empty
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
        f'{_back_nav("../", "All Windows benchmarks")}'
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
            f'{_back_nav("../", "All Windows benchmarks")}'
            f'{_heading_with_badge("Release benchmarks", "release")}'
            '<p class="subtitle">RC-to-final performance history, isolated by release series.</p>'
            f'{_channel_directory_cards(releases_dir, data_root, kind="release")}',
        ),
        encoding='utf-8',
    )
    (prs_dir / 'index.html').write_text(
        _layout(
            'Pull request benchmarks',
            f'{_back_nav("../", "All Windows benchmarks")}'
            f'{_heading_with_badge("Pull request benchmarks", "pr")}'
            '<p class="subtitle">Persistent benchmark history for explicitly tested pull requests.</p>'
            f'{_channel_directory_cards(prs_dir, data_root, kind="pr")}',
        ),
        encoding='utf-8',
    )

    nightly_env = load_run_environment(desktop_dir.parent.parent / 'data')
    host_panel = _machine_info_panel(nightly_env)
    body = (
        '<h1>Windows Benchmark Dashboard</h1>'
        '<p class="subtitle">Nightly, pull request, and release results are stored '
        'and charted independently.</p>'
        f'{host_panel}'
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
    readme_lines = [
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
    ]
    readme_lines.extend(_machine_info_markdown(nightly_env))
    (desktop_dir / 'README.md').write_text('\n'.join(readme_lines), encoding='utf-8')
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
    *,
    nightly_column: str = '',
) -> list[str]:
    nightly_note = (
        f' **{nightly_column}** is that nightly run — the latest nightly when this PR was measured.'
        if nightly_column else ''
    )
    nightly_header = f' {nightly_column} |' if nightly_column else ''
    nightly_divider = '----------------------|' if nightly_column else ''
    empty_row_tail = '| — | — | — | — |' + (' — |' if nightly_column else '')
    lines = [
        '## Scenario summary',
        '',
        'Latest result for every tested scenario. Speed categories:',
        '',
        '**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**',
        '',
        'Reference parity (where shown) means the latest value '
        'is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** '
        'because the e2e test now waits for tab content (Jul 2026).'
        + nightly_note,
        '',
        '| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 |'
        f'{nightly_header} CPU | RAM | Measured |',
        '|--------------|------|----------|-------------------|-----------|'
        f'{nightly_divider}-----|-----|----------|',
    ]
    for page in pages:
        for area, area_label in PRODUCT_AREAS:
            groups = _scenario_groups(page, charts_by_id, area)
            if not groups:
                lines.append(
                    f'| {page.title} | {area_label} | Not tested | Not tested '
                    f'{empty_row_tail}'
                )
                continue
            for group in groups:
                snapshot = _scenario_snapshot(group, summaries)
                build, date = _measured_parts(snapshot.measured)
                measured_cell = (
                    f'{build}<br>{date}'
                    if build != '—' or date != '—' else '—'
                )
                nightly_cell = (
                    f'{_reference_markdown(snapshot.vs_nightly)} | '
                    if nightly_column else ''
                )
                lines.append(
                    f'| {page.title} | {area_label} | {snapshot.scenario.display_name} '
                    f'| {_load_time_markdown(snapshot)} | '
                    f'{_reference_markdown(snapshot.vs_reference)} | '
                    f'{nightly_cell}'
                    f'{_metric_or_dash(snapshot.cpu_chart, snapshot.cpu)} | '
                    f'{_metric_or_dash(snapshot.ram_chart, snapshot.ram)} '
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
    runs: pd.DataFrame | None = None,
    channel: str = 'nightly',
    nightly_baseline_label: str = '',
    pr_number: str = '',
    pr_title: str = '',
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
    if channel == 'pr' and pr_number:
        readme_heading = _pr_heading_markdown(pr_number, pr_title)
    else:
        readme_heading = 'Windows — performance benchmarks'
    lines = [
        f'# {readme_heading}',
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

    stamp_frame = runs if runs is not None else pd.DataFrame()
    lines.extend(_last_run_markdown(stamp_frame))
    charts_by_id = {chart.test_id: chart for chart in chart_tests}
    scenario_summaries = summaries or {}
    lines.extend(
        _github_summary_markdown(
            pages, charts_by_id, scenario_summaries,
            nightly_column=nightly_baseline_label,
        )
    )

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
