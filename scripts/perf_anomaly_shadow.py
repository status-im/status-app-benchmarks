#!/usr/bin/env python3
"""Discord shadow mode for the perf anomaly detector (stage 2 — P2 in the 2026-07-06
design). Posts "WOULD FILE: …" messages to the perf alert webhook so the team audits
the detector live for 1–2 weeks BEFORE any GitHub issue creation is armed. This script
never touches the GitHub API.

Throttle (design §5b): post on first detection and on state change — a new finding or
a recovery — never a nightly "still broken" repeat. Finding identity is (kind, surface),
kept in a small JSON state file between runs. A finding only "recovers" when its surface
was actually measured this run and is healthy; a surface missing from the data (truncated
CSV, dropped from the nightly set) carries forward silently — never a false all-clear.

Usage: perf_anomaly_shadow.py <data-dir> --state <file> [--post]
Dry-run by default: prints the exact message (or "silent") and updates no state.
--post sends to $PERF_ALERT_WEBHOOK (same env as perf-nightly.sh's alert()) and saves
state only after a successful POST (at-least-once delivery).
"""
import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

import perf_anomaly_detect as pad

DISCORD_MAX = 1900   # Discord rejects content >2000 chars; leave headroom


def current_entries(report):
    """{'kind:surface': display line} for the hard would-file findings only."""
    entries = {}
    for e in report["regressions"]:
        last = e["nights"][-1]
        entries[f"regression:{e['surface']}"] = (
            f"🔴 WOULD FILE (regression): {pad.prettify(e['surface'])} — "
            f"{e['baseline']:.2f}s → {last['median']:.2f}s ({last['pct']:+.0f}%) "
            f"vs same-OS baseline, {e['streak']} nights sustained")
    for e in report["slow_band"]:
        stale = " — STALE" if e.get("stale") else ""
        entries[f"slow_band:{e['surface']}"] = (
            f"🟠 WOULD FILE (slow band): {pad.prettify(e['surface'])} — "
            f"{e['latest']:.2f}s, >1.0s for {e['days']} days since {e['entered']} "
            f"(last measured {e['last_measured']}{stale})")
    return entries


def evaluate(report, prev_keys):
    """(message | None, next_state). SystemExit on an empty report — zero measured
    surfaces means broken input, and 'recovering' every open finding off the back of
    a truncated CSV is the worst possible shadow output."""
    if not report["surfaces"]:
        sys.exit("shadow: report contains zero measured surfaces — refusing to evaluate")
    measured = set(report["surfaces"])
    entries = current_entries(report)
    unmeasured = {k for k in prev_keys - set(entries)
                  if k.split(":", 1)[1] not in measured}   # carry forward, no post
    new = sorted(k for k in entries if k not in prev_keys)
    recovered = sorted(prev_keys - set(entries) - unmeasured)
    next_state = set(entries) | unmeasured

    if not new and not recovered:
        return None, next_state
    lines = ["**perf anomaly detector — shadow mode (nothing is filed)**"]
    lines += [entries[k] for k in new]
    for k in recovered:
        kind, surface = k.split(":", 1)
        lines.append(f"🟢 recovered: {pad.prettify(surface)} ({kind.replace('_', ' ')})")
    continuing = len(entries) - len(new)
    if continuing:
        lines.append(f"({continuing} continuing finding(s) not repeated)")
    return "\n".join(lines), next_state


def load_state(path):
    try:
        keys = json.loads(Path(path).read_text())["keys"]
        return set(keys) if (isinstance(keys, list)
                             and all(isinstance(k, str) for k in keys)) else set()
    except (OSError, ValueError, KeyError, TypeError):
        return set()


def save_state(path, keys):
    path = Path(path)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps({"keys": sorted(keys)}, indent=1))
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("data_dir")
    ap.add_argument("--state", required=True, help="JSON state file for the throttle")
    ap.add_argument("--post", action="store_true",
                    help="actually POST to $PERF_ALERT_WEBHOOK and save state")
    args = ap.parse_args()

    rows, env = pad.load_data(args.data_dir)
    msg, next_state = evaluate(pad.detect(rows, env), load_state(args.state))

    if msg is None:
        print("shadow: no state change — silent")
        return
    if len(msg) > DISCORD_MAX:
        msg = msg[:DISCORD_MAX] + "\n… (truncated)"
    if not args.post:
        print("shadow DRY-RUN — would post:\n" + msg)
        return
    webhook = os.environ.get("PERF_ALERT_WEBHOOK")
    if not webhook:
        sys.exit("shadow: --post but PERF_ALERT_WEBHOOK is not set")
    req = urllib.request.Request(webhook, method="POST",
                                 data=json.dumps({"content": msg}).encode(),
                                 headers={"Content-Type": "application/json",
                                          # Discord 403s urllib's default User-Agent
                                          "User-Agent": "perf-nightly-bot/1.0"})
    try:
        urllib.request.urlopen(req, timeout=30)
    except OSError as e:   # state NOT saved -> re-posts next run (at-least-once)
        sys.exit(f"shadow: webhook POST failed ({e}) — state unchanged")
    save_state(args.state, next_state)
    print("shadow: posted\n" + msg)


if __name__ == "__main__":
    main()
