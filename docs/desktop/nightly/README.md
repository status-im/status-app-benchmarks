# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 22, 2026 · [`2969f8bf1`](https://github.com/status-im/status-app/commit/2969f8bf1d6da2fcf7e1a95ada7fd1dc0d347c93)

## Send timing

Latest time to **Sent** (one tick) and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Sent | Delivered | Commit | Date |
|----------|------|-----------|--------|------|
| 1000-character text in a 3-person group | — | — | — | — |
| a 5-image album in a 3-person group | — | — | — | — |
| a GIF in a 3-person group | — | — | — | — |
| 10 texts with 0.5s delay in a 3-person group | — | — | — | — |
| 1000-character text in a 1-on-1 chat | — | — | — | — |
| a 5-image album in a 1-on-1 chat | — | — | — | — |
| a GIF in a 1-on-1 chat | — | — | — | — |
| 10 texts with 0.5s delay in a 1-on-1 chat | — | — | — | — |
| 1000-character text in a community #general channel | — | — | — | — |
| a 5-image album in a community #general channel | — | — | — | — |
| a GIF in a community #general channel | — | — | — | — |
| 10 texts with 0.5s delay in a community #general channel | — | — | — | — |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.516s · Ok | +0.144s slower | 61.4% | 726.3 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.482s · Fast | +0.103s slower | 54.7% | 769.7 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.175s · Fast | parity | 35.5% | 724.2 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.520s · Ok | parity | 61.6% | 688.8 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.377s · Fast | parity | 15.6% | 761.3 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.305s · Fast | -0.166s faster | 31.1% | 727.3 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.305s · Fast | parity | 23.2% | 749.4 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.022s · Slow | +0.134s slower | 26.8% | 789.5 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.599s · Ok | +0.101s slower | 20.1% | 859.2 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.945s · Near ok | -0.614s faster | 54.4% | 722.0 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.410s · Fast | -0.158s faster | 27.9% | 888.5 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.135s · Fast | no baseline | 47.0% | 670.7 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.172s · Fast | no baseline | 45.6% | 678.0 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.231s · Fast | no baseline | 47.1% | 685.1 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.122s · Fast | no baseline | 28.3% | 702.4 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.163s · Fast | no baseline | 64.8% | 717.3 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.123s · Fast | no baseline | 61.8% | 692.0 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.940s · Near ok | no baseline | 42.4% | 772.6 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 2.968s · Slow | no baseline | 8.8% | 773.1 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.001s · Slow | no baseline | 13.3% | 792.0 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 5.205s · Slow | no baseline | 5.6% | 845.9 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.443s · Fast | no baseline | 3.5% | 876.5 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 2.665s · Slow | no baseline | 2.0% | 876.5 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 0.796s · Ok | no baseline | 11.8% | 877.2 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 3.210s · Slow | no baseline | 3.8% | 877.2 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 0.711s · Ok | no baseline | 59.6% | 818.9 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 2.552s · Slow | no baseline | 64.9% | 819.3 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.007s · Slow | no baseline | 10.9% | 813.3 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.318s · Slow | no baseline | 1.7% | 808.3 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 0.582s · Ok | no baseline | 6.7% | 870.3 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 3.242s · Slow | no baseline | 3.6% | 870.6 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.767s · Ok | no baseline | 21.3% | 868.4 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 3.034s · Slow | no baseline | 9.5% | 868.0 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.456s · Fast | no baseline | 46.2% | 795.0 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 2.814s · Slow | no baseline | 8.2% | 796.7 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 5.124s · Slow | no baseline | 9.5% | 815.8 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 8.417s · Slow | no baseline | 7.4% | 941.0 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 0.654s · Ok | no baseline | 4.4% | 942.7 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.032s · Slow | no baseline | 7.5% | 920.4 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 1.135s · Slow | no baseline | 7.2% | 914.3 MB | 2969f8bf1<br>2026-09-22 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 4.591s · Slow | no baseline | 5.3% | 913.3 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.310s · Fast | -0.174s faster | 32.5% | 825.4 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.498s · Fast | parity | 66.4% | 800.8 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.275s · Fast | -0.127s faster | 34.5% | 834.6 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.557s · Ok | -0.192s faster | 34.9% | 877.2 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.400s · Fast | parity | 34.1% | 792.5 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.482s · Fast | -0.440s faster | 39.0% | 838.8 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.320s · Fast | parity | 34.8% | 789.2 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.738s · Slow | parity | 62.1% | 854.2 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.775s · Ok | parity | 37.5% | 833.3 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.650s · Ok | -0.717s faster | 52.5% | 811.4 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.657s · Ok | +0.125s slower | 61.9% | 907.5 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 1.153s · Slow | no baseline | 33.5% | 816.5 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 1.207s · Slow | no baseline | 49.3% | 825.4 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.564s · Slow | no baseline | 64.6% | 779.9 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.560s · Ok | no baseline | 45.4% | 779.8 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.662s · Ok | no baseline | 61.2% | 825.1 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.225s · Fast | no baseline | 71.3% | 770.7 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.189s · Fast | -0.036s faster | 42.6% | 844.6 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.556s · Ok | parity | 67.2% | 861.6 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.511s · Ok | +0.164s slower | 24.5% | 840.4 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.550s · Ok | -0.259s faster | 51.7% | 837.9 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.502s · Ok | +0.067s slower | 67.3% | 841.6 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.659s · Ok | -0.291s faster | 38.9% | 851.0 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.396s · Fast | +0.068s slower | 58.9% | 837.7 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.823s · Slow | parity | 44.6% | 912.2 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.798s · Ok | +0.135s slower | 54.6% | 957.0 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.648s · Ok | -0.650s faster | 44.2% | 804.8 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.794s · Ok | +0.280s slower | 61.3% | 956.0 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.488s · Fast | no baseline | 54.9% | 835.2 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.434s · Fast | no baseline | 54.9% | 803.3 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.402s · Fast | no baseline | 57.4% | 881.5 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.324s · Fast | no baseline | 58.9% | 842.5 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.572s · Ok | no baseline | 60.2% | 829.8 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.231s · Fast | no baseline | 65.5% | 818.2 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 2.657s · Slow | -1.118s faster | 46.2% | 744.4 MB | 2969f8bf1<br>2026-09-22 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.205s · Slow | parity | 28.2% | 827.0 MB | 2969f8bf1<br>2026-09-22 |

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

