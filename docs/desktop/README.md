# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** This README renders inline PNG images on GitHub — works without
> GitHub Pages. For interactive charts (hover tooltips, zoom), use the
> [interactive dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) once GitHub Pages is enabled.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

## System info

**Host:** WINDOWS-NODE-01 · **Windows:** Windows Server 2022 Standard 21H2 · **OS build:** 20348.1487 · **CPU:** AMD Ryzen 7 PRO 8700GE w/ Radeon 780M Graphics · **RAM:** 63 GB

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Ok near slow** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.381s · Fast | parity | 33.1% | 673.5 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.512s · Ok | +0.133s slower | 25.8% | 764.2 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.142s · Fast | parity | 57.8% | 783.1 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.683s · Ok | parity | 40.7% | 692.3 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.520s · Ok | +0.106s slower | 65.3% | 735.2 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.580s · Ok | +0.109s slower | 26.6% | 811.6 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.262s · Fast | parity | 33.5% | 807.2 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.028s · Slow | +0.140s slower | 25.6% | 798.6 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.336s · Fast | -0.162s faster | 22.3% | 841.5 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.182s · Slow | -0.377s faster | 34.8% | 853.0 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.346s · Fast | -0.223s faster | 33.3% | 849.3 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.206s · Fast | no baseline | 16.7% | 658.1 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.409s · Fast | no baseline | 34.4% | 716.8 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 16.046s · Slow | no baseline | 36.1% | 766.2 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.190s · Fast | no baseline | 31.7% | 766.8 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.214s · Fast | no baseline | 42.6% | 671.2 MB | 403e647e7<br>2026-08-06 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.233s · Fast | no baseline | 34.2% | 711.1 MB | 403e647e7<br>2026-08-06 |
| New user profile | Messenger | Not tested | Not tested | — | — | — | — |
| New user profile | Communities | Not tested | Not tested | — | — | — | — |
| New user profile | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.571s · Ok | +0.087s slower | 48.5% | 784.2 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.627s · Ok | parity | 43.1% | 892.7 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.330s · Fast | -0.072s faster | 40.7% | 766.6 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.538s · Ok | -0.211s faster | 60.7% | 758.0 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.466s · Fast | parity | 38.2% | 763.8 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.754s · Ok | -0.168s faster | 31.4% | 806.4 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.314s · Fast | parity | 50.3% | 766.8 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.653s · Slow | parity | 41.2% | 791.3 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.561s · Ok | -0.120s faster | 24.3% | 772.1 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.480s · Fast | -0.887s faster | 48.7% | 801.0 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.540s · Ok | parity | 37.0% | 790.0 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.616s · Ok | no baseline | 61.0% | 740.3 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 1.567s · Slow | no baseline | 46.0% | 1109.6 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 7.264s · Slow | no baseline | 51.6% | 1453.1 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 6.592s · Slow | no baseline | 41.6% | 1206.6 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.956s · Ok | no baseline | 49.6% | 756.9 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.743s · Ok | no baseline | 41.2% | 765.1 MB | 403e647e7<br>2026-08-06 |
| Returning user (semi-heavy wallet account) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.418s · Fast | +0.193s slower | 36.4% | 847.1 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.598s · Ok | parity | 41.6% | 902.4 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.477s · Fast | +0.130s slower | 39.2% | 760.8 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.534s · Ok | -0.275s faster | 59.8% | 859.8 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.496s · Fast | parity | 64.9% | 812.8 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.595s · Ok | -0.355s faster | 42.3% | 801.9 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.364s · Fast | parity | 58.7% | 788.5 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.195s · Slow | -0.575s faster | 33.5% | 781.3 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.645s · Ok | parity | 54.1% | 782.7 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.616s · Ok | -0.682s faster | 35.4% | 783.9 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.594s · Ok | +0.080s slower | 61.4% | 825.5 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 1.321s · Slow | no baseline | 45.1% | 768.8 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 1.580s · Slow | no baseline | 50.7% | 1282.4 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 7.016s · Slow | no baseline | 56.8% | 1973.2 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 19.906s · Slow | no baseline | 49.6% | 1645.4 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.679s · Ok | no baseline | 36.7% | 769.8 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.709s · Ok | no baseline | 51.6% | 806.7 MB | 403e647e7<br>2026-08-06 |
| Returning user (heavy account from Alex) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Wallet | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 4.028s · Slow | parity | 26.5% | 822.8 MB | 403e647e7<br>2026-08-06 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.232s · Slow | parity | 28.9% | 920.2 MB | 403e647e7<br>2026-08-06 |
| Returning user (Status community member) | Browser | Not tested | Not tested | — | — | — | — |

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
