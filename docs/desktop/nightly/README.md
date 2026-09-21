# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 21, 2026 · [`39901f54d`](https://github.com/status-im/status-app/commit/39901f54d783f9f17885e09976fffb3d5bb1aa77)

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.663s · Ok | +0.291s slower | 60.4% | 749.0 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.496s · Fast | +0.117s slower | 71.9% | 793.1 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.156s · Fast | parity | 62.7% | 695.2 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.478s · Fast | -0.133s faster | 26.8% | 728.6 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.384s · Fast | parity | 18.1% | 782.5 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.294s · Fast | -0.177s faster | 21.4% | 729.9 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.289s · Fast | parity | 10.5% | 779.6 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 0.991s · Near ok | parity | 38.3% | 745.5 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.659s · Ok | +0.161s slower | 24.9% | 850.1 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.024s · Slow | -0.535s faster | 41.8% | 736.9 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.798s · Ok | +0.229s slower | 23.1% | 885.4 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.142s · Fast | no baseline | 78.1% | 675.3 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.172s · Fast | no baseline | 39.8% | 709.4 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.250s · Fast | no baseline | 30.5% | 695.2 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.115s · Fast | no baseline | 45.2% | 691.5 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.249s · Fast | no baseline | 57.3% | 766.3 MB | 39901f54d<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.111s · Fast | no baseline | 17.9% | 782.0 MB | 39901f54d<br>2026-09-21 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | — · No data | — | — | — | — |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | — · No data | — | — | — | — |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | — · No data | — | — | — | — |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.435s · Fast | parity | 26.6% | 837.6 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.549s · Ok | parity | 65.7% | 798.4 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.523s · Ok | +0.121s slower | 21.1% | 801.5 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.531s · Ok | -0.218s faster | 30.6% | 842.8 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.409s · Fast | parity | 34.4% | 767.3 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.697s · Ok | -0.225s faster | 30.3% | 786.1 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.336s · Fast | parity | 53.4% | 764.7 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.744s · Slow | parity | 50.7% | 841.1 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.804s · Ok | +0.123s slower | 44.5% | 823.4 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.800s · Ok | -0.567s faster | 41.9% | 829.5 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.734s · Ok | +0.202s slower | 44.9% | 919.6 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 3.522s · Slow | no baseline | 68.4% | 756.0 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.459s · Fast | no baseline | 55.6% | 763.5 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.244s · Fast | no baseline | 34.5% | 865.7 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.573s · Ok | no baseline | 43.5% | 836.7 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.809s · Ok | no baseline | 61.3% | 800.6 MB | 39901f54d<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.208s · Fast | no baseline | 60.6% | 798.5 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.933s · Near ok | +0.708s slower | 47.1% | 942.7 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.569s · Ok | parity | 69.5% | 868.2 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.494s · Fast | +0.147s slower | 31.8% | 861.1 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.522s · Ok | -0.287s faster | 51.9% | 788.4 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.448s · Fast | parity | 58.8% | 821.2 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.537s · Ok | -0.413s faster | 51.9% | 780.4 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.348s · Fast | parity | 61.8% | 808.5 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.284s · Slow | -0.486s faster | 52.2% | 917.2 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.854s · Ok | +0.191s slower | 55.4% | 918.2 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.650s · Ok | -0.648s faster | 27.7% | 913.1 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.776s · Ok | +0.262s slower | 65.7% | 959.9 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 1.009s · Slow | no baseline | 51.4% | 796.6 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.438s · Fast | no baseline | 69.1% | 846.5 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.340s · Fast | no baseline | 54.9% | 854.8 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.161s · Fast | no baseline | 72.0% | 809.1 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.653s · Ok | no baseline | 71.6% | 881.1 MB | 39901f54d<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.242s · Fast | no baseline | 66.2% | 836.8 MB | 39901f54d<br>2026-09-21 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.023s · Slow | -0.752s faster | 43.8% | 852.2 MB | 39901f54d<br>2026-09-21 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.171s · Slow | parity | 21.1% | 834.0 MB | 39901f54d<br>2026-09-21 |

## New user profile

Newly created profiles with no pre-seeded data. Wallet scenarios use one fresh user; messenger send timing uses 1-on-1 and 3-person group chats; community send timing uses one joined community on #general.

### User data profile

- **Stored data:** No pre-seeded data
- **Wallet:** 1 wallet accounts · 0 tokens with balance > 0 · 0 NFTs · 0 transactions
- **Messenger:** 1 1-on-1 chats · 1 group chats
- **Communities:** 1 joined communities · 0 spectated communities

### Wallet

