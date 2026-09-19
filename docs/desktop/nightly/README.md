# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 19, 2026 · [`f89efa625`](https://github.com/status-im/status-app/commit/f89efa62503f4969b8b78a19f7ccf98ef08d4bf5)

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.468s · Fast | +0.096s slower | 60.6% | 689.1 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.491s · Fast | +0.112s slower | 68.7% | 806.5 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.142s · Fast | parity | 54.2% | 747.5 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.472s · Fast | -0.139s faster | 37.5% | 745.5 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.397s · Fast | parity | 19.7% | 826.5 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.288s · Fast | -0.183s faster | 26.5% | 702.1 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.293s · Fast | parity | 23.8% | 761.5 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 0.994s · Near ok | parity | 57.9% | 735.7 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.522s · Ok | parity | 26.7% | 877.3 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.006s · Slow | -0.553s faster | 30.8% | 715.9 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.319s · Fast | -0.249s faster | 17.0% | 901.8 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.129s · Fast | no baseline | 18.0% | 739.4 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.183s · Fast | no baseline | 43.6% | 767.0 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.231s · Fast | no baseline | 47.4% | 694.8 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.127s · Fast | no baseline | 38.2% | 718.0 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.136s · Fast | no baseline | 19.7% | 746.0 MB | f89efa625<br>2026-09-19 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.100s · Fast | no baseline | 32.9% | 736.0 MB | f89efa625<br>2026-09-19 |
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
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.402s · Fast | -0.082s faster | 48.2% | 835.3 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.541s · Ok | parity | 75.7% | 782.1 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.607s · Ok | +0.205s slower | 58.1% | 875.5 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.467s · Fast | -0.282s faster | 58.5% | 758.5 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.399s · Fast | parity | 31.0% | 741.5 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.458s · Fast | -0.464s faster | 28.5% | 787.3 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.328s · Fast | parity | 37.2% | 757.3 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.816s · Slow | parity | 59.5% | 872.1 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.754s · Ok | parity | 39.9% | 829.4 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.584s · Ok | -0.783s faster | 42.9% | 741.6 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.541s · Ok | parity | 35.8% | 890.3 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.685s · Ok | no baseline | 66.6% | 748.9 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.489s · Fast | no baseline | 44.2% | 776.5 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.355s · Fast | no baseline | 75.3% | 945.1 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.598s · Ok | no baseline | 54.2% | 827.2 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.696s · Ok | no baseline | 64.1% | 902.6 MB | f89efa625<br>2026-09-19 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.199s · Fast | no baseline | 54.3% | 808.8 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.649s · Ok | +0.424s slower | 46.0% | 885.9 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.586s · Ok | parity | 72.4% | 838.8 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.333s · Fast | parity | 22.2% | 795.6 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.517s · Ok | -0.292s faster | 29.9% | 859.1 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.473s · Fast | parity | 61.3% | 840.6 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 1.043s · Slow | parity | 47.4% | 821.8 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.351s · Fast | parity | 57.2% | 838.4 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.376s · Slow | -0.394s faster | 52.2% | 900.8 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.771s · Ok | +0.108s slower | 62.6% | 891.4 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.718s · Ok | -0.580s faster | 32.7% | 854.3 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.927s · Near ok | +0.413s slower | 68.8% | 982.5 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.405s · Fast | no baseline | 53.6% | 833.4 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.421s · Fast | no baseline | 59.5% | 795.3 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.301s · Fast | no baseline | 53.2% | 776.5 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.143s · Fast | no baseline | 70.6% | 792.7 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.647s · Ok | no baseline | 57.9% | 872.2 MB | f89efa625<br>2026-09-19 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.222s · Fast | no baseline | 62.2% | 831.4 MB | f89efa625<br>2026-09-19 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 2.737s · Slow | -1.038s faster | 54.4% | 742.3 MB | f89efa625<br>2026-09-19 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.222s · Slow | parity | 28.2% | 861.2 MB | f89efa625<br>2026-09-19 |

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
