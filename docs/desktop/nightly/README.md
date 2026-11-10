# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Nov 10, 2026 · [`f4a17a0fe`](https://github.com/status-im/status-app/commit/f4a17a0feb3480c398763cff40b5105d6b45732c)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.868s | 1.428s | 1.863s | f4a17a0fe | 2026-11-10 |
| a 5-image album in a 3-person group | 3.750s | 4.322s | 4.868s | f4a17a0fe | 2026-11-10 |
| a GIF in a 3-person group | 0.463s | 0.957s | 1.365s | f4a17a0fe | 2026-11-10 |
| 10 texts with 0.5s delay in a 3-person group | 0.679s | 1.199s | 4.001s | f4a17a0fe | 2026-11-10 |
| 1000-character text in a 1-on-1 chat | 0.623s | 1.010s | 3.227s | f4a17a0fe | 2026-11-10 |
| a 5-image album in a 1-on-1 chat | 3.857s | 4.435s | 5.057s | f4a17a0fe | 2026-11-10 |
| a GIF in a 1-on-1 chat | 0.524s | 0.960s | 1.425s | f4a17a0fe | 2026-11-10 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.709s | 1.308s | 3.800s | f4a17a0fe | 2026-11-10 |
| 1000-character text in a community #general channel | 0.559s | 0.907s | 7.529s | f4a17a0fe | 2026-11-10 |
| a 5-image album in a community #general channel | 3.669s | 4.380s | 9.827s | f4a17a0fe | 2026-11-10 |
| a GIF in a community #general channel | 0.545s | 1.325s | 3.265s | f4a17a0fe | 2026-11-10 |
| 10 texts with 0.5s delay in a community #general channel | 1.175s | 2.321s | 5.273s | f4a17a0fe | 2026-11-10 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.544s · Ok | +0.172s slower | 22.4% | 557.8 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.353s · Fast | parity | 49.2% | 584.9 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.149s · Fast | parity | 56.1% | 555.7 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.437s · Fast | -0.174s faster | 57.0% | 619.7 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.395s · Fast | parity | 44.5% | 610.8 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.421s · Fast | parity | 63.7% | 580.1 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.310s · Fast | parity | 36.2% | 594.3 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.441s · Slow | +0.553s slower | 44.7% | 625.4 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.355s · Fast | -0.143s faster | 38.3% | 617.9 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.954s · Near ok | -0.605s faster | 49.6% | 565.6 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.348s · Fast | -0.221s faster | 36.1% | 651.2 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 1.667s · Slow | no baseline | 63.5% | 611.0 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.179s · Fast | no baseline | 40.8% | 599.2 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.253s · Fast | no baseline | 86.9% | 607.6 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.138s · Fast | no baseline | 54.0% | 605.8 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.141s · Fast | no baseline | 51.1% | 605.9 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.119s · Fast | no baseline | 67.7% | 600.4 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.868s · Ok | no baseline | 46.6% | 655.7 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 1.428s · Slow | no baseline | 49.3% | 656.1 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 1.863s · Slow | no baseline | 72.6% | 657.0 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 3.750s · Slow | no baseline | 47.5% | 620.4 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 4.322s · Slow | no baseline | 3.1% | 608.7 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 4.868s · Slow | no baseline | 6.2% | 610.6 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.463s · Fast | no baseline | 5.2% | 610.9 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.957s · Near ok | no baseline | 5.4% | 611.0 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 1.365s · Slow | no baseline | 7.3% | 611.0 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.679s · Ok | no baseline | 7.2% | 619.9 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.199s · Slow | no baseline | 7.1% | 619.4 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 4.001s · Slow | no baseline | 6.1% | 623.1 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.623s · Ok | no baseline | 15.6% | 569.7 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 1.010s · Slow | no baseline | 3.6% | 569.7 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 3.227s · Slow | no baseline | 4.3% | 569.7 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.857s · Slow | no baseline | 23.3% | 580.4 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 4.435s · Slow | no baseline | 2.6% | 583.8 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 5.057s · Slow | no baseline | 7.2% | 586.4 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.524s · Ok | no baseline | 8.1% | 587.0 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 0.960s · Near ok | no baseline | 8.3% | 587.0 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 1.425s · Slow | no baseline | 7.3% | 587.0 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.709s · Ok | no baseline | 8.2% | 610.5 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.308s · Slow | no baseline | 8.4% | 610.9 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 3.800s · Slow | no baseline | 6.4% | 612.9 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.559s · Ok | no baseline | 27.0% | 626.3 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.907s · Near ok | no baseline | 1.1% | 627.4 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 7.529s · Slow | no baseline | 9.0% | 637.9 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 3.669s · Slow | no baseline | 9.9% | 655.7 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 4.380s · Slow | no baseline | 9.1% | 663.2 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 9.827s · Slow | no baseline | 9.7% | 662.9 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.545s · Ok | no baseline | 4.0% | 665.9 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.325s · Slow | no baseline | 4.0% | 665.9 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.265s · Slow | no baseline | 6.8% | 667.7 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.175s · Slow | no baseline | 4.5% | 647.6 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.321s · Slow | no baseline | 4.6% | 645.7 MB | f4a17a0fe<br>2026-11-10 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.273s · Slow | no baseline | 4.7% | 643.5 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 1.332s · Slow | +0.848s slower | 31.3% | 510.2 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.464s · Fast | -0.116s faster | 56.5% | 543.9 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.258s · Fast | -0.144s faster | 53.8% | 524.2 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.477s · Fast | -0.272s faster | 39.7% | 530.5 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.432s · Fast | parity | 32.9% | 527.7 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.424s · Fast | -0.498s faster | 37.3% | 516.0 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.337s · Fast | parity | 36.6% | 501.9 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.457s · Slow | -0.333s faster | 17.7% | 524.4 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.397s · Fast | -0.284s faster | 37.5% | 513.0 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.969s · Near ok | -0.398s faster | 49.2% | 551.7 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.412s · Fast | -0.120s faster | 45.9% | 573.8 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.251s · Fast | no baseline | 29.6% | 519.8 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.448s · Fast | no baseline | 42.1% | 575.6 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.364s · Slow | no baseline | 45.3% | 548.2 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.532s · Ok | no baseline | 31.9% | 552.4 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.470s · Fast | no baseline | 50.6% | 519.2 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.154s · Fast | no baseline | 51.2% | 522.7 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 1.419s · Slow | +1.194s slower | 25.9% | 530.3 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.488s · Fast | -0.095s faster | 53.3% | 565.2 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.306s · Fast | parity | 56.7% | 529.7 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.534s · Ok | -0.275s faster | 51.7% | 534.2 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.427s · Fast | parity | 54.1% | 562.5 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.544s · Ok | -0.406s faster | 46.1% | 525.3 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.360s · Fast | parity | 63.6% | 535.4 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.045s · Slow | -0.725s faster | 37.3% | 543.9 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.435s · Fast | -0.228s faster | 63.1% | 544.9 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.596s · Ok | -0.702s faster | 44.9% | 536.8 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.523s · Ok | parity | 62.2% | 608.9 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.384s · Fast | no baseline | 52.1% | 524.1 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.642s · Ok | no baseline | 63.6% | 588.7 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.788s · Slow | no baseline | 59.0% | 560.1 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.987s · Near ok | no baseline | 61.6% | 578.7 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.429s · Fast | no baseline | 55.0% | 530.5 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.176s · Fast | no baseline | 61.2% | 551.6 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.734s · Slow | parity | 27.6% | 558.7 MB | f4a17a0fe<br>2026-11-10 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 3.668s · Slow | +1.566s slower | 31.2% | 683.8 MB | f4a17a0fe<br>2026-11-10 |

