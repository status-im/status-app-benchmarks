import sys
import unittest
from pathlib import Path

import pandas as pd

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))

import android_perf_publish as app  # noqa: E402
import benchmark_mobile as b  # noqa: E402


def name(short):
    return 'test_android_%s_response_time' % short


ALL = ['wallet', 'wallet_send', 'wallet_swap', 'wallet_receive', 'wallet_buy', 'messages',
       'market', 'communities', 'settings', 'activity_center', 'home']
OS_NEW, OS_OLD = 'os-new', 'os-old'


class Store:
    """A small performance_metrics frame plus the run-environment and label maps the card reads."""

    def __init__(self):
        self.rows, self.env, self.labels = [], {}, {}

    def build(self, hash_, date, values, os=OS_NEW, label=None, device=b.GATE_DEVICE, runs=6):
        for short, median in values.items():
            self.rows.append({'commit_hash': hash_, 'date': pd.Timestamp(date), 'device': device,
                              'test_name': name(short), 'metric': 'response_time',
                              'median_time': median, 'run_count': runs})
        if os is not None:
            self.env[hash_] = os
        self.labels[hash_] = label if label is not None else '%s\nnightly · %s' % (date, hash_)
        return self

    def card(self, shipped=('2.38.2',)):
        perf = pd.DataFrame(self.rows)
        card, rows = app._scorecard(perf, self.env, self.labels,
                                    list(shipped) if shipped is not None else None)
        return card, {r[0]: r for r in rows}


def full(value=0.65, **over):
    v = {s: value for s in ALL}
    v.update(over)
    return v


def verdict(rows, disp):
    return rows[disp][2][0]


class ResolutionVerdicts(unittest.TestCase):
    """Item 4: a change smaller than one timer step is never called a change."""

    def card(self, base_value, new_value):
        s = Store()
        s.build('ga0001', '2026-07-20', full(wallet=base_value), label='2.38.2')
        s.build('abc123', '2026-09-29', full(wallet=new_value))
        return s.card()[1]

    def test_a_few_percent_is_within_resolution(self):
        rows = self.card(0.65, 0.70)                 # +8%: the old card called this a change or parity
        self.assertEqual(verdict(rows, 'Wallet'), "no measurable change")
        self.assertEqual(rows['Wallet'][2][1], app.GREY)
        self.assertEqual(rows['Wallet'][1], '0.65s → 0.70s')

    def test_less_than_a_step_is_within_resolution(self):
        self.assertEqual(verdict(self.card(0.65, 1.05), 'Wallet'), "no measurable change")

    def test_one_step_slower_is_shown(self):
        self.assertEqual(verdict(self.card(0.65, 1.20), 'Wallet'), '▲ +0.55s slower')

    def test_one_step_faster_is_shown(self):
        rows = self.card(1.15, 0.65)                 # steps measure 0.50–0.56 s, so 0.50 is a whole step
        self.assertEqual(verdict(rows, 'Wallet'), '▼ −0.50s faster')
        self.assertEqual(rows['Wallet'][2][1], app.GREEN)

    def test_speed_band_stays_coloured_when_within_resolution(self):
        rows = self.card(0.65, 0.70)
        self.assertEqual(rows['Wallet'][3], ('ok', app.BLUE))


class BelowResolution(unittest.TestCase):
    """Item 5: surfaces that were in the lowest bin on every recent run are greyed, not removed."""

    def test_lowest_bin_surface_is_greyed_and_kept(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(home=0.10), label='2.38.2')
        s.build('aaa111', '2026-09-20', full(home=0.09))
        s.build('abc123', '2026-09-29', full(home=0.093))
        rows = s.card()[1]
        self.assertEqual(verdict(rows, 'Home'), "too fast to time")
        self.assertEqual(rows['Home'][1], '0.10s → 0.09s')
        self.assertEqual(rows['Home'][3], ('fast', app.GREY))
        self.assertEqual(len(rows), len(app.SCORECARD_SURFACES))

    def test_one_higher_reading_in_the_window_keeps_the_comparison(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(home=0.10), label='2.38.2')
        s.build('aaa111', '2026-09-20', full(home=0.378))   # a half-step median: some runs missed the first screenshot
        s.build('abc123', '2026-09-29', full(home=0.093))
        self.assertEqual(verdict(s.card()[1], 'Home'), "no measurable change")

    def test_readings_older_than_the_window_do_not_count(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(home=0.10), label='2.38.2')
        s.build('old111', '2026-09-01', full(home=0.65))    # 28 days before the card's build
        s.build('abc123', '2026-09-29', full(home=0.093))
        self.assertEqual(verdict(s.card()[1], 'Home'), "too fast to time")

    def test_card_reading_out_of_the_lowest_bin_is_never_hidden(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(home=0.10), label='2.38.2')
        s.build('aaa111', '2026-09-25', full(home=0.09))
        s.build('abc123', '2026-09-29', full(home=0.65))
        self.assertEqual(verdict(s.card()[1], 'Home'), '▲ +0.55s slower')


    def test_a_large_improvement_from_the_release_is_not_hidden(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(home=1.20), label='2.38.2')
        s.build('aaa111', '2026-09-20', full(home=0.10))
        s.build('abc123', '2026-09-29', full(home=0.09))
        self.assertEqual(verdict(s.card()[1], 'Home'), '▼ −1.11s faster')

    def test_no_baseline_still_greys_a_lowest_bin_surface(self):
        s = Store()
        s.build('abc123', '2026-09-29', full(home=0.09))
        self.assertEqual(verdict(s.card()[1], 'Home'), "too fast to time")


