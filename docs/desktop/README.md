# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** This README renders inline PNG images on GitHub — works without
> GitHub Pages. For interactive charts (hover tooltips, zoom), use the
> [interactive dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) once GitHub Pages is enabled.

Full CSV history: [`data/`](../../data/).

## System info

**Host:** WINDOWS-NODE-01 · **Windows:** Windows Server 2022 Standard 21H2 · **OS build:** 20348.1487 · **CPU:** AMD Ryzen 7 PRO 8700GE w/ Radeon 780M Graphics · **RAM:** 63 GB

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Ok near slow** · **>1.0s Slow**

Reference parity means the latest value is within ±15% of 2.38.0.

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.466s · Fast | no baseline | 12.9% | 668.7 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.482s · Fast | parity | 39.5% | 830.2 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.162s · Fast | no baseline | 77.7% | 743.9 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.582s · Ok | no baseline | 22.6% | 780.2 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.487s · Fast | no baseline | 64.7% | 853.0 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.895s · Ok | no baseline | 43.1% | 767.5 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.309s · Fast | no baseline | 51.4% | 775.2 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.503s · Slow | no baseline | 46.0% | 763.3 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.607s · Ok | no baseline | 57.1% | 808.8 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.630s · Slow | no baseline | 50.8% | 716.5 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.709s · Ok | parity | 62.0% | 782.5 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.316s · Fast | no baseline | 25.1% | 796.9 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 17.036s · Slow | no baseline | 36.3% | 730.1 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.192s · Fast | no baseline | 42.8% | 742.6 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.135s · Fast | no baseline | 47.0% | 768.2 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.192s · Fast | no baseline | 39.2% | 770.3 MB | 0e23fd3cc · 2026-07-17 |
| New user profile | Messenger | Not tested | Not tested | — | — | — | — |
| New user profile | Communities | Not tested | Not tested | — | — | — | — |
| New user profile | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.647s · Ok | no baseline | 37.4% | 695.1 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.694s · Ok | parity | 51.2% | 856.5 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.407s · Fast | no baseline | 33.1% | 700.2 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.605s · Ok | no baseline | 40.0% | 699.4 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.500s · Ok | no baseline | 62.8% | 734.8 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.537s · Ok | no baseline | 20.0% | 695.0 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.339s · Fast | no baseline | 52.4% | 730.9 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.492s · Slow | no baseline | 49.6% | 769.4 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.995s · Ok | no baseline | 66.1% | 797.8 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 1.154s · Slow | no baseline | 26.5% | 712.4 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.728s · Ok | parity | 64.3% | 795.3 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.705s · Ok | no baseline | 36.5% | 786.6 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 20.407s · Slow | no baseline | 38.2% | 751.9 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.760s · Ok | no baseline | 44.2% | 875.2 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.790s · Ok | no baseline | 34.3% | 707.6 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.770s · Ok | no baseline | 56.4% | 777.0 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (heavy wallet account) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.338s · Fast | no baseline | 42.6% | 807.4 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.764s · Ok | parity | 39.5% | 883.6 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.347s · Fast | no baseline | 32.8% | 793.1 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.962s · Ok | no baseline | 45.4% | 824.2 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.497s · Fast | no baseline | 61.6% | 834.9 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 1.355s · Slow | no baseline | 44.2% | 804.1 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.345s · Fast | no baseline | 66.5% | 836.1 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 2.019s · Slow | no baseline | 22.5% | 860.8 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.974s · Ok | no baseline | 64.6% | 875.1 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 1.569s · Slow | no baseline | 51.8% | 844.1 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.734s · Ok | parity | 71.3% | 880.1 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.952s · Ok | no baseline | 49.5% | 908.6 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 41.000s · Slow | no baseline | 39.1% | 880.5 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 2.545s · Slow | no baseline | 56.2% | 1128.5 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.757s · Ok | no baseline | 37.9% | 890.2 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.726s · Ok | no baseline | 45.0% | 912.6 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Wallet | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.954s · Slow | parity | 17.2% | 748.5 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.287s · Slow | parity | 11.2% | 989.4 MB | 0e23fd3cc · 2026-07-17 |
| Returning user (Status community member) | Browser | Not tested | Not tested | — | — | — | — |

## New user profile

Newly created user profile (no-preseeded user data)

### User data profile

- **Stored data:** No pre-seeded data
- **Wallet:** 0 tokens with balance > 0 · 0 NFTs · 0 transactions
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

## Returning user (heavy wallet account)

Returning user with wallet_load profile (~29 MB user data).

### User data profile

- **Stored data:** ~29 MB
- **Wallet:** TBD tokens with balance > 0 · TBD NFTs · TBD transactions
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

## Returning user (medium heavy wallet account from Alex)

Returning user with wallet_load_alex profile (~16 MB user data).

### User data profile

- **Stored data:** ~16 MB
- **Wallet:** TBD tokens with balance > 0 · TBD NFTs · TBD transactions
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
- **Wallet:** 0 tokens with balance > 0 · 0 NFTs · 0 transactions
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