- [Time to open Wallet for the first time after login](charts/wallet_first_open_time_fresh.html)

- [CPU usage while opening Wallet for the first time after login](charts/wallet_first_open_cpu_fresh.html)

- [RAM usage while opening Wallet for the first time after login](charts/wallet_first_open_ram_fresh.html)

- [Time to reopen Wallet in the same session](charts/wallet_repeat_open_time_fresh.html)

- [CPU usage while reopening Wallet in the same session](charts/wallet_repeat_open_cpu_fresh.html)

- [RAM usage while reopening Wallet in the same session](charts/wallet_repeat_open_ram_fresh.html)

- [Time to open a Wallet account for the first time in the session](charts/wallet_account_first_open_time_fresh.html)

- [CPU usage while opening a Wallet account for the first time in the session](charts/wallet_account_first_open_cpu_fresh.html)

- [RAM usage while opening a Wallet account for the first time in the session](charts/wallet_account_first_open_ram_fresh.html)

- [Time to open the Add account modal for the first time in the session](charts/wallet_add_account_first_open_time_fresh.html)

- [CPU usage while opening the Add account modal for the first time in the session](charts/wallet_add_account_first_open_cpu_fresh.html)

- [RAM usage while opening the Add account modal for the first time in the session](charts/wallet_add_account_first_open_ram_fresh.html)

- [Time to reopen the Add account modal in the same session](charts/wallet_add_account_time_fresh.html)

- [CPU usage while reopening the Add account modal in the same session](charts/wallet_add_account_cpu_fresh.html)

- [RAM usage while reopening the Add account modal in the same session](charts/wallet_add_account_ram_fresh.html)

- [Time to open the Receive modal for the first time in the session](charts/wallet_receive_first_open_time_fresh.html)

- [CPU usage while opening the Receive modal for the first time in the session](charts/wallet_receive_first_open_cpu_fresh.html)

- [RAM usage while opening the Receive modal for the first time in the session](charts/wallet_receive_first_open_ram_fresh.html)

- [Time to reopen the Receive modal in the same session](charts/wallet_receive_time_fresh.html)

- [CPU usage while reopening the Receive modal in the same session](charts/wallet_receive_cpu_fresh.html)

- [RAM usage while reopening the Receive modal in the same session](charts/wallet_receive_ram_fresh.html)

- [Time to open the Send modal for the first time in the session](charts/wallet_send_first_open_time_fresh.html)

- [CPU usage while opening the Send modal for the first time in the session](charts/wallet_send_first_open_cpu_fresh.html)

- [RAM usage while opening the Send modal for the first time in the session](charts/wallet_send_first_open_ram_fresh.html)

- [Time to reopen the Send modal in the same session](charts/wallet_send_time_fresh.html)

- [CPU usage while reopening the Send modal in the same session](charts/wallet_send_cpu_fresh.html)

- [RAM usage while reopening the Send modal in the same session](charts/wallet_send_ram_fresh.html)

- [Time to open the Swap modal for the first time in the session](charts/wallet_swap_first_open_time_fresh.html)

- [CPU usage while opening the Swap modal for the first time in the session](charts/wallet_swap_first_open_cpu_fresh.html)

- [RAM usage while opening the Swap modal for the first time in the session](charts/wallet_swap_first_open_ram_fresh.html)

- [Time to reopen the Swap modal in the same session](charts/wallet_swap_time_fresh.html)

- [CPU usage while reopening the Swap modal in the same session](charts/wallet_swap_cpu_fresh.html)

- [RAM usage while reopening the Swap modal in the same session](charts/wallet_swap_ram_fresh.html)

- [Time to open the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_time_fresh.html)

- [CPU usage while opening the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_cpu_fresh.html)

- [RAM usage while opening the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_ram_fresh.html)

- [Time to reopen the Assets tab in the same session](charts/wallet_assets_tab_time_fresh.html)

- [CPU usage while reopening the Assets tab in the same session](charts/wallet_assets_tab_cpu_fresh.html)

- [RAM usage while reopening the Assets tab in the same session](charts/wallet_assets_tab_ram_fresh.html)

- [Time to open the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_time_fresh.html)

- [CPU usage while opening the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_cpu_fresh.html)

- [RAM usage while opening the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_ram_fresh.html)

- [Time to reopen the Collectibles tab in the same session](charts/wallet_collectibles_tab_time_fresh.html)

- [CPU usage while reopening the Collectibles tab in the same session](charts/wallet_collectibles_tab_cpu_fresh.html)

- [RAM usage while reopening the Collectibles tab in the same session](charts/wallet_collectibles_tab_ram_fresh.html)

