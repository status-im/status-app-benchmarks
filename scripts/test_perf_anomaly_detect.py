#!/usr/bin/env python3
"""Back-test for perf_anomaly_detect.py — the arming prerequisite from the 2026-07-02
threshold decision: the detector must FIRE on known-real moves and STAY SILENT on the
known-noise cases, before anything is wired to Discord or GitHub.

Run:  python3 test_perf_anomaly_detect.py <data-dir>
where <data-dir> holds performance_metrics.csv + run_environment.csv from
status-im/status-app-benchmarks master (the system of record).

Every expected set below was derived by hand from the CSV series BEFORE the detector
was written (values quoted in comments = ground truth as of the 2026-07-07 CSV).
All assertions pin as_of dates so future CSV appends cannot change outcomes. Known
residual assumption: RealHistory clips rows by date <= 2026-07-07, so a row appended
LATER but dated earlier (the CSV does this — 2959dc, the "N" re-measures) would enter
the replay; that only breaks if someone backfills a non-"N" nightly row into the past.
"""
import sys
import unittest
from pathlib import Path

import perf_anomaly_detect as pad
import perf_anomaly_shadow as shadow

DATA_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")


def surfaces(report, key):
    return {e["surface"] for e in report[key]}


def entry(report, key, surface):
    return next(e for e in report[key] if e["surface"] == surface)


def make_rows(baseline, nights, name="test_android_synth_response_time"):
    rows = [{"commit_hash": pad.GA_BASE, "date": "2026-06-01T12:00:00",
             "device": pad.GATE_DEVICE, "test_name": name,
             "metric": "response_time", "median_time": str(baseline)}]
    for i, v in enumerate(nights):
        rows.append({"commit_hash": f"syn{i:03}", "date": f"2026-06-{10 + i:02}T12:00:00",
                     "device": pad.GATE_DEVICE, "test_name": name,
                     "metric": "response_time", "median_time": str(v)})
    return rows


class SyntheticRules(unittest.TestCase):
    """Rule mechanics on fully synthetic series — pins the +15% boundary, the 3-night
    persistence window, and the sub-0.3s absolute floor."""

    def make(self, baseline, nights):
        return make_rows(baseline, nights)

    def fires(self, baseline, nights, as_of=None):
        report = pad.detect(self.make(baseline, nights), {}, as_of=as_of)
        return "test_android_synth_response_time" in surfaces(report, "regressions")

    def test_20pct_step_fires_exactly_on_third_night(self):
        nights = [0.60, 0.72, 0.72, 0.72]  # step lands 06-11; 3rd over-threshold night = 06-13
        self.assertFalse(self.fires(0.60, nights, as_of="2026-06-11"))
        self.assertFalse(self.fires(0.60, nights, as_of="2026-06-12"))
        self.assertTrue(self.fires(0.60, nights, as_of="2026-06-13"))
        report = pad.detect(self.make(0.60, nights), {}, as_of="2026-06-13")
        self.assertEqual(entry(report, "regressions", "test_android_synth_response_time")["fired"],
                         "2026-06-13")

    def test_14pct_step_never_fires(self):
        self.assertFalse(self.fires(0.60, [0.684, 0.684, 0.684, 0.684]))

    def test_exactly_15pct_does_not_fire(self):
        # fire means MORE than 15% slower, not 15% exactly
        self.assertFalse(self.fires(0.60, [0.69, 0.69, 0.69]))

    def test_two_night_blip_recovers_silently(self):
        self.assertFalse(self.fires(0.60, [0.72, 0.72, 0.60]))

    def test_two_night_blip_is_pending_not_fired(self):
        report = pad.detect(self.make(0.60, [0.72, 0.72]), {})
        self.assertIn("test_android_synth_response_time", surfaces(report, "pending"))

    def test_subfloor_pct_alone_does_not_fire(self):
        # +30% on a 0.10s baseline is a 0.03s move — below the 0.15s absolute floor
        self.assertFalse(self.fires(0.10, [0.13, 0.13, 0.13]))

    def test_subfloor_fires_when_absolute_move_clears_floor(self):
        self.assertTrue(self.fires(0.10, [0.30, 0.30, 0.30]))

    def test_band_needs_two_distinct_days_not_two_results(self):
        # The lived triage rule is "two INDEPENDENT days" >1.0s. The CSV has same-date
        # double-run days (06-19/06-22/06-26), so two same-day in-band results must not
        # count as band entry — that is the single-night spike the rule excludes.
        rows = make_rows(0.60, [1.20])
        rows.append({"commit_hash": "synX", "date": rows[-1]["date"],  # 2nd run, same day
                     "device": pad.GATE_DEVICE, "test_name": "test_android_synth_response_time",
                     "metric": "response_time", "median_time": "1.25"})
        report = pad.detect(rows, {})
        self.assertNotIn("test_android_synth_response_time", surfaces(report, "slow_band"))
        self.assertIn("test_android_synth_response_time", surfaces(report, "watch"))

    def test_detect_reports_evaluated_surfaces(self):
        report = pad.detect(self.make(0.60, [0.61]), {})
        self.assertEqual(report["surfaces"], ["test_android_synth_response_time"])
        report = pad.detect([], {})
        self.assertEqual(report["surfaces"], [])


