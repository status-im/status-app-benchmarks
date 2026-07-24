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
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.430s · Fast | +0.058s slower | 16.1% | 672.1 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.473s · Fast | +0.094s slower | 34.7% | 810.8 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.164s · Fast | parity | 29.3% | 729.9 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 1.093s · Slow | +0.482s slower | 48.9% | 664.1 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.477s · Fast | +0.063s slower | 59.5% | 698.3 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.432s · Fast | parity | 38.9% | 660.1 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.320s · Fast | parity | 56.2% | 719.4 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.373s · Slow | +0.485s slower | 40.0% | 678.4 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.663s · Ok | +0.165s slower | 67.3% | 714.0 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.457s · Slow | parity | 41.9% | 718.1 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.652s · Ok | parity | 65.1% | 728.0 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.414s · Fast | no baseline | 41.4% | 724.4 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 16.402s · Slow | no baseline | 37.6% | 762.4 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.184s · Fast | no baseline | 42.4% | 724.6 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.203s · Fast | no baseline | 61.8% | 754.6 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.221s · Fast | no baseline | 39.2% | 759.9 MB | 0c1c2b028<br>2026-07-24 |
| New user profile | Messenger | Not tested | Not tested | — | — | — | — |
| New user profile | Communities | Not tested | Not tested | — | — | — | — |
| New user profile | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.250s · Fast | -0.234s faster | 30.8% | 694.4 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.679s · Ok | +0.099s slower | 44.4% | 862.8 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.449s · Fast | parity | 39.5% | 683.6 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.707s · Ok | parity | 58.9% | 750.6 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.501s · Ok | parity | 62.7% | 763.1 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.560s · Ok | -0.362s faster | 39.9% | 693.2 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.369s · Fast | parity | 36.2% | 720.9 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 2.069s · Slow | +0.279s slower | 20.2% | 743.8 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.807s · Ok | +0.126s slower | 64.4% | 799.4 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 1.510s · Slow | parity | 36.8% | 718.4 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.721s · Ok | +0.189s slower | 69.4% | 798.5 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 1.248s · Slow | no baseline | 55.3% | 1131.0 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 39.150s · Slow | no baseline | 45.9% | 1434.6 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 1.946s · Slow | no baseline | 49.1% | 1200.5 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 1.052s · Slow | no baseline | 50.3% | 703.5 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.732s · Ok | no baseline | 61.2% | 784.6 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (heavy wallet account) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.538s · Ok | +0.313s slower | 27.2% | 741.8 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.743s · Ok | +0.160s slower | 46.0% | 925.2 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.419s · Fast | +0.072s slower | 49.4% | 718.5 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.841s · Ok | parity | 35.8% | 722.4 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.459s · Fast | parity | 41.3% | 761.2 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.486s · Fast | -0.464s faster | 33.4% | 703.9 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.352s · Fast | parity | 70.9% | 747.1 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.899s · Slow | parity | 47.6% | 774.7 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.925s · Ok | +0.262s slower | 42.0% | 866.8 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 1.998s · Slow | +0.700s slower | 46.1% | 756.4 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.765s · Ok | +0.251s slower | 31.6% | 830.6 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 1.322s · Slow | no baseline | 57.2% | 1324.9 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 52.066s · Slow | no baseline | 48.0% | 3117.6 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 11.603s · Slow | no baseline | 54.4% | 1588.7 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.692s · Ok | no baseline | 27.9% | 712.0 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.720s · Ok | no baseline | 63.0% | 797.4 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (medium heavy wallet account from Alex) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Wallet | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 4.167s · Slow | parity | 19.9% | 737.0 MB | 0c1c2b028<br>2026-07-24 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.106s · Slow | parity | 32.8% | 811.8 MB | 0c1c2b028<br>2026-07-24 |
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
