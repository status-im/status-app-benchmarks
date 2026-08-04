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
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.402s · Fast | parity | 24.7% | 677.7 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.470s · Fast | +0.091s slower | 36.7% | 842.3 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.175s · Fast | parity | 30.5% | 793.4 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.472s · Fast | -0.139s faster | 12.1% | 899.4 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.385s · Fast | parity | 16.2% | 852.9 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.475s · Fast | parity | 38.2% | 808.9 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.399s · Fast | +0.097s slower | 31.9% | 817.2 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 0.908s · Ok | parity | 37.0% | 769.2 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.379s · Fast | -0.119s faster | 48.4% | 803.5 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.671s · Slow | parity | 59.8% | 771.3 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.337s · Fast | -0.231s faster | 30.5% | 845.6 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.333s · Fast | no baseline | 45.4% | 673.1 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.358s · Fast | no baseline | 42.1% | 743.5 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 15.974s · Slow | no baseline | 39.5% | 798.7 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.185s · Fast | no baseline | 34.3% | 764.9 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.195s · Fast | no baseline | 57.0% | 800.3 MB | b53180ff9<br>2026-08-04 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.225s · Fast | no baseline | 34.3% | 822.1 MB | b53180ff9<br>2026-08-04 |
| New user profile | Messenger | Not tested | Not tested | — | — | — | — |
| New user profile | Communities | Not tested | Not tested | — | — | — | — |
| New user profile | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.334s · Fast | -0.150s faster | 19.0% | 738.2 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.592s · Ok | parity | 52.0% | 882.6 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.927s · Ok | +0.525s slower | 35.8% | 768.3 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.804s · Ok | parity | 63.7% | 747.3 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.471s · Fast | parity | 32.2% | 748.8 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.702s · Ok | -0.220s faster | 40.9% | 786.2 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.323s · Fast | parity | 42.9% | 755.3 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.262s · Slow | -0.528s faster | 29.9% | 730.7 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.595s · Ok | parity | 30.0% | 752.4 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.770s · Ok | -0.597s faster | 27.9% | 718.6 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.395s · Fast | -0.137s faster | 30.5% | 754.0 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.375s · Fast | no baseline | 60.9% | 726.3 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 1.288s · Slow | no baseline | 43.2% | 1047.7 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 22.188s · Slow | no baseline | 44.8% | 1538.5 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 2.051s · Slow | no baseline | 42.1% | 1113.7 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.677s · Ok | no baseline | 61.3% | 734.3 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.627s · Ok | no baseline | 39.0% | 771.1 MB | b53180ff9<br>2026-08-04 |
| Returning user (semi-heavy wallet account) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.335s · Fast | +0.110s slower | 46.1% | 745.4 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.612s · Ok | parity | 36.5% | 855.0 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.445s · Fast | +0.098s slower | 45.0% | 768.7 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.654s · Ok | -0.155s faster | 51.6% | 768.1 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.479s · Fast | parity | 58.9% | 779.7 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.498s · Fast | -0.452s faster | 32.7% | 773.5 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.349s · Fast | parity | 58.6% | 774.0 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.229s · Slow | -0.541s faster | 39.9% | 765.9 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.488s · Fast | -0.175s faster | 59.9% | 774.4 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.787s · Ok | -0.511s faster | 43.5% | 767.2 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.428s · Fast | -0.086s faster | 70.7% | 789.6 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 1.335s · Slow | no baseline | 24.5% | 780.3 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 1.316s · Slow | no baseline | 54.8% | 1225.0 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 37.456s · Slow | no baseline | 47.8% | 3079.2 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 14.540s · Slow | no baseline | 47.2% | 1210.4 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.707s · Ok | no baseline | 59.3% | 779.6 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.700s · Ok | no baseline | 62.0% | 821.1 MB | b53180ff9<br>2026-08-04 |
| Returning user (heavy account from Alex) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Wallet | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.617s · Slow | parity | 35.8% | 761.1 MB | b53180ff9<br>2026-08-04 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.091s · Slow | parity | 29.8% | 819.4 MB | b53180ff9<br>2026-08-04 |
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