class RealHistory(unittest.TestCase):
    """Replays against the real benchmarks CSV, pinned to as_of dates."""

    @classmethod
    def setUpClass(cls):
        cls.rows, cls.env = pad.load_data(DATA_DIR)

    def detect(self, as_of, baseline_mode="same_os", extra_rows=(), extra_env=()):
        rows = [r for r in self.rows if r["date"][:10] <= "2026-07-07"] + list(extra_rows)
        env = dict(self.env, **dict(extra_env))
        return pad.detect(rows, env, as_of=as_of, baseline_mode=baseline_mode)

    # ── MUST FIRE ────────────────────────────────────────────────────────────────

    def test_os_shift_fires_when_compared_cross_os(self):
        # The real Android-16 shift moved surfaces +9..+30% vs the pre-Android-16
        # 2.38.0 baseline. Sustained carriers as-of 06-29: settings_language 0.524→
        # 0.614/0.615/0.627 (+17..20%) and settings_browser 0.540→0.664/0.633/0.642
        # (+17..23%) — every Android-16 night over. Settings and wallet hover around the
        # +15% line, so they fire transiently: settings at 06-22 (ff50da/5b1794/
        # 962c77 all +19..23%), wallet at 06-25 (c32b3c/f016ed/4283ab +15.4/+17.1/
        # +17.4%); by 06-29 each has a sub-15% night in its trailing window
        # (settings 06cc48 +14.3%, wallet 6efd31 +14.7%).
        report = self.detect("2026-06-29", baseline_mode="cross_os")
        self.assertLessEqual({"test_android_settings_language_response_time",
                              "test_android_settings_browser_response_time"},
                             surfaces(report, "regressions"))
        self.assertNotIn("test_android_settings_response_time", surfaces(report, "regressions"))

        settings_peak = self.detect("2026-06-22", baseline_mode="cross_os")
        self.assertEqual(entry(settings_peak, "regressions",
                               "test_android_settings_response_time")["fired"], "2026-06-22")
        wallet_peak = self.detect("2026-06-25", baseline_mode="cross_os")
        self.assertEqual(entry(wallet_peak, "regressions",
                               "test_android_wallet_response_time")["fired"], "2026-06-25")

    def test_os_shift_absorbed_by_same_os_baseline(self):
        # Same window, production mode: the same-OS baseline (5f66deN) absorbs the
        # OS shift — zero hard fires up to 06-29 (settings' real move starts 06-30).
        report = self.detect("2026-06-29")
        self.assertEqual(surfaces(report, "regressions"), set())

    def test_send_swap_fire_exactly_on_third_slow_night(self):
        # CSV has ONE slow nightly point (07-05: send 1.097, swap 1.320). The 07-07
        # confirmation was a manual re-measure that never entered the CSV, so today the
        # 3-night rule legitimately has NOT fired. Appending the known-real 07-07 values
        # (send 1.081, swap 1.100) plus one synthetic third night must fire it exactly
        # on that third night. Baselines (5f66deN): send 0.690, swap 0.663 → all +50%+.
        extra = []
        for name, v77, v78 in (("test_android_wallet_send_response_time", 1.081, 1.09),
                               ("test_android_wallet_swap_response_time", 1.100, 1.11)):
            extra.append({"commit_hash": "da0988", "date": "2026-07-07T12:00:00",
                          "device": pad.GATE_DEVICE, "test_name": name,
                          "metric": "response_time", "median_time": str(v77)})
            extra.append({"commit_hash": "syn3rd", "date": "2026-07-08T12:00:00",
                          "device": pad.GATE_DEVICE, "test_name": name,
                          "metric": "response_time", "median_time": str(v78)})
        send_swap = {"test_android_wallet_send_response_time",
                     "test_android_wallet_swap_response_time"}

        real_today = self.detect("2026-07-07")
        self.assertFalse(send_swap & surfaces(real_today, "regressions"))

        aug = lambda as_of: self.detect(as_of, extra_rows=extra, extra_env=[("syn3rd", "16")])
        self.assertFalse(send_swap & surfaces(aug("2026-07-07"), "regressions"))  # 2 nights: still silent
        fired = aug("2026-07-08")
        self.assertLessEqual(send_swap, surfaces(fired, "regressions"))
        for s in send_swap:
            self.assertEqual(entry(fired, "regressions", s)["fired"], "2026-07-08")

    def test_send_swap_enter_slow_band_on_second_independent_day(self):
        # Detector B mirrors the manual triage that produced status-app#21429: Send/Swap
        # were placed in the band on exactly two independent days >1.0s (07-05 + 07-07).
        extra = [{"commit_hash": "da0988", "date": "2026-07-07T12:00:00",
                  "device": pad.GATE_DEVICE, "test_name": name,
                  "metric": "response_time", "median_time": str(v)}
                 for name, v in (("test_android_wallet_send_response_time", 1.081),
                                 ("test_android_wallet_swap_response_time", 1.100))]
        report = self.detect("2026-07-07", extra_rows=extra)
        self.assertLessEqual({"test_android_wallet_send_response_time",
                              "test_android_wallet_swap_response_time"},
                             surfaces(report, "slow_band"))

    def test_todays_real_regressions_are_settings_and_wallet(self):
        # The rule's genuine output on today's CSV — both correspond to real, known moves:
        #  - settings: 0.635 baseline → 1.167/1.190/1.100/0.971/0.971 (06-30→07-07),
        #    5 nights ≥ +53%; fired 07-02 (3rd night). Still +53% today.
        #  - wallet:   1.212 baseline → 1.417/1.496/1.532 (07-02→07-07), fired 07-07
        #    (the known wallet-tab slow-mode thread).
        report = self.detect("2026-07-07")
        self.assertEqual(surfaces(report, "regressions"),
                         {"test_android_settings_response_time",
                          "test_android_wallet_response_time"})
        self.assertEqual(entry(report, "regressions", "test_android_settings_response_time")["fired"],
                         "2026-07-02")
        self.assertEqual(entry(report, "regressions", "test_android_wallet_response_time")["fired"],
                         "2026-07-07")

    def test_todays_slow_band_membership(self):
        # Matches the #21429 categorisation computed from the CSV alone: wallet steady
        # >1.0s across all 22 nights; the first/cold-open set sustained in-band.
        report = self.detect("2026-07-07")
        self.assertEqual(surfaces(report, "slow_band"),
                         {"test_android_wallet_response_time",
                          "test_android_settings_cold_open",
                          "test_android_settings_first_open",
                          "test_android_messages_first_open",
                          "test_android_communities_first_open",
                          "test_android_market_first_open"})

    # ── MUST STAY SILENT ─────────────────────────────────────────────────────────

    def test_wallet_first_open_single_night_blip_silent(self):
        # 07-05 spiked to 1.150 (baseline 0.621); the 07-07 re-measure read 0.52.
        # One night → neither detector fires; it sits on the watch list only.
        report = self.detect("2026-07-07")
        self.assertNotIn("test_android_wallet_first_open", surfaces(report, "regressions"))
        self.assertNotIn("test_android_wallet_first_open", surfaces(report, "slow_band"))
        self.assertIn("test_android_wallet_first_open", surfaces(report, "watch"))

    def test_settings_hovering_at_the_band_line_silent_today(self):
        # Settings tab: 1.167/1.190/1.100 then 0.971/0.971 — left the band on the last
        # two nightlies, so today's B output must not list it (hard or watch).
        report = self.detect("2026-07-07")
        self.assertNotIn("test_android_settings_response_time", surfaces(report, "slow_band"))
        self.assertNotIn("test_android_settings_response_time", surfaces(report, "watch"))

    def test_excluded_surfaces_never_hard_fire_on_any_night(self):
        # Market (bimodal ~0.5–1.1s, +45..89% swings vs baseline) and the networked
        # Communities surfaces move grossly all through the history; they must be
        # soft-notes on every single replay night, never a hard alert of either kind.
        dates = sorted({r["date"][:10] for r in self.rows if r["date"][:10] <= "2026-07-07"})
        for d in dates:
            report = self.detect(d)
            hard = surfaces(report, "regressions") | surfaces(report, "slow_band") | surfaces(report, "watch")
            self.assertFalse(pad.EXCLUDED & hard, f"excluded surface fired hard on {d}: {pad.EXCLUDED & hard}")

    def test_todays_soft_notes_and_watch(self):
        report = self.detect("2026-07-07")
        self.assertEqual(surfaces(report, "soft_notes"), pad.EXCLUDED)
        self.assertEqual(surfaces(report, "watch"),
                         {"test_android_wallet_send_response_time",
                          "test_android_wallet_swap_response_time",
                          "test_android_wallet_first_open",
                          "test_android_market_cold_open",
                          "test_android_communities_cold_open"})

    def test_stale_findings_are_tagged(self):
        # Newest CSV data is 07-07; communities/market first-open were last measured
        # 06-29 (8 days — stale), messages_first_open 07-05 (2 days — fresh).
        report = self.detect("2026-07-07")
        self.assertTrue(entry(report, "slow_band", "test_android_communities_first_open")["stale"])
        self.assertTrue(entry(report, "slow_band", "test_android_market_first_open")["stale"])
        self.assertFalse(entry(report, "slow_band", "test_android_messages_first_open")["stale"])

    def test_missing_run_environment_hard_fails(self):
        # Without run_environment.csv every build silently reads as pre-Android-16,
        # the wrong-OS baseline wins, and the report emits cross-OS regressions
        # labelled "same-OS". A required input, not optional enrichment.
        import tempfile, shutil
        with tempfile.TemporaryDirectory() as d:
            shutil.copy(DATA_DIR / "performance_metrics.csv", d)
            with self.assertRaises(SystemExit):
                pad.load_data(d)