- [Time to Sent after sending 1000-character text in a 3-person group](charts/group_chat_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/group_chat_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/group_chat_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a 3-person group](charts/group_chat_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/group_chat_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/group_chat_plain_text_delivered_ram.html)

- [Time to Sent after sending a 5-image album in a 3-person group](charts/group_chat_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/group_chat_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/group_chat_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a 3-person group](charts/group_chat_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/group_chat_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/group_chat_album_delivered_ram.html)

- [Time to Sent after sending a GIF in a 3-person group](charts/group_chat_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/group_chat_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/group_chat_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a 3-person group](charts/group_chat_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/group_chat_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/group_chat_gif_delivered_ram.html)

- [Time to Sent after sending 10 texts with 0.5s delay in a 3-person group](charts/group_chat_burst_sent_time.html)

- [CPU usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/group_chat_burst_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/group_chat_burst_sent_ram.html)

- [Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group](charts/group_chat_burst_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/group_chat_burst_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/group_chat_burst_delivered_ram.html)

- [Time to Sent after sending 1000-character text in a 1-on-1 chat](charts/direct_chat_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/direct_chat_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/direct_chat_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a 1-on-1 chat](charts/direct_chat_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/direct_chat_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/direct_chat_plain_text_delivered_ram.html)

- [Time to Sent after sending a 5-image album in a 1-on-1 chat](charts/direct_chat_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/direct_chat_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/direct_chat_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a 1-on-1 chat](charts/direct_chat_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/direct_chat_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/direct_chat_album_delivered_ram.html)

- [Time to Sent after sending a GIF in a 1-on-1 chat](charts/direct_chat_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/direct_chat_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/direct_chat_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a 1-on-1 chat](charts/direct_chat_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/direct_chat_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/direct_chat_gif_delivered_ram.html)

- [Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat](charts/direct_chat_burst_sent_time.html)

- [CPU usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/direct_chat_burst_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/direct_chat_burst_sent_ram.html)

- [Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat](charts/direct_chat_burst_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/direct_chat_burst_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/direct_chat_burst_delivered_ram.html)

### Communities

**Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

- [Time to Sent after sending 1000-character text in a community #general channel](charts/community_general_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/community_general_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/community_general_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a community #general channel](charts/community_general_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/community_general_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/community_general_plain_text_delivered_ram.html)

- [Time to Sent after sending a 5-image album in a community #general channel](charts/community_general_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/community_general_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/community_general_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a community #general channel](charts/community_general_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/community_general_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/community_general_album_delivered_ram.html)

- [Time to Sent after sending a GIF in a community #general channel](charts/community_general_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/community_general_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/community_general_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a community #general channel](charts/community_general_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/community_general_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/community_general_gif_delivered_ram.html)

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
