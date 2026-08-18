# [#21975](https://github.com/status-im/status-app/pull/21975) perf: mobile section extras

Automated test suite performance tracking for the Windows desktop app.
Charts show every requested run for this pull request. Each point is one benchmark run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** This README renders inline PNG images on GitHub — works without
> GitHub Pages. For interactive charts (hover tooltips, zoom), use the
> [interactive dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) once GitHub Pages is enabled.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Aug 18, 2026 · [`7ea77e`](https://github.com/status-im/status-app/commit/7ea77e82feb2afb2069604132371ffb259d06cc2)

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026). **vs nightly · Aug 18, 2026** is that nightly run — the latest nightly when this PR was measured.

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | vs nightly · Aug 18, 2026 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|----------------------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.601s · Ok | no baseline | +0.201s slower | 60.6% | 706.4 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.624s · Ok | no baseline | +0.175s slower | 71.0% | 767.1 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.134s · Fast | no baseline | parity | 22.4% | 742.9 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.447s · Fast | no baseline | -0.091s faster | 9.2% | 763.7 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.416s · Fast | no baseline | parity | 11.3% | 770.3 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.303s · Fast | no baseline | -0.083s faster | 32.4% | 683.4 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.305s · Fast | no baseline | parity | 15.6% | 710.2 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.031s · Slow | no baseline | parity | 26.5% | 732.0 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.360s · Fast | no baseline | parity | 20.1% | 774.4 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.031s · Slow | no baseline | parity | 25.8% | 778.6 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.313s · Fast | no baseline | parity | 26.3% | 828.5 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.165s · Fast | no baseline | parity | 7.2% | 752.9 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.532s · Ok | no baseline | +0.159s slower | 69.9% | 779.5 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.316s · Fast | no baseline | +0.154s slower | 20.3% | 712.6 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.257s · Fast | no baseline | +0.108s slower | 39.5% | 728.4 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.377s · Fast | no baseline | +0.162s slower | 23.9% | 764.2 MB | 7ea77e<br>2026-08-18 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.297s · Fast | no baseline | +0.089s slower | 42.2% | 829.2 MB | 7ea77e<br>2026-08-18 |
| New user profile | Messenger | Not tested | Not tested | — | — | — | — | — |
| New user profile | Communities | Not tested | Not tested | — | — | — | — | — |
| New user profile | Browser | Not tested | Not tested | — | — | — | — | — |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 1.007s · Slow | no baseline | +0.576s slower | 49.3% | 790.6 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.818s · Ok | no baseline | +0.238s slower | 68.6% | 840.3 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.290s · Fast | no baseline | -0.137s faster | 18.9% | 765.1 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 1.118s · Slow | no baseline | +0.551s slower | 33.9% | 781.0 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.446s · Fast | no baseline | parity | 29.3% | 739.7 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.621s · Ok | no baseline | -0.325s faster | 39.6% | 703.0 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.327s · Fast | no baseline | parity | 35.4% | 694.0 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.374s · Slow | no baseline | +0.216s slower | 69.1% | 746.9 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.490s · Fast | no baseline | parity | 38.8% | 756.1 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 1.022s · Slow | no baseline | +0.388s slower | 56.2% | 802.8 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.532s · Ok | no baseline | parity | 33.6% | 794.5 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.367s · Fast | no baseline | -0.933s faster | 70.0% | 707.5 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.906s · Near ok | no baseline | +0.197s slower | 62.3% | 711.5 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.351s · Fast | no baseline | +0.092s slower | 59.0% | 747.0 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.313s · Fast | no baseline | +0.085s slower | 65.9% | 718.6 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 1.055s · Slow | no baseline | +0.384s slower | 64.5% | 765.5 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.792s · Ok | no baseline | +0.157s slower | 70.8% | 751.2 MB | 7ea77e<br>2026-08-18 |
| Returning user (semi-heavy wallet account) | Messenger | Not tested | Not tested | — | — | — | — | — |
| Returning user (semi-heavy wallet account) | Communities | Not tested | Not tested | — | — | — | — | — |
| Returning user (semi-heavy wallet account) | Browser | Not tested | Not tested | — | — | — | — | — |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 1.066s · Slow | no baseline | +0.791s slower | 56.4% | 824.4 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.877s · Ok | no baseline | +0.242s slower | 69.3% | 863.1 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.423s · Fast | no baseline | parity | 43.3% | 784.5 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.532s · Ok | no baseline | -0.396s faster | 50.9% | 802.9 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.485s · Fast | no baseline | parity | 62.2% | 798.2 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.523s · Ok | no baseline | -0.548s faster | 48.3% | 779.2 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.351s · Fast | no baseline | parity | 50.0% | 765.5 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.154s · Slow | no baseline | -0.725s faster | 72.8% | 801.3 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.520s · Ok | no baseline | -0.132s faster | 50.4% | 773.1 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.856s · Ok | no baseline | +0.261s slower | 29.6% | 810.5 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.642s · Ok | no baseline | parity | 56.1% | 865.4 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.236s · Fast | no baseline | -0.343s faster | 46.1% | 807.4 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.979s · Near ok | no baseline | +0.142s slower | 71.9% | 789.7 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.338s · Fast | no baseline | +0.136s slower | 67.6% | 767.4 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.323s · Fast | no baseline | +0.134s slower | 64.2% | 771.4 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 1.170s · Slow | no baseline | +0.210s slower | 52.2% | 801.6 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.781s · Ok | no baseline | parity | 75.6% | 804.8 MB | 7ea77e<br>2026-08-18 |
| Returning user (heavy account from Alex) | Messenger | Not tested | Not tested | — | — | — | — | — |
| Returning user (heavy account from Alex) | Communities | Not tested | Not tested | — | — | — | — | — |
| Returning user (heavy account from Alex) | Browser | Not tested | Not tested | — | — | — | — | — |
| Returning user (Status community member) | Wallet | Not tested | Not tested | — | — | — | — | — |
| Returning user (Status community member) | Messenger | Not tested | Not tested | — | — | — | — | — |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.711s · Slow | no baseline | -1.210s faster | 53.7% | 692.8 MB | 7ea77e<br>2026-08-18 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.200s · Slow | no baseline | parity | 17.6% | 852.0 MB | 7ea77e<br>2026-08-18 |
| Returning user (Status community member) | Browser | Not tested | Not tested | — | — | — | — | — |

