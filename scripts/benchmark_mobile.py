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
    """Mobile response chart: seconds axis, build-name x-axis, explanatory
    subtitle, methodology footnote. Separate from plot_performance so desktop
    charts are unaffected."""
    # Exact name (or a parametrized `pattern[param]`), not substring: otherwise a
    # future longer surface name (e.g. ..._send_max_response_time) would silently
    # bleed into the ..._send_response_time chart. And only response_time rows, so
    # a memory/cpu metric sharing the store never lands on a seconds axis.
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

    MAX_BUILDS = 30  # Volo: keep up to ~30 data points (newer replace older)
    builds = data.drop_duplicates('commit_hash').sort_values('date')
    if len(builds) > MAX_BUILDS:
        data = data[data['commit_hash'].isin(set(builds['commit_hash'].tail(MAX_BUILDS)))]
    n_builds = data['commit_hash'].nunique()
    fig, ax = plt.subplots(figsize=(min(18.0, max(8.2, n_builds * 0.7)), 5.2))
    # Shared build order: place every line's points at the GLOBAL build index (not a
    # per-line 0..n), so a line missing some builds still lands under the right x-axis
    # label instead of shifting left. (All current charts are single-line; this guards
    # a future multi-line/parametrized surface with uneven per-build coverage.)
    order = data.drop_duplicates('commit_hash').sort_values('date')
    build_index = {h: i for i, h in enumerate(order['commit_hash'])}
    names = list(data['test_name'].unique())
    any_low = False
    for idx, test_name in enumerate(names):
        vd = data[data['test_name'] == test_name].copy().sort_values('date')
        color = PERFORMANCE_COLORS[idx % len(PERFORMANCE_COLORS)]
        y = (vd[value_col] * scale).tolist()
        x = [build_index[h] for h in vd['commit_hash']]
        lbl = test_name.split('[')[1].split(']')[0] if '[' in test_name else None
        ax.plot(x, y, marker='o', linewidth=2, markersize=7, color=color, zorder=3, label=lbl)
        # Normal-range band: ±15% around the latest build's value (the current
        # regime). A point outside it is a step-change, not nightly noise. Anchored
        # on the latest, not the series, so a genuine regression (e.g. Market's
        # 2x) sits clearly outside the band rather than recentring it.
        if test.band and y:
            mid = y[-1]
            ax.axhspan(mid * 0.85, mid * 1.15, color=color, alpha=0.10, lw=0, zorder=0)
        # Ring points summarised from fewer than 3 samples (cold/first-opens are
        # single-shot) so a reader doesn't read a 1-sample point as a 6-run median.
        rc = vd['run_count'].tolist() if 'run_count' in vd.columns else []
        low = [(xi, yi) for xi, yi, c in zip(x, y, rc) if str(c).isdigit() and int(c) < 3]
        if low:
            any_low = True
            lx, ly = zip(*low)
            ax.scatter(lx, ly, s=150, facecolors='none', edgecolors='#c0392b',
                       linewidths=1.8, zorder=4)
        if len(names) == 1:
            for xi, yi in zip(x, y):
                ax.annotate(_fmt(yi, test.unit), (xi, yi), textcoords='offset points',
                            xytext=(0, 10), ha='center', fontsize=9, fontweight='bold')

    # Concise, angled labels so build names stay legible (Volo: build data wasn't readable).
    # Drop the commit hash from the axis (noise to a reader; still in the data), keep date +
    # build name, and rotate so neighbours never collide even at 30 points.
    def _short(h, d):
        raw = labels.get(h)
        if not raw:
            return f"{d:%Y-%m-%d}\n{h[:6]}"
        parts = raw.split('\n')
        date = parts[0] if parts else f"{d:%Y-%m-%d}"
        name = parts[1].split(' · ')[0] if len(parts) > 1 else h[:6]
        return f"{date}\n{name}"
    xt = [_short(h, d) for h, d in zip(order['commit_hash'], order['date'])]
    ax.set_xticks(range(len(xt)))
    ax.set_xticklabels(xt, fontsize=8, rotation=35, ha='right', rotation_mode='anchor')
    # Device OS-change divider: a step across this line can be the device software,
    # not the app, so points on opposite sides aren't directly comparable.
    for bi in _os_boundary_indices(order):
        ax.axvline(bi - 0.5, ls=':', lw=1.3, color='#8e44ad', alpha=0.8, zorder=1)
        ax.text(bi - 0.5, 1.005, 'device OS update', transform=ax.get_xaxis_transform(),
                ha='center', va='bottom', fontsize=7, color='#8e44ad', rotation=0)
    ax.set_ylabel(test.ylabel, fontsize=11)
    ymax = max((data[value_col] * scale).max(), test.target or 0)
    ax.set_ylim(0, ymax * 1.3)
    if test.target:
        ax.axhline(test.target, ls='--', lw=1, color='#c0392b', alpha=0.6)
        ax.text(len(xt) - 1, test.target, f' {_fmt(test.target, test.unit)} target',
                va='bottom', ha='right', fontsize=8, color='#c0392b')
    ax.grid(axis='y', alpha=0.3)
    ax.set_axisbelow(True)
    fig.suptitle(test.display_name, fontweight='bold', fontsize=13, y=0.98)
    if test.description:
        ax.set_title(test.description, fontsize=9.5, color='dimgray', pad=10)
    if len(names) > 1:
        ax.legend(loc='best', fontsize=8)
    if any_low:
        ax.text(0.99, 0.97, 'ringed = <3 samples', transform=ax.transAxes,
                ha='right', va='top', fontsize=7.5, color='#c0392b')
    if test.band:
        ax.text(0.01, 0.97, 'shaded = ±15% of latest (normal range)', transform=ax.transAxes,
                ha='left', va='top', fontsize=7.5, color='gray')
    if test.footnote:
        fig.text(0.5, 0.015, test.footnote, ha='center', fontsize=8, color='gray')
    fig.subplots_adjust(top=0.86, bottom=0.26)
    fig.savefig(output_dir / test.graph_filename, dpi=160)
    plt.close()
    print(f"Generated {test.graph_filename} (mobile)")
