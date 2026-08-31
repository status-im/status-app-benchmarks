#!/usr/bin/env python3
"""Perf anomaly detector — stage 1 of the auto-filer (detection only, zero side effects).

Reads data/android/performance_metrics.csv (+ run_environment.csv) from the
status-app-benchmarks clone and reports what the ratified rules would raise:

  A — regression: median > +15% vs the same-OS release baseline, sustained over 3
      consecutive nightly results; surfaces with a baseline under 0.3s additionally
      need an absolute move > 0.15s (rules ratified 2026-07-02, tracker decisions log;
      research: qa/investigations/anomaly-detector-threshold-research-2026-07-01.md).
  B — slow band: screen sitting above 1.0s for 2+ consecutive results (single-night
      spikes excluded — the lived triage rule behind status-app#21429). Chronically
      variable surfaces (Market, Communities tabs, directory/featured) are soft-notes,
      never hard alerts.

Usage: perf_anomaly_detect.py <data-dir> [--as-of YYYY-MM-DD] [--json] [--cross-os]
--cross-os compares against the pre-OS-shift baseline regardless of regime — back-test
only, proves the engine sees a real OS-sized step that same-OS mode absorbs.
Back-test (arming prerequisite): test_perf_anomaly_detect.py <data-dir>.
"""
import argparse
import csv
import datetime
import io
import json
import sys
from pathlib import Path

GA_BASE = "3ef171"          # last shipped GA with measured data (2.38.2); roll per release
GATE_DEVICE = "SM-A366B"    # the gate's reference phone — never mix devices
THRESHOLD = 0.15            # A: fire above +15% vs baseline
STREAK = 3                  # A: sustained over N consecutive nightly results
ABS_FLOOR_BASE = 0.30       # A: baselines under this also need...
ABS_FLOOR_MOVE = 0.15       # ...an absolute move above this (kills sub-floor % explosion)
BAND = 1.0                  # B: the slow band
BAND_STREAK = 2             # B: consecutive DISTINCT DAYS in band before it counts
                            # (A deliberately counts results, per the ratified wording)
STALE_DAYS = 7              # findings older than this vs the newest data are tagged stale
EXCLUDED = {                # variable/networked — soft-note only, never hard-fire
    "test_android_market_response_time",
    "test_android_communities_response_time",
    "test_android_communities_directory_load",
    "test_android_featured_community_open",
}
AREA = {"wallet": "Wallet", "settings": "Settings", "messages": "Messages",
        "market": "Market", "communities": "Communities", "featured": "Featured",
        "home": "Home", "activity": "Activity"}


def load_data(data_dir):
    data_dir = Path(data_dir)
    rows = list(csv.DictReader(io.StringIO((data_dir / "performance_metrics.csv").read_text())))
    env_file = data_dir / "run_environment.csv"
    # Required, not enrichment: without it every build reads as pre-Android-16 and the
    # wrong-OS baseline wins — cross-OS regressions confidently labelled "same-OS".
    try:
        env = {r["commit_hash"]: r["android"]
               for r in csv.DictReader(io.StringIO(env_file.read_text()))}
    except OSError:
        sys.exit(f"{env_file} missing — refusing to run (OS regimes unknown)")
    if not env:
        sys.exit(f"{env_file} is empty — refusing to run (OS regimes unknown)")
    return rows, env


def prettify(name):
    s, tag = name.replace("test_android_", ""), ""
    for suffix, t in (("_cold_open", " · cold open"), ("_first_open", " · first open"),
                      ("_response_time", "")):
        if s.endswith(suffix):
            s, tag = s[: -len(suffix)], t
            break
    parts = s.split("_")
    head = AREA.get(parts[0], parts[0].capitalize())
    rest = " ".join(parts[1:])
    return (head if not rest else f"{head} ▸ {rest}") + tag


