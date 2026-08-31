#!/usr/bin/env python3
"""Publish helper for the Android response-time charts.

  append <test_run_log> <hash> <date> <label> <device> <data_dir>
      Parse the framework log's canonical perf lines

        ANDROID_NAV name=<test_name> metric=<m> unit=<u> median=<x> \
                    n=<k> attempted=<a> samples=[...]

      into trend rows and append them to <data_dir>/performance_metrics.csv
      (re-runs of the same build+device+metric replace, not duplicate), and
      record the build's display name in <data_dir>/build_labels.csv. Prints the
      surfaces it found so the caller can gate on completeness.

  charts <data_dir> <docs_dir>
      Regenerate ONLY the android charts (reuses the repo's plot_performance_mobile)
      from <data_dir> into <docs_dir>. Does not touch the shared summary charts.

The emitter (utils/response_timer.py:emit_perf) owns the line format and the full
test_name, so adding a surface never needs a change here. `device` and `metric`
are first-class columns so multiple phones / metric types (response_time, rss_mb,
cpu_pct, ...) can share one store without colliding.
"""
import csv
import os
import re
import statistics
import subprocess
import sys
from pathlib import Path

import pandas as pd

# Overridable so the chart step can be dry-run against a checkout anywhere — the charts are
# published to a shared dashboard, and being un-runnable off the Pi means nobody eyeballs
# them before they go out.
REPO = Path(os.environ.get("BENCHMARKS_REPO", "/home/wispa/status-app-benchmarks"))
CHART_ARCHIVE = Path(os.environ.get("PERF_CHART_ARCHIVE", Path.home() / "perf-chart-archive"))
sys.path.insert(0, str(REPO / "scripts"))
import benchmark_mobile as b  # noqa: E402  (matplotlib charting; never `benchmark`, which pulls in plotly)

# Canonical line emitted by emit_perf. test_name is read verbatim — no suffix
# inference — so the emitter is the single owner of surface naming.
PERF_RE = re.compile(
    r"ANDROID_NAV name=(\S+) metric=(\S+) unit=(\S+) median=([0-9.]+) "
    r"n=(\d+) attempted=(\d+) samples=\[([0-9.,\s]*)\]")
# grep pre-filter (binary-safe) for the file-tree case; PERF_RE does the real parse.
GREP_RE = r"ANDROID_NAV name=[^ ]+ metric=[^ ]+ unit=[^ ]+ median=[0-9.]+ n=[0-9]+ attempted=[0-9]+ samples=\[[^]]*\]"
HEADER = ["commit_hash", "date", "device", "test_name", "status", "metric", "unit",
          "min_time", "max_time", "avg_time", "median_time", "run_count", "attempted", "all_runs"]


def _row(hash_, date, device, name, metric, unit, samples, attempted):
    return {
        "commit_hash": hash_, "date": date, "device": device,
        "test_name": name, "status": "passed", "metric": metric, "unit": unit,
        "min_time": round(min(samples), 3), "max_time": round(max(samples), 3),
        "avg_time": round(sum(samples) / len(samples), 3),
        "median_time": round(statistics.median(samples), 3),
        "run_count": len(samples), "attempted": attempted,
        "all_runs": ",".join(str(x) for x in samples),
    }


def append(log, hash_, date, label, device, data_dir):
    data_dir = Path(data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    csv_path = data_dir / "performance_metrics.csv"
    labels_path = data_dir / "build_labels.csv"

    src = Path(log)
    if src.is_file():
        text = src.read_text(errors="ignore")
    else:
        text = subprocess.run(
            ["grep", "-rhoaE", GREP_RE, str(src)],
            capture_output=True, text=True).stdout

    seen = {}  # test_name -> (metric, unit, samples, attempted); line is duplicated across logs
    for line in text.splitlines():
        m = PERF_RE.search(line)
        if not m:
            continue
        name, metric, unit = m.group(1), m.group(2), m.group(3)
        attempted = int(m.group(6))
        samples = [float(x) for x in m.group(7).split(",") if x.strip()]
        if not samples:
            continue
        seen.setdefault((name, metric), (unit, samples, attempted))
    rows = [_row(hash_, date, device, name, metric, unit, samples, attempted)
            for (name, metric), (unit, samples, attempted) in seen.items()]
    if not rows:
        print(f"no ANDROID_NAV perf lines under {log}")
        return 0

    existing = list(csv.DictReader(open(csv_path))) if csv_path.exists() else []
    new_keys = {(r["test_name"], r["metric"]) for r in rows}
    keep = [r for r in existing
            if not (r.get("commit_hash") == hash_ and r.get("device") == device
                    and (r.get("test_name"), r.get("metric", "response_time")) in new_keys)]
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HEADER)
        w.writeheader()
        for r in keep:
            w.writerow(_legacy_fill(r))
        for r in rows:
            w.writerow(r)

    # Preserve any extra columns (notably `exclude`, which keeps a pre-final build
    # off the published charts) — a plain commit_hash,label rewrite would wipe them
    # on the next nightly and the hidden build would reappear.
    labels = {}
    if labels_path.exists():
        for r in csv.DictReader(open(labels_path)):
            labels[r["commit_hash"]] = {"label": r.get("label", ""),
                                        "exclude": r.get("exclude", "")}
    labels[hash_] = {"label": label, "exclude": labels.get(hash_, {}).get("exclude", "")}
    with open(labels_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["commit_hash", "label", "exclude"])
        for h, v in labels.items():
            w.writerow([h, v["label"], v["exclude"]])

    names = sorted(r["test_name"] for r in rows)
    print(f"appended {len(rows)} surfaces for {hash_} on {device} -> {csv_path}")
    print("surfaces: " + ",".join(names))
    return len(rows)


def _legacy_fill(r):
    """Map an existing CSV row onto the current HEADER, filling columns added since
    it was written. A row with a malformed all_runs must not abort the whole rewrite
    (it would brick every future append), so median back-compute is best-effort."""
    r.setdefault("device", "")
    r.setdefault("metric", "response_time")
    r.setdefault("unit", "s")
    r.setdefault("attempted", r.get("run_count", ""))
    if not r.get("median_time") and r.get("all_runs"):
        try:
            runs = [float(x) for x in r["all_runs"].split(",") if x.strip()]
            r["median_time"] = round(statistics.median(runs), 3) if runs else r.get("avg_time", "")
        except ValueError:
            r["median_time"] = r.get("avg_time", "")
    return {k: r.get(k, "") for k in HEADER}