class OneBuildPerCard(unittest.TestCase):
    """Item 6: every row is from one build; a gap says so instead of borrowing another build's value."""

    def test_unmeasured_surface_does_not_borrow_an_older_value(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(), label='2.38.2')
        s.build('aaa111', '2026-09-25', full(market=0.63))
        s.build('abc123', '2026-09-29', {k: 0.65 for k in ALL if k not in ('market', 'communities')})
        card, rows = s.card()
        self.assertEqual(card['build'], 'abc123')
        self.assertEqual(rows['Market'][1:], ('—', ('not measured on this build', app.GREY), ('', app.GREY)))
        self.assertEqual(verdict(rows, 'Communities'), 'not measured on this build')

    def test_a_build_that_ran_only_a_few_surfaces_is_not_the_card(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(), label='2.38.2')
        s.build('aaa111', '2026-09-25', full())
        s.build('adhoc1', '2026-09-30', {'wallet': 0.65, 'settings': 0.65, 'home': 0.1})
        self.assertEqual(s.card()[0]['build'], 'aaa111')

    def test_an_old_release_remeasured_on_a_new_os_is_not_the_card(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(), os=OS_OLD, label='2.38.2')
        s.build('aaa111', '2026-09-25', full())
        s.build('ga0001N', '2026-09-28', full(), label='2026-09-28\n2.38.2·ZG1')
        card = s.card()[0]
        self.assertEqual(card['build'], 'aaa111')
        self.assertEqual(card['base'], 'ga0001N')

    def test_same_day_tie_goes_to_the_build_appended_last(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(), label='2.38.2')
        s.build('first1', '2026-09-29', full())
        s.build('second', '2026-09-29', full())
        self.assertEqual(s.card()[0]['build'], 'second')

    def test_no_qualifying_build(self):
        s = Store()
        s.build('adhoc1', '2026-09-30', {'wallet': 0.65})
        card, rows = s.card()
        self.assertIsNone(card['build'])
        self.assertTrue(all(r[2][0] == 'no data' for r in rows.values()))