## New user profile

Newly created profiles with no pre-seeded data. Wallet scenarios use one fresh user; messenger send timing uses 1-on-1 and 3-person group chats; community send timing uses one joined community on #general.

### User data profile

- **Stored data:** No pre-seeded data
- **Wallet:** 1 wallet accounts · 0 tokens with balance > 0 · 0 NFTs · 0 transactions
- **Messenger:** 1 1-on-1 chats · 1 group chats
- **Communities:** 1 joined communities · 0 spectated communities

### Wallet

- [Time to open Wallet for the first time after login](charts/wallet_first_open_time_fresh.html)

- [CPU usage while opening Wallet for the first time after login](charts/wallet_first_open_cpu_fresh.html)

- [RAM usage while opening Wallet for the first time after login](charts/wallet_first_open_ram_fresh.html)

- [Time to reopen Wallet in the same session](charts/wallet_repeat_open_time_fresh.html)

- [CPU usage while reopening Wallet in the same session](charts/wallet_repeat_open_cpu_fresh.html)

- [RAM usage while reopening Wallet in the same session](charts/wallet_repeat_open_ram_fresh.html)

- [Time to open a Wallet account for the first time in the session](charts/wallet_account_first_open_time_fresh.html)

- [CPU usage while opening a Wallet account for the first time in the session](charts/wallet_account_first_open_cpu_fresh.html)