def _plot_first_vs_returning(perf, docs_dir):
    """Grouped-bar snapshot: first-open (cold) vs returning (warm) per nav tab, on the
    latest build that carries first-open data. The cold-vs-warm view — both sides are
    measured to fully-rendered (the same criterion), so the gap is real. First-open is
    single-sample, so treat it as indicative."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    # Wallet is omitted: it is the post-login landing screen, so by the time the
    # first-open test navigates back to it the screen is already built — its "first
    # open" is really a warm re-open and would plot an impossible first < returning bar.
    tabs = ["messages", "settings", "market", "communities"]
    excluded = b._excluded_builds()
    if excluded:
        perf = perf[~perf["commit_hash"].isin(excluded)]
    if "metric" in perf.columns:  # seconds-axis response_time rows only
        perf = perf[perf["metric"] == "response_time"]
    if "device" in perf.columns:  # gate phone only — shared hashes exist across phones
        perf = perf[perf["device"] == b.GATE_DEVICE]
    fo = perf[perf["test_name"].str.endswith("_first_open")]
    if fo.empty:
        return
    build = fo.sort_values("date")["commit_hash"].iloc[-1]
    sub = perf[perf["commit_hash"] == build]

    def med(name):
        r = sub[sub["test_name"] == name]
        return float(r["median_time"].iloc[0]) if len(r) else 0.0
    first = [med(f"test_android_{t}_first_open") for t in tabs]
    warm = [med(f"test_android_{t}_response_time") for t in tabs]
    x = np.arange(len(tabs))
    w = 0.38
    fig, ax = plt.subplots(figsize=(8.6, 5.0))
    bars = [(ax.bar(x - w / 2, first, w, label="first open (cold)", color="#e67e22"), first),
            (ax.bar(x + w / 2, warm, w, label="returning (warm)", color="#2980b9"), warm)]
    for group, vals in bars:
        for rect, v in zip(group, vals):
            if v:
                ax.annotate(f"{v:.2f}", (rect.get_x() + rect.get_width() / 2, v),
                            textcoords="offset points", xytext=(0, 3), ha="center", fontsize=8)
    ax.set_xticks(x)
    ax.set_xticklabels([t.capitalize() for t in tabs])
    ax.set_ylabel("seconds")
    ax.grid(axis="y", alpha=0.3)
    ax.set_axisbelow(True)
    ax.legend(loc="upper right", fontsize=9)
    fig.suptitle("First open vs returning — Android nav tabs", fontweight="bold", fontsize=13)
    ax.set_title(f"build {build} · first open pays full page construction; returning is the cached re-open",
                 fontsize=9.5, color="dimgray", pad=10)
    fig.text(0.5, 0.01, "Both timed to fully-rendered (comparable). First-open is single-sample. "
             "Wallet omitted (post-login landing — its first open is already warm). ~0.06-0.1s floor.",
             ha="center", fontsize=8, color="gray")
    fig.subplots_adjust(top=0.88, bottom=0.13)
    fig.savefig(docs_dir / "android_first_vs_returning.png", dpi=160)
    plt.close()
    print("Generated android_first_vs_returning.png (mobile)")


def _plot_scorecard(perf, docs_dir):
    """At-a-glance 'now' card — per surface: the change vs the last shipped release (parity /
    regression, in seconds) and an absolute SPEED band (fast/ok/slow). PER-SURFACE latest, so it
    never goes artificially stale though nightlies re-measure only a few surfaces. Variable /
    single-sample / stale surfaces are greyed and never assert a verdict. Drift over time lives in
    the per-surface trend charts; the verdict-led ship card is _plot_release_gate (per RC)."""
    import matplotlib.pyplot as plt

    GA_BASE, GA_NAME, GA_N = "3ef171", "2.38.2", "3ef171N"   # last shipped release; roll per release
    GATE_DEVICE = b.GATE_DEVICE
    FLOOR_S = 0.20
    FAST, SLOW, NEAR = 0.50, 1.00, 0.90        # nav UX bands; NEAR*SLOW = within 10% of the slow line
    NOISE = {"test_android_wallet_response_time": 0.05,   # tighter where the run-to-run noise is measured
             "test_android_settings_response_time": 0.06}
    NOISE_DEFAULT = 0.08                        # within this fraction of the baseline reads as parity / noise
    STALE_DAYS = 14
    NETWORKED = {"test_android_communities_response_time"}
    REDEFINED = {"test_android_settings_response_time": "redefined 2026-08-30 (profile menu) — not comparable"}
    VARIABLE = {"test_android_market_response_time"}    # content-gated: render time varies build-to-build; greyed, excluded from drift
    GREEN, RED, AMBER, GREY, BLUE, INK = "#27ae60", "#c0392b", "#e67e22", "#7f8c8d", "#2c7fb8", "#444444"
    HEADLINE = [
        ("Wallet", "test_android_wallet_response_time"),
        ("Wallet ▸ Send", "test_android_wallet_send_response_time"),
        ("Wallet ▸ Swap", "test_android_wallet_swap_response_time"),
        ("Wallet ▸ Receive", "test_android_wallet_receive_response_time"),
        ("Wallet ▸ Buy", "test_android_wallet_buy_response_time"),
        ("Messenger", "test_android_messages_response_time"),
        ("Market", "test_android_market_response_time"),
        ("Communities", "test_android_communities_response_time"),
        ("Settings", "test_android_settings_response_time"),
        ("Activity Centre", "test_android_activity_center_response_time"),
        ("Home", "test_android_home_response_time"),
    ]

    excluded = b._excluded_builds()
    p = perf[~perf["commit_hash"].isin(excluded)].copy() if excluded else perf.copy()
    if "metric" in p.columns:
        p = p[p["metric"] == "response_time"]
    if "device" in p.columns:
        p = p[p["device"] == GATE_DEVICE]
    env = b._run_environments()
    os_of = lambda h: env.get(h, "legacy")
    real = p[~p["commit_hash"].astype(str).str.endswith("N")]
    newest_date = real["date"].max() if len(real) else None
    cur_os = os_of(real.sort_values("date")["commit_hash"].iloc[-1]) if len(real) else "legacy"
    ga_build = next((h for h in (GA_BASE, GA_N)
                     if os_of(h) == cur_os and len(p[p["commit_hash"] == h])), None)

    def latest(name):   # this surface's most recent point on the current OS (not a baseline / N re-measure)
        c = p[(p["test_name"] == name) & (~p["commit_hash"].isin([GA_BASE, GA_N]))
              & (~p["commit_hash"].astype(str).str.endswith("N"))].sort_values("date", kind="stable")
        cur = c[c["commit_hash"].map(os_of) == cur_os]
        cc = cur if len(cur) else c
        return cc.iloc[-1] if len(cc) else None

    def base(name):
        if ga_build is None:
            return None
        r = p[(p["commit_hash"] == ga_build) & (p["test_name"] == name)]
        return float(r["median_time"].iloc[0]) if len(r) else None

    def speed_band(val):
        if val < FAST:
            return "fast", GREEN
        if val <= SLOW:
            return "ok", (AMBER if val > NEAR * SLOW else BLUE)
        return "slow", RED

    rows = []
    for disp, name in HEADLINE:
        r = latest(name)
        if r is None:
            rows.append((disp, "—", ("no data", GREY), ("", GREY), ""))
            continue
        val = float(r["median_time"])
        meas = "%s · %s" % (str(r["date"])[5:10], r["commit_hash"])
        try:
            rc = int(float(r["run_count"]))
        except Exception:
            rc = 0
        bv = base(name)
        stale = newest_date is not None and (newest_date - r["date"]).days > STALE_DAYS
        noise = NOISE.get(name, NOISE_DEFAULT)
        band, bcol = speed_band(val)
        nums = ("%.2fs → %.2fs" % (bv, val)) if bv else ("— → %.2fs" % val)

        caveat = ("single sample" if rc < 2 else "variable" if name in VARIABLE
                  else "networked" if name in NETWORKED else "redefined" if name in REDEFINED
                  else "stale" if stale else None)

        if caveat:                                          # greyed; raw numbers shown but no verdict asserted
            verdict = (caveat, AMBER if caveat == "networked" else GREY)
            speed_cell = (band, GREY)
        else:
            speed_cell = (band, bcol)
            if bv is None:
                verdict = ("no baseline", GREY)
            elif val < FLOOR_S and bv < FLOOR_S:            # both near-instant: sub-floor delta is noise
                verdict = ("✓ parity", GREEN)
            elif val < FLOOR_S or bv < FLOOR_S:
                # Only ONE side at the floor. The delta is then mostly the floor reading, not a
                # real change (2.38.2 read Buy at 0.11s and Home at 0.10s, so a normal 0.6s today
                # prints as "+0.5s slower"). State the pair, assert nothing.
                verdict = ("floor-limited baseline" if bv < FLOOR_S else "floor-limited reading", GREY)
            else:
                d = val - bv
                if abs(d) / bv <= noise:
                    verdict = ("✓ parity", GREEN)
                elif d > 0:
                    verdict = ("▲ +%.2fs slower" % d, RED)
                else:
                    verdict = ("▼ −%.2fs faster" % (-d), GREEN)
        rows.append((disp, nums, verdict, speed_cell, meas))

    n = len(rows)
    ROW_H = 0.34
    fig_h = 2.0 + n * ROW_H + 1.0
    fig, ax = plt.subplots(figsize=(8.2, fig_h))
    ax.set_position([0, 0, 1, 1])
    ax.axis("off")

    def Y(t):
        return 1 - t / fig_h

    ax.text(0.5, Y(0.45), "Android performance — scorecard", ha="center", va="center",
            fontsize=15, fontweight="bold", transform=ax.transAxes)
    ax.text(0.5, Y(0.85),
            "each surface's latest vs the last shipped release (%s)  ·  %s  ·  lower is better" % (GA_NAME, GATE_DEVICE),
            ha="center", va="center", fontsize=8.6, color="dimgray", transform=ax.transAxes)
    cx = dict(surface=0.030, nums=0.250, verdict=0.450, speed=0.670, meas=0.965)
    hy = Y(1.55)
    ax.text(cx["surface"], hy, "surface", fontsize=9.3, fontweight="bold", transform=ax.transAxes)
    ax.text(cx["nums"], hy, "last release → latest", fontsize=9.3, fontweight="bold", transform=ax.transAxes)
    ax.text(cx["speed"], hy, "speed", fontsize=9.3, fontweight="bold", transform=ax.transAxes)
    ax.text(cx["meas"], hy, "measured", fontsize=9.3, fontweight="bold", ha="right", transform=ax.transAxes)
    ax.plot([cx["surface"], cx["meas"]], [Y(1.72)] * 2, color="#cccccc", lw=0.8, transform=ax.transAxes)

    for i, (disp, nums, verdict, speed_cell, meas) in enumerate(rows):
        yy = Y(2.0 + i * ROW_H + ROW_H * 0.5)
        indent = cx["surface"] + (0.035 if disp.startswith("Wallet ▸") else 0)
        ax.text(indent, yy, disp, fontsize=9.1, va="center", transform=ax.transAxes, color="#1a1a1a")
        ax.text(cx["nums"], yy, nums, fontsize=8.4, va="center", transform=ax.transAxes, color=INK)
        vt, vcol = verdict
        ax.text(cx["verdict"], yy, vt, fontsize=8.4, va="center", transform=ax.transAxes, color=vcol, fontweight="bold")
        st, scol = speed_cell
        if st:
            ax.text(cx["speed"], yy, st, fontsize=8.2, va="center", ha="left", transform=ax.transAxes,
                    color="white", fontweight="bold", bbox=dict(boxstyle="round,pad=0.3", fc=scol, ec="none"))
        ax.text(cx["meas"], yy, meas, fontsize=7.8, va="center", ha="right", transform=ax.transAxes, color="#999999")

    ax.text(0.020, Y(2.0 + n * ROW_H + 0.52),
            "speed:  fast < 0.5s   ·   ok 0.5–1.0s (amber = within 10% of the slow line)   ·   slow > 1.0s",
            ha="left", va="top", fontsize=7.5, color="gray", transform=ax.transAxes)
    ax.text(0.020, Y(2.0 + n * ROW_H + 0.78),
            "vs last release: parity = within run-to-run noise; otherwise the change in seconds.  Greyed = variable / single-sample / stale — never asserted as a pass.  Variable = content-gated; its median swings build-to-build, so it's excluded from drift.",
            ha="left", va="top", fontsize=7.5, color="gray", transform=ax.transAxes)
    ax.text(0.020, Y(2.0 + n * ROW_H + 1.04),
            "Fresh account · one mid-range phone (Samsung A36) · median of the build's runs.  Drift over time is in the per-surface trend charts.",
            ha="left", va="top", fontsize=7.5, color="gray", transform=ax.transAxes)
    fig.savefig(docs_dir / "android_scorecard.png", dpi=160, bbox_inches="tight")
    plt.close()
    print("Generated android_scorecard.png (mobile)")


LOWEND_SURFACES = [
    ("Wallet", "test_android_wallet_response_time"),
    ("Wallet ▸ Assets", "test_android_wallet_assets_response_time"),
    ("Wallet ▸ Collectibles", "test_android_wallet_collectibles_response_time"),
    ("Wallet ▸ History", "test_android_wallet_history_response_time"),
    ("Wallet ▸ Send", "test_android_wallet_send_response_time"),
    ("Wallet ▸ Swap", "test_android_wallet_swap_response_time"),
    ("Wallet ▸ Buy", "test_android_wallet_buy_response_time"),
    ("Messenger", "test_android_messages_response_time"),
    ("Market", "test_android_market_response_time"),
    ("Communities", "test_android_communities_response_time"),
    ("Settings", "test_android_settings_response_time"),
]


def _lowend_frames(perf):
    """(low-end rows, gate rows) for the response-time surfaces, published builds only."""
    excluded = b._excluded_builds()
    p = perf[~perf["commit_hash"].isin(excluded)].copy() if excluded else perf.copy()
    if "metric" in p.columns:
        p = p[p["metric"] == "response_time"]
    return p[p["device"] == b.LOWEND_DEVICE], p[p["device"] == b.GATE_DEVICE]


def _plot_lowend_scorecard(perf, docs_dir):
    """Low-end baseline card — the budget phone (Redmi A5) beside the gate phone.

    Deliberately NOT the release gate. The gate scores ONE reference phone so a move is
    attributable to the build; this card answers a different question — how the app feels on
    the cheapest hardware we support — so the two are published separately and never mixed.
    Same honesty rules as the gate card: a surface that is unmeasured, below the measurement
    floor, single-sample or stale shows its raw number but never a comparison, and the gate
    number is only compared when BOTH phones ran the SAME build (a cross-build ratio is
    marked, because the gate phone's own surfaces move between builds too)."""
    import matplotlib.pyplot as plt

    FLOOR_S = 0.20
    FAST, SLOW, NEAR = 0.50, 1.00, 0.90     # same nav UX bands as the gate card
    STALE_DAYS = 21                          # weekly lane — a fortnight is one missed run
    VARIABLE = {"test_android_market_response_time"}       # content-gated, swings build-to-build
    GREEN, RED, AMBER, GREY, BLUE, INK = "#27ae60", "#c0392b", "#e67e22", "#7f8c8d", "#2c7fb8", "#444444"

    low, gate = _lowend_frames(perf)
    newest = low["date"].max() if len(low) else None

    def latest(frame, name):
        c = frame[frame["test_name"] == name].sort_values("date", kind="stable")
        return c.iloc[-1] if len(c) else None

    def gate_at(name, build):
        r = gate[(gate["test_name"] == name) & (gate["commit_hash"] == build)]
        return float(r["median_time"].iloc[-1]) if len(r) else None

    def speed_band(v):
        if v < FAST:
            return "fast", GREEN
        if v <= SLOW:
            return "ok", (AMBER if v > NEAR * SLOW else BLUE)
        return "slow", RED

    rows = []
    for disp, name in LOWEND_SURFACES:
        r = latest(low, name)
        if r is None:
            rows.append((disp, "—", ("not yet measured", GREY), ("", GREY), ""))
            continue
        val = float(r["median_time"])
        build = str(r["commit_hash"])
        meas = "%s · %s" % (str(r["date"])[5:10], build)
        try:
            rc = int(float(r["run_count"]))
        except Exception:
            rc = 0

        gv, mark = gate_at(name, build), ""
        if gv is None:                       # no same-build gate run -> compare, but say so
            gr = latest(gate, name)
            gv, mark = (float(gr["median_time"]), " *") if gr is not None else (None, "")

        # Either side at the floor kills the pair, not just the low-end side: a sub-frame
        # reading against a real one prints a ratio (Communities read 1.60s vs 0.10s) that
        # says the budget phone is 16x faster. Show the low-end number alone and say why.
        floored = val < FLOOR_S or (gv is not None and gv < FLOOR_S)
        stale = newest is not None and (newest - r["date"]).days > STALE_DAYS
        caveat = ("single sample" if rc < 2
                  else "floor-limited pair" if floored
                  else "variable (content-gated)" if name in VARIABLE
                  else "no comparable gate run" if gv is None
                  else "stale" if stale else None)
        nums = ("%.2fs → %.2fs" % (gv, val)) if (gv and not floored) else ("— → %.2fs" % val)
        band, bcol = speed_band(val)
        if caveat:                           # greyed: the number stands, the comparison does not
            rows.append((disp, nums, (caveat, GREY), (band, GREY), meas))
        else:
            rows.append((disp, nums, ("%.1f× the A36%s" % (val / gv, mark), INK), (band, bcol), meas))

    n = len(rows)
    ROW_H = 0.34
    fig_h = 2.0 + n * ROW_H + 1.3
    fig, ax = plt.subplots(figsize=(8.6, fig_h))
    ax.set_position([0, 0, 1, 1])
    ax.axis("off")

    def Y(t):
        return 1 - t / fig_h

    ax.text(0.5, Y(0.45), "Android performance — low-end baseline (%s)" % b.LOWEND_NAME,
            ha="center", va="center", fontsize=15, fontweight="bold", transform=ax.transAxes)
    ax.text(0.5, Y(0.85),
            "each surface's latest on the budget phone, beside the gate phone (%s) on the same build  ·  lower is better" % b.GATE_DEVICE,
            ha="center", va="center", fontsize=8.6, color="dimgray", transform=ax.transAxes)
    cx = dict(surface=0.030, nums=0.250, verdict=0.470, speed=0.680, meas=0.965)
    hy = Y(1.55)
    ax.text(cx["surface"], hy, "surface", fontsize=9.3, fontweight="bold", transform=ax.transAxes)
    ax.text(cx["nums"], hy, "A36 → %s" % b.LOWEND_NAME, fontsize=9.3, fontweight="bold", transform=ax.transAxes)
    ax.text(cx["speed"], hy, "speed", fontsize=9.3, fontweight="bold", transform=ax.transAxes)
    ax.text(cx["meas"], hy, "measured", fontsize=9.3, fontweight="bold", ha="right", transform=ax.transAxes)
    ax.plot([cx["surface"], cx["meas"]], [Y(1.72)] * 2, color="#cccccc", lw=0.8, transform=ax.transAxes)

    for i, (disp, nums, verdict, speed_cell, meas) in enumerate(rows):
        yy = Y(2.0 + i * ROW_H + ROW_H * 0.5)
        indent = cx["surface"] + (0.035 if disp.startswith("Wallet ▸") else 0)
        ax.text(indent, yy, disp, fontsize=9.1, va="center", transform=ax.transAxes, color="#1a1a1a")
        ax.text(cx["nums"], yy, nums, fontsize=8.4, va="center", transform=ax.transAxes, color=INK)
        vt, vcol = verdict
        ax.text(cx["verdict"], yy, vt, fontsize=8.4, va="center", transform=ax.transAxes,
                color=vcol, fontweight=("bold" if vcol != GREY else "normal"))
        st, scol = speed_cell
        if st:
            ax.text(cx["speed"], yy, st, fontsize=8.2, va="center", ha="left", transform=ax.transAxes,
                    color="white", fontweight="bold", bbox=dict(boxstyle="round,pad=0.3", fc=scol, ec="none"))
        ax.text(cx["meas"], yy, meas, fontsize=7.8, va="center", ha="right", transform=ax.transAxes, color="#999999")

    foot = Y(2.0 + n * ROW_H + 0.52)
    ax.text(0.020, foot,
            "speed:  fast < 0.5s   ·   ok 0.5–1.0s (amber = within 10% of the slow line)   ·   slow > 1.0s",
            ha="left", va="top", fontsize=7.5, color="gray", transform=ax.transAxes)
    ax.text(0.020, Y(2.0 + n * ROW_H + 0.78),
            "NOT a release gate. The gate scores one reference phone (Samsung A36) so a move is attributable to the build; this is a separate low-end baseline — the two are never mixed.  '*' = no same-build gate run, so the ratio spans two builds.",
            ha="left", va="top", fontsize=7.5, color="gray", transform=ax.transAxes)
    ax.text(0.020, Y(2.0 + n * ROW_H + 1.04),
            "Greyed = not yet measured / below the ~0.1s measurement floor / single sample / stale — never asserted as a comparison.",
            ha="left", va="top", fontsize=7.5, color="gray", transform=ax.transAxes)
    ax.text(0.020, Y(2.0 + n * ROW_H + 1.30),
            "Fresh account · %s (Android 15 Go edition) · refreshed weekly · median of the build's runs." % b.LOWEND_NAME,
            ha="left", va="top", fontsize=7.5, color="gray", transform=ax.transAxes)
    fig.savefig(docs_dir / "android_lowend_scorecard.png", dpi=160, bbox_inches="tight")
    plt.close()
    print("Generated android_lowend_scorecard.png (mobile)")


def _plot_lowend_vs_gate(perf, docs_dir):
    """Grouped-bar snapshot: gate phone vs budget phone on the newest build BOTH measured.
    One build only — a mixed-build pair would read the gate phone's own build-to-build
    movement as a device gap. Surfaces at the measurement floor are dropped rather than
    drawn: two sub-frame readings make a ratio that is all noise."""
    import matplotlib.pyplot as plt
    import numpy as np

    FLOOR_S = 0.20
    low, gate = _lowend_frames(perf)
    if not len(low) or not len(gate):
        return
    shared = set(gate["commit_hash"]) & set(low["commit_hash"])
    if not shared:
        print("no build measured on both phones — skipping android_lowend_vs_gate.png")
        return
    build = low[low["commit_hash"].isin(shared)].sort_values("date", kind="stable")["commit_hash"].iloc[-1]
    lb, gb = low[low["commit_hash"] == build], gate[gate["commit_hash"] == build]

    # Kept in step with the low-end scorecard: a surface it refuses to put a ratio on must not
    # get one here either. The bars are real measurements, so they stay — only the "x" drops.
    VARIABLE = {"test_android_market_response_time"}
    pairs, dropped, ungraded = [], [], []
    for disp, name in LOWEND_SURFACES:
        lr, gr = lb[lb["test_name"] == name], gb[gb["test_name"] == name]
        if not len(lr) or not len(gr):
            continue
        lv, gv = float(lr["median_time"].iloc[-1]), float(gr["median_time"].iloc[-1])
        if lv < FLOOR_S or gv < FLOOR_S:
            dropped.append((disp, gv, lv))
            continue
        if name in VARIABLE:
            ungraded.append(disp)
        pairs.append((disp, gv, lv))
    if not pairs:
        print("no above-floor surface pair on %s — skipping android_lowend_vs_gate.png" % build)
        return

    labels = [p[0] for p in pairs]
    gvals, lvals = [p[1] for p in pairs], [p[2] for p in pairs]
    x = np.arange(len(pairs))
    w = 0.38
    fig, ax = plt.subplots(figsize=(max(8.6, len(pairs) * 1.35), 5.2))
    bars = [(ax.bar(x - w / 2, gvals, w, label="Samsung A36 (gate phone)", color="#2980b9"), gvals),
            (ax.bar(x + w / 2, lvals, w, label="%s (low-end)" % b.LOWEND_NAME, color="#e67e22"), lvals)]
    for group, vals in bars:
        for rect, v in zip(group, vals):
            ax.annotate("%.2f" % v, (rect.get_x() + rect.get_width() / 2, v),
                        textcoords="offset points", xytext=(0, 3), ha="center", fontsize=8)
    for xi, (disp, gv, lv) in enumerate(pairs):
        if disp in ungraded:
            continue
        ax.annotate("%.1f×" % (lv / gv), (xi, max(gv, lv)), textcoords="offset points",
                    xytext=(0, 16), ha="center", fontsize=8.5, fontweight="bold", color="#7f4f24")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9, rotation=20, ha="right", rotation_mode="anchor")
    ax.set_ylabel("seconds")
    ax.set_ylim(0, max(max(gvals), max(lvals)) * 1.30)
    ax.grid(axis="y", alpha=0.3)
    ax.set_axisbelow(True)
    ax.legend(loc="upper right", fontsize=9)
    fig.suptitle("Navigation response — gate phone vs low-end", fontweight="bold", fontsize=13)
    ax.set_title("build %s · both phones, same build · lower is better" % build,
                 fontsize=9.5, color="dimgray", pad=10)
    note = "Fresh account · median of the build's runs."
    if ungraded:
        note += "  No ratio shown for %s (content-gated: its median swings build-to-build)." % ", ".join(ungraded)
    if dropped:
        note += "  Omitted (at the ~0.1s measurement floor on one or both phones): %s." % ", ".join(d[0] for d in dropped)
    fig.text(0.5, 0.01, note, ha="center", fontsize=8, color="gray")
    fig.subplots_adjust(top=0.88, bottom=0.22)
    fig.savefig(docs_dir / "android_lowend_vs_gate.png", dpi=160)
    plt.close()
    print("Generated android_lowend_vs_gate.png (mobile)")