- [Time to open the History tab for the first time in the session](charts/wallet_activity_tab_first_open_time_fresh.html)

- [CPU usage while opening the History tab for the first time in the session](charts/wallet_activity_tab_first_open_cpu_fresh.html)

- [RAM usage while opening the History tab for the first time in the session](charts/wallet_activity_tab_first_open_ram_fresh.html)

- [Time to reopen the History tab in the same session](charts/wallet_activity_tab_time_fresh.html)

- [CPU usage while reopening the History tab in the same session](charts/wallet_activity_tab_cpu_fresh.html)

- [RAM usage while reopening the History tab in the same session](charts/wallet_activity_tab_ram_fresh.html)

### Messenger

**Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

**Time to Sent after sending 1000-character text in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending 1000-character text in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending a 5-image album in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending a 5-image album in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending a GIF in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending a GIF in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending 10 texts with 0.5s delay in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending 1000-character text in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending 1000-character text in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending a 5-image album in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending a 5-image album in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending a GIF in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending a GIF in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

### Communities

**Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

**Time to Sent after sending 1000-character text in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending 1000-character text in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending 1000-character text**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending a 5-image album in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending a 5-image album in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending a 5-image album**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending a GIF in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending a GIF in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending a GIF**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Sent after sending 10 texts with 0.5s delay in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Sent after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Sent after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay**

_No data yet — chart will appear after the next nightly benchmark run._

## Returning user (semi-heavy wallet account)

Returning user with semi-heavy wallet account (~34 MB user data).

### User data profile

- **Stored data:** ~34 MB
- **Wallet:** 3 wallet accounts · 83 tokens with balance > 0 · 166 NFTs · 736 transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 0 joined communities · 0 spectated communities

### Wallet

- [Time to open Wallet for the first time after login](charts/wallet_first_open_time_wallet_load.html)

- [CPU usage while opening Wallet for the first time after login](charts/wallet_first_open_cpu_wallet_load.html)

- [RAM usage while opening Wallet for the first time after login](charts/wallet_first_open_ram_wallet_load.html)

- [Time to reopen Wallet in the same session](charts/wallet_repeat_open_time_wallet_load.html)

- [CPU usage while reopening Wallet in the same session](charts/wallet_repeat_open_cpu_wallet_load.html)

- [RAM usage while reopening Wallet in the same session](charts/wallet_repeat_open_ram_wallet_load.html)

- [Time to open a Wallet account for the first time in the session](charts/wallet_account_first_open_time_wallet_load.html)

- [CPU usage while opening a Wallet account for the first time in the session](charts/wallet_account_first_open_cpu_wallet_load.html)

- [RAM usage while opening a Wallet account for the first time in the session](charts/wallet_account_first_open_ram_wallet_load.html)

- [Time to open the Add account modal for the first time in the session](charts/wallet_add_account_first_open_time_wallet_load.html)

- [CPU usage while opening the Add account modal for the first time in the session](charts/wallet_add_account_first_open_cpu_wallet_load.html)

- [RAM usage while opening the Add account modal for the first time in the session](charts/wallet_add_account_first_open_ram_wallet_load.html)

- [Time to reopen the Add account modal in the same session](charts/wallet_add_account_time_wallet_load.html)

- [CPU usage while reopening the Add account modal in the same session](charts/wallet_add_account_cpu_wallet_load.html)

- [RAM usage while reopening the Add account modal in the same session](charts/wallet_add_account_ram_wallet_load.html)

- [Time to open the Receive modal for the first time in the session](charts/wallet_receive_first_open_time_wallet_load.html)

- [CPU usage while opening the Receive modal for the first time in the session](charts/wallet_receive_first_open_cpu_wallet_load.html)

- [RAM usage while opening the Receive modal for the first time in the session](charts/wallet_receive_first_open_ram_wallet_load.html)

- [Time to reopen the Receive modal in the same session](charts/wallet_receive_time_wallet_load.html)

- [CPU usage while reopening the Receive modal in the same session](charts/wallet_receive_cpu_wallet_load.html)

- [RAM usage while reopening the Receive modal in the same session](charts/wallet_receive_ram_wallet_load.html)

- [Time to open the Send modal for the first time in the session](charts/wallet_send_first_open_time_wallet_load.html)

- [CPU usage while opening the Send modal for the first time in the session](charts/wallet_send_first_open_cpu_wallet_load.html)

- [RAM usage while opening the Send modal for the first time in the session](charts/wallet_send_first_open_ram_wallet_load.html)

