# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 18, 2026 · [`26d9baf9e`](https://github.com/status-im/status-app/commit/26d9baf9eb84b5a792b19d836e1eb0e694d17d99)

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.474s · Fast | +0.102s slower | 47.8% | 771.2 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.489s · Fast | +0.110s slower | 53.5% | 823.7 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.107s · Fast | -0.050s faster | 23.9% | 684.7 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.760s · Ok | +0.149s slower | 41.1% | 859.0 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.375s · Fast | parity | 19.2% | 746.4 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.288s · Fast | -0.183s faster | 39.0% | 781.9 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.298s · Fast | parity | 15.7% | 751.8 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.231s · Slow | +0.343s slower | 38.3% | 810.3 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.605s · Ok | +0.107s slower | 23.5% | 886.0 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.009s · Slow | -0.550s faster | 49.6% | 731.3 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.542s · Ok | parity | 24.0% | 925.0 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.137s · Fast | no baseline | 33.6% | 686.4 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.178s · Fast | no baseline | 40.3% | 717.0 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.264s · Fast | no baseline | 46.9% | 747.8 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.127s · Fast | no baseline | 52.9% | 795.7 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.148s · Fast | no baseline | 62.7% | 797.8 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.158s · Fast | no baseline | 42.4% | 768.5 MB | 26d9baf9e<br>2026-09-18 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | — · No data | — | — | — | — |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.388s · Fast | -0.096s faster | 42.2% | 849.9 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.551s · Ok | parity | 67.4% | 790.7 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.395s · Fast | parity | 31.0% | 818.9 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.551s · Ok | -0.198s faster | 65.0% | 771.1 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.392s · Fast | -0.073s faster | 45.5% | 788.6 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.629s · Ok | -0.293s faster | 50.6% | 789.7 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.312s · Fast | parity | 40.8% | 756.7 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.228s · Slow | -0.562s faster | 39.7% | 873.4 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.801s · Ok | +0.120s slower | 45.0% | 855.1 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 1.099s · Slow | -0.268s faster | 56.6% | 835.3 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.565s · Ok | parity | 37.4% | 923.4 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 1.806s · Slow | no baseline | 65.5% | 793.1 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.440s · Fast | no baseline | 49.0% | 819.4 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.471s · Slow | no baseline | 66.4% | 824.7 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.546s · Ok | no baseline | 55.2% | 800.1 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.679s · Ok | no baseline | 57.0% | 828.2 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.203s · Fast | no baseline | 65.6% | 777.1 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.519s · Ok | +0.294s slower | 48.2% | 811.4 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.625s · Ok | parity | 66.8% | 885.3 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.459s · Fast | +0.112s slower | 46.3% | 777.6 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.492s · Fast | -0.317s faster | 59.6% | 767.2 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.434s · Fast | parity | 55.5% | 803.6 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 1.115s · Slow | +0.165s slower | 56.0% | 796.3 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.405s · Fast | +0.077s slower | 71.3% | 829.6 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.240s · Slow | -0.530s faster | 55.6% | 833.7 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.792s · Ok | +0.129s slower | 51.8% | 869.1 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.679s · Ok | -0.619s faster | 40.2% | 795.7 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.618s · Ok | +0.104s slower | 57.5% | 921.7 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.303s · Fast | no baseline | 29.1% | 817.9 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.462s · Fast | no baseline | 60.2% | 818.5 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.356s · Fast | no baseline | 58.0% | 873.9 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.300s · Fast | no baseline | 55.6% | 824.7 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.818s · Ok | no baseline | 59.4% | 834.6 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.254s · Fast | no baseline | 62.8% | 844.1 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.039s · Slow | -0.736s faster | 52.2% | 794.8 MB | 26d9baf9e<br>2026-09-18 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.226s · Slow | parity | 31.9% | 842.7 MB | 26d9baf9e<br>2026-09-18 |

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

**Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

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

**Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

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