def _plot_release_gate(perf, docs_dir):
    """Performance scorecard — the view a reviewer reads by eye to decide a ship.

    Leads with a one-line verdict and sorts the surfaces that need attention to the
    top. Built so a stale / flaky / single-sample / un-baselined surface can never
    read as a clean pass:
      - one reference phone only (GATE_DEVICE) — never mixes devices;
      - rolling baseline = the last shipped GA (GA_BASE), compared on the SAME device OS;
      - a surface with no data for the build being scored renders STALE (grey);
      - single-sample (first/cold-open) and below-floor surfaces are INDICATIVE, never a
        hard regression/parity verdict;
      - the regression margin is per-surface where the run-to-run noise was MEASURED, and
        a conservative default (clearly flagged) where it was not;
      - Market (variable / content-gated) and Communities (networked) are not graded; a
        normally-excluded surface that moves grossly still escalates the headline to REVIEW;
      - a scope footer states what the gate does NOT cover, so green != "perf is fine".
    Regenerated every run, so the published reference stays current with no manual upkeep.
    """
    import matplotlib.pyplot as plt

    # ── gate config — the only knobs; roll these forward ──────────────────────────
    GA_BASE = "3ef171"      # last shipped GA that HAS measured data (2.38.2). Roll per release.
    GA_NAME = "2.38.2"      # its friendly name for the header.
    GATE_DEVICE = b.GATE_DEVICE  # the gate's reference phone (A36). Score ONE device — the CSV is
                                 # multi-device, and a stray row from another phone must not be
                                 # compared as if it were this one.
    FLOOR_S = 0.20          # at/below this the reading is latency, not render -> "within one frame".
    # Regression margin = how much slower than GA counts as a regression. TIGHT where the
    # run-to-run noise was actually MEASURED (variance study), CONSERVATIVE + flagged where it
    # was not. A single global margin is the wrong shape for a heterogeneous surface set, and the
    # within-build min/max spread is too outlier-sensitive to derive a per-surface margin from.
    NOISE = {"test_android_wallet_response_time": 0.06,    # measured between-run CV ~1.5%
             "test_android_settings_response_time": 0.08}  # measured between-run CV ~2.3%
    NOISE_DEFAULT = 0.12   # surfaces whose noise floor is NOT yet measured — coarse; RE-VALIDATE.
    VARIABLE = {"test_android_market_response_time"}  # content-gated: render time varies build-to-build; greyed, excluded from drift
                           # surfaces. A newly-bimodal surface must be ADDED here by hand — with
                           # n<=6 reps no single-build statistic reliably auto-detects bimodality
                           # (Market's is a cross-run effect), so there is deliberately no auto-flag.
    NETWORKED = {"test_android_communities_response_time"}  # network-dependent -> indicative.
    REDEFINED = {"test_android_settings_response_time": "redefined 2026-08-30 (profile menu) — not comparable"}
    GROSS_SPREAD = 3.0     # a build whose samples span >3x is clearly unstable this run -> low conf.
    GROSS_MOVE = 1.5       # a normally-excluded surface that moved >1.5x vs GA escalates the headline.

    GREEN, RED, AMBER, GREY = "#27ae60", "#c0392b", "#e67e22", "#7f8c8d"

    excluded = b._excluded_builds()
    p = perf[~perf["commit_hash"].isin(excluded)].copy() if excluded else perf.copy()
    if "metric" in p.columns:  # seconds-axis response_time rows only
        p = p[p["metric"] == "response_time"]
    if "device" in p.columns:  # ONE reference phone — never mix devices on the gate card
        p = p[p["device"] == GATE_DEVICE]
    labels = b._build_labels()
    env = b._run_environments()
    os_of = lambda h: env.get(h, "legacy")

    # Build under test = newest real point (not an "N" OS re-measurement of an old release).
    # Stable sort so same-date builds (the runner stamps date-only at noon) break the tie
    # deterministically on append order — the last-measured of a tied day wins, not a coin flip.
    real = p[~p["commit_hash"].astype(str).str.endswith("N")]
    if not len(real):                                     # no gate data -> honest empty card, no crash
        fig, ax = plt.subplots(figsize=(9.7, 2.4))
        ax.axis("off")
        ax.text(0.5, 0.6, "Android performance — release gate (per-RC)", ha="center", fontsize=15, fontweight="bold")
        ax.text(0.5, 0.35, f"no gate data for {GATE_DEVICE} yet", ha="center", fontsize=10, color="dimgray")
        fig.savefig(docs_dir / "android_release_gate.png", dpi=160, bbox_inches="tight")
        plt.close()
        print("Generated android_release_gate.png (mobile) — empty (no data)")
        return
    scored = real.sort_values("date", kind="stable")["commit_hash"].iloc[-1]
    scored_os = os_of(scored)
    scored_label = labels.get(scored, scored).replace("\n", " · ")

    # GA baseline on the SAME OS as the scored build. Comparing across an OS shift invents
    # regressions (an OS update moved Wallet ~13% on the same APK), so if the GA wasn't
    # re-measured on this OS for a surface, that surface shows "no same-OS baseline".
    ga_same_os = next((h for h in (GA_BASE, GA_BASE + "N")
                       if os_of(h) == scored_os and len(p[p["commit_hash"] == h])), None)

    def ga_base(name):
        if ga_same_os is None:
            return None
        r = p[(p["commit_hash"] == ga_same_os) & (p["test_name"] == name)]
        return float(r["median_time"].iloc[0]) if len(r) else None

    def scored_row(name):
        r = p[(p["commit_hash"] == scored) & (p["test_name"] == name)]
        return r.iloc[-1] if len(r) else None       # last-appended row for this build+device

    def last_seen(name):
        c = real[real["test_name"] == name].sort_values("date", kind="stable")
        if not len(c):
            return (None, None, None)
        r = c.iloc[-1]
        return (float(r["median_time"]), str(r["commit_hash"]), str(r["date"])[:10])

    AREA = {"wallet": "Wallet", "settings": "Settings", "messages": "Messages",
            "market": "Market", "communities": "Communities", "featured": "Featured"}

    def prettify(name):
        s = name.replace("test_android_", "")
        tag = ""
        if s.endswith("_cold_open"):
            s, tag = s[:-10], " · cold open"
        elif s.endswith("_first_open"):
            s, tag = s[:-11], " · first open"
        elif s.endswith("_response_time"):
            s = s[:-14]
        parts = s.split("_")
        area = AREA.get(parts[0], parts[0].capitalize())
        rest = " ".join(parts[1:])
        head = area if not rest else f"{area} ▸ {rest[0].upper() + rest[1:]}"
        return head + tag

    # ── classify every surface the gate has ever measured ─────────────────────────
    REG, LOWC, NOBASE, OK, INDIC, STALE = 0, 1, 2, 3, 4, 5   # rank: lower = more attention
    rows = []
    gross_movers = []   # normally-excluded (variable/networked) surfaces that moved grossly vs GA -> escalate headline
    for name in sorted(p["test_name"].unique()):
        row = scored_row(name)
        if row is None:                              # no data for the build being scored -> STALE
            lv, lh, ld = last_seen(name)
            change = f"(last {lv:.2f}s)" if lv is not None else "—"
            asof = f"{ld} · {lh}" if lh else "never measured"
            rows.append((STALE, prettify(name), change, asof, "stale — no data", GREY))
            continue
        asof = f"{str(row['date'])[:10]} · {scored}"
        val = float(row["median_time"]) if row["median_time"] not in ("", None) else 0.0
        try:
            rc = int(float(row["run_count"]))
        except Exception:
            rc = 0
        try:
            runs = [float(x) for x in str(row["all_runs"]).split(",") if x.strip()]
        except Exception:
            runs = []
        bv = ga_base(name)
        change = f"{bv:.2f}s → {val:.2f}s" if bv else f"~{val:.2f}s"

        if rc < 2 or len(runs) < 2:                  # single sample -> never a hard verdict
            rows.append((INDIC, prettify(name), change, asof, "single sample (indicative)", GREY))
        elif val <= 0:                               # no usable median -> can't verify
            rows.append((LOWC, prettify(name), "—", asof, "unverifiable (no samples)", AMBER))
        elif val < FLOOR_S:                          # below the measurement floor -> latency, not render
            rows.append((INDIC, prettify(name), f"~{val:.2f}s", asof, "within one frame", GREY))
        elif bv is not None and bv < FLOOR_S:
            # GA read this surface at the floor, so val/bv is the floor reading, not a change.
            rows.append((INDIC, prettify(name), change, asof, "floor-limited baseline", GREY))
        elif name in REDEFINED:                      # the surface changed meaning -> no comparable baseline
            rows.append((NOBASE, prettify(name), f"~{val:.2f}s", asof, REDEFINED[name], GREY))
        elif name in VARIABLE or name in NETWORKED:
            tag = "variable (content-gated)" if name in VARIABLE else "networked (indicative)"
            if bv and val / bv > GROSS_MOVE:
                gross_movers.append(prettify(name))
                tag += f" — ▲ ~{val / bv:.1f}×"
            rows.append((LOWC, prettify(name), change, asof, tag, AMBER))
        elif runs and min(runs) > 0 and max(runs) / min(runs) > GROSS_SPREAD:
            rows.append((LOWC, prettify(name), change, asof,
                         f"low confidence (samples span {max(runs) / min(runs):.0f}×)", AMBER))
        elif bv is None:
            rows.append((NOBASE, prettify(name), f"~{val:.2f}s", asof, "no same-OS baseline", GREY))
        else:
            ratio = val / bv
            margin = NOISE.get(name, NOISE_DEFAULT)
            tail = "" if name in NOISE else " *"     # '*' marks a coarse (unmeasured-noise) call
            if ratio > 1 + margin:
                rows.append((REG, prettify(name), change, asof, f"▲ +{round((ratio - 1) * 100)}% vs {GA_NAME}{tail}", RED))
            elif ratio < 1 - margin:
                rows.append((OK, prettify(name), change, asof, f"▼ −{round((1 - ratio) * 100)}% vs {GA_NAME}{tail}", GREEN))
            else:
                rows.append((OK, prettify(name), change, asof, f"✓ parity{tail}", GREEN))

    rows.sort(key=lambda r: (r[0], r[1]))

    # ── verdict header ────────────────────────────────────────────────────────────
    def names_for(rank):
        return [r[1] for r in rows if r[0] == rank]

    def short(lst, k=2):
        if not lst:
            return ""
        return f" ({', '.join(lst[:k])}{f' +{len(lst) - k} more' if len(lst) > k else ''})"

    regs, lowc, nobase = names_for(REG), names_for(LOWC), names_for(NOBASE)
    n_ok, n_indic, n_stale = (sum(1 for r in rows if r[0] == k) for k in (OK, INDIC, STALE))
    n = len(rows)
    thin = (n_stale + len(nobase)) > n * 0.34        # >~a third of the gate dark -> not "CLEAR"

    parts = [f"{len(regs)} regressed{short(regs)}", f"{len(lowc)} not graded{short(lowc)}",
             f"{n_ok} OK"]
    if n_indic:
        parts.append(f"{n_indic} indicative")
    if nobase:
        parts.append(f"{len(nobase)} no same-OS baseline")
    parts.append(f"{n_stale} stale")
    verdict = "   ·   ".join(parts)
    if regs or gross_movers:
        vcol, vlead = RED, "REVIEW"
        if gross_movers and not regs:
            verdict = f"a normally-excluded surface moved sharply ({', '.join(gross_movers[:2])})   ·   " + verdict
    elif lowc or thin:
        vcol, vlead = AMBER, "CAUTION"
    else:
        vcol, vlead = GREEN, "CLEAR"

    # ── render (fixed inch geometry so row spacing is constant for any surface count) ──
    ROW_H, TOP_PAD, FOOT_PAD = 0.236, 2.35, 1.40
    fig_h = TOP_PAD + n * ROW_H + FOOT_PAD
    fig, ax = plt.subplots(figsize=(9.9, fig_h))
    ax.set_position([0, 0, 1, 1])
    ax.axis("off")

    def Y(t):
        return 1 - t / fig_h

    os_note = "  ·  same device OS" if ga_same_os else "  ·  NO same-OS baseline (re-baseline needed)"
    ax.text(0.5, Y(0.42), "Android performance — release gate (per-RC)", ha="center", va="center",
            fontsize=15, fontweight="bold", transform=ax.transAxes)
    ax.text(0.5, Y(0.82), f"build under test: {scored_label}    ·    baseline: last release {GA_NAME}{os_note}    ·    {GATE_DEVICE}  ·  lower is better",
            ha="center", va="center", fontsize=8.6, color="dimgray", transform=ax.transAxes)
    ax.text(0.5, Y(1.42), f"{vlead}:   {verdict}", ha="center", va="center", fontsize=11, fontweight="bold",
            color="white", bbox=dict(boxstyle="round,pad=0.5", fc=vcol, ec="none"), transform=ax.transAxes)

    hy = Y(1.98)
    ax.text(0.030, hy, "Surface", fontsize=9, fontweight="bold", transform=ax.transAxes)
    ax.text(0.430, hy, "last release → this build", fontsize=9, fontweight="bold", transform=ax.transAxes)
    ax.text(0.670, hy, "measured", fontsize=9, fontweight="bold", transform=ax.transAxes)
    ax.text(0.985, hy, "Status", fontsize=9, fontweight="bold", ha="right", transform=ax.transAxes)
    ax.plot([0.030, 0.985], [Y(2.14)] * 2, color="#cccccc", lw=0.8, transform=ax.transAxes)

    for i, (rank, label, change, asof, status, col) in enumerate(rows):
        yy = Y(TOP_PAD + i * ROW_H + ROW_H * 0.5)
        grey = rank in (STALE, NOBASE, INDIC)
        ax.text(0.030, yy, label, fontsize=8.3, va="center", transform=ax.transAxes,
                color=("#8a8a8a" if grey else "#1a1a1a"))
        ax.text(0.430, yy, change, fontsize=8.0, va="center", transform=ax.transAxes,
                color=("#9a9a9a" if grey else "#555555"))
        ax.text(0.670, yy, asof, fontsize=7.6, va="center", transform=ax.transAxes,
                color=("#aaaaaa" if rank == STALE else "#888888"))
        ax.text(0.985, yy, status, fontsize=8.0, va="center", ha="right", transform=ax.transAxes,
                color="white", fontweight="bold", bbox=dict(boxstyle="round,pad=0.28", fc=col, ec="none"))

    fy = Y(TOP_PAD + n * ROW_H + 0.55)
    foot = (
        "Scope: fresh account · one mid-range phone (Samsung A36) · UI-navigation timings (median of the build's runs).\n"
        "Does NOT cover: large / loaded accounts · low-end devices · memory / thermal · battery (#21149) · message delivery (#20999).\n"
        "A green scorecard means fresh-account UI responsiveness didn't regress — it does NOT mean performance is fine. "
        "'within one frame' = at/below the ~0.1 s floor.  '*' = coarse call (surface noise not yet measured)."
    )
    ax.text(0.5, fy, foot, ha="center", va="top", fontsize=7.4, color="gray",
            transform=ax.transAxes, linespacing=1.5)

    fig.savefig(docs_dir / "android_release_gate.png", dpi=160, bbox_inches="tight")
    plt.close()
    print("Generated android_release_gate.png (mobile)")


