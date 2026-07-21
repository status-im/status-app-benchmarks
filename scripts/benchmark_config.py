"""Benchmark configuration loaded from tests_config.toml."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Optional

import tomli as tomllib

CHART_WINDOW_DAYS = 30
DEFAULT_CONFIG = Path('scripts/tests_config.toml')
LOAD_TIME_FOOTNOTE = 'Each point = average of 5 runs on that build.'
DESKTOP_BUILD_LABELS = Path('data/desktop/build_labels.csv')

MetricsKind = Literal['performance', 'cpu', 'ram']
ProductArea = Literal['wallet', 'messenger', 'communities', 'browser']


@dataclass(frozen=True)
class ChartDefaults:
    slow_threshold_s: float = 1.0
    fast_threshold_s: float = 0.5
    ok_near_slow_ratio: float = 0.10
    regression_pct: float = 0.15
    regression_consecutive: int = 3
    rolling_window: int = 5
    backlog_slow_of_last_n: int = 5
    backlog_slow_min_count: int = 3
    baselines: tuple[str, ...] = ()
    reference_build: Optional[str] = None


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
    area: ProductArea
    source_pattern: Optional[str] = None
    color: Optional[str] = None
    footnote: str = ''
    description: str = ''
    show_speed_zones: bool = False
    show_rolling_average: bool = False
    reference_build: Optional[str] = None
    baselines: tuple[str, ...] = ()
    historical_patterns: tuple[str, ...] = ()
    historical_attachment_keywords: tuple[str, ...] = ()


@dataclass(frozen=True)
class BenchmarkPage:
    slug: str
    title: str
    description: str
    test_ids: tuple[str, ...]
    user_data_size: str
    wallet_accounts: str
    wallet_tokens: str
    wallet_nfts: str
    wallet_transactions: str
    messenger_direct_chats: str
    messenger_group_chats: str
    communities_joined: str
    communities_spectated: str


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


def load_desktop_build_labels(labels_file: Path = DESKTOP_BUILD_LABELS) -> dict[str, str]:
    """Map commit_hash -> display label (| separates lines on the chart axis)."""
    if not labels_file.exists():
        return {}
    labels: dict[str, str] = {}
    with open(labels_file, newline='', encoding='utf-8') as handle:
        for row in csv.DictReader(handle):
            if row.get('exclude'):
                continue
            commit_hash = row.get('commit_hash', '').strip()
            label = row.get('label', '').strip()
            if commit_hash and label:
                labels[commit_hash] = label
    return labels


def _load_defaults(raw: dict) -> ChartDefaults:
    entry = raw.get('defaults', {})
    baselines = entry.get('baselines', [])
    return ChartDefaults(
        slow_threshold_s=entry.get('slow_threshold_s', 1.0),
        fast_threshold_s=entry.get('fast_threshold_s', 0.5),
        ok_near_slow_ratio=entry.get('ok_near_slow_ratio', 0.10),
        regression_pct=entry.get('regression_pct', 0.15),
        regression_consecutive=entry.get('regression_consecutive', 3),
        rolling_window=entry.get('rolling_window', 5),
        backlog_slow_of_last_n=entry.get('backlog_slow_of_last_n', 5),
        backlog_slow_min_count=entry.get('backlog_slow_min_count', 3),
        baselines=tuple(baselines),
        reference_build=entry.get('reference_build'),
    )


def _load_chart_tests(
    entries: list[dict],
    *,
    metrics_kind: MetricsKind,
    value_column: str,
    default_ylabel: str,
    default_attachment_keyword: str,
    defaults: ChartDefaults,
    default_footnote: str = '',
    default_show_speed_zones: bool = False,
    default_show_rolling_average: bool = False,
    inherit_baselines: bool = True,
) -> list[ChartTest]:
    charts = []
    for entry in entries:
        _require_fields(
            entry,
            'test_id', 'display_name', 'graph_filename', 'pattern',
            context=f'{metrics_kind} test',
        )
        if 'baselines' in entry:
            baselines = tuple(entry['baselines'])
        elif inherit_baselines:
            baselines = defaults.baselines
        else:
            baselines = ()
        reference_build = (
            entry['reference_build'] if 'reference_build' in entry
            else (defaults.reference_build if inherit_baselines else None)
        )
        charts.append(ChartTest(
            test_id=entry['test_id'],
            display_name=entry['display_name'],
            graph_filename=entry['graph_filename'],
            pattern=entry['pattern'],
            ylabel=entry.get('ylabel', default_ylabel),
            value_column=entry.get('value_column', value_column),
            metrics_kind=metrics_kind,
            attachment_keyword=entry.get('attachment_keyword', default_attachment_keyword),
            area=entry.get('area', 'wallet'),
            source_pattern=entry.get('source_pattern'),
            color=entry.get('color'),
            footnote=entry.get('footnote', default_footnote),
            description=entry.get('description', ''),
            show_speed_zones=entry.get('show_speed_zones', default_show_speed_zones),
            show_rolling_average=entry.get('show_rolling_average', default_show_rolling_average),
            reference_build=reference_build,
            baselines=baselines,
            historical_patterns=tuple(entry.get('historical_patterns', [])),
            historical_attachment_keywords=tuple(
                entry.get('historical_attachment_keywords', [])
            ),
        ))
    return charts


def _expand_wallet_scenarios(
    raw: dict,
    defaults: ChartDefaults,
) -> tuple[list[ChartTest], dict[str, list[str]]]:
    profiles = raw.get('wallet_profile_variants', [])
    scenarios = raw.get('wallet_scenarios', [])
    if not profiles and not scenarios:
        return [], {}
    if not profiles or not scenarios:
        raise ValueError(
            'Both [[wallet_profile_variants]] and [[wallet_scenarios]] are required'
        )

    performance_entries = []
    cpu_entries = []
    ram_entries = []
    page_test_ids: dict[str, list[str]] = {}

    for scenario in scenarios:
        _require_fields(
            scenario,
            'scenario_id', 'display_name', 'resource_action',
            'test_pattern', 'graph_stem', 'footnote',
            context='wallet scenario',
        )
        for profile in profiles:
            _require_fields(
                profile,
                'suffix', 'param_id', 'page_slug', 'footnote_prefix',
                context='wallet profile variant',
            )
            suffix = profile['suffix']
            scenario_id = scenario['scenario_id']
            source_pattern = f"{scenario['test_pattern']}[{profile['param_id']}]"
            series_test_pattern = scenario.get(
                'series_test_pattern', scenario['test_pattern']
            )
            test_pattern = f"{series_test_pattern}[{profile['param_id']}]"
            historical_patterns = [
                f"{pattern}[{profile['param_id']}]"
                for pattern in scenario.get('historical_test_patterns', [])
            ]
            historical_attachment_subjects = scenario.get(
                'historical_attachment_subjects', []
            )
            if (
                historical_attachment_subjects
                and len(historical_attachment_subjects) != len(historical_patterns)
            ):
                raise ValueError(
                    f"Wallet scenario {scenario_id!r} must define one "
                    'historical_attachment_subject per historical_test_pattern'
                )
            footnote = f"{profile['footnote_prefix']} · {scenario['footnote']}"
            attachment_subject = scenario.get('attachment_subject')
            base_entry = {
                'area': 'wallet',
                'pattern': test_pattern,
                'source_pattern': source_pattern,
                'historical_patterns': historical_patterns,
                'footnote': footnote,
            }
            metric_entries = (
                (
                    performance_entries,
                    {
                        **base_entry,
                        'test_id': f'test_{scenario_id}_time_{suffix}',
                        'display_name': scenario['display_name'],
                        'description': 'Lower is better.',
                        'graph_filename': f"{scenario['graph_stem']}_time_{suffix}.png",
                        **(
                            {'attachment_keyword': f'{attachment_subject} load time'}
                            if attachment_subject else {}
                        ),
                        'historical_attachment_keywords': [
                            f'{subject} load time'
                            for subject in historical_attachment_subjects
                        ],
                    },
                ),
                (
                    cpu_entries,
                    {
                        **base_entry,
                        'test_id': f'test_{scenario_id}_cpu_{suffix}',
                        'display_name': f"CPU usage while {scenario['resource_action']}",
                        'graph_filename': f"{scenario['graph_stem']}_cpu_{suffix}.png",
                        **(
                            {'attachment_keyword': f'{attachment_subject} CPU usage'}
                            if attachment_subject else {}
                        ),
                        'historical_attachment_keywords': [
                            f'{subject} CPU usage'
                            for subject in historical_attachment_subjects
                        ],
                    },
                ),
                (
                    ram_entries,
                    {
                        **base_entry,
                        'test_id': f'test_{scenario_id}_ram_{suffix}',
                        'display_name': f"RAM usage while {scenario['resource_action']}",
                        'graph_filename': f"{scenario['graph_stem']}_ram_{suffix}.png",
                        **(
                            {'attachment_keyword': f'{attachment_subject} RAM usage'}
                            if attachment_subject else {}
                        ),
                        'historical_attachment_keywords': [
                            f'{subject} RAM usage'
                            for subject in historical_attachment_subjects
                        ],
                    },
                ),
            )
            page_ids = page_test_ids.setdefault(profile['page_slug'], [])
            for entries, entry in metric_entries:
                entries.append(entry)
                page_ids.append(entry['test_id'])

    charts = [
        *_load_chart_tests(
            performance_entries,
            metrics_kind='performance',
            value_column='avg_time',
            default_ylabel='seconds',
            default_attachment_keyword='load time',
            defaults=defaults,
            default_show_speed_zones=True,
            default_show_rolling_average=True,
        ),
        *_load_chart_tests(
            cpu_entries,
            metrics_kind='cpu',
            value_column='avg_cpu',
            default_ylabel='CPU Usage (%)',
            default_attachment_keyword='cpu usage',
            defaults=defaults,
            default_show_rolling_average=True,
        ),
        *_load_chart_tests(
            ram_entries,
            metrics_kind='ram',
            value_column='avg_ram_mb',
            default_ylabel='RAM Usage (MB)',
            default_attachment_keyword='ram usage',
            defaults=defaults,
            default_show_rolling_average=True,
        ),
    ]
    return charts, page_test_ids


def _load_pages(
    entries: list[dict],
    generated_test_ids: Optional[dict[str, list[str]]] = None,
) -> list[BenchmarkPage]:
    generated_test_ids = generated_test_ids or {}
    pages = []
    for entry in entries:
        _require_fields(entry, 'slug', 'title', context='page')
        wallet = entry.get('wallet', {})
        messenger = entry.get('messenger', {})
        communities = entry.get('communities', {})
        test_ids = [
            *generated_test_ids.get(entry['slug'], []),
            *entry.get('test_ids', []),
        ]
        pages.append(BenchmarkPage(
            slug=entry['slug'],
            title=entry['title'],
            description=entry.get('description', ''),
            test_ids=tuple(test_ids),
            user_data_size=str(entry.get('user_data_size', 'TBD')),
            wallet_accounts=str(wallet.get('accounts', 'TBD')),
            wallet_tokens=str(wallet.get('tokens', 'TBD')),
            wallet_nfts=str(wallet.get('nfts', 'TBD')),
            wallet_transactions=str(wallet.get('transactions', 'TBD')),
            messenger_direct_chats=str(messenger.get('direct_chats', 'TBD')),
            messenger_group_chats=str(messenger.get('group_chats', 'TBD')),
            communities_joined=str(communities.get('joined', 'TBD')),
            communities_spectated=str(communities.get('spectated', 'TBD')),
        ))
    return pages


def _validate_config(pages: list[BenchmarkPage], charts: list[ChartTest]) -> None:
    chart_ids = [chart.test_id for chart in charts]
    duplicate_ids = sorted({
        test_id for test_id in chart_ids if chart_ids.count(test_id) > 1
    })
    if duplicate_ids:
        raise ValueError(f'Duplicate chart test IDs: {", ".join(duplicate_ids)}')

    graph_filenames = [chart.graph_filename for chart in charts]
    duplicate_filenames = sorted({
        filename for filename in graph_filenames
        if graph_filenames.count(filename) > 1
    })
    if duplicate_filenames:
        raise ValueError(
            f'Duplicate chart filenames: {", ".join(duplicate_filenames)}'
        )

    known_ids = set(chart_ids)
    for page in pages:
        duplicate_page_ids = sorted({
            test_id for test_id in page.test_ids
            if page.test_ids.count(test_id) > 1
        })
        if duplicate_page_ids:
            raise ValueError(
                f'Duplicate chart IDs on page {page.slug}: '
                + ', '.join(duplicate_page_ids)
            )
        unknown_ids = sorted(set(page.test_ids) - known_ids)
        if unknown_ids:
            raise ValueError(
                f'Unknown chart IDs on page {page.slug}: {", ".join(unknown_ids)}'
            )


def load_benchmark_config(config_file: Path) -> BenchmarkConfig:
    if not config_file.exists():
        raise FileNotFoundError(f'Config file not found: {config_file}')

    with open(config_file, 'rb') as handle:
        raw = tomllib.load(handle)

    defaults = _load_defaults(raw)
    wallet_charts, generated_page_test_ids = _expand_wallet_scenarios(raw, defaults)

    load_time_tests = _load_chart_tests(
        raw.get('tests', []),
        metrics_kind='performance',
        value_column='avg_time',
        default_ylabel='seconds',
        default_attachment_keyword='load time',
        defaults=defaults,
        default_footnote=LOAD_TIME_FOOTNOTE,
        default_show_speed_zones=True,
        default_show_rolling_average=True,
    )
    if not load_time_tests and not any(
        chart.metrics_kind == 'performance' for chart in wallet_charts
    ):
        raise ValueError(f'No [[tests]] sections found in {config_file}')

    charts = [
        *wallet_charts,
        *load_time_tests,
        *_load_chart_tests(
            raw.get('cpu_tests', []),
            metrics_kind='cpu',
            value_column='avg_cpu',
            default_ylabel='CPU Usage (%)',
            default_attachment_keyword='cpu usage',
            defaults=defaults,
            default_show_rolling_average=True,
        ),
        *_load_chart_tests(
            raw.get('ram_tests', []),
            metrics_kind='ram',
            value_column='avg_ram_mb',
            default_ylabel='RAM Usage (MB)',
            default_attachment_keyword='ram usage',
            defaults=defaults,
            default_show_rolling_average=True,
        ),
    ]

    pages = _load_pages(raw.get('pages', []), generated_page_test_ids)
    configured_page_slugs = {page.slug for page in pages}
    unknown_generated_pages = sorted(
        set(generated_page_test_ids) - configured_page_slugs
    )
    if unknown_generated_pages:
        raise ValueError(
            'Wallet profile variants reference unknown pages: '
            + ', '.join(unknown_generated_pages)
        )
    _validate_config(pages, charts)

    return BenchmarkConfig(
        pages=tuple(pages),
        charts=tuple(charts),
        defaults=defaults,
    )
