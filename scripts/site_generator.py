"""Static HTML site generator for GitHub Pages benchmark dashboard."""

from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Optional

import pandas as pd

from benchmark_config import CHART_WINDOW_DAYS, BenchmarkPage, ChartEntry
from environment_parser import RUN_ENVIRONMENT_FIELDS

CHARTS_DIR = 'charts'
SITE_TITLE = 'Status App Benchmarks'
MACHINE_FIELD_LABELS = {
    'hostname': 'Host',
    'windows_version': 'Windows',
    'os_build': 'OS build',
    'cpu': 'CPU',
    'ram_gb': 'RAM',
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
    section.chart {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem 1.25rem 1.25rem;
      margin-bottom: 1.5rem;
    }
    section.chart h2 { margin: 0 0 0.75rem; font-size: 1.05rem; }
    section.chart iframe {
      width: 100%;
      height: 540px;
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


def _chart_iframe(chart_path: str) -> str:
    return (
        f'<iframe src="{escape(chart_path)}" '
        'title="Interactive chart" loading="lazy"></iframe>'
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
        f'<h2>{escape(chart.display_name)}</h2>'
        f'{_chart_iframe(chart_path)}'
        '</section>'
    )


def write_site(
    output_dir: Path,
    pages: tuple[BenchmarkPage, ...],
    charts_by_test_id: dict[str, ChartEntry],
    *,
    chart_labels: dict[str, str] | None = None,
    run_environment: pd.DataFrame | None = None,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    env_frame = run_environment if run_environment is not None else pd.DataFrame()
    machine_panel = _machine_info_panel(env_frame)
    labels = chart_labels or {}

    cards = ''.join(
        f'<a class="card" href="{escape(page.slug)}.html">'
        f'<h2>{escape(page.title)}</h2>'
        f'<p>{escape(page.description)}</p></a>'
        for page in pages
    )
    index_body = (
        '<h1>Windows Benchmark Dashboard</h1>'
        f'<p class="subtitle">Performance metrics from the last {CHART_WINDOW_DAYS} days. '
        'Each point is one nightly run — x-axis shows build date; hover a point for commit hash. '
        'Load-time charts plot the average of runs per build.</p>'
        f'{machine_panel}'
        '<h2 style="margin-top:2rem">Scenarios</h2>'
        f'<div class="grid">{cards}</div>'
        '<p class="note">Raw CSV history lives in the repository <code>data/</code> folder. '
        'PNG charts on GitHub: '
        '<a href="https://github.com/status-im/status-app-benchmarks/blob/master/docs/desktop/README.md">'
        'docs/desktop/README.md</a>.</p>'
    )
    (output_dir / 'index.html').write_text(_layout('Dashboard', index_body), encoding='utf-8')
    print('Generated index.html')

    expected_pages = {f'{page.slug}.html' for page in pages}
    for page in pages:
        sections = []
        for test_id in page.test_ids:
            chart = charts_by_test_id.get(test_id)
            if chart is not None:
                sections.append(_chart_section(chart))
            else:
                sections.append(_placeholder_section(labels.get(test_id, test_id)))
        page_body = (
            '<nav class="back"><a href="index.html">← Dashboard</a></nav>'
            f'<h1>{escape(page.title)}</h1>'
            f'<p class="subtitle">{escape(page.description)}</p>'
            f'{"".join(sections)}'
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
        run_environment=env_frame,
    )


def write_github_readme(
    output_dir: Path,
    pages: tuple[BenchmarkPage, ...],
    charts_by_test_id: dict[str, ChartEntry],
    *,
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

    for page in pages:
        page_charts = [
            charts_by_test_id[test_id]
            for test_id in page.test_ids
            if test_id in charts_by_test_id
        ]
        lines.extend([f'## {page.title}', '', page.description, ''])
        if not page_charts:
            lines.append(
                '_No data yet — charts will appear after the next nightly benchmark run._'
            )
            lines.append('')
            continue
        for chart in page_charts:
            png_name = Path(chart.html_filename).with_suffix('.png').name
            lines.append(f'![{chart.display_name}](./{png_name})')
            lines.append('')

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