- [RAM usage while opening a Wallet account for the first time in the session](charts/wallet_account_first_open_ram_fresh.html)

- [Time to open the Add account modal for the first time in the session](charts/wallet_add_account_first_open_time_fresh.html)

- [CPU usage while opening the Add account modal for the first time in the session](charts/wallet_add_account_first_open_cpu_fresh.html)

- [RAM usage while opening the Add account modal for the first time in the session](charts/wallet_add_account_first_open_ram_fresh.html)

- [Time to reopen the Add account modal in the same session](charts/wallet_add_account_time_fresh.html)

- [CPU usage while reopening the Add account modal in the same session](charts/wallet_add_account_cpu_fresh.html)

- [RAM usage while reopening the Add account modal in the same session](charts/wallet_add_account_ram_fresh.html)

- [Time to open the Receive modal for the first time in the session](charts/wallet_receive_first_open_time_fresh.html)

- [CPU usage while opening the Receive modal for the first time in the session](charts/wallet_receive_first_open_cpu_fresh.html)

- [RAM usage while opening the Receive modal for the first time in the session](charts/wallet_receive_first_open_ram_fresh.html)

- [Time to reopen the Receive modal in the same session](charts/wallet_receive_time_fresh.html)

- [CPU usage while reopening the Receive modal in the same session](charts/wallet_receive_cpu_fresh.html)

- [RAM usage while reopening the Receive modal in the same session](charts/wallet_receive_ram_fresh.html)

- [Time to open the Send modal for the first time in the session](charts/wallet_send_first_open_time_fresh.html)

- [CPU usage while opening the Send modal for the first time in the session](charts/wallet_send_first_open_cpu_fresh.html)

- [RAM usage while opening the Send modal for the first time in the session](charts/wallet_send_first_open_ram_fresh.html)

- [Time to reopen the Send modal in the same session](charts/wallet_send_time_fresh.html)

- [CPU usage while reopening the Send modal in the same session](charts/wallet_send_cpu_fresh.html)

- [RAM usage while reopening the Send modal in the same session](charts/wallet_send_ram_fresh.html)

- [Time to open the Swap modal for the first time in the session](charts/wallet_swap_first_open_time_fresh.html)

- [CPU usage while opening the Swap modal for the first time in the session](charts/wallet_swap_first_open_cpu_fresh.html)

- [RAM usage while opening the Swap modal for the first time in the session](charts/wallet_swap_first_open_ram_fresh.html)

- [Time to reopen the Swap modal in the same session](charts/wallet_swap_time_fresh.html)

- [CPU usage while reopening the Swap modal in the same session](charts/wallet_swap_cpu_fresh.html)

- [RAM usage while reopening the Swap modal in the same session](charts/wallet_swap_ram_fresh.html)

- [Time to open the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_time_fresh.html)

- [CPU usage while opening the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_cpu_fresh.html)

- [RAM usage while opening the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_ram_fresh.html)

- [Time to reopen the Assets tab in the same session](charts/wallet_assets_tab_time_fresh.html)

- [CPU usage while reopening the Assets tab in the same session](charts/wallet_assets_tab_cpu_fresh.html)

- [RAM usage while reopening the Assets tab in the same session](charts/wallet_assets_tab_ram_fresh.html)