## New user profile

Newly created user profile (no-preseeded user data)

### User data profile

- **Stored data:** No pre-seeded data
- **Wallet:** 1 wallet accounts · 0 tokens with balance > 0 · 0 NFTs · 0 transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 0 joined communities · 0 spectated communities

### Wallet

![Time to open Wallet for the first time after login](./wallet_first_open_time_fresh.png)

![CPU usage while opening Wallet for the first time after login](./wallet_first_open_cpu_fresh.png)

![RAM usage while opening Wallet for the first time after login](./wallet_first_open_ram_fresh.png)

![Time to reopen Wallet in the same session](./wallet_repeat_open_time_fresh.png)

![CPU usage while reopening Wallet in the same session](./wallet_repeat_open_cpu_fresh.png)

![RAM usage while reopening Wallet in the same session](./wallet_repeat_open_ram_fresh.png)

![Time to open a Wallet account for the first time in the session](./wallet_account_first_open_time_fresh.png)

![CPU usage while opening a Wallet account for the first time in the session](./wallet_account_first_open_cpu_fresh.png)

![RAM usage while opening a Wallet account for the first time in the session](./wallet_account_first_open_ram_fresh.png)

![Time to open the Add account modal for the first time in the session](./wallet_add_account_first_open_time_fresh.png)

![CPU usage while opening the Add account modal for the first time in the session](./wallet_add_account_first_open_cpu_fresh.png)

![RAM usage while opening the Add account modal for the first time in the session](./wallet_add_account_first_open_ram_fresh.png)

![Time to reopen the Add account modal in the same session](./wallet_add_account_time_fresh.png)

![CPU usage while reopening the Add account modal in the same session](./wallet_add_account_cpu_fresh.png)

![RAM usage while reopening the Add account modal in the same session](./wallet_add_account_ram_fresh.png)

![Time to open the Receive modal for the first time in the session](./wallet_receive_first_open_time_fresh.png)

![CPU usage while opening the Receive modal for the first time in the session](./wallet_receive_first_open_cpu_fresh.png)

![RAM usage while opening the Receive modal for the first time in the session](./wallet_receive_first_open_ram_fresh.png)

