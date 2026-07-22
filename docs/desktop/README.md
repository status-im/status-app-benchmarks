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
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.453s · Fast | +0.081s slower | 11.6% | 801.2 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.486s · Fast | +0.107s slower | 43.2% | 842.9 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.464s · Fast | +0.307s slower | 50.0% | 769.4 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.608s · Ok | parity | 29.4% | 750.3 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.482s · Fast | +0.068s slower | 48.7% | 751.4 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.891s · Ok | +0.420s slower | 59.2% | 760.9 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.308s · Fast | parity | 62.0% | 752.3 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.507s · Slow | +0.619s slower | 45.6% | 811.6 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.604s · Ok | +0.106s slower | 51.3% | 789.0 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.953s · Slow | +0.394s slower | 44.0% | 804.4 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.644s · Ok | parity | 64.2% | 830.8 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.397s · Fast | no baseline | 37.0% | 805.7 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 16.545s · Slow | no baseline | 40.8% | 797.9 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.199s · Fast | no baseline | 31.7% | 760.5 MB | dbde82852<br>2026-07-22 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.177s · Fast | no baseline | 40.9% | 687.8 MB | abe104848<br>2026-07-22 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.171s · Fast | no baseline | 35.9% | 696.7 MB | abe104848<br>2026-07-22 |
| New user profile | Messenger | Not tested | Not tested | — | — | — | — |
| New user profile | Communities | Not tested | Not tested | — | — | — | — |
| New user profile | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.651s · Ok | +0.167s slower | 40.7% | 709.1 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.714s · Ok | +0.134s slower | 42.2% | 868.8 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.373s · Fast | parity | 18.2% | 710.8 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.649s · Ok | parity | 38.9% | 735.2 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.534s · Ok | parity | 59.9% | 751.9 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.574s · Ok | -0.348s faster | 35.2% | 699.8 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.321s · Fast | parity | 28.3% | 719.8 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.645s · Slow | parity | 63.6% | 755.5 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 1.097s · Slow | +0.416s slower | 66.9% | 784.0 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 1.541s · Slow | parity | 26.2% | 731.0 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.763s · Ok | +0.231s slower | 68.3% | 805.4 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 1.286s · Slow | no baseline | 58.6% | 1123.9 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 39.837s · Slow | no baseline | 44.0% | 1416.3 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 1.970s · Slow | no baseline | 50.0% | 1139.8 MB | dbde82852<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.777s · Ok | no baseline | 43.7% | 705.0 MB | abe104848<br>2026-07-22 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.732s · Ok | no baseline | 57.1% | 770.7 MB | abe104848<br>2026-07-22 |
| Returning user (heavy wallet account) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.316s · Fast | +0.091s slower | 32.5% | 730.2 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.783s · Ok | +0.200s slower | 48.5% | 906.8 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.466s · Fast | +0.119s slower | 39.8% | 737.4 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.656s · Ok | -0.153s faster | 49.9% | 747.1 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.510s · Ok | +0.075s slower | 56.8% | 787.7 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.979s · Ok | parity | 47.8% | 729.7 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.330s · Fast | parity | 48.6% | 793.6 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 2.049s · Slow | +0.279s slower | 25.9% | 785.0 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.970s · Ok | +0.307s slower | 37.3% | 873.8 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 1.887s · Slow | +0.589s slower | 52.8% | 787.6 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.878s · Ok | +0.364s slower | 40.9% | 863.7 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 1.324s · Slow | no baseline | 54.6% | 1400.6 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 49.568s · Slow | no baseline | 46.1% | 2757.3 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 7.651s · Slow | no baseline | 56.6% | 1611.3 MB | dbde82852<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.789s · Ok | no baseline | 45.8% | 753.4 MB | abe104848<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.887s · Ok | no baseline | 50.9% | 867.9 MB | abe104848<br>2026-07-22 |
| Returning user (medium heavy wallet account from Alex) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Wallet | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.649s · Slow | parity | 19.6% | 758.4 MB | dbde82852<br>2026-07-22 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.103s · Slow | parity | 32.6% | 844.9 MB | dbde82852<br>2026-07-22 |
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

Returning user with wallet_load profile (~34 MB user data).

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

Returning user with wallet_load_alex profile (~35 MB user data).

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