- [Time to reopen the Send modal in the same session](charts/wallet_send_time_wallet_load.html)

- [CPU usage while reopening the Send modal in the same session](charts/wallet_send_cpu_wallet_load.html)

- [RAM usage while reopening the Send modal in the same session](charts/wallet_send_ram_wallet_load.html)

- [Time to open the Swap modal for the first time in the session](charts/wallet_swap_first_open_time_wallet_load.html)

- [CPU usage while opening the Swap modal for the first time in the session](charts/wallet_swap_first_open_cpu_wallet_load.html)

- [RAM usage while opening the Swap modal for the first time in the session](charts/wallet_swap_first_open_ram_wallet_load.html)

- [Time to reopen the Swap modal in the same session](charts/wallet_swap_time_wallet_load.html)

- [CPU usage while reopening the Swap modal in the same session](charts/wallet_swap_cpu_wallet_load.html)

- [RAM usage while reopening the Swap modal in the same session](charts/wallet_swap_ram_wallet_load.html)

- [Time to open the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_time_wallet_load.html)

- [CPU usage while opening the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_cpu_wallet_load.html)

- [RAM usage while opening the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_ram_wallet_load.html)

- [Time to reopen the Assets tab in the same session](charts/wallet_assets_tab_time_wallet_load.html)

- [CPU usage while reopening the Assets tab in the same session](charts/wallet_assets_tab_cpu_wallet_load.html)

- [RAM usage while reopening the Assets tab in the same session](charts/wallet_assets_tab_ram_wallet_load.html)

- [Time to open the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_time_wallet_load.html)

- [CPU usage while opening the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_cpu_wallet_load.html)

- [RAM usage while opening the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_ram_wallet_load.html)

- [Time to reopen the Collectibles tab in the same session](charts/wallet_collectibles_tab_time_wallet_load.html)

- [CPU usage while reopening the Collectibles tab in the same session](charts/wallet_collectibles_tab_cpu_wallet_load.html)

- [RAM usage while reopening the Collectibles tab in the same session](charts/wallet_collectibles_tab_ram_wallet_load.html)

- [Time to open the History tab for the first time in the session](charts/wallet_activity_tab_first_open_time_wallet_load.html)

- [CPU usage while opening the History tab for the first time in the session](charts/wallet_activity_tab_first_open_cpu_wallet_load.html)

- [RAM usage while opening the History tab for the first time in the session](charts/wallet_activity_tab_first_open_ram_wallet_load.html)

- [Time to reopen the History tab in the same session](charts/wallet_activity_tab_time_wallet_load.html)

- [CPU usage while reopening the History tab in the same session](charts/wallet_activity_tab_cpu_wallet_load.html)

- [RAM usage while reopening the History tab in the same session](charts/wallet_activity_tab_ram_wallet_load.html)

## Returning user (heavy account from Alex)

Returning user with heavy account from Alex (~35 MB user data).

### User data profile

- **Stored data:** ~35 MB
- **Wallet:** 4 wallet accounts · 144 tokens with balance > 0 · 773 NFTs · 5239 transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 0 joined communities · 0 spectated communities

### Wallet

- [Time to open Wallet for the first time after login](charts/wallet_first_open_time_wallet_load_alex.html)

- [CPU usage while opening Wallet for the first time after login](charts/wallet_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening Wallet for the first time after login](charts/wallet_first_open_ram_wallet_load_alex.html)

- [Time to reopen Wallet in the same session](charts/wallet_repeat_open_time_wallet_load_alex.html)

- [CPU usage while reopening Wallet in the same session](charts/wallet_repeat_open_cpu_wallet_load_alex.html)

- [RAM usage while reopening Wallet in the same session](charts/wallet_repeat_open_ram_wallet_load_alex.html)

- [Time to open a Wallet account for the first time in the session](charts/wallet_account_first_open_time_wallet_load_alex.html)

- [CPU usage while opening a Wallet account for the first time in the session](charts/wallet_account_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening a Wallet account for the first time in the session](charts/wallet_account_first_open_ram_wallet_load_alex.html)

- [Time to open the Add account modal for the first time in the session](charts/wallet_add_account_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the Add account modal for the first time in the session](charts/wallet_add_account_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the Add account modal for the first time in the session](charts/wallet_add_account_first_open_ram_wallet_load_alex.html)

- [Time to reopen the Add account modal in the same session](charts/wallet_add_account_time_wallet_load_alex.html)

- [CPU usage while reopening the Add account modal in the same session](charts/wallet_add_account_cpu_wallet_load_alex.html)

