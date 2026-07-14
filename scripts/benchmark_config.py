"""Benchmark configuration loaded from tests_config.toml."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Optional

import tomli as tomllib

CHART_WINDOW_DAYS = 30
DEFAULT_CONFIG = Path('scripts/tests_config.toml')
LOAD_TIME_FOOTNOTE = 'Each point = average of runs on that build.'
RUN_SPREAD_FOOTNOTE = (
    'Line = average across runs on that build; shaded band = min–max. '
    'Hover a point to see all individual run values.'
)

MetricsKind = Literal['performance', 'cpu', 'ram']


@dataclass(frozen=True)
class ChartTest:
    test_id: str
    display_name: str
    graph_filename: str
    pattern: str
    ylabel: str
    value_column: str
    metrics_kind: MetricsKind
    attachment_keyword: str
    color: Optional[str] = None
    footnote: str = ''
    show_run_spread: bool = False


@dataclass(frozen=True)
class BenchmarkPage:
    slug: str
    title: str
    description: str
    test_ids: tuple[str, ...]


@dataclass(frozen=True)
class ChartEntry:
    display_name: str
    html_filename: str
    footnote: str = ''


@dataclass(frozen=True)
class BenchmarkConfig:
    pages: tuple[BenchmarkPage, ...]
    charts: tuple[ChartTest, ...]


def _require_fields(raw: dict, *fields: str, context: str = 'config') -> None:
    for field in fields:
        if field not in raw:
            raise ValueError(f'Missing required field {field!r} in {context}')


def _load_chart_tests(
    entries: list[dict],
    *,
    metrics_kind: MetricsKind,
    value_column: str,
    default_ylabel: str,
    default_attachment_keyword: str,
    default_footnote: str = '',
) -> list[ChartTest]:
    charts = []
    for entry in entries:
        _require_fields(
            entry,
            'test_id', 'display_name', 'graph_filename', 'pattern',
            context=f'{metrics_kind} test',
        )
        show_run_spread = bool(entry.get('show_run_spread', False))
        if 'footnote' in entry:
            footnote = entry['footnote']
        elif show_run_spread:
            footnote = RUN_SPREAD_FOOTNOTE
        else:
            footnote = default_footnote
        charts.append(ChartTest(
            test_id=entry['test_id'],
            display_name=entry['display_name'],
            graph_filename=entry['graph_filename'],
            pattern=entry['pattern'],
            ylabel=entry.get('ylabel', default_ylabel),
            value_column=entry.get('value_column', value_column),
            metrics_kind=metrics_kind,
            attachment_keyword=entry.get('attachment_keyword', default_attachment_keyword),
            color=entry.get('color'),
            footnote=footnote,
            show_run_spread=show_run_spread,
        ))
    return charts


def _load_pages(entries: list[dict]) -> list[BenchmarkPage]:
    pages = []
    for entry in entries:
        _require_fields(entry, 'slug', 'title', 'test_ids', context='page')
        pages.append(BenchmarkPage(
            slug=entry['slug'],
            title=entry['title'],
            description=entry.get('description', ''),
            test_ids=tuple(entry['test_ids']),
        ))
    return pages


def load_benchmark_config(config_file: Path) -> BenchmarkConfig:
    if not config_file.exists():
        raise FileNotFoundError(f'Config file not found: {config_file}')

    with open(config_file, 'rb') as handle:
        raw = tomllib.load(handle)

    load_time_tests = _load_chart_tests(
        raw.get('tests', []),
        metrics_kind='performance',
        value_column='avg_time',
        default_ylabel='Load Time (s)',
        default_attachment_keyword='load time',
        default_footnote=LOAD_TIME_FOOTNOTE,
    )
    if not load_time_tests:
        raise ValueError(f'No [[tests]] sections found in {config_file}')

    charts = [
        *load_time_tests,
        *_load_chart_tests(
            raw.get('cpu_tests', []),
            metrics_kind='cpu',
            value_column='avg_cpu',
            default_ylabel='CPU Usage (%)',
            default_attachment_keyword='cpu usage',
        ),
        *_load_chart_tests(
            raw.get('ram_tests', []),
            metrics_kind='ram',
            value_column='avg_ram_mb',
            default_ylabel='RAM Usage (MB)',
            default_attachment_keyword='ram usage',
        ),
    ]

    return BenchmarkConfig(
        pages=tuple(_load_pages(raw.get('pages', []))),
        charts=tuple(charts),
    )
