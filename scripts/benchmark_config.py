"""Benchmark configuration loaded from tests_config.toml."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Optional

import tomli as tomllib

CHART_WINDOW_DAYS = 30
DEFAULT_CONFIG = Path('scripts/tests_config.toml')
LOAD_TIME_FOOTNOTE = 'Each point = average of 5 runs on that build.'

MetricsKind = Literal['performance', 'cpu', 'ram']


@dataclass(frozen=True)
class ChartDefaults:
    slow_threshold_s: float = 1.0
    fast_threshold_s: float = 0.5
    regression_pct: float = 0.15
    regression_consecutive: int = 3
    rolling_window: int = 5
    backlog_slow_of_last_n: int = 5
    backlog_slow_min_count: int = 3


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
    description: str = ''
    show_speed_zones: bool = False
    show_rolling_average: bool = False
    reference_build: Optional[str] = None
    baselines: tuple[str, ...] = ()


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
    defaults: ChartDefaults


def _require_fields(raw: dict, *fields: str, context: str = 'config') -> None:
    for field in fields:
        if field not in raw:
            raise ValueError(f'Missing required field {field!r} in {context}')


def _load_defaults(raw: dict) -> ChartDefaults:
    entry = raw.get('defaults', {})
    return ChartDefaults(
        slow_threshold_s=entry.get('slow_threshold_s', 1.0),
        fast_threshold_s=entry.get('fast_threshold_s', 0.5),
        regression_pct=entry.get('regression_pct', 0.15),
        regression_consecutive=entry.get('regression_consecutive', 3),
        rolling_window=entry.get('rolling_window', 5),
        backlog_slow_of_last_n=entry.get('backlog_slow_of_last_n', 5),
        backlog_slow_min_count=entry.get('backlog_slow_min_count', 3),
    )


def _load_chart_tests(
    entries: list[dict],
    *,
    metrics_kind: MetricsKind,
    value_column: str,
    default_ylabel: str,
    default_attachment_keyword: str,
    default_footnote: str = '',
    default_show_speed_zones: bool = False,
    default_show_rolling_average: bool = False,
) -> list[ChartTest]:
    charts = []
    for entry in entries:
        _require_fields(
            entry,
            'test_id', 'display_name', 'graph_filename', 'pattern',
            context=f'{metrics_kind} test',
        )
        baselines = entry.get('baselines', [])
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
            footnote=entry.get('footnote', default_footnote),
            description=entry.get('description', ''),
            show_speed_zones=entry.get('show_speed_zones', default_show_speed_zones),
            show_rolling_average=entry.get('show_rolling_average', default_show_rolling_average),
            reference_build=entry.get('reference_build'),
            baselines=tuple(baselines),
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

    defaults = _load_defaults(raw)

    load_time_tests = _load_chart_tests(
        raw.get('tests', []),
        metrics_kind='performance',
        value_column='avg_time',
        default_ylabel='seconds',
        default_attachment_keyword='load time',
        default_footnote=LOAD_TIME_FOOTNOTE,
        default_show_speed_zones=True,
        default_show_rolling_average=True,
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
        defaults=defaults,
    )