![Time to reopen the Receive modal in the same session](./wallet_receive_time_fresh.png)

![CPU usage while reopening the Receive modal in the same session](./wallet_receive_cpu_fresh.png)

![RAM usage while reopening the Receive modal in the same session](./wallet_receive_ram_fresh.png)

![Time to open the Send modal for the first time in the session](./wallet_send_first_open_time_fresh.png)

![CPU usage while opening the Send modal for the first time in the session](./wallet_send_first_open_cpu_fresh.png)

![RAM usage while opening the Send modal for the first time in the session](./wallet_send_first_open_ram_fresh.png)

![Time to reopen the Send modal in the same session](./wallet_send_time_fresh.png)

![CPU usage while reopening the Send modal in the same session](./wallet_send_cpu_fresh.png)

![RAM usage while reopening the Send modal in the same session](./wallet_send_ram_fresh.png)

![Time to open the Swap modal for the first time in the session](./wallet_swap_first_open_time_fresh.png)

![CPU usage while opening the Swap modal for the first time in the session](./wallet_swap_first_open_cpu_fresh.png)

![RAM usage while opening the Swap modal for the first time in the session](./wallet_swap_first_open_ram_fresh.png)

![Time to reopen the Swap modal in the same session](./wallet_swap_time_fresh.png)

![CPU usage while reopening the Swap modal in the same session](./wallet_swap_cpu_fresh.png)

![RAM usage while reopening the Swap modal in the same session](./wallet_swap_ram_fresh.png)

![Time to open the Assets tab for the first time in the session](./wallet_assets_tab_first_open_time_fresh.png)

![CPU usage while opening the Assets tab for the first time in the session](./wallet_assets_tab_first_open_cpu_fresh.png)

![RAM usage while opening the Assets tab for the first time in the session](./wallet_assets_tab_first_open_ram_fresh.png)

![Time to reopen the Assets tab in the same session](./wallet_assets_tab_time_fresh.png)

![CPU usage while reopening the Assets tab in the same session](./wallet_assets_tab_cpu_fresh.png)

![RAM usage while reopening the Assets tab in the same session](./wallet_assets_tab_ram_fresh.png)

![Time to open the Collectibles tab for the first time in the session](./wallet_collectibles_tab_first_open_time_fresh.png)

![CPU usage while opening the Collectibles tab for the first time in the session](./wallet_collectibles_tab_first_open_cpu_fresh.png)

![RAM usage while opening the Collectibles tab for the first time in the session](./wallet_collectibles_tab_first_open_ram_fresh.png)

![Time to reopen the Collectibles tab in the same session](./wallet_collectibles_tab_time_fresh.png)

![CPU usage while reopening the Collectibles tab in the same session](./wallet_collectibles_tab_cpu_fresh.png)

![RAM usage while reopening the Collectibles tab in the same session](./wallet_collectibles_tab_ram_fresh.png)

![Time to open the History tab for the first time in the session](./wallet_activity_tab_first_open_time_fresh.png)

![CPU usage while opening the History tab for the first time in the session](./wallet_activity_tab_first_open_cpu_fresh.png)

![RAM usage while opening the History tab for the first time in the session](./wallet_activity_tab_first_open_ram_fresh.png)

![Time to reopen the History tab in the same session](./wallet_activity_tab_time_fresh.png)

![CPU usage while reopening the History tab in the same session](./wallet_activity_tab_cpu_fresh.png)

![RAM usage while reopening the History tab in the same session](./wallet_activity_tab_ram_fresh.png)

### Messenger

_Not tested for this user profile._

### Communities

_Not tested for this user profile._

### Browser

_Not tested for this user profile._

## Returning user (semi-heavy wallet account)

Returning user with semi-heavy wallet account (~34 MB user data).

### User data profile

- **Stored data:** ~34 MB
- **Wallet:** 3 wallet accounts · 83 tokens with balance > 0 · 166 NFTs · 736 transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 0 joined communities · 0 spectated communities

### Wallet

![Time to open Wallet for the first time after login](./wallet_first_open_time_wallet_load.png)

![CPU usage while opening Wallet for the first time after login](./wallet_first_open_cpu_wallet_load.png)

![RAM usage while opening Wallet for the first time after login](./wallet_first_open_ram_wallet_load.png)

![Time to reopen Wallet in the same session](./wallet_repeat_open_time_wallet_load.png)