def detect(rows, env, as_of=None, baseline_mode="same_os"):
    regime = lambda h: env.get(h, "legacy")
    usable = []
    for i, r in enumerate(rows):
        try:
            median = float(r["median_time"])
        except (KeyError, ValueError, TypeError):
            continue
        if (r.get("metric") == "response_time" and r.get("device") == GATE_DEVICE
                and median > 0 and (as_of is None or r["date"][:10] <= as_of)):
            usable.append((r["date"][:10], i, r["commit_hash"], r["test_name"], median))
    usable.sort(key=lambda t: (t[0], t[1]))   # stable on append order within a date

    by_surface, baselines = {}, {}
    for date, _, build, name, median in usable:
        if build == GA_BASE or build == GA_BASE + "N":
            baselines.setdefault((build, name), median)
        if not build.endswith("N"):     # "N" builds = out-of-band OS re-measures, not nightlies
            by_surface.setdefault(name, []).append((date, build, median))

    report = {"as_of": as_of, "baseline_mode": baseline_mode,
              "surfaces": sorted(by_surface), "regressions": [], "pending": [],
              "slow_band": [], "watch": [], "soft_notes": [], "no_baseline": []}
    horizon = max((d for d, *_ in usable), default=None)   # newest data anywhere in the CSV

    def age_days(date):
        return (datetime.date.fromisoformat(horizon) - datetime.date.fromisoformat(date)).days

    for name, nights in sorted(by_surface.items()):
        last_date, last_build, latest = nights[-1]
        latest_regime = regime(last_build)
        stale = age_days(last_date) > STALE_DAYS

        base = base_build = None
        candidates = (GA_BASE,) if baseline_mode == "cross_os" else (GA_BASE, GA_BASE + "N")
        for cand in candidates:
            if (cand, name) in baselines and (baseline_mode == "cross_os"
                                              or regime(cand) == latest_regime):
                base, base_build = baselines[(cand, name)], cand
                break

        a_run = []                       # trailing consecutive over-threshold nights
        if base:
            for date, build, median in reversed(nights):
                if regime(build) != latest_regime:   # same OS regime only
                    break
                over = (median / base > 1 + THRESHOLD + 1e-9
                        and (base >= ABS_FLOOR_BASE or median - base > ABS_FLOOR_MOVE))
                if not over:
                    break
                a_run.append((date, build, median, round((median / base - 1) * 100, 1)))
            a_run.reverse()

        b_run = []                       # trailing consecutive in-band nights
        for date, build, median in reversed(nights):
            if median <= BAND:
                break
            b_run.append((date, build, median))
        b_run.reverse()

        if name in EXCLUDED:
            report["soft_notes"].append({
                "surface": name, "latest": latest, "last_measured": last_date,
                "band_streak": len(b_run),
                "vs_base_pct": round((latest / base - 1) * 100, 1) if base else None})
            continue

        if len(a_run) >= STREAK:
            report["regressions"].append({
                "surface": name, "baseline": base, "baseline_build": base_build,
                "android_version": latest_regime, "streak": len(a_run), "start": a_run[0][0],
                "fired": a_run[STREAK - 1][0],
                "nights": [{"date": d, "build": b, "median": m, "pct": p}
                           for d, b, m, p in a_run]})
        elif a_run:
            report["pending"].append({"surface": name, "baseline": base,
                                      "streak": len(a_run), "latest": latest,
                                      "pct": a_run[-1][3], "last_measured": last_date})
        elif base is None:
            report["no_baseline"].append({"surface": name, "latest": latest,
                                          "last_measured": last_date})

        band_days = sorted({d for d, _, _ in b_run})   # independent DAYS, not results —
        if len(band_days) >= BAND_STREAK:              # a same-day double-run is one spike
            category = ("first_cold" if name.endswith(("_first_open", "_cold_open"))
                        else "steady")
            report["slow_band"].append({
                "surface": name, "category": category, "streak": len(b_run),
                "days": len(band_days), "entered": b_run[0][0],
                "confirmed": band_days[BAND_STREAK - 1], "latest": latest,
                "latest_build": last_build, "last_measured": last_date, "stale": stale})
        elif b_run:
            report["watch"].append({"surface": name, "latest": latest,
                                    "last_measured": last_date, "stale": stale})
    return report


def render(report):
    out = [f"perf anomaly report — as of {report['as_of'] or 'latest'} "
           f"(baseline mode: {report['baseline_mode']}; baselines: {GA_BASE} = 2.38.2 GA "
           f"pre-Android-16, {GA_BASE}N = its Android 16 re-measure)"]
    stale_tag = lambda e: " — STALE" if e.get("stale") else ""
    for e in report["regressions"]:
        series = ", ".join(f"{n['date'][5:]} {n['median']:.2f}s ({n['pct']:+.0f}%)"
                           for n in e["nights"])
        out.append(f"WOULD FILE (regression): {prettify(e['surface'])} — "
                   f"{e['baseline']:.2f}s → {e['nights'][-1]['median']:.2f}s "
                   f"({e['nights'][-1]['pct']:+.0f}%) vs same-OS {e['baseline_build']}, "
                   f"{e['streak']} nights sustained [{series}]")
    for e in report["slow_band"]:
        out.append(f"WOULD FILE (slow band): {prettify(e['surface'])} — {e['latest']:.2f}s, "
                   f">1.0s for {e['days']} days since {e['entered']} "
                   f"({e['category']}, last measured {e['last_measured']}{stale_tag(e)})")
    for e in report["pending"]:
        out.append(f"pending ({e['streak']}/{STREAK} nights): {prettify(e['surface'])} — "
                   f"{e['latest']:.2f}s ({e['pct']:+.0f}% vs {e['baseline']:.2f}s baseline)")
    for e in report["watch"]:
        out.append(f"watch (1 day in band): {prettify(e['surface'])} — "
                   f"{e['latest']:.2f}s on {e['last_measured']}{stale_tag(e)}")
    for e in report["soft_notes"]:
        vs = f", {e['vs_base_pct']:+.0f}% vs baseline" if e["vs_base_pct"] is not None else ""
        out.append(f"soft note (variable/networked, never filed): {prettify(e['surface'])} — "
                   f"{e['latest']:.2f}s{vs}, in band {e['band_streak']} results")
    if len(out) == 1:
        out.append("nothing to raise")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    def iso_date(s):
        datetime.date.fromisoformat(s)
        return s

    ap.add_argument("data_dir", help="dir with performance_metrics.csv + run_environment.csv")
    ap.add_argument("--as-of", type=iso_date, help="replay as of this date (YYYY-MM-DD)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--cross-os", action="store_true", help="back-test only: pre-shift baseline")
    args = ap.parse_args()
    rows, env = load_data(args.data_dir)
    report = detect(rows, env, as_of=args.as_of,
                    baseline_mode="cross_os" if args.cross_os else "same_os")
    print(json.dumps(report, indent=2) if args.json else render(report))


if __name__ == "__main__":
    main()
