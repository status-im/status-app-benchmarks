# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** This README renders inline PNG images on GitHub — works without
> GitHub Pages. For interactive charts (hover tooltips, zoom), use the
> [interactive dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) once GitHub Pages is enabled.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 06, 2026 · [`3ddecdb8b`](https://github.com/status-im/status-app/commit/3ddecdb8bb372b3046b575909e13f996258b1e0e)

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.605s · Ok | +0.233s slower | 75.5% | 772.0 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.674s · Ok | +0.295s slower | 73.0% | 830.8 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.133s · Fast | -0.024s faster | 7.3% | 700.2 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.438s · Fast | -0.173s faster | 10.6% | 824.7 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.451s · Fast | parity | 14.2% | 813.8 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.398s · Fast | -0.073s faster | 35.4% | 708.3 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.456s · Fast | +0.154s slower | 20.6% | 760.3 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.007s · Slow | parity | 28.1% | 691.9 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.354s · Fast | -0.144s faster | 28.2% | 801.6 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.979s · Near ok | -0.580s faster | 25.9% | 805.0 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.313s · Fast | -0.256s faster | 17.3% | 805.0 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.127s · Fast | no baseline | 4.4% | 696.5 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.352s · Fast | no baseline | 70.7% | 755.0 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.303s · Fast | no baseline | 12.5% | 700.3 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.310s · Fast | no baseline | 24.7% | 764.5 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.202s · Fast | no baseline | 13.2% | 729.5 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.250s · Fast | no baseline | 38.5% | 780.8 MB | 3ddecdb8b<br>2026-09-06 |
| New user profile | Messenger | Not tested | Not tested | — | — | — | — |
| New user profile | Communities | Not tested | Not tested | — | — | — | — |
| New user profile | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.643s · Ok | +0.159s slower | 41.2% | 832.9 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.861s · Ok | +0.281s slower | 71.4% | 822.4 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.320s · Fast | -0.082s faster | 18.6% | 770.4 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.623s · Ok | -0.126s faster | 48.7% | 898.1 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.456s · Fast | parity | 45.3% | 803.1 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.552s · Ok | -0.370s faster | 42.8% | 756.9 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.339s · Fast | parity | 43.2% | 743.0 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.408s · Slow | -0.382s faster | 25.6% | 800.9 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.599s · Ok | parity | 30.2% | 783.8 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.978s · Near ok | -0.389s faster | 42.9% | 827.3 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.435s · Fast | -0.097s faster | 33.0% | 809.4 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.422s · Fast | no baseline | 85.4% | 763.3 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.731s · Ok | no baseline | 63.1% | 758.1 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.966s · Slow | no baseline | 43.9% | 844.5 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 1.404s · Slow | no baseline | 55.8% | 823.0 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.800s · Ok | no baseline | 55.1% | 833.1 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.723s · Ok | no baseline | 61.6% | 804.2 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (semi-heavy wallet account) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.401s · Fast | +0.176s slower | 49.2% | 823.9 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.868s · Ok | +0.285s slower | 68.3% | 834.9 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.962s · Near ok | +0.615s slower | 53.4% | 835.3 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.946s · Near ok | +0.137s slower | 51.2% | 794.0 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.547s · Ok | +0.112s slower | 65.5% | 850.6 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.565s · Ok | -0.385s faster | 51.0% | 823.9 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.356s · Fast | parity | 64.3% | 840.2 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.497s · Slow | -0.273s faster | 47.0% | 821.6 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.504s · Ok | -0.159s faster | 41.6% | 817.2 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 1.136s · Slow | parity | 69.1% | 885.9 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.592s · Ok | +0.078s slower | 39.5% | 894.5 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.911s · Near ok | no baseline | 56.2% | 827.2 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.794s · Ok | no baseline | 69.4% | 838.1 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.309s · Fast | no baseline | 74.1% | 871.8 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.779s · Ok | no baseline | 68.5% | 821.2 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.691s · Ok | no baseline | 44.0% | 818.5 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.776s · Ok | no baseline | 66.7% | 844.4 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (heavy account from Alex) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Wallet | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 2.701s · Slow | -1.074s faster | 53.8% | 795.1 MB | 3ddecdb8b<br>2026-09-06 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.190s · Slow | parity | 52.7% | 858.2 MB | 3ddecdb8b<br>2026-09-06 |
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
