# Android — navigation response time

How quickly the Android app reacts when you tap to switch screens — for example,
tap **Wallet** and time until the Wallet screen is drawn. Tracked across builds so we
can see whether performance improves or regresses.

- **Lower is better.** Most points are the **mean of 6 runs** on a **fresh account**
  (Samsung A36); charts that work differently (single cold samples, screens faster
  than the measurement floor) say so in their footnotes.
- Measured with a screenshot/pixel timer that reads the screen directly — the Qt UI's
  accessibility tree is unreliable for timing, so we don't rely on it.
- The screenshot round-trip bounds resolution to roughly **0.45 s**: anything faster
  shows up as a small near-constant value and should be read as "within one frame",
  not as a precise latency.
- Charts show the most recent builds; the x-axis is labelled by build
  (date · version/rc · short hash). Full history lives in
  [`data/android/`](../../data/android/).

## Navigation tabs

![Wallet navigation response time](./android_wallet_response_time.png)
![Settings navigation response time](./android_settings_response_time.png)
![Messages navigation response time](./android_messages_response_time.png)

> Messages arrives faster than our ~0.45 s screenshot floor, so its chart shows the
> **fastest of 6** rather than the mean (the mean would be misleading).

![Market navigation response time](./android_market_response_time.png)
![Communities navigation response time](./android_communities_response_time.png)

## First open

The session's *first* open of a screen includes one-time content construction, so it
is tracked separately from the warm navigation trend above. Each point is a
**single cold sample** — a session only has one first open. (It is not always slower
than warm navigation; Wallet's first open lands close to its warm time.)

![Wallet first open](./android_wallet_first_open.png)
![Messages first open](./android_messages_first_open.png)
![Settings first open](./android_settings_first_open.png)
![Market first open](./android_market_first_open.png)
![Communities first open](./android_communities_first_open.png)

## Settings sub-screens

Time from tapping an entry inside Settings until that screen is drawn. Every entry
on the Settings list is covered except **Wallet** (its measurement fails
consistently and is being investigated separately), **Sign out & Quit**
(destructive) and the backup banner (an action, not a screen).

> From the 2.38.0-rc.8 build onward these measurements confirm the *identity* of the
> arrived screen against a calibrated title region. Earlier points timed arrival
> correctly but used a weaker check that could not distinguish one sub-screen from
> another.

![Settings Profile response time](./android_settings_profile_response_time.png)
![Settings Password response time](./android_settings_password_response_time.png)
![Settings Messaging response time](./android_settings_messaging_response_time.png)
![Settings ENS usernames response time](./android_settings_ens_response_time.png)
![Settings Appearance response time](./android_settings_appearance_response_time.png)
![Settings Language & Currency response time](./android_settings_language_response_time.png)
![Settings Notifications response time](./android_settings_notifications_response_time.png)
![Settings Syncing response time](./android_settings_syncing_response_time.png)
![Settings Browser response time](./android_settings_browser_response_time.png)
![Settings Advanced response time](./android_settings_advanced_response_time.png)
![Settings About response time](./android_settings_about_response_time.png)
![Settings Communities response time](./android_settings_communities_response_time.png)
![Settings Keycard response time](./android_settings_keycard_response_time.png)
![Settings Privacy and security response time](./android_settings_privacy_response_time.png)
![Settings On-device backup response time](./android_settings_backup_response_time.png)

## Wallet actions

Time from tapping an action in the account view until its sheet/flow is drawn. The
action is opened once unmeasured first, so the samples reflect steady-state use.

![Wallet Receive response time](./android_wallet_receive_response_time.png)
![Wallet Send response time](./android_wallet_send_response_time.png)
![Wallet Swap response time](./android_wallet_swap_response_time.png)
![Wallet Buy response time](./android_wallet_buy_response_time.png)

> Receive and Buy open faster than the ~0.45 s floor, so their charts show the
> **fastest of 6** and should be read as "within one frame".

## Wallet accounts

Opening an account is measured as a **single cold sample** (repeat opens hit the
cached view and drop below the floor); adding an account is a normal 6-run mean.

![Wallet account open response time](./android_wallet_account_open_response_time.png)
![Wallet Add account response time](./android_wallet_add_account_response_time.png)

---

Generated by `scripts/benchmark.py` (the mobile chart path) from `data/android/`,
refreshed per release-candidate build. The desktop benchmarks and their charts are
unchanged — see the [repository README](../../README.md).
