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
             "Wallet omitted (post-login landing — its first open is already warm). "
             "The timer works in screenshot steps of about %.2f s." % STEP_S,
             ha="center", fontsize=8, color="gray")
    fig.subplots_adjust(top=0.88, bottom=0.13)
    fig.savefig(docs_dir / "android_first_vs_returning.png", dpi=160)
    plt.close()
    print("Generated android_first_vs_returning.png (mobile)")


# The response-time timer takes screenshots one after another and reports the start of the
# first one that shows the new screen. Readings therefore land on a grid one screenshot apart:
# about 0.55 s on the Samsung A36, where single steps measure 0.50–0.56 s. A screen that is
# already there at the first screenshot reads about 0.1 s, whatever its real time.
STEP_S = 0.55
MIN_STEP_CHANGE_S = 0.45   # smallest change that is a whole step, given the 0.50–0.56 s spread
LOWEST_BIN_S = 0.20        # below this, the screen was ready at the first screenshot
RECENT_DAYS = 14
RELEASES_API = "https://api.github.com/repos/status-im/status-app/releases?per_page=100"

SCORECARD_SURFACES = [
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

GREEN, RED, AMBER, GREY, BLUE, INK = "#27ae60", "#c0392b", "#e67e22", "#7f8c8d", "#2c7fb8", "#444444"


def _release_name(label):
    """'2026-06-16|2.38.0 · 5f66de' -> '2.38.0', and '2026-08-30|2.38.2·ZG1' -> '2.38.2'."""
    return re.split(r"[|\n]", str(label))[-1].split("·")[0].strip()


def _shipped_from_api(releases):
    """Tag names of shipped releases, newest first. Drafts and pre-releases (the RCs) are not shipped."""
    shipped = [r for r in releases if not r.get("draft") and not r.get("prerelease")]
    shipped.sort(key=lambda r: r.get("published_at") or "", reverse=True)
    return [r["tag_name"] for r in shipped]


def _shipped_releases():
    """Shipped status-app releases from GitHub, newest first, or None if GitHub can't be reached."""
    import json
    import urllib.request
    req = urllib.request.Request(RELEASES_API, headers={"Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return _shipped_from_api(json.load(resp))
    except Exception as e:
        print("scorecard: could not read GitHub releases (%s)" % e)
        return None


def _resolve_baseline(p, os_of, labels, shipped, cur_os, skip_name=""):
    """The baseline is the newest shipped release that the gate phone measured on its current
    firmware. A firmware update moves the numbers by itself, so a release measured on other
    firmware is never used. Returns (build, release name, reason); build is None when no release
    qualifies."""
    if cur_os is None:
        return None, None, "the card's build has no recorded firmware, so no release can be matched to it"
    source = "on GitHub"
    if shipped is None:
        names = {_release_name(v) for v in labels.values()}
        shipped = sorted((n for n in names if re.fullmatch(r"\d+(\.\d+)+", n)),
                         key=lambda n: tuple(int(x) for x in n.split(".")), reverse=True)
        source = "in build_labels.csv (GitHub could not be reached)"
    shipped = [n for n in shipped if n != skip_name]
    if not shipped:
        return None, None, "no shipped release found %s" % source
    rows = p.groupby("commit_hash").size()
    for name in shipped:
        builds = [h for h, v in labels.items()
                  if _release_name(v) == name and h in rows.index and os_of(h) == cur_os]
        if not builds:
            continue
        build = max(builds, key=lambda h: rows[h])
        if name == shipped[0]:
            why = "the newest shipped release %s, measured on this phone's current firmware" % source
        else:
            why = ("the newest shipped release %s, %s, has no data from this phone on its current firmware; "
                   "%s is the newest release that does" % (source, shipped[0], name))
        return build, name, why
    return None, None, "no shipped release %s has data from this phone on its current firmware" % source


def _card_build(p):
    """The newest build that measured more than half of the headline surfaces. Builds that ran only
    a few surfaces (one-off checks) never become the card's build."""
    names = [n for _, n in SCORECARD_SURFACES]
    c = p[p["test_name"].isin(names)
          & ~p["commit_hash"].astype(str).str.endswith("N")].copy()   # "N" = an old release re-measured on a newer OS
    if not len(c):
        return None
    c["order"] = range(len(c))
    cover = c.groupby("commit_hash").agg(n=("test_name", "nunique"), date=("date", "max"), order=("order", "max"))
    cover = cover[cover["n"] * 2 > len(names)]
    if not len(cover):
        return None
    # Builds are stamped with a date only, so a same-day tie goes to the build appended last.
    return cover.sort_values(["date", "order"]).index[-1]


def _below_resolution(p, name, os_of, cur_os, until):
    """True when every reading of this surface in the RECENT_DAYS up to `until` (the card's build
    included) is in the lowest bin. Such a screen is ready before the first screenshot, so the
    timer cannot say how fast it is."""
    w = p[(p["test_name"] == name) & (p["date"] <= until)
          & (p["date"] > until - pd.Timedelta(RECENT_DAYS, unit="D"))
          & ~p["commit_hash"].astype(str).str.endswith("N")]
    w = w[w["commit_hash"].map(os_of) == cur_os]
    return len(w) > 0 and bool((w["median_time"].astype(float) < LOWEST_BIN_S).all())


def _speed_band(val):
    FAST, SLOW, NEAR = 0.50, 1.00, 0.90        # nav UX bands; NEAR*SLOW = within 10% of the slow line
    if val < FAST:
        return "fast", GREEN
    if val <= SLOW:
        return "ok", (AMBER if val > NEAR * SLOW else BLUE)
    return "slow", RED


def _scorecard(perf, env, labels, shipped, excluded=()):
    """The scorecard's content, without drawing it. Every row comes from ONE build: the newest that
    measured most of the headline surfaces. A surface that build did not measure says so; it never
    borrows a value from another build. Returns (card, rows): card describes the build and its
    baseline, and each row is (surface, numbers, (verdict, colour), (speed band, colour))."""
    NETWORKED = {"test_android_communities_response_time"}
    # Settings moved from the side bar to the profile menu in 2.39.0, so a baseline from an older
    # release timed a different route.
    REDEFINED = {"test_android_settings_response_time": (2, 39, 0)}
    VARIABLE = {"test_android_market_response_time"}       # content-gated: render time varies build-to-build

    p = perf[~perf["commit_hash"].isin(excluded)].copy() if excluded else perf.copy()
    if "metric" in p.columns:
        p = p[p["metric"] == "response_time"]
    if "device" in p.columns:
        p = p[p["device"] == b.GATE_DEVICE]
    os_of = env.get

    build = _card_build(p)
    card = dict(build=build, label="", date=None, base=None, base_name=None,
                base_why="no build has measured most of the headline surfaces yet")
    if build is None:
        return card, [(d, "—", ("no data", GREY), ("", GREY)) for d, _ in SCORECARD_SURFACES]
    cur_os = os_of(build)
    rows_b = p[p["commit_hash"] == build]
    card["date"] = rows_b["date"].max()
    card["label"] = labels.get(build, "")
    card["base"], card["base_name"], card["base_why"] = _resolve_baseline(
        p, os_of, labels, shipped, cur_os, skip_name=_release_name(labels.get(build, "")))

    def base(name):
        r = p[(p["commit_hash"] == card["base"]) & (p["test_name"] == name)]
        return float(r["median_time"].iloc[-1]) if len(r) else None

    def redefined(name):
        if name not in REDEFINED:
            return False
        try:
            return tuple(int(x) for x in card["base_name"].split(".")) < REDEFINED[name]
        except (AttributeError, ValueError):
            return True

    rows = []
    for disp, name in SCORECARD_SURFACES:
        r = rows_b[rows_b["test_name"] == name]
        if not len(r):
            rows.append((disp, "—", ("not measured on this build", GREY), ("", GREY)))
            continue
        r = r.iloc[-1]
        val = float(r["median_time"])
        bv = base(name)
        try:
            rc = int(float(r["run_count"]))
        except Exception:
            rc = 0
        nums = ("%.2fs → %.2fs" % (bv, val)) if bv is not None else ("— → %.2fs" % val)
        band, bcol = _speed_band(val)
        # Greyed only when the release was in the lowest bin too, so a real drop into it still shows.
        low = (bv is None or bv < LOWEST_BIN_S) and _below_resolution(p, name, os_of, cur_os, card["date"])
        caveat = ("too fast to time" if low
                  else "single sample" if rc < 2 else "variable" if name in VARIABLE
                  else "networked" if name in NETWORKED else "redefined" if redefined(name) else None)
        if caveat:                                          # greyed; raw numbers shown but no verdict asserted
            rows.append((disp, nums, (caveat, AMBER if caveat == "networked" else GREY), (band, GREY)))
        elif bv is None:
            rows.append((disp, nums, ("no baseline", GREY), (band, bcol)))
        elif abs(val - bv) < MIN_STEP_CHANGE_S:
            rows.append((disp, nums, ("no measurable change", GREY), (band, bcol)))
        elif val > bv:
            rows.append((disp, nums, ("▲ +%.2fs slower" % (val - bv), RED), (band, bcol)))
        else:
            rows.append((disp, nums, ("▼ −%.2fs faster" % (bv - val), GREEN), (band, bcol)))
    return card, rows


def _plot_scorecard(perf, docs_dir):
    """At-a-glance 'now' card: one build, each headline surface against the last shipped release,
    plus an absolute SPEED band (fast/ok/slow). Drift over time lives in the per-surface charts."""
    import matplotlib.pyplot as plt

    card, rows = _scorecard(perf, b._run_environments(), b._build_labels(), _shipped_releases(),
                            b._excluded_builds())
    if card["base"]:
        print("scorecard baseline: %s (build %s): %s" % (card["base_name"], card["base"], card["base_why"]))
    else:
        print("scorecard baseline: none: %s" % card["base_why"])

    if card["build"] is None:
        build_txt = "no build has measured most of the headline surfaces yet"
    else:
        build_txt = ("build " + card["label"].replace("\n", " · ") if card["label"]
                     else "build %s · %s" % (card["build"], str(card["date"])[:10]))
    base_txt = ("vs the last shipped release (%s)" % card["base_name"] if card["base"]
                else "no baseline on this phone's current firmware")

    n = len(rows)
    ROW_H = 0.34
    fig_h = 2.0 + n * ROW_H + 1.55
    fig, ax = plt.subplots(figsize=(8.2, fig_h))
    ax.set_position([0, 0, 1, 1])
    ax.axis("off")

    def Y(t):
        return 1 - t / fig_h

    ax.text(0.5, Y(0.45), "Android performance — scorecard", ha="center", va="center",
            fontsize=15, fontweight="bold", transform=ax.transAxes)
    ax.text(0.5, Y(0.85), "%s  ·  %s  ·  %s  ·  lower is better" % (build_txt, base_txt, b.GATE_DEVICE),
            ha="center", va="center", fontsize=8.6, color="dimgray", transform=ax.transAxes)
    cx = dict(surface=0.030, nums=0.250, verdict=0.440, speed=0.880)
    hy = Y(1.55)
    ax.text(cx["surface"], hy, "surface", fontsize=9.3, fontweight="bold", transform=ax.transAxes)
    ax.text(cx["nums"], hy, "last release → this build", fontsize=9.3, fontweight="bold", transform=ax.transAxes)
    ax.text(cx["speed"], hy, "speed", fontsize=9.3, fontweight="bold", transform=ax.transAxes)
    ax.plot([cx["surface"], 0.965], [Y(1.72)] * 2, color="#cccccc", lw=0.8, transform=ax.transAxes)

    for i, (disp, nums, verdict, speed_cell) in enumerate(rows):
        yy = Y(2.0 + i * ROW_H + ROW_H * 0.5)
        indent = cx["surface"] + (0.035 if disp.startswith("Wallet ▸") else 0)
        ax.text(indent, yy, disp, fontsize=9.1, va="center", transform=ax.transAxes, color="#1a1a1a")
        ax.text(cx["nums"], yy, nums, fontsize=8.4, va="center", transform=ax.transAxes, color=INK)
        vt, vcol = verdict
        ax.text(cx["verdict"], yy, vt, fontsize=8.4, va="center", transform=ax.transAxes, color=vcol,
                fontweight=("normal" if vcol == GREY else "bold"))
        st, scol = speed_cell
        if st:
            ax.text(cx["speed"], yy, st, fontsize=8.2, va="center", ha="left", transform=ax.transAxes,
                    color="white", fontweight="bold", bbox=dict(boxstyle="round,pad=0.3", fc=scol, ec="none"))

    foot = [
        "speed:  fast < 0.5s   ·   ok 0.5–1.0s (amber = within 10% of the slow line)   ·   slow > 1.0s",
        "A change is shown only when it is at least one timer step (about %.2f s on the A36); smaller changes" % STEP_S,
        "read \"no measurable change\".  \"Too fast to time\" = the screen was ready at the first screenshot",
        "(under %.1f s) on every build in the last %d days." % (LOWEST_BIN_S, RECENT_DAYS),
        "Greyed = never asserted as a pass.  Variable = content-gated; its median swings build-to-build.",
        "Every row is from the one build named above.  Fresh account · one mid-range phone (Samsung A36) · median of",
        "the build's runs.  Drift over time is in the per-surface trend charts.",
    ]
    for k, line in enumerate(foot):
        ax.text(0.020, Y(2.0 + n * ROW_H + 0.40 + k * 0.19), line,
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
    Same honesty rules as the gate card: a surface that is unmeasured, ready at the first
    screenshot, single-sample or stale shows its raw number but never a comparison, and the gate
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

        # Either side in the lowest bin kills the pair, not just the low-end side: a first-screenshot
        # reading against a real one prints a ratio (Communities read 1.60s vs 0.10s) that
        # says the budget phone is 16x faster. Show the low-end number alone and say why.
        floored = val < FLOOR_S or (gv is not None and gv < FLOOR_S)
        stale = newest is not None and (newest - r["date"]).days > STALE_DAYS
        caveat = ("single sample" if rc < 2
                  else ("too fast to time" if val < FLOOR_S else "A36 too fast to time") if floored
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
            "Greyed = not yet measured / too fast to time (ready at the first screenshot, under 0.2 s) / single sample / stale — never asserted as a comparison.",
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
    movement as a device gap. Surfaces ready at the first screenshot are dropped rather than
    drawn: two such readings make a ratio that is all noise."""
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
        print("no surface pair above the lowest bin on %s — skipping android_lowend_vs_gate.png" % build)
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
        note += "  Omitted (too fast to time on one or both phones): %s." % ", ".join(d[0] for d in dropped)
    fig.text(0.5, 0.01, note, ha="center", fontsize=8, color="gray")
    fig.subplots_adjust(top=0.88, bottom=0.22)
    fig.savefig(docs_dir / "android_lowend_vs_gate.png", dpi=160)
    plt.close()
    print("Generated android_lowend_vs_gate.png (mobile)")


def _lowend_variant(t):
    """The same surface, charted on the low-end phone: own file, own footnote, everything
    else (statistic, resolution caveats, baselines) inherited so the two charts stay readable
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
