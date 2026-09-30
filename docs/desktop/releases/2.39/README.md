# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show the full RC-to-final history for this release. Each point is one requested benchmark run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 30, 2026 · [`a4a0c3`](https://github.com/status-im/status-app/commit/a4a0c3325e3a60e7275dca0be970512fbd9343c1)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | — | — | — | — | — |
| a 5-image album in a 3-person group | — | — | — | — | — |
| a GIF in a 3-person group | — | — | — | — | — |
| 10 texts with 0.5s delay in a 3-person group | — | — | — | — | — |
| 1000-character text in a 1-on-1 chat | — | — | — | — | — |
| a 5-image album in a 1-on-1 chat | — | — | — | — | — |
| a GIF in a 1-on-1 chat | — | — | — | — | — |
| 10 texts with 0.5s delay in a 1-on-1 chat | — | — | — | — | — |
| 1000-character text in a community #general channel | — | — | — | — | — |
| a 5-image album in a community #general channel | — | — | — | — | — |
| a GIF in a community #general channel | — | — | — | — | — |
| 10 texts with 0.5s delay in a community #general channel | — | — | — | — | — |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.609s · Ok | +0.237s slower | 65.2% | 767.0 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.616s · Ok | +0.237s slower | 72.5% | 856.0 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.388s · Fast | +0.231s slower | 61.8% | 820.1 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.603s · Ok | parity | 60.2% | 806.0 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.423s · Fast | parity | 21.4% | 771.0 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.320s · Fast | -0.151s faster | 51.2% | 739.6 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.387s · Fast | +0.085s slower | 35.1% | 774.6 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.122s · Slow | +0.234s slower | 58.2% | 892.7 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.684s · Ok | +0.186s slower | 44.1% | 960.9 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.048s · Slow | -0.511s faster | 52.9% | 796.7 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.553s · Ok | parity | 32.9% | 926.4 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.193s · Fast | no baseline | 49.7% | 771.8 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.213s · Fast | no baseline | 60.0% | 783.5 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.349s · Fast | no baseline | 73.9% | 772.8 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.134s · Fast | no baseline | 51.7% | 765.6 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.263s · Fast | no baseline | 55.8% | 826.5 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.183s · Fast | no baseline | 58.1% | 812.5 MB | a4a0c3<br>2026-09-30 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | — · No data | — | — | — | — |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.597s · Ok | +0.113s slower | 41.2% | 832.8 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.834s · Ok | +0.254s slower | 70.6% | 847.9 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 1.252s · Slow | +0.850s slower | 48.3% | 829.1 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.983s · Near ok | +0.234s slower | 52.8% | 833.1 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.468s · Fast | parity | 30.6% | 806.6 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.580s · Ok | -0.342s faster | 52.1% | 896.6 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.338s · Fast | parity | 30.4% | 809.9 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.153s · Slow | -0.637s faster | 44.6% | 888.9 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.918s · Near ok | +0.237s slower | 58.1% | 891.8 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.859s · Ok | -0.508s faster | 44.1% | 832.9 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.618s · Ok | +0.086s slower | 33.6% | 953.4 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 7.951s · Slow | no baseline | 66.6% | 791.3 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.411s · Fast | no baseline | 50.2% | 820.4 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 5.229s · Slow | no baseline | 63.0% | 908.5 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.538s · Ok | no baseline | 47.0% | 929.6 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.951s · Near ok | no baseline | 52.4% | 835.0 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.260s · Fast | no baseline | 67.6% | 850.7 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 1.704s · Slow | +1.479s slower | 56.9% | 954.7 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.902s · Near ok | +0.319s slower | 75.9% | 885.2 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.593s · Ok | +0.246s slower | 47.2% | 937.6 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.548s · Ok | -0.261s faster | 48.6% | 845.7 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.515s · Ok | +0.080s slower | 61.5% | 861.8 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.974s · Near ok | parity | 63.3% | 874.8 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.371s · Fast | parity | 61.3% | 808.0 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.818s · Slow | parity | 54.6% | 944.1 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.770s · Ok | +0.107s slower | 56.0% | 920.5 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 1.475s · Slow | parity | 67.4% | 892.9 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.700s · Ok | +0.186s slower | 52.7% | 1005.8 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.421s · Fast | no baseline | 61.3% | 894.5 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.784s · Ok | no baseline | 68.0% | 891.3 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.990s · Slow | no baseline | 73.1% | 902.4 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 1.000s · Near ok | no baseline | 60.2% | 896.8 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.842s · Ok | no baseline | 67.7% | 914.3 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.266s · Fast | no baseline | 70.9% | 896.8 MB | a4a0c3<br>2026-09-30 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.442s · Slow | parity | 43.9% | 796.8 MB | a4a0c3<br>2026-09-30 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.197s · Slow | parity | 19.7% | 870.9 MB | a4a0c3<br>2026-09-30 |

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

**Time to Visible after sending 1000-character text in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Visible after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Visible after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending 1000-character text in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending 1000-character text in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Visible after sending a 5-image album in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Visible after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Visible after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending a 5-image album in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending a 5-image album in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Visible after sending a GIF in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Visible after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Visible after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending a GIF in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending a GIF in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Visible after sending 10 texts with 0.5s delay in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Visible after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Visible after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending 10 texts with 0.5s delay in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Visible after sending 1000-character text in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Visible after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Visible after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending 1000-character text in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending 1000-character text in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Visible after sending a 5-image album in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Visible after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Visible after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending a 5-image album in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending a 5-image album in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Visible after sending a GIF in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Visible after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Visible after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending a GIF in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending a GIF in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Visible after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Visible after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

### Communities

**Visible** is the time from pressing Send until the outgoing message appears in the chat view, before ticks. **Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

**Time to Visible after sending 1000-character text in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Visible after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Visible after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending 1000-character text in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending 1000-character text in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Visible after sending a 5-image album in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Visible after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Visible after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending a 5-image album in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending a 5-image album in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Visible after sending a GIF in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Visible after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Visible after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending a GIF in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending a GIF in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Visible after sending 10 texts with 0.5s delay in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Visible after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Visible after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending 10 texts with 0.5s delay in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

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
