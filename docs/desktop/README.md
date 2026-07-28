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
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.398s · Fast | parity | 15.8% | 667.5 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.437s · Fast | +0.058s slower | 45.0% | 742.2 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.176s · Fast | parity | 52.3% | 723.7 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.655s · Ok | parity | 34.4% | 662.8 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.470s · Fast | parity | 61.7% | 722.4 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.423s · Fast | parity | 33.2% | 665.8 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.311s · Fast | parity | 58.6% | 679.7 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 0.718s · Ok | -0.170s faster | 33.0% | 740.7 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.404s · Fast | -0.094s faster | 60.5% | 749.8 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.359s · Slow | parity | 36.6% | 698.1 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.389s · Fast | -0.179s faster | 65.4% | 779.4 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.358s · Fast | no baseline | 34.8% | 726.0 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 17.456s · Slow | no baseline | 35.4% | 708.3 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.164s · Fast | no baseline | 46.7% | 749.3 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.210s · Fast | no baseline | 52.0% | 686.7 MB | cf137ac67<br>2026-07-28 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.213s · Fast | no baseline | 36.8% | 691.2 MB | cf137ac67<br>2026-07-28 |
| New user profile | Messenger | Not tested | Not tested | — | — | — | — |
| New user profile | Communities | Not tested | Not tested | — | — | — | — |
| New user profile | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.307s · Fast | -0.177s faster | 46.1% | 708.2 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.556s · Ok | parity | 43.8% | 875.7 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.416s · Fast | parity | 25.9% | 670.7 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.577s · Ok | -0.172s faster | 44.6% | 755.2 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.486s · Fast | parity | 56.9% | 743.9 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.514s · Ok | -0.408s faster | 23.6% | 686.2 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.309s · Fast | parity | 37.2% | 695.7 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.821s · Slow | parity | 52.1% | 707.2 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.558s · Ok | -0.123s faster | 61.2% | 742.0 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 1.430s · Slow | parity | 50.5% | 775.8 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.475s · Fast | parity | 66.5% | 789.2 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 1.096s · Slow | no baseline | 52.3% | 1062.1 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 41.414s · Slow | no baseline | 44.6% | 1441.6 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 2.450s · Slow | no baseline | 42.0% | 1165.2 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.682s · Ok | no baseline | 45.0% | 688.6 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.631s · Ok | no baseline | 53.7% | 742.6 MB | cf137ac67<br>2026-07-28 |
| Returning user (heavy wallet account) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.218s · Fast | parity | 24.3% | 738.8 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.610s · Ok | parity | 46.6% | 870.3 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.437s · Fast | +0.090s slower | 48.5% | 717.7 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.614s · Ok | -0.195s faster | 46.6% | 734.8 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.451s · Fast | parity | 38.5% | 758.8 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.952s · Ok | parity | 52.6% | 704.5 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.337s · Fast | parity | 54.3% | 737.7 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.415s · Slow | -0.355s faster | 41.5% | 745.4 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.563s · Ok | -0.100s faster | 37.2% | 800.0 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 1.249s · Slow | parity | 51.1% | 762.0 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.497s · Fast | parity | 64.3% | 804.4 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 1.268s · Slow | no baseline | 57.7% | 1495.2 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 48.217s · Slow | no baseline | 48.4% | 2466.6 MB | 0b7c6c324<br>2026-07-27 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 6.345s · Slow | no baseline | 52.8% | 1609.5 MB | 0b7c6c324<br>2026-07-27 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.597s · Ok | no baseline | 49.4% | 748.8 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.638s · Ok | no baseline | 47.8% | 747.6 MB | cf137ac67<br>2026-07-28 |
| Returning user (medium heavy wallet account from Alex) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Wallet | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.251s · Slow | parity | 20.8% | 758.2 MB | cf137ac67<br>2026-07-28 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.130s · Slow | parity | 34.1% | 807.8 MB | cf137ac67<br>2026-07-28 |
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