![CPU usage while reopening Wallet in the same session](./wallet_repeat_open_cpu_wallet_load.png)

![RAM usage while reopening Wallet in the same session](./wallet_repeat_open_ram_wallet_load.png)

![Time to open a Wallet account for the first time in the session](./wallet_account_first_open_time_wallet_load.png)

![CPU usage while opening a Wallet account for the first time in the session](./wallet_account_first_open_cpu_wallet_load.png)

![RAM usage while opening a Wallet account for the first time in the session](./wallet_account_first_open_ram_wallet_load.png)

![Time to open the Add account modal for the first time in the session](./wallet_add_account_first_open_time_wallet_load.png)

![CPU usage while opening the Add account modal for the first time in the session](./wallet_add_account_first_open_cpu_wallet_load.png)

![RAM usage while opening the Add account modal for the first time in the session](./wallet_add_account_first_open_ram_wallet_load.png)

![Time to reopen the Add account modal in the same session](./wallet_add_account_time_wallet_load.png)

![CPU usage while reopening the Add account modal in the same session](./wallet_add_account_cpu_wallet_load.png)

![RAM usage while reopening the Add account modal in the same session](./wallet_add_account_ram_wallet_load.png)

![Time to open the Receive modal for the first time in the session](./wallet_receive_first_open_time_wallet_load.png)

![CPU usage while opening the Receive modal for the first time in the session](./wallet_receive_first_open_cpu_wallet_load.png)

![RAM usage while opening the Receive modal for the first time in the session](./wallet_receive_first_open_ram_wallet_load.png)

![Time to reopen the Receive modal in the same session](./wallet_receive_time_wallet_load.png)

![CPU usage while reopening the Receive modal in the same session](./wallet_receive_cpu_wallet_load.png)

![RAM usage while reopening the Receive modal in the same session](./wallet_receive_ram_wallet_load.png)

![Time to open the Send modal for the first time in the session](./wallet_send_first_open_time_wallet_load.png)

![CPU usage while opening the Send modal for the first time in the session](./wallet_send_first_open_cpu_wallet_load.png)

![RAM usage while opening the Send modal for the first time in the session](./wallet_send_first_open_ram_wallet_load.png)

![Time to reopen the Send modal in the same session](./wallet_send_time_wallet_load.png)

![CPU usage while reopening the Send modal in the same session](./wallet_send_cpu_wallet_load.png)

![RAM usage while reopening the Send modal in the same session](./wallet_send_ram_wallet_load.png)

![Time to open the Swap modal for the first time in the session](./wallet_swap_first_open_time_wallet_load.png)

![CPU usage while opening the Swap modal for the first time in the session](./wallet_swap_first_open_cpu_wallet_load.png)

![RAM usage while opening the Swap modal for the first time in the session](./wallet_swap_first_open_ram_wallet_load.png)

![Time to reopen the Swap modal in the same session](./wallet_swap_time_wallet_load.png)

![CPU usage while reopening the Swap modal in the same session](./wallet_swap_cpu_wallet_load.png)

![RAM usage while reopening the Swap modal in the same session](./wallet_swap_ram_wallet_load.png)

![Time to open the Assets tab for the first time in the session](./wallet_assets_tab_first_open_time_wallet_load.png)

![CPU usage while opening the Assets tab for the first time in the session](./wallet_assets_tab_first_open_cpu_wallet_load.png)

![RAM usage while opening the Assets tab for the first time in the session](./wallet_assets_tab_first_open_ram_wallet_load.png)

![Time to reopen the Assets tab in the same session](./wallet_assets_tab_time_wallet_load.png)

![CPU usage while reopening the Assets tab in the same session](./wallet_assets_tab_cpu_wallet_load.png)

![RAM usage while reopening the Assets tab in the same session](./wallet_assets_tab_ram_wallet_load.png)

![Time to open the Collectibles tab for the first time in the session](./wallet_collectibles_tab_first_open_time_wallet_load.png)

![CPU usage while opening the Collectibles tab for the first time in the session](./wallet_collectibles_tab_first_open_cpu_wallet_load.png)

![RAM usage while opening the Collectibles tab for the first time in the session](./wallet_collectibles_tab_first_open_ram_wallet_load.png)