- [Time to open the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_time_fresh.html)

- [CPU usage while opening the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_cpu_fresh.html)

- [RAM usage while opening the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_ram_fresh.html)

- [Time to reopen the Collectibles tab in the same session](charts/wallet_collectibles_tab_time_fresh.html)

- [CPU usage while reopening the Collectibles tab in the same session](charts/wallet_collectibles_tab_cpu_fresh.html)

- [RAM usage while reopening the Collectibles tab in the same session](charts/wallet_collectibles_tab_ram_fresh.html)

- [Time to open the History tab for the first time in the session](charts/wallet_activity_tab_first_open_time_fresh.html)

- [CPU usage while opening the History tab for the first time in the session](charts/wallet_activity_tab_first_open_cpu_fresh.html)

- [RAM usage while opening the History tab for the first time in the session](charts/wallet_activity_tab_first_open_ram_fresh.html)

- [Time to reopen the History tab in the same session](charts/wallet_activity_tab_time_fresh.html)

- [CPU usage while reopening the History tab in the same session](charts/wallet_activity_tab_cpu_fresh.html)

- [RAM usage while reopening the History tab in the same session](charts/wallet_activity_tab_ram_fresh.html)

### Messenger

**Visible** is the time from pressing Send until the outgoing message appears in the chat view, before ticks. **Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

- [Time to Visible after sending 1000-character text in a 3-person group](charts/group_chat_plain_text_visible_time.html)

- [CPU usage while waiting for Visible after sending 1000-character text](charts/group_chat_plain_text_visible_cpu.html)

- [RAM usage while waiting for Visible after sending 1000-character text](charts/group_chat_plain_text_visible_ram.html)

- [Time to Sent after sending 1000-character text in a 3-person group](charts/group_chat_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/group_chat_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/group_chat_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a 3-person group](charts/group_chat_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/group_chat_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/group_chat_plain_text_delivered_ram.html)

- [Time to Visible after sending a 5-image album in a 3-person group](charts/group_chat_album_visible_time.html)

- [CPU usage while waiting for Visible after sending a 5-image album](charts/group_chat_album_visible_cpu.html)

- [RAM usage while waiting for Visible after sending a 5-image album](charts/group_chat_album_visible_ram.html)

- [Time to Sent after sending a 5-image album in a 3-person group](charts/group_chat_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/group_chat_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/group_chat_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a 3-person group](charts/group_chat_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/group_chat_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/group_chat_album_delivered_ram.html)

- [Time to Visible after sending a GIF in a 3-person group](charts/group_chat_gif_visible_time.html)

- [CPU usage while waiting for Visible after sending a GIF](charts/group_chat_gif_visible_cpu.html)

- [RAM usage while waiting for Visible after sending a GIF](charts/group_chat_gif_visible_ram.html)

- [Time to Sent after sending a GIF in a 3-person group](charts/group_chat_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/group_chat_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/group_chat_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a 3-person group](charts/group_chat_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/group_chat_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/group_chat_gif_delivered_ram.html)

- [Time to Visible after sending 10 texts with 0.5s delay in a 3-person group](charts/group_chat_burst_visible_time.html)

- [CPU usage while waiting for Visible after sending 10 texts with 0.5s delay](charts/group_chat_burst_visible_cpu.html)

- [RAM usage while waiting for Visible after sending 10 texts with 0.5s delay](charts/group_chat_burst_visible_ram.html)

- [Time to Sent after sending 10 texts with 0.5s delay in a 3-person group](charts/group_chat_burst_sent_time.html)

- [CPU usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/group_chat_burst_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/group_chat_burst_sent_ram.html)

- [Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group](charts/group_chat_burst_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/group_chat_burst_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/group_chat_burst_delivered_ram.html)

- [Time to Visible after sending 1000-character text in a 1-on-1 chat](charts/direct_chat_plain_text_visible_time.html)

- [CPU usage while waiting for Visible after sending 1000-character text](charts/direct_chat_plain_text_visible_cpu.html)

- [RAM usage while waiting for Visible after sending 1000-character text](charts/direct_chat_plain_text_visible_ram.html)

