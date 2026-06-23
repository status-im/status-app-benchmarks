#!/usr/bin/env python3
"""Mobile (Android) performance charts — matplotlib/seaborn.

Deliberately separate from benchmark.py (desktop charts, plotly): this module
imports only matplotlib + seaborn + pandas + tomli and never plotly/kaleido, which
do not build on the Raspberry Pi that generates the mobile charts. Loaded by
android_perf_publish.py; the two charting paths share no dependencies.
"""
from __future__ import annotations

import csv as _csv
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import pandas as pd
import tomli as tomllib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid", palette="muted")
plt.rcParams.update({
    "figure.dpi": 200, "savefig.bbox": "tight", "font.size": 11,
    "axes.titlesize": 14, "axes.labelsize": 12,
    "xtick.labelsize": 10, "ytick.labelsize": 10, "legend.fontsize": 10,
})

PERFORMANCE_COLORS = ['#10AC84', '#2E86DE', '#F79F1F', '#54A0FF']


@dataclass
class PerformanceTest:
    test_id: str
    display_name: str
    graph_filename: str
    pattern: str
    ylabel: str = "Load Time (ms)"
    color: Optional[str] = None
    unit: str = "ms"          # "ms" or "s" (seconds axis)
    metric: str = "avg"       # "avg" or "min" (min for floor-limited screens)
    x_axis: str = "date"      # "date" or "build"
    description: str = ""      # subtitle under the title
    footnote: str = ""
    target: Optional[float] = None
    band: bool = False        # shade a +/-15% normal range behind the line


def load_config(config_file: Path) -> List[PerformanceTest]:
    with open(config_file, 'rb') as f:
        config = tomllib.load(f)
    tests = []
    for tc in config.get('tests', []):
        tests.append(PerformanceTest(
            test_id=tc['test_id'], display_name=tc['display_name'],
            graph_filename=tc['graph_filename'], pattern=tc['pattern'],
            ylabel=tc.get('ylabel', 'Load Time (ms)'), color=tc.get('color'),
            unit=tc.get('unit', 'ms'), metric=tc.get('metric', 'avg'),
            x_axis=tc.get('x_axis', 'date'), description=tc.get('description', ''),
            footnote=tc.get('footnote', ''), target=tc.get('target'),
            band=tc.get('band', False)))
    return tests


def _build_labels():
    """Optional commit_hash -> display label map (data-trend/build_labels.csv),
    so the mobile x-axis shows real build names. '|' in a label becomes a line
    break. Falls back to date+hash when a build is not listed."""
    import csv as _csv
    p = Path(__file__).resolve().parent.parent / 'data' / 'android' / 'build_labels.csv'
    out = {}
    if p.exists():
        for row in _csv.DictReader(open(p, encoding='utf-8')):
            out[row['commit_hash']] = row['label'].replace('|', '\n')
    return out


def _excluded_builds():
    """Build hashes hidden from the published charts (an optional `exclude` column
    in build_labels.csv). The raw rows stay in performance_metrics.csv — this only
    keeps a build off the trend, e.g. a pre-final build that muddies the release
    story. Missing column => nothing excluded (back-compatible)."""
    import csv as _csv
    p = Path(__file__).resolve().parent.parent / 'data' / 'android' / 'build_labels.csv'
    out = set()
    if p.exists():
        for row in _csv.DictReader(open(p, encoding='utf-8')):
            if str(row.get('exclude') or '').strip().lower() in ('1', 'true', 'yes', 'y'):
                out.add(row['commit_hash'])
    return out


def _run_environments():
    """commit_hash -> device OS fingerprint (data/android/run_environment.csv).
    Used to draw a divider where the device software changed, so a baseline step
    that is really an OS/One UI update isn't misread as an app change. Builds with
    no recorded environment are treated as one earlier 'legacy' regime."""
    import csv as _csv
    p = Path(__file__).resolve().parent.parent / 'data' / 'android' / 'run_environment.csv'
    out = {}
    if p.exists():
        for row in _csv.DictReader(open(p, encoding='utf-8')):
            out[row['commit_hash']] = row.get('fingerprint') or row.get('oneui') or 'recorded'
    return out


def _android16_builds():
    """Build hashes measured on the gate OS regime — Android 16 (One UI 8). Volo asked to
    'stick with Android 16 One UI 8', so the trend charts show only this regime: it drops the
    pre-update legacy points and the OS-divider clutter, and keeps one comparable timeline. A
    build with no recorded environment is treated as pre-regime and left off."""
    import csv as _csv
    p = Path(__file__).resolve().parent.parent / 'data' / 'android' / 'run_environment.csv'
    out = set()
    if p.exists():
        for row in _csv.DictReader(open(p, encoding='utf-8')):
            if str(row.get('android', '')).strip() == '16':
                out.add(row['commit_hash'])
    return out


