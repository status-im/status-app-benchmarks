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
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.431s · Fast | +0.059s slower | 16.3% | 724.7 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.433s · Fast | parity | 53.5% | 794.2 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.168s · Fast | parity | 34.9% | 757.8 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.666s · Ok | parity | 36.5% | 660.7 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.473s · Fast | parity | 56.7% | 690.6 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.477s · Fast | parity | 46.4% | 746.9 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.317s · Fast | parity | 55.8% | 760.4 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.157s · Slow | +0.269s slower | 46.4% | 659.2 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.510s · Ok | parity | 57.5% | 705.7 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.442s · Slow | parity | 56.2% | 816.3 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.517s · Ok | parity | 57.3% | 800.0 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.357s · Fast | no baseline | 37.2% | 751.6 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 16.435s · Slow | no baseline | 38.2% | 764.9 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.178s · Fast | no baseline | 34.2% | 760.1 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.230s · Fast | no baseline | 50.2% | 730.6 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.205s · Fast | no baseline | 49.6% | 735.9 MB | 8b23a3fe3<br>2026-07-29 |
| New user profile | Messenger | Not tested | Not tested | — | — | — | — |
| New user profile | Communities | Not tested | Not tested | — | — | — | — |
| New user profile | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.344s · Fast | -0.140s faster | 51.2% | 729.3 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.592s · Ok | parity | 40.4% | 891.1 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.440s · Fast | parity | 50.6% | 697.9 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.626s · Ok | -0.123s faster | 37.1% | 756.7 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.498s · Fast | parity | 66.0% | 751.9 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.489s · Fast | -0.433s faster | 36.8% | 721.3 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.304s · Fast | -0.059s faster | 37.8% | 728.8 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.269s · Slow | -0.521s faster | 30.5% | 759.7 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.538s · Ok | -0.143s faster | 61.8% | 784.0 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.794s · Ok | -0.573s faster | 35.8% | 702.6 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.424s · Fast | -0.108s faster | 62.8% | 778.2 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 1.113s · Slow | no baseline | 56.1% | 1055.0 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 40.209s · Slow | no baseline | 46.1% | 1407.6 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 1.963s · Slow | no baseline | 46.0% | 1164.1 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.616s · Ok | no baseline | 56.9% | 699.2 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.667s · Ok | no baseline | 60.6% | 753.9 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (heavy wallet account) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.270s · Fast | +0.045s slower | 45.5% | 714.9 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.597s · Ok | parity | 52.8% | 905.6 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.442s · Fast | +0.095s slower | 45.9% | 717.1 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.672s · Ok | -0.137s faster | 31.6% | 734.5 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.486s · Fast | parity | 63.1% | 767.8 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.622s · Ok | -0.328s faster | 28.6% | 730.8 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.356s · Fast | parity | 52.7% | 767.1 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.617s · Slow | parity | 50.0% | 766.1 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.546s · Ok | -0.117s faster | 68.9% | 810.6 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.729s · Ok | -0.569s faster | 40.4% | 703.5 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.414s · Fast | -0.100s faster | 65.9% | 786.6 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 1.234s · Slow | no baseline | 56.5% | 1281.6 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 56.774s · Slow | no baseline | 47.7% | 2984.0 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 16.857s · Slow | no baseline | 44.3% | 1176.8 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.647s · Ok | no baseline | 54.2% | 744.3 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.599s · Ok | no baseline | 55.9% | 761.6 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (medium heavy wallet account from Alex) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Wallet | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.531s · Slow | parity | 22.8% | 743.0 MB | 8b23a3fe3<br>2026-07-29 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.130s · Slow | parity | 35.0% | 819.5 MB | 8b23a3fe3<br>2026-07-29 |
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