- [RAM usage while reopening the Add account modal in the same session](charts/wallet_add_account_ram_wallet_load_alex.html)

- [Time to open the Receive modal for the first time in the session](charts/wallet_receive_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the Receive modal for the first time in the session](charts/wallet_receive_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the Receive modal for the first time in the session](charts/wallet_receive_first_open_ram_wallet_load_alex.html)

- [Time to reopen the Receive modal in the same session](charts/wallet_receive_time_wallet_load_alex.html)

- [CPU usage while reopening the Receive modal in the same session](charts/wallet_receive_cpu_wallet_load_alex.html)

- [RAM usage while reopening the Receive modal in the same session](charts/wallet_receive_ram_wallet_load_alex.html)

- [Time to open the Send modal for the first time in the session](charts/wallet_send_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the Send modal for the first time in the session](charts/wallet_send_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the Send modal for the first time in the session](charts/wallet_send_first_open_ram_wallet_load_alex.html)

- [Time to reopen the Send modal in the same session](charts/wallet_send_time_wallet_load_alex.html)

- [CPU usage while reopening the Send modal in the same session](charts/wallet_send_cpu_wallet_load_alex.html)

- [RAM usage while reopening the Send modal in the same session](charts/wallet_send_ram_wallet_load_alex.html)

- [Time to open the Swap modal for the first time in the session](charts/wallet_swap_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the Swap modal for the first time in the session](charts/wallet_swap_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the Swap modal for the first time in the session](charts/wallet_swap_first_open_ram_wallet_load_alex.html)

- [Time to reopen the Swap modal in the same session](charts/wallet_swap_time_wallet_load_alex.html)

- [CPU usage while reopening the Swap modal in the same session](charts/wallet_swap_cpu_wallet_load_alex.html)

- [RAM usage while reopening the Swap modal in the same session](charts/wallet_swap_ram_wallet_load_alex.html)

- [Time to open the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the Assets tab for the first time in the session](charts/wallet_assets_tab_first_open_ram_wallet_load_alex.html)

- [Time to reopen the Assets tab in the same session](charts/wallet_assets_tab_time_wallet_load_alex.html)

- [CPU usage while reopening the Assets tab in the same session](charts/wallet_assets_tab_cpu_wallet_load_alex.html)

- [RAM usage while reopening the Assets tab in the same session](charts/wallet_assets_tab_ram_wallet_load_alex.html)

- [Time to open the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the Collectibles tab for the first time in the session](charts/wallet_collectibles_tab_first_open_ram_wallet_load_alex.html)

- [Time to reopen the Collectibles tab in the same session](charts/wallet_collectibles_tab_time_wallet_load_alex.html)

- [CPU usage while reopening the Collectibles tab in the same session](charts/wallet_collectibles_tab_cpu_wallet_load_alex.html)

- [RAM usage while reopening the Collectibles tab in the same session](charts/wallet_collectibles_tab_ram_wallet_load_alex.html)

- [Time to open the History tab for the first time in the session](charts/wallet_activity_tab_first_open_time_wallet_load_alex.html)

- [CPU usage while opening the History tab for the first time in the session](charts/wallet_activity_tab_first_open_cpu_wallet_load_alex.html)

- [RAM usage while opening the History tab for the first time in the session](charts/wallet_activity_tab_first_open_ram_wallet_load_alex.html)

- [Time to reopen the History tab in the same session](charts/wallet_activity_tab_time_wallet_load_alex.html)

- [CPU usage while reopening the History tab in the same session](charts/wallet_activity_tab_cpu_wallet_load_alex.html)

- [RAM usage while reopening the History tab in the same session](charts/wallet_activity_tab_ram_wallet_load_alex.html)

## Returning user (Status community member)

Returning user with Status community already joined.

### User data profile

- **Stored data:** TBD
- **Wallet:** 1 wallet accounts · 0 tokens with balance > 0 · 0 NFTs · 0 transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 1 joined communities · 0 spectated communities

### Communities

- [Time to open Status community for the first time after login](charts/community_first_open_loading_time_member.html)

- [Time to reopen Status community in the same session](charts/community_second_open_loading_time_member.html)

- [CPU usage while opening Status community for the first time after login](charts/community_first_open_cpu_member.html)

- [CPU usage while reopening Status community in the same session](charts/community_second_open_cpu_member.html)

- [RAM usage while opening Status community for the first time after login](charts/community_first_open_ram_member.html)

- [RAM usage while reopening Status community in the same session](charts/community_second_open_ram_member.html)

---

Generated by `scripts/benchmark.py graphs` from `data/`. Refreshed nightly by Jenkins.
