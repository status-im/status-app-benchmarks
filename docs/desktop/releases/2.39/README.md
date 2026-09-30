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
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.615s · Ok | +0.243s slower | 62.1% | 811.2 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.611s · Ok | +0.232s slower | 71.0% | 857.8 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.154s · Fast | parity | 54.7% | 733.8 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.589s · Ok | parity | 38.8% | 793.5 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.459s · Fast | parity | 32.8% | 826.1 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.423s · Fast | parity | 52.9% | 765.8 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.301s · Fast | parity | 16.6% | 808.7 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.102s · Slow | +0.214s slower | 64.1% | 861.3 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.780s · Ok | +0.282s slower | 52.3% | 914.3 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.120s · Slow | -0.439s faster | 54.9% | 834.1 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.359s · Fast | -0.210s faster | 43.1% | 981.3 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.199s · Fast | no baseline | 71.7% | 743.0 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.218s · Fast | no baseline | 49.5% | 744.3 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.350s · Fast | no baseline | 46.7% | 821.5 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.139s · Fast | no baseline | 59.9% | 809.7 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.250s · Fast | no baseline | 49.7% | 717.7 MB | a4a0c3<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.123s · Fast | no baseline | 66.0% | 721.6 MB | a4a0c3<br>2026-09-30 |
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
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 1.000s · Slow | +0.516s slower | 25.5% | 801.7 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.890s · Ok | +0.310s slower | 71.0% | 834.0 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 1.334s · Slow | +0.932s slower | 42.3% | 825.2 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 1.180s · Slow | +0.431s slower | 57.7% | 847.4 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.700s · Ok | +0.235s slower | 50.7% | 820.5 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.487s · Fast | -0.435s faster | 41.1% | 806.0 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.317s · Fast | parity | 28.9% | 816.7 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 2.838s · Slow | +1.048s slower | 59.4% | 900.6 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.825s · Ok | +0.144s slower | 27.6% | 921.4 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.772s · Ok | -0.595s faster | 33.1% | 808.0 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.687s · Ok | +0.155s slower | 69.8% | 990.5 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 7.399s · Slow | no baseline | 68.8% | 805.0 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.418s · Fast | no baseline | 45.0% | 838.1 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 4.463s · Slow | no baseline | 57.8% | 868.2 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.443s · Fast | no baseline | 39.9% | 953.5 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.956s · Near ok | no baseline | 48.0% | 811.5 MB | a4a0c3<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.417s · Fast | no baseline | 53.8% | 844.8 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 1.094s · Slow | +0.869s slower | 50.7% | 870.5 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 3.680s · Slow | +3.097s slower | 72.9% | 913.7 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.504s · Ok | +0.157s slower | 59.9% | 894.9 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.628s · Ok | -0.181s faster | 63.4% | 874.0 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.480s · Fast | parity | 63.4% | 835.0 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.585s · Ok | -0.365s faster | 51.6% | 905.6 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.359s · Fast | parity | 73.0% | 810.1 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.224s · Slow | -0.546s faster | 67.2% | 892.8 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.788s · Ok | +0.125s slower | 52.8% | 927.1 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.814s · Ok | -0.484s faster | 62.5% | 1005.5 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.737s · Ok | +0.223s slower | 46.7% | 1002.9 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.440s · Fast | no baseline | 72.0% | 924.2 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.597s · Ok | no baseline | 55.5% | 885.9 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.018s · Slow | no baseline | 65.9% | 890.7 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.850s · Ok | no baseline | 55.9% | 868.3 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.747s · Ok | no baseline | 57.4% | 913.8 MB | a4a0c3<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.256s · Fast | no baseline | 62.1% | 867.8 MB | a4a0c3<br>2026-09-30 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.767s · Slow | parity | 32.1% | 899.3 MB | a4a0c3<br>2026-09-30 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.200s · Slow | parity | 17.2% | 873.8 MB | a4a0c3<br>2026-09-30 |

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