def _lowend_variant(t):
    """The same surface, charted on the low-end phone: own file, own footnote, everything
    else (statistic, floor caveats, baselines) inherited so the two charts stay readable
    side by side. Generated from the gate config rather than a second config file — a
    duplicated surface list would drift the moment one side gained a surface."""
    import dataclasses
    foot = t.footnote.replace("Samsung A36", f"{b.LOWEND_NAME} · Android 15 Go edition")
    if foot == t.footnote:
        foot = (f"{b.LOWEND_NAME} · Android 15 Go edition · " + foot) if foot else \
            f"Fresh account · {b.LOWEND_NAME} · Android 15 Go edition"
    return dataclasses.replace(
        t, device=b.LOWEND_DEVICE,
        graph_filename=t.graph_filename.replace("android_", "android_lowend_", 1),
        display_name=t.display_name.replace("Android —", f"Android ({b.LOWEND_NAME}) —"),
        footnote=foot + " · refreshed weekly")


def charts(data_dir, docs_dir):
    import shutil
    data_dir, docs_dir = Path(data_dir), Path(docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)
    perf = pd.read_csv(data_dir / "performance_metrics.csv")
    perf["date"] = pd.to_datetime(perf["date"], format="mixed")  # tolerate date-only vs ISO timestamps
    latest = perf.sort_values("date").iloc[-1]
    stamp = f"{latest['date'].date()}_{latest['commit_hash']}"  # e.g. 2026-06-08_8e3dee
    archive = CHART_ARCHIVE  # outside the repo (kept local, not committed)
    archive.mkdir(parents=True, exist_ok=True)
    lowend_seen = set(perf[perf["device"] == b.LOWEND_DEVICE]["test_name"])
    lowend_dir = docs_dir / "lowend"
    lowend_dir.mkdir(parents=True, exist_ok=True)
    for t in b.load_config(REPO / "scripts/tests_config_android.toml"):
        if not t.pattern.startswith("test_android"):
            continue
        b.plot_performance_mobile(perf, t, docs_dir)
        canonical = docs_dir / t.graph_filename
        if canonical.exists():  # also keep a sortable/searchable dated+hashed copy
            shutil.copy2(canonical, archive / f"{canonical.stem}_{stamp}.png")
        if not t.device and t.pattern in lowend_seen:
            b.plot_performance_mobile(perf, _lowend_variant(t), lowend_dir)
    _plot_first_vs_returning(perf, docs_dir)
    _plot_scorecard(perf, docs_dir)
    _plot_lowend_scorecard(perf, docs_dir)
    _plot_lowend_vs_gate(perf, docs_dir)
    print(f"regenerated android charts -> {docs_dir}  (+ archive/*_{stamp}.png)")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "append":
        append(*sys.argv[2:8])
    elif mode == "charts":
        charts(*sys.argv[2:4])
    else:
        print(__doc__)
        sys.exit(2)