- [Time to Sent after sending 1000-character text in a 1-on-1 chat](charts/direct_chat_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/direct_chat_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/direct_chat_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a 1-on-1 chat](charts/direct_chat_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/direct_chat_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/direct_chat_plain_text_delivered_ram.html)

- [Time to Visible after sending a 5-image album in a 1-on-1 chat](charts/direct_chat_album_visible_time.html)

- [CPU usage while waiting for Visible after sending a 5-image album](charts/direct_chat_album_visible_cpu.html)

- [RAM usage while waiting for Visible after sending a 5-image album](charts/direct_chat_album_visible_ram.html)

- [Time to Sent after sending a 5-image album in a 1-on-1 chat](charts/direct_chat_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/direct_chat_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/direct_chat_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a 1-on-1 chat](charts/direct_chat_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/direct_chat_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/direct_chat_album_delivered_ram.html)

- [Time to Visible after sending a GIF in a 1-on-1 chat](charts/direct_chat_gif_visible_time.html)

- [CPU usage while waiting for Visible after sending a GIF](charts/direct_chat_gif_visible_cpu.html)

- [RAM usage while waiting for Visible after sending a GIF](charts/direct_chat_gif_visible_ram.html)

- [Time to Sent after sending a GIF in a 1-on-1 chat](charts/direct_chat_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/direct_chat_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/direct_chat_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a 1-on-1 chat](charts/direct_chat_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/direct_chat_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/direct_chat_gif_delivered_ram.html)

- [Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat](charts/direct_chat_burst_visible_time.html)

- [CPU usage while waiting for Visible after sending 10 texts with 0.5s delay](charts/direct_chat_burst_visible_cpu.html)

- [RAM usage while waiting for Visible after sending 10 texts with 0.5s delay](charts/direct_chat_burst_visible_ram.html)

- [Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat](charts/direct_chat_burst_sent_time.html)

- [CPU usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/direct_chat_burst_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/direct_chat_burst_sent_ram.html)

- [Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat](charts/direct_chat_burst_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/direct_chat_burst_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/direct_chat_burst_delivered_ram.html)

### Communities

**Visible** is the time from pressing Send until the outgoing message appears in the chat view, before ticks. **Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