![Time to reopen the Collectibles tab in the same session](./wallet_collectibles_tab_time_wallet_load.png)

![CPU usage while reopening the Collectibles tab in the same session](./wallet_collectibles_tab_cpu_wallet_load.png)

![RAM usage while reopening the Collectibles tab in the same session](./wallet_collectibles_tab_ram_wallet_load.png)

![Time to open the History tab for the first time in the session](./wallet_activity_tab_first_open_time_wallet_load.png)

![CPU usage while opening the History tab for the first time in the session](./wallet_activity_tab_first_open_cpu_wallet_load.png)

![RAM usage while opening the History tab for the first time in the session](./wallet_activity_tab_first_open_ram_wallet_load.png)

![Time to reopen the History tab in the same session](./wallet_activity_tab_time_wallet_load.png)

![CPU usage while reopening the History tab in the same session](./wallet_activity_tab_cpu_wallet_load.png)

![RAM usage while reopening the History tab in the same session](./wallet_activity_tab_ram_wallet_load.png)

### Messenger

_Not tested for this user profile._

### Communities

_Not tested for this user profile._

### Browser

_Not tested for this user profile._

## Returning user (heavy account from Alex)

Returning user with heavy account from Alex (~35 MB user data).

### User data profile

- **Stored data:** ~35 MB
- **Wallet:** 4 wallet accounts · 144 tokens with balance > 0 · 773 NFTs · 5239 transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 0 joined communities · 0 spectated communities

### Wallet

![Time to open Wallet for the first time after login](./wallet_first_open_time_wallet_load_alex.png)

![CPU usage while opening Wallet for the first time after login](./wallet_first_open_cpu_wallet_load_alex.png)

![RAM usage while opening Wallet for the first time after login](./wallet_first_open_ram_wallet_load_alex.png)

![Time to reopen Wallet in the same session](./wallet_repeat_open_time_wallet_load_alex.png)

![CPU usage while reopening Wallet in the same session](./wallet_repeat_open_cpu_wallet_load_alex.png)

![RAM usage while reopening Wallet in the same session](./wallet_repeat_open_ram_wallet_load_alex.png)

![Time to open a Wallet account for the first time in the session](./wallet_account_first_open_time_wallet_load_alex.png)

![CPU usage while opening a Wallet account for the first time in the session](./wallet_account_first_open_cpu_wallet_load_alex.png)

![RAM usage while opening a Wallet account for the first time in the session](./wallet_account_first_open_ram_wallet_load_alex.png)

![Time to open the Add account modal for the first time in the session](./wallet_add_account_first_open_time_wallet_load_alex.png)

![CPU usage while opening the Add account modal for the first time in the session](./wallet_add_account_first_open_cpu_wallet_load_alex.png)

![RAM usage while opening the Add account modal for the first time in the session](./wallet_add_account_first_open_ram_wallet_load_alex.png)

![Time to reopen the Add account modal in the same session](./wallet_add_account_time_wallet_load_alex.png)

![CPU usage while reopening the Add account modal in the same session](./wallet_add_account_cpu_wallet_load_alex.png)

![RAM usage while reopening the Add account modal in the same session](./wallet_add_account_ram_wallet_load_alex.png)

![Time to open the Receive modal for the first time in the session](./wallet_receive_first_open_time_wallet_load_alex.png)

![CPU usage while opening the Receive modal for the first time in the session](./wallet_receive_first_open_cpu_wallet_load_alex.png)

![RAM usage while opening the Receive modal for the first time in the session](./wallet_receive_first_open_ram_wallet_load_alex.png)

![Time to reopen the Receive modal in the same session](./wallet_receive_time_wallet_load_alex.png)

![CPU usage while reopening the Receive modal in the same session](./wallet_receive_cpu_wallet_load_alex.png)

![RAM usage while reopening the Receive modal in the same session](./wallet_receive_ram_wallet_load_alex.png)

![Time to open the Send modal for the first time in the session](./wallet_send_first_open_time_wallet_load_alex.png)

![CPU usage while opening the Send modal for the first time in the session](./wallet_send_first_open_cpu_wallet_load_alex.png)

![RAM usage while opening the Send modal for the first time in the session](./wallet_send_first_open_ram_wallet_load_alex.png)

![Time to reopen the Send modal in the same session](./wallet_send_time_wallet_load_alex.png)

