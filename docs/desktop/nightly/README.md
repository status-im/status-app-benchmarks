# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** This README renders inline PNG images on GitHub — works without
> GitHub Pages. For interactive charts (hover tooltips, zoom), use the
> [interactive dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) once GitHub Pages is enabled.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 02, 2026 · [`a11b7535f`](https://github.com/status-im/status-app/commit/a11b7535f68b5138fcabe40730d536b4f5be8083)

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.610s · Ok | +0.238s slower | 68.3% | 776.1 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.648s · Ok | +0.269s slower | 70.6% | 851.9 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.155s · Fast | parity | 3.5% | 809.0 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.586s · Ok | parity | 22.2% | 792.9 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.411s · Fast | parity | 11.9% | 775.3 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.389s · Fast | -0.082s faster | 37.1% | 707.4 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.297s · Fast | parity | 10.7% | 775.0 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 0.570s · Ok | -0.318s faster | 17.3% | 712.8 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.377s · Fast | -0.121s faster | 26.3% | 801.7 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.998s · Near ok | -0.561s faster | 28.2% | 711.7 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.313s · Fast | -0.256s faster | 19.2% | 806.7 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.151s · Fast | no baseline | 23.6% | 850.3 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.361s · Fast | no baseline | 57.4% | 824.5 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.384s · Fast | no baseline | 34.6% | 778.9 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.245s · Fast | no baseline | 48.7% | 806.0 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.264s · Fast | no baseline | 28.7% | 790.4 MB | a11b7535f<br>2026-09-02 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.286s · Fast | no baseline | 38.2% | 823.8 MB | a11b7535f<br>2026-09-02 |
| New user profile | Messenger | Not tested | Not tested | — | — | — | — |
| New user profile | Communities | Not tested | Not tested | — | — | — | — |
| New user profile | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.839s · Ok | +0.355s slower | 29.1% | 847.9 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.877s · Ok | +0.297s slower | 72.8% | 870.4 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.477s · Fast | +0.075s slower | 30.9% | 777.0 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.869s · Ok | +0.120s slower | 70.6% | 814.3 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.471s · Fast | parity | 34.7% | 793.9 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.973s · Near ok | parity | 40.4% | 782.9 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.331s · Fast | parity | 38.6% | 756.2 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.680s · Slow | parity | 50.3% | 794.3 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.469s · Fast | -0.212s faster | 27.7% | 764.2 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 1.098s · Slow | -0.269s faster | 37.1% | 792.0 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.470s · Fast | parity | 32.4% | 790.5 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.174s · Fast | no baseline | 62.7% | 852.3 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.807s · Ok | no baseline | 64.1% | 803.8 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 2.400s · Slow | no baseline | 42.2% | 807.3 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 1.284s · Slow | no baseline | 58.9% | 834.4 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.821s · Ok | no baseline | 68.4% | 873.2 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.821s · Ok | no baseline | 68.8% | 814.4 MB | a11b7535f<br>2026-09-02 |
| Returning user (semi-heavy wallet account) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (semi-heavy wallet account) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.794s · Ok | +0.569s slower | 73.6% | 914.5 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.917s · Near ok | +0.334s slower | 67.7% | 900.5 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.552s · Ok | +0.205s slower | 48.4% | 826.2 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.950s · Near ok | +0.141s slower | 53.3% | 822.6 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.504s · Ok | +0.069s slower | 60.2% | 853.3 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.560s · Ok | -0.390s faster | 49.7% | 852.9 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.355s · Fast | parity | 53.4% | 804.8 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.494s · Slow | -0.276s faster | 38.9% | 825.5 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.643s · Ok | parity | 68.1% | 850.4 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.710s · Ok | -0.588s faster | 46.0% | 812.3 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.622s · Ok | +0.108s slower | 55.5% | 861.7 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.358s · Fast | no baseline | 70.2% | 876.8 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.755s · Ok | no baseline | 69.5% | 861.3 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.666s · Ok | no baseline | 53.6% | 832.7 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.424s · Fast | no baseline | 72.1% | 856.2 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.795s · Ok | no baseline | 74.3% | 836.2 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.822s · Ok | no baseline | 75.7% | 856.6 MB | a11b7535f<br>2026-09-02 |
| Returning user (heavy account from Alex) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (heavy account from Alex) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Wallet | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 2.579s · Slow | -1.196s faster | 51.6% | 792.2 MB | a11b7535f<br>2026-09-02 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.188s · Slow | parity | 22.1% | 874.9 MB | a11b7535f<br>2026-09-02 |
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
