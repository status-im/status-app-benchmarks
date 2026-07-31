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
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.420s · Fast | parity | 26.8% | 713.9 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.518s · Ok | +0.139s slower | 47.0% | 842.5 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.160s · Fast | parity | 35.3% | 702.2 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.682s · Ok | parity | 49.4% | 754.1 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.612s · Ok | +0.198s slower | 52.9% | 772.5 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.460s · Fast | parity | 31.4% | 741.5 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.368s · Fast | +0.066s slower | 54.6% | 743.3 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.078s · Slow | +0.190s slower | 44.0% | 726.0 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.377s · Fast | -0.121s faster | 67.5% | 738.0 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.318s · Slow | -0.241s faster | 48.5% | 742.9 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.368s · Fast | -0.201s faster | 58.9% | 792.5 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 13.547s · Slow | no baseline | 56.7% | 693.2 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.344s · Fast | no baseline | 29.8% | 729.5 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 16.008s · Slow | no baseline | 35.9% | 735.7 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.176s · Fast | no baseline | 52.8% | 758.8 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.220s · Fast | no baseline | 36.7% | 683.4 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.213s · Fast | no baseline | 42.0% | 682.8 MB | 4d5f214a1<br>2026-07-31 |
| New user profile | Messenger | Not tested | Not tested | — | — | — | — |
| New user profile | Communities | Not tested | Not tested | — | — | — | — |
| New user profile | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.334s · Fast | -0.150s faster | 36.1% | 679.3 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.575s · Ok | parity | 53.3% | 868.9 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.405s · Fast | parity | 29.1% | 690.6 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.594s · Ok | -0.155s faster | 53.7% | 701.3 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.488s · Fast | parity | 61.3% | 732.9 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.736s · Ok | -0.186s faster | 38.2% | 769.4 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.316s · Fast | parity | 39.8% | 756.8 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.507s · Slow | -0.283s faster | 38.1% | 767.2 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.743s · Ok | parity | 64.6% | 782.2 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 1.246s · Slow | parity | 35.6% | 740.9 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.415s · Fast | -0.117s faster | 61.5% | 767.8 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 21.523s · Slow | no baseline | 64.3% | 713.8 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 1.055s · Slow | no baseline | 36.3% | 1141.3 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 40.689s · Slow | no baseline | 44.1% | 1552.4 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 1.734s · Slow | no baseline | 43.5% | 1136.6 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.740s · Ok | no baseline | 61.0% | 760.4 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.683s · Ok | no baseline | 59.2% | 775.0 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (semi-heavy wallet account) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.282s · Fast | +0.057s slower | 33.6% | 736.5 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.620s · Ok | parity | 51.6% | 921.6 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.418s · Fast | +0.071s slower | 34.3% | 774.9 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.623s · Ok | -0.186s faster | 45.0% | 740.9 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.470s · Fast | parity | 56.2% | 760.6 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.513s · Ok | -0.437s faster | 36.4% | 714.1 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.311s · Fast | parity | 41.4% | 752.6 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.173s · Slow | -0.597s faster | 37.9% | 709.8 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.490s · Fast | -0.173s faster | 45.8% | 790.2 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.777s · Ok | -0.521s faster | 40.1% | 699.1 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.426s · Fast | -0.088s faster | 67.9% | 779.7 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.554s · Ok | no baseline | 55.0% | 771.1 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 1.309s · Slow | no baseline | 58.2% | 1283.3 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 69.592s · Slow | no baseline | 47.1% | 3481.4 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 21.113s · Slow | no baseline | 49.0% | 1281.1 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.733s · Ok | no baseline | 35.1% | 773.1 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.676s · Ok | no baseline | 62.9% | 796.7 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (heavy account from Alex) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Wallet | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 2.839s · Slow | -0.936s faster | 35.5% | 750.0 MB | 4d5f214a1<br>2026-07-31 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.129s · Slow | parity | 37.0% | 835.9 MB | 4d5f214a1<br>2026-07-31 |
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