class GaBaseline(unittest.TestCase):
    """Item 7: the baseline is the newest shipped release the gate phone measured on its current OS."""

    def test_shipped_releases_skip_drafts_and_prereleases(self):
        api = [
            {'tag_name': '2.39.0-rc.7', 'draft': False, 'prerelease': True, 'published_at': '2026-09-29T21:59:03Z'},
            {'tag_name': '2.38.1', 'draft': False, 'prerelease': False, 'published_at': '2026-06-19T23:43:37Z'},
            {'tag_name': '2.38.2', 'draft': False, 'prerelease': False, 'published_at': '2026-07-21T09:08:29Z'},
            {'tag_name': '2.40.0', 'draft': True, 'prerelease': False, 'published_at': None},
        ]
        self.assertEqual(app._shipped_from_api(api), ['2.38.2', '2.38.1'])

    def test_release_name_from_label(self):
        self.assertEqual(app._release_name('2026-06-16\n2.38.0 · 5f66de'), '2.38.0')
        self.assertEqual(app._release_name('2026-08-30|2.38.2·ZG1'), '2.38.2')
        self.assertEqual(app._release_name('2.38.2'), '2.38.2')
        self.assertEqual(app._release_name('2026-09-29\n2.39.0-rc.7 · a4a0c3'), '2.39.0-rc.7')

    def test_newest_release_with_same_os_data_is_used(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(wallet=1.15), label='2.38.2')
        s.build('abc123', '2026-09-29', full(wallet=0.65))
        card, rows = s.card(shipped=['2.38.2', '2.38.1'])
        self.assertEqual((card['base'], card['base_name']), ('ga0001', '2.38.2'))
        self.assertIn('newest shipped release on GitHub', card['base_why'])
        self.assertEqual(rows['Wallet'][1], '1.15s → 0.65s')

    def test_newest_release_without_same_os_data_falls_back(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(), label='2.38.2')
        s.build('ga0002', '2026-10-05', full(), os=OS_OLD, label='2026-10-05\n2.39.0 · ga0002')
        s.build('abc123', '2026-10-08', full())
        card = s.card(shipped=['2.39.0', '2.38.2'])[0]
        self.assertEqual((card['base'], card['base_name']), ('ga0001', '2.38.2'))
        self.assertIn('2.39.0, has no data from this phone on its current firmware', card['base_why'])

    def test_newest_release_not_measured_at_all_falls_back(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(), label='2.38.2')
        s.build('abc123', '2026-10-08', full())
        card = s.card(shipped=['2.39.0', '2.38.2'])[0]
        self.assertEqual(card['base_name'], '2.38.2')

    def test_prefers_the_same_os_remeasure_of_a_release(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(wallet=1.30), os=OS_OLD, label='2.38.2')
        s.build('ga0001N', '2026-08-30', full(wallet=1.16), label='2026-08-30\n2.38.2·ZG1')
        s.build('abc123', '2026-09-29', full(wallet=1.11))
        card, rows = s.card()
        self.assertEqual(card['base'], 'ga0001N')
        self.assertEqual(rows['Wallet'][1], '1.16s → 1.11s')

    def test_no_release_on_the_current_os_means_no_baseline(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(), os=OS_OLD, label='2.38.2')
        s.build('abc123', '2026-09-29', full())
        card, rows = s.card()
        self.assertIsNone(card['base'])
        self.assertEqual(verdict(rows, 'Wallet'), 'no baseline')
        self.assertEqual(rows['Wallet'][1], '— → 0.65s')

    def test_card_build_without_recorded_firmware_gets_no_baseline(self):
        s = Store()
        s.build('ga0000', '2026-06-16', full(), os=None, label='2026-06-16\n2.38.0 · ga0000')
        s.build('ga0001', '2026-07-20', full(), label='2.38.2')
        s.build('abc123', '2026-09-29', full(), os=None)
        card, rows = s.card(shipped=['2.38.2', '2.38.0'])
        self.assertIsNone(card['base'])
        self.assertIn('no recorded firmware', card['base_why'])
        self.assertEqual(verdict(rows, 'Wallet'), 'no baseline')

    def test_release_without_recorded_firmware_is_never_the_baseline(self):
        s = Store()
        s.build('ga0000', '2026-06-16', full(), os=None, label='2026-06-16\n2.38.0 · ga0000')
        s.build('abc123', '2026-09-29', full())
        self.assertIsNone(s.card(shipped=['2.38.0'])[0]['base'])

    def test_settings_is_redefined_against_a_release_before_the_route_change(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(settings=0.65), label='2.38.2')
        s.build('abc123', '2026-09-29', full(settings=1.20))
        self.assertEqual(verdict(s.card()[1], 'Settings'), 'redefined')

    def test_settings_compares_once_the_baseline_has_the_new_route(self):
        s = Store()
        s.build('ga0002', '2026-10-05', full(settings=0.65), label='2026-10-05\n2.39.0 · ga0002')
        s.build('abc123', '2026-10-08', full(settings=1.20))
        self.assertEqual(verdict(s.card(shipped=['2.39.0'])[1], 'Settings'), '▲ +0.55s slower')

    def test_github_unreachable_uses_release_names_from_labels(self):
        s = Store()
        s.build('ga0000', '2026-06-19', full(), label='2026-06-19\n2.38.1 · ga0000')
        s.build('ga0001', '2026-07-20', full(), label='2.38.2')
        s.build('rc0007', '2026-09-28', full(), label='2026-09-28\n2.39.0-rc.7 · rc0007')
        s.build('abc123', '2026-09-29', full())
        card = s.card(shipped=None)[0]
        self.assertEqual(card['base_name'], '2.38.2')
        self.assertIn('GitHub could not be reached', card['base_why'])

    def test_card_build_is_not_its_own_baseline(self):
        s = Store()
        s.build('ga0001', '2026-07-20', full(wallet=1.15), label='2.38.2')
        s.build('ga0002', '2026-10-05', full(wallet=0.65), label='2026-10-05\n2.39.0 · ga0002')
        card, rows = s.card(shipped=['2.39.0', '2.38.2'])
        self.assertEqual(card['build'], 'ga0002')
        self.assertEqual(card['base_name'], '2.38.2')
        self.assertEqual(verdict(rows, 'Wallet'), '▼ −0.50s faster')


if __name__ == '__main__':
    unittest.main()