def _os_boundary_indices(order):
    """Indices i (in the date-ordered build list) where the device OS regime changes
    from build i-1 to build i — i.e. where to draw a 'device OS update' divider."""
    env = _run_environments()
    regimes = [env.get(h, 'legacy') for h in order['commit_hash']]
    return [i for i in range(1, len(regimes)) if regimes[i] != regimes[i - 1]]


def _fmt(v, unit):
    return f"{v:.2f}s" if unit == 's' else f"{v:.0f} ms"


def plot_performance_mobile(performance, test, output_dir):
    """Mobile response chart: seconds axis, build-name x-axis. Android 16 / One UI 8 only.
    The two release baselines (2.37.1, 2.38.0) are pinned as fixed LEFT columns so every chart
    'starts' with them, and a faint dashed line marks the last-release level. For a nav-tab
    surface the FIRST-open series is overlaid as a second (dashed) line, each first-open point
    annotated with how much slower it is than its repeat-open counterpart, e.g. 1.40s (+50%).
    Separate from plot_performance so desktop charts are unaffected."""
    name_match = (performance['test_name'] == test.pattern) | \
        performance['test_name'].str.startswith(test.pattern + '[', na=False)
    data = performance[name_match].copy()
    if 'metric' in data.columns:
        data = data[data['metric'] == 'response_time']
    excluded = _excluded_builds()
    if excluded:
        data = data[~data['commit_hash'].isin(excluded)]
    a16 = _android16_builds()          # Volo: Android 16 / One UI 8 only — drop legacy-OS points
    if a16:
        data = data[data['commit_hash'].isin(a16)]
    if data.empty:
        print(f"Warning: No data for {test.pattern}")
        return
    value_col = "min_time" if test.metric == "min" else "median_time"
    scale = 1.0 if test.unit == 's' else 1000.0
    labels = _build_labels()

    # Pin the two release baselines as fixed LEFT columns, then up to MAX_RECENT recent builds by
    # date (Volo: 'two baselines should start every chart' + 'keep up to ~30 data points').
    BASELINES = ["760417N", "5f66deN"]   # 2.37.1 / 2.38.0 re-measured on Android 16 (One UI 8)
    GA_BUILD = "5f66deN"                  # last release -> the dashed reference level
    MAX_RECENT = 28
    allb = data.drop_duplicates('commit_hash').sort_values('date')
    present = list(allb['commit_hash'])
    base_order = [h for h in BASELINES if h in present]
    recent = [h for h in present if h not in BASELINES][-MAX_RECENT:]
    order_hashes = base_order + recent
    data = data[data['commit_hash'].isin(order_hashes)]
    build_index = {h: i for i, h in enumerate(order_hashes)}
    n_builds, n_base = len(order_hashes), len(base_order)
    dmap = dict(zip(allb['commit_hash'], allb['date']))

    fig, ax = plt.subplots(figsize=(min(18.0, max(8.2, n_builds * 0.8)), 5.4))

    # First-open companion (nav tabs have a *_first_open series) -> overlay as a 2nd line.
    fo = performance[performance['test_name'] == test.pattern.replace('_response_time', '_first_open')].copy()
    if 'metric' in fo.columns:
        fo = fo[fo['metric'] == 'response_time']
    fo = fo[fo['commit_hash'].isin(order_hashes)].sort_values('date')
    # Wallet is the post-login landing screen, so its 'first open' is already warm — an
    # artifact (first < repeat), not a cold open; omit the overlay like the first-vs-returning chart.
    FO_SKIP = {"test_android_wallet_response_time"}
    has_fo = test.pattern.endswith('_response_time') and len(fo) > 0 and test.pattern not in FO_SKIP

    names = list(data['test_name'].unique())
    any_low = False
    warm_by_build = {}
    for idx, test_name in enumerate(names):
        vd = data[data['test_name'] == test_name].copy().sort_values('date')
        color = PERFORMANCE_COLORS[idx % len(PERFORMANCE_COLORS)]
        y = (vd[value_col] * scale).tolist()
        x = [build_index[h] for h in vd['commit_hash']]
        warm_by_build = {h: v * scale for h, v in zip(vd['commit_hash'], vd[value_col])}
        lbl = (test_name.split('[')[1].split(']')[0] if '[' in test_name
               else ('repeat open' if has_fo else None))
        ax.plot(x, y, marker='o', linewidth=2, markersize=7, color=color, zorder=3, label=lbl)
        if test.band and y:
            mid = y[-1]
            ax.axhspan(mid * 0.85, mid * 1.15, color=color, alpha=0.10, lw=0, zorder=0)
        rc = vd['run_count'].tolist() if 'run_count' in vd.columns else []
        low = [(xi, yi) for xi, yi, c in zip(x, y, rc) if str(c).isdigit() and int(c) < 3]
        if low:
            any_low = True
            lx, ly = zip(*low)
            ax.scatter(lx, ly, s=150, facecolors='none', edgecolors='#c0392b', linewidths=1.8, zorder=4)
        if len(names) == 1:
            dy = -15 if has_fo else 10        # warm below the point when first-open sits above it
            for xi, yi in zip(x, y):
                ax.annotate(_fmt(yi, test.unit), (xi, yi), textcoords='offset points',
                            xytext=(0, dy), ha='center', fontsize=8.5, fontweight='bold')

    if has_fo:
        fyl = (fo[value_col] * scale).tolist()
        fxl = [build_index[h] for h in fo['commit_hash']]
        ax.plot(fxl, fyl, marker='s', linewidth=1.6, markersize=6, linestyle='--',
                color='#e67e22', zorder=3, label='first open')
        for h, xi, yi in zip(fo['commit_hash'], fxl, fyl):
            w = warm_by_build.get(h)
            # only show the % vs repeat when the repeat baseline is above the ~0.2s floor —
            # against a sub-floor (near-instant) repeat the ratio explodes into a meaningless
            # number (e.g. 2.2s vs 0.08s = +2600%).
            if w and w > 0.20 * scale:
                d = round((yi / w - 1) * 100)
                pct = f" ({'+' if d > 0 else ''}{d}%)"
            else:
                pct = ""
            ax.annotate(f"{_fmt(yi, test.unit)}{pct}", (xi, yi), textcoords='offset points',
                        xytext=(0, 9), ha='center', fontsize=8, color='#d35400', fontweight='bold')
        any_low = True   # first-open is single-shot

    def _short(h, is_base):
        raw = labels.get(h)
        if is_base:
            nm = raw.split('\n')[1].split('·')[0].strip() if raw and '\n' in raw else (raw or h[:6])
            return f"{nm}\nbaseline"
        if not raw:
            d = dmap.get(h)
            return f"{d:%Y-%m-%d}\n{h[:6]}" if d is not None else h[:6]
        parts = raw.split('\n')
        return f"{parts[0]}\n{parts[1].split(' · ')[0] if len(parts) > 1 else h[:6]}"
    xt = [_short(h, i < n_base) for i, h in enumerate(order_hashes)]
    ax.set_xticks(range(len(xt)))
    ax.set_xticklabels(xt, fontsize=8, rotation=35, ha='right', rotation_mode='anchor')

    if 0 < n_base < n_builds:            # separator between pinned baselines and the live trend
        ax.axvline(n_base - 0.5, ls='-', lw=1, color='#bbbbbb', alpha=0.9, zorder=1)
        ax.text(n_base - 0.5, 1.005, 'baselines | trend', transform=ax.get_xaxis_transform(),
                ha='center', va='bottom', fontsize=7, color='#999999')

    gv = data[(data['commit_hash'] == GA_BUILD) & (data['test_name'] == test.pattern)]
    if len(gv):                          # dashed last-release reference level
        lvl = float(gv[value_col].iloc[0]) * scale
        ax.axhline(lvl, ls='--', lw=1, color='#888888', alpha=0.6, zorder=1)
        ax.text(len(xt) - 1, lvl, ' 2.38.0', va='bottom', ha='right', fontsize=7.5, color='#888888')

    ax.set_ylabel(test.ylabel, fontsize=11)
    ymax = max((data[value_col] * scale).max(), test.target or 0)
    if has_fo:
        ymax = max(ymax, (fo[value_col] * scale).max())
    ax.set_ylim(0, ymax * 1.35)
    if test.target:
        ax.axhline(test.target, ls='--', lw=1, color='#c0392b', alpha=0.6)
        ax.text(len(xt) - 1, test.target, f' {_fmt(test.target, test.unit)} target',
                va='bottom', ha='right', fontsize=8, color='#c0392b')
    ax.grid(axis='y', alpha=0.3)
    ax.set_axisbelow(True)
    fig.suptitle(test.display_name, fontweight='bold', fontsize=13, y=0.98)
    if test.description:
        ax.set_title(test.description, fontsize=9.5, color='dimgray', pad=10)
    if has_fo or len(names) > 1:
        ax.legend(loc='best', fontsize=8)
    if any_low:
        ax.text(0.99, 0.97, 'ringed = <3 samples', transform=ax.transAxes,
                ha='right', va='top', fontsize=7.5, color='#c0392b')
    if test.band:
        ax.text(0.01, 0.03, 'shaded = ±15% of latest (normal range)', transform=ax.transAxes,
                ha='left', va='bottom', fontsize=7.5, color='gray')
    if test.footnote:
        fig.text(0.5, 0.015, test.footnote, ha='center', fontsize=8, color='gray')
    fig.subplots_adjust(top=0.86, bottom=0.30)
    fig.savefig(output_dir / test.graph_filename, dpi=160)
    plt.close()
    print(f"Generated {test.graph_filename} (mobile)")