- [Time to Visible after sending 1000-character text in a community #general channel](charts/community_general_plain_text_visible_time.html)

- [CPU usage while waiting for Visible after sending 1000-character text](charts/community_general_plain_text_visible_cpu.html)

- [RAM usage while waiting for Visible after sending 1000-character text](charts/community_general_plain_text_visible_ram.html)

- [Time to Sent after sending 1000-character text in a community #general channel](charts/community_general_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/community_general_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/community_general_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a community #general channel](charts/community_general_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/community_general_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/community_general_plain_text_delivered_ram.html)

- [Time to Visible after sending a 5-image album in a community #general channel](charts/community_general_album_visible_time.html)

- [CPU usage while waiting for Visible after sending a 5-image album](charts/community_general_album_visible_cpu.html)

- [RAM usage while waiting for Visible after sending a 5-image album](charts/community_general_album_visible_ram.html)

- [Time to Sent after sending a 5-image album in a community #general channel](charts/community_general_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/community_general_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/community_general_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a community #general channel](charts/community_general_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/community_general_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/community_general_album_delivered_ram.html)

- [Time to Visible after sending a GIF in a community #general channel](charts/community_general_gif_visible_time.html)

- [CPU usage while waiting for Visible after sending a GIF](charts/community_general_gif_visible_cpu.html)

- [RAM usage while waiting for Visible after sending a GIF](charts/community_general_gif_visible_ram.html)

- [Time to Sent after sending a GIF in a community #general channel](charts/community_general_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/community_general_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/community_general_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a community #general channel](charts/community_general_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/community_general_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/community_general_gif_delivered_ram.html)

- [Time to Visible after sending 10 texts with 0.5s delay in a community #general channel](charts/community_general_burst_visible_time.html)

- [CPU usage while waiting for Visible after sending 10 texts with 0.5s delay](charts/community_general_burst_visible_cpu.html)

- [RAM usage while waiting for Visible after sending 10 texts with 0.5s delay](charts/community_general_burst_visible_ram.html)

- [Time to Sent after sending 10 texts with 0.5s delay in a community #general channel](charts/community_general_burst_sent_time.html)

- [CPU usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/community_general_burst_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/community_general_burst_sent_ram.html)

- [Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel](charts/community_general_burst_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/community_general_burst_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/community_general_burst_delivered_ram.html)

## Returning user (semi-heavy wallet account)

Returning user with semi-heavy wallet account (~34 MB user data).

### User data profile

- **Stored data:** ~34 MB
- **Wallet:** 3 wallet accounts · 83 tokens with balance > 0 · 166 NFTs · 736 transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 0 joined communities · 0 spectated communities

### Wallet

- [Time to open Wallet for the first time after login](charts/wallet_first_open_time_wallet_load.html)

- [CPU usage while opening Wallet for the first time after login](charts/wallet_first_open_cpu_wallet_load.html)

- [RAM usage while opening Wallet for the first time after login](charts/wallet_first_open_ram_wallet_load.html)

- [Time to reopen Wallet in the same session](charts/wallet_repeat_open_time_wallet_load.html)

- [CPU usage while reopening Wallet in the same session](charts/wallet_repeat_open_cpu_wallet_load.html)

- [RAM usage while reopening Wallet in the same session](charts/wallet_repeat_open_ram_wallet_load.html)

- [Time to open a Wallet account for the first time in the session](charts/wallet_account_first_open_time_wallet_load.html)

- [CPU usage while opening a Wallet account for the first time in the session](charts/wallet_account_first_open_cpu_wallet_load.html)

- [RAM usage while opening a Wallet account for the first time in the session](charts/wallet_account_first_open_ram_wallet_load.html)

- [Time to open the Add account modal for the first time in the session](charts/wallet_add_account_first_open_time_wallet_load.html)

- [CPU usage while opening the Add account modal for the first time in the session](charts/wallet_add_account_first_open_cpu_wallet_load.html)

- [RAM usage while opening the Add account modal for the first time in the session](charts/wallet_add_account_first_open_ram_wallet_load.html)

- [Time to reopen the Add account modal in the same session](charts/wallet_add_account_time_wallet_load.html)

- [CPU usage while reopening the Add account modal in the same session](charts/wallet_add_account_cpu_wallet_load.html)

- [RAM usage while reopening the Add account modal in the same session](charts/wallet_add_account_ram_wallet_load.html)

- [Time to open the Receive modal for the first time in the session](charts/wallet_receive_first_open_time_wallet_load.html)

- [CPU usage while opening the Receive modal for the first time in the session](charts/wallet_receive_first_open_cpu_wallet_load.html)

- [RAM usage while opening the Receive modal for the first time in the session](charts/wallet_receive_first_open_ram_wallet_load.html)

- [Time to reopen the Receive modal in the same session](charts/wallet_receive_time_wallet_load.html)

- [CPU usage while reopening the Receive modal in the same session](charts/wallet_receive_cpu_wallet_load.html)

- [RAM usage while reopening the Receive modal in the same session](charts/wallet_receive_ram_wallet_load.html)

- [Time to open the Send modal for the first time in the session](charts/wallet_send_first_open_time_wallet_load.html)

- [CPU usage while opening the Send modal for the first time in the session](charts/wallet_send_first_open_cpu_wallet_load.html)

- [RAM usage while opening the Send modal for the first time in the session](charts/wallet_send_first_open_ram_wallet_load.html)

- [Time to reopen the Send modal in the same session](charts/wallet_send_time_wallet_load.html)

- [CPU usage while reopening the Send modal in the same session](charts/wallet_send_cpu_wallet_load.html)

- [RAM usage while reopening the Send modal in the same session](charts/wallet_send_ram_wallet_load.html)

- [Time to open the Swap modal for the first time in the session](charts/wallet_swap_first_open_time_wallet_load.html)

- [CPU usage while opening the Swap modal for the first time in the session](charts/wallet_swap_first_open_cpu_wallet_load.html)

- [RAM usage while opening the Swap modal for the first time in the session](charts/wallet_swap_first_open_ram_wallet_load.html)

- [Time to reopen the Swap modal in the same session](charts/wallet_swap_time_wallet_load.html)

- [CPU usage while reopening the Swap modal in the same session](charts/wallet_swap_cpu_wallet_load.html)

- [RAM usage while reopening the Swap modal in the same session](charts/wallet_swap_ram_wallet_load.html)

- [Time to open the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_time_wallet_load.html)

- [CPU usage while opening the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_cpu_wallet_load.html)

- [RAM usage while opening the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_ram_wallet_load.html)

- [Time to reopen the Assets tab in the same session](charts/wallet_assets_tab_time_wallet_load.html)

- [CPU usage while reopening the Assets tab in the same session](charts/wallet_assets_tab_cpu_wallet_load.html)

- [RAM usage while reopening the Assets tab in the same session](charts/wallet_assets_tab_ram_wallet_load.html)

- [Time to open the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_time_wallet_load.html)

- [CPU usage while opening the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_cpu_wallet_load.html)

- [RAM usage while opening the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_ram_wallet_load.html)

- [Time to reopen the Collectibles tab in the same session](charts/wallet_collectibles_tab_time_wallet_load.html)

- [CPU usage while reopening the Collectibles tab in the same session](charts/wallet_collectibles_tab_cpu_wallet_load.html)

- [RAM usage while reopening the Collectibles tab in the same session](charts/wallet_collectibles_tab_ram_wallet_load.html)

- [Time to open the History tab for the first time in the session](charts/wallet_activity_tab_first_open_time_wallet_load.html)

- [CPU usage while opening the History tab for the first time in the session](charts/wallet_activity_tab_first_open_cpu_wallet_load.html)

- [RAM usage while opening the History tab for the first time in the session](charts/wallet_activity_tab_first_open_ram_wallet_load.html)

- [Time to reopen the History tab in the same session](charts/wallet_activity_tab_time_wallet_load.html)

- [CPU usage while reopening the History tab in the same session](charts/wallet_activity_tab_cpu_wallet_load.html)

- [RAM usage while reopening the History tab in the same session](charts/wallet_activity_tab_ram_wallet_load.html)

## Returning user (heavy account from Alex)

Returning user with heavy account from Alex (~35 MB user data).

### User data profile

- **Stored data:** ~35 MB
- **Wallet:** 4 wallet accounts · 144 tokens with balance > 0 · 773 NFTs · 5239 transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 0 joined communities · 0 spectated communities

### Wallet

- [Time to open Wallet for the first time after login](charts/wallet_first_open_time_wallet_load_alex.html)

- [CPU usage while opening Wallet for the first time after login](charts/wallet_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening Wallet for the first time after login](charts/wallet_first_open_ram_wallet_load_alex.html)

- [Time to reopen Wallet in the same session](charts/wallet_repeat_open_time_wallet_load_alex.html)

- [CPU usage while reopening Wallet in the same session](charts/wallet_repeat_open_cpu_wallet_load_alex.html)

- [RAM usage while reopening Wallet in the same session](charts/wallet_repeat_open_ram_wallet_load_alex.html)

- [Time to open a Wallet account for the first time in the session](charts/wallet_account_first_open_time_wallet_load_alex.html)

- [CPU usage while opening a Wallet account for the first time in the session](charts/wallet_account_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening a Wallet account for the first time in the session](charts/wallet_account_first_open_ram_wallet_load_alex.html)

- [Time to open the Add account modal for the first time in the session](charts/wallet_add_account_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the Add account modal for the first time in the session](charts/wallet_add_account_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the Add account modal for the first time in the session](charts/wallet_add_account_first_open_ram_wallet_load_alex.html)

- [Time to reopen the Add account modal in the same session](charts/wallet_add_account_time_wallet_load_alex.html)

- [CPU usage while reopening the Add account modal in the same session](charts/wallet_add_account_cpu_wallet_load_alex.html)

- [RAM usage while reopening the Add account modal in the same session](charts/wallet_add_account_ram_wallet_load_alex.html)

- [Time to open the Receive modal for the first time in the session](charts/wallet_receive_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the Receive modal for the first time in the session](charts/wallet_receive_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the Receive modal for the first time in the session](charts/wallet_receive_first_open_ram_wallet_load_alex.html)

- [Time to reopen the Receive modal in the same session](charts/wallet_receive_time_wallet_load_alex.html)

- [CPU usage while reopening the Receive modal in the same session](charts/wallet_receive_cpu_wallet_load_alex.html)

- [RAM usage while reopening the Receive modal in the same session](charts/wallet_receive_ram_wallet_load_alex.html)

- [Time to open the Send modal for the first time in the session](charts/wallet_send_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the Send modal for the first time in the session](charts/wallet_send_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the Send modal for the first time in the session](charts/wallet_send_first_open_ram_wallet_load_alex.html)

- [Time to reopen the Send modal in the same session](charts/wallet_send_time_wallet_load_alex.html)

- [CPU usage while reopening the Send modal in the same session](charts/wallet_send_cpu_wallet_load_alex.html)

- [RAM usage while reopening the Send modal in the same session](charts/wallet_send_ram_wallet_load_alex.html)

- [Time to open the Swap modal for the first time in the session](charts/wallet_swap_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the Swap modal for the first time in the session](charts/wallet_swap_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the Swap modal for the first time in the session](charts/wallet_swap_first_open_ram_wallet_load_alex.html)

- [Time to reopen the Swap modal in the same session](charts/wallet_swap_time_wallet_load_alex.html)

- [CPU usage while reopening the Swap modal in the same session](charts/wallet_swap_cpu_wallet_load_alex.html)

- [RAM usage while reopening the Swap modal in the same session](charts/wallet_swap_ram_wallet_load_alex.html)

- [Time to open the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_ram_wallet_load_alex.html)

- [Time to reopen the Assets tab in the same session](charts/wallet_assets_tab_time_wallet_load_alex.html)

- [CPU usage while reopening the Assets tab in the same session](charts/wallet_assets_tab_cpu_wallet_load_alex.html)

- [RAM usage while reopening the Assets tab in the same session](charts/wallet_assets_tab_ram_wallet_load_alex.html)

- [Time to open the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_ram_wallet_load_alex.html)

- [Time to reopen the Collectibles tab in the same session](charts/wallet_collectibles_tab_time_wallet_load_alex.html)

- [CPU usage while reopening the Collectibles tab in the same session](charts/wallet_collectibles_tab_cpu_wallet_load_alex.html)

- [RAM usage while reopening the Collectibles tab in the same session](charts/wallet_collectibles_tab_ram_wallet_load_alex.html)

- [Time to open the History tab for the first time in the session](charts/wallet_activity_tab_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the History tab for the first time in the session](charts/wallet_activity_tab_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the History tab for the first time in the session](charts/wallet_activity_tab_first_open_ram_wallet_load_alex.html)

- [Time to reopen the History tab in the same session](charts/wallet_activity_tab_time_wallet_load_alex.html)

- [CPU usage while reopening the History tab in the same session](charts/wallet_activity_tab_cpu_wallet_load_alex.html)

- [RAM usage while reopening the History tab in the same session](charts/wallet_activity_tab_ram_wallet_load_alex.html)

## Returning user (Status community member)

Returning user with Status community already joined.

### User data profile

- **Stored data:** TBD
- **Wallet:** 1 wallet accounts · 0 tokens with balance > 0 · 0 NFTs · 0 transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 1 joined communities · 0 spectated communities

### Communities

- [Time to open Status community for the first time after login](charts/community_first_open_loading_time_member.html)

- [Time to reopen Status community in the same session](charts/community_second_open_loading_time_member.html)

- [CPU usage while opening Status community for the first time after login](charts/community_first_open_cpu_member.html)

- [CPU usage while reopening Status community in the same session](charts/community_second_open_cpu_member.html)

- [RAM usage while opening Status community for the first time after login](charts/community_first_open_ram_member.html)

- [RAM usage while reopening Status community in the same session](charts/community_second_open_ram_member.html)

---

Generated by `scripts/benchmark.py graphs` from `data/`. Refreshed nightly by Jenkins.