class ShadowThrottle(unittest.TestCase):
    """Discord shadow-mode throttling: post on first detection and on state change
    (new finding / recovery), NEVER a nightly "still broken" repeat — the design's
    anti-rot rule. Identity is (kind, surface), so night-to-night median wiggles on
    an already-reported finding do not re-post."""

    def report_with(self, regression=False, band=False, band_healthy=False):
        rows = []
        if regression:   # 3 sustained +20% nights on a 0.60s baseline
            rows += make_rows(0.60, [0.72, 0.72, 0.72], name="test_android_synth_response_time")
        if band:         # 2 consecutive nights above 1.0s
            rows += make_rows(0.60, [1.20, 1.20], name="test_android_synth2_response_time")
        if band_healthy:  # same surface measured again, back under the band
            rows += make_rows(0.60, [1.20, 1.20, 0.80], name="test_android_synth2_response_time")
        return pad.detect(rows, {})

    def test_first_detection_posts_everything(self):
        report = self.report_with(regression=True, band=True)
        entries = shadow.current_entries(report)
        self.assertEqual(set(entries), {"regression:test_android_synth_response_time",
                                        "slow_band:test_android_synth2_response_time"})
        msg, _ = shadow.evaluate(report, set())
        self.assertIn("WOULD FILE", msg)
        self.assertIn("Synth", msg)
        self.assertIn("Synth2", msg)

    def test_unchanged_state_is_silent(self):
        report = self.report_with(regression=True)
        prev = set(shadow.current_entries(report))
        msg, state = shadow.evaluate(report, prev)
        self.assertIsNone(msg)
        self.assertEqual(state, prev)

    def test_only_the_new_finding_posts(self):
        prev = set(shadow.current_entries(self.report_with(regression=True)))
        report = self.report_with(regression=True, band=True)
        msg, _ = shadow.evaluate(report, prev)
        self.assertIn("Synth2", msg)
        self.assertNotIn("WOULD FILE (regression): Synth —", msg)  # continuing item not repeated
        self.assertIn("1 continuing", msg)

    def test_recovery_posts_once_with_pretty_name(self):
        prev = set(shadow.current_entries(self.report_with(regression=True, band=True)))
        report = self.report_with(regression=True, band_healthy=True)  # synth2 re-measured, healthy
        msg, state = shadow.evaluate(report, prev)
        self.assertIn("recovered", msg)
        self.assertIn("Synth2", msg)
        self.assertNotIn("test_android_synth2_response_time", msg)  # pretty names, not raw keys
        self.assertNotIn("slow_band:test_android_synth2_response_time", state)

    def test_unmeasured_surface_never_recovers(self):
        # A truncated CSV / surface dropped from the nightly set is NOT a recovery —
        # false all-clears would poison the shadow audit. The finding carries forward
        # silently until the surface is actually measured again.
        prev = set(shadow.current_entries(self.report_with(regression=True, band=True)))
        report = self.report_with(regression=True)   # synth2 absent from the data entirely
        msg, state = shadow.evaluate(report, prev)
        self.assertIsNone(msg)
        self.assertEqual(state, prev)   # carried forward, not dropped

    def test_empty_report_aborts_instead_of_recovering_everything(self):
        prev = {"regression:test_android_synth_response_time"}
        with self.assertRaises(SystemExit):
            shadow.evaluate(pad.detect([], {}), prev)

    def test_state_roundtrip(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            state = Path(d) / "state.json"
            self.assertEqual(shadow.load_state(state), set())
            shadow.save_state(state, {"regression:x", "slow_band:y"})
            self.assertEqual(shadow.load_state(state), {"regression:x", "slow_band:y"})

    def test_load_state_rejects_malformed_shapes(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            state = Path(d) / "state.json"
            for bad in ('{"keys": 5}', '{"keys": "abc"}', "not json", "[]"):
                state.write_text(bad)
                self.assertEqual(shadow.load_state(state), set(), f"shape: {bad!r}")


if __name__ == "__main__":
    if not (DATA_DIR / "performance_metrics.csv").exists():
        sys.exit(f"usage: {sys.argv[0]} <dir with performance_metrics.csv + run_environment.csv>")
    unittest.main(argv=[sys.argv[0]], verbosity=2)