![CPU usage while reopening the Send modal in the same session](./wallet_send_cpu_wallet_load_alex.png)

![RAM usage while reopening the Send modal in the same session](./wallet_send_ram_wallet_load_alex.png)

![Time to open the Swap modal for the first time in the session](./wallet_swap_first_open_time_wallet_load_alex.png)

![CPU usage while opening the Swap modal for the first time in the session](./wallet_swap_first_open_cpu_wallet_load_alex.png)

![RAM usage while opening the Swap modal for the first time in the session](./wallet_swap_first_open_ram_wallet_load_alex.png)

![Time to reopen the Swap modal in the same session](./wallet_swap_time_wallet_load_alex.png)

![CPU usage while reopening the Swap modal in the same session](./wallet_swap_cpu_wallet_load_alex.png)

![RAM usage while reopening the Swap modal in the same session](./wallet_swap_ram_wallet_load_alex.png)

![Time to open the Assets tab for the first time in the session](./wallet_assets_tab_first_open_time_wallet_load_alex.png)

![CPU usage while opening the Assets tab for the first time in the session](./wallet_assets_tab_first_open_cpu_wallet_load_alex.png)

![RAM usage while opening the Assets tab for the first time in the session](./wallet_assets_tab_first_open_ram_wallet_load_alex.png)

![Time to reopen the Assets tab in the same session](./wallet_assets_tab_time_wallet_load_alex.png)

![CPU usage while reopening the Assets tab in the same session](./wallet_assets_tab_cpu_wallet_load_alex.png)

![RAM usage while reopening the Assets tab in the same session](./wallet_assets_tab_ram_wallet_load_alex.png)

![Time to open the Collectibles tab for the first time in the session](./wallet_collectibles_tab_first_open_time_wallet_load_alex.png)

![CPU usage while opening the Collectibles tab for the first time in the session](./wallet_collectibles_tab_first_open_cpu_wallet_load_alex.png)

![RAM usage while opening the Collectibles tab for the first time in the session](./wallet_collectibles_tab_first_open_ram_wallet_load_alex.png)

![Time to reopen the Collectibles tab in the same session](./wallet_collectibles_tab_time_wallet_load_alex.png)

![CPU usage while reopening the Collectibles tab in the same session](./wallet_collectibles_tab_cpu_wallet_load_alex.png)

![RAM usage while reopening the Collectibles tab in the same session](./wallet_collectibles_tab_ram_wallet_load_alex.png)

![Time to open the History tab for the first time in the session](./wallet_activity_tab_first_open_time_wallet_load_alex.png)

![CPU usage while opening the History tab for the first time in the session](./wallet_activity_tab_first_open_cpu_wallet_load_alex.png)

![RAM usage while opening the History tab for the first time in the session](./wallet_activity_tab_first_open_ram_wallet_load_alex.png)

![Time to reopen the History tab in the same session](./wallet_activity_tab_time_wallet_load_alex.png)

![CPU usage while reopening the History tab in the same session](./wallet_activity_tab_cpu_wallet_load_alex.png)

![RAM usage while reopening the History tab in the same session](./wallet_activity_tab_ram_wallet_load_alex.png)

### Messenger

_Not tested for this user profile._

### Communities

_Not tested for this user profile._

### Browser

_Not tested for this user profile._

## Returning user (Status community member)

Returning user with Status community already joined.

### User data profile

- **Stored data:** TBD
- **Wallet:** 1 wallet accounts · 0 tokens with balance > 0 · 0 NFTs · 0 transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 1 joined communities · 0 spectated communities

### Wallet

_Not tested for this user profile._

### Messenger

_Not tested for this user profile._

### Communities

![Time to open Status community for the first time after login](./community_first_open_loading_time_member.png)

![Time to reopen Status community in the same session](./community_second_open_loading_time_member.png)

![CPU usage while opening Status community for the first time after login](./community_first_open_cpu_member.png)

![CPU usage while reopening Status community in the same session](./community_second_open_cpu_member.png)

![RAM usage while opening Status community for the first time after login](./community_first_open_ram_member.png)

![RAM usage while reopening Status community in the same session](./community_second_open_ram_member.png)

### Browser

_Not tested for this user profile._

---

Generated by `scripts/benchmark.py graphs` from `data/`. Refreshed nightly by Jenkins.
