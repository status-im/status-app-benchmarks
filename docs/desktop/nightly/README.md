# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 24, 2026 · [`02b09eb8f`](https://github.com/status-im/status-app/commit/02b09eb8fe7318ba1266f321046b6f97c0990e28)

## Send timing

Latest time to **Sent** (one tick) and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Sent | Delivered | Commit | Date |
|----------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.459s | 1.218s | 02b09eb8f | 2026-09-24 |
| a 5-image album in a 3-person group | 2.991s | 5.116s | 02b09eb8f | 2026-09-24 |
| a GIF in a 3-person group | 0.484s | 2.707s | 02b09eb8f | 2026-09-24 |
| 10 texts with 0.5s delay in a 3-person group | 0.974s | 2.053s | 02b09eb8f | 2026-09-24 |
| 1000-character text in a 1-on-1 chat | 0.523s | 0.878s | 02b09eb8f | 2026-09-24 |
| a 5-image album in a 1-on-1 chat | 3.027s | 3.520s | 02b09eb8f | 2026-09-24 |
| a GIF in a 1-on-1 chat | 1.009s | 1.474s | 02b09eb8f | 2026-09-24 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.885s | 3.076s | 02b09eb8f | 2026-09-24 |
| 1000-character text in a community #general channel | 0.454s | 2.147s | 02b09eb8f | 2026-09-24 |
| a 5-image album in a community #general channel | 5.089s | 9.047s | 02b09eb8f | 2026-09-24 |
| a GIF in a community #general channel | 0.629s | 3.616s | 02b09eb8f | 2026-09-24 |
| 10 texts with 0.5s delay in a community #general channel | 1.168s | 4.698s | 02b09eb8f | 2026-09-24 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.747s · Ok | +0.375s slower | 61.9% | 734.9 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.420s · Fast | parity | 55.1% | 791.8 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.108s · Fast | -0.049s faster | 7.1% | 683.8 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.382s · Fast | -0.229s faster | 14.7% | 679.7 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.384s · Fast | parity | 13.4% | 752.9 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.384s · Fast | -0.087s faster | 36.7% | 735.1 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.299s · Fast | parity | 19.9% | 774.6 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.046s · Slow | +0.158s slower | 34.6% | 769.3 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.613s · Ok | +0.115s slower | 25.6% | 890.0 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.961s · Near ok | -0.598s faster | 48.4% | 781.0 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.560s · Ok | parity | 21.7% | 894.1 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.397s · Fast | no baseline | 61.7% | 735.1 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.182s · Fast | no baseline | 36.0% | 780.6 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.560s · Ok | no baseline | 63.6% | 774.3 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.121s · Fast | no baseline | 44.5% | 776.1 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.165s · Fast | no baseline | 63.0% | 691.9 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.104s · Fast | no baseline | 43.7% | 685.9 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.459s · Fast | no baseline | 30.5% | 745.9 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 1.218s · Slow | no baseline | 2.7% | 745.9 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 2.991s · Slow | no baseline | 7.0% | 765.3 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 5.116s · Slow | no baseline | 4.3% | 815.5 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.484s · Fast | no baseline | 1.8% | 859.2 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 2.707s · Slow | no baseline | 2.4% | 859.2 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 0.974s · Near ok | no baseline | 11.7% | 858.5 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 2.053s · Slow | no baseline | 4.1% | 858.8 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 0.523s · Ok | no baseline | 3.1% | 782.8 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 0.878s · Ok | no baseline | 4.5% | 785.9 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.027s · Slow | no baseline | 22.7% | 821.9 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 3.520s · Slow | no baseline | 3.5% | 839.3 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.009s · Slow | no baseline | 2.9% | 841.0 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 1.474s · Slow | no baseline | 27.5% | 920.9 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.885s · Ok | no baseline | 11.0% | 883.6 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 3.076s · Slow | no baseline | 6.3% | 882.4 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.454s · Fast | no baseline | 19.7% | 833.8 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 2.147s · Slow | no baseline | 4.0% | 833.9 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 5.089s · Slow | no baseline | 6.0% | 852.5 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 9.047s · Slow | no baseline | 5.8% | 983.2 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 0.629s · Ok | no baseline | 3.7% | 985.9 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.616s · Slow | no baseline | 10.3% | 965.8 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 1.168s · Slow | no baseline | 7.0% | 961.1 MB | 02b09eb8f<br>2026-09-24 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 4.698s · Slow | no baseline | 5.2% | 959.8 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.367s · Fast | -0.117s faster | 24.9% | 815.7 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.541s · Ok | parity | 66.6% | 771.2 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.599s · Ok | +0.197s slower | 42.6% | 806.2 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.701s · Ok | parity | 45.9% | 837.0 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.401s · Fast | parity | 27.3% | 789.1 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.359s · Fast | -0.563s faster | 35.4% | 743.4 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.323s · Fast | parity | 41.1% | 741.5 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.719s · Slow | parity | 34.5% | 831.2 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.454s · Fast | -0.227s faster | 35.9% | 848.0 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.568s · Ok | -0.799s faster | 34.5% | 824.5 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.611s · Ok | parity | 48.4% | 902.8 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 1.131s · Slow | no baseline | 60.2% | 836.1 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.527s · Ok | no baseline | 44.1% | 816.5 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 2.002s · Slow | no baseline | 54.8% | 851.9 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.513s · Ok | no baseline | 44.1% | 843.6 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.684s · Ok | no baseline | 50.8% | 861.6 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.215s · Fast | no baseline | 73.6% | 817.0 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.590s · Ok | +0.365s slower | 37.5% | 833.8 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.557s · Ok | parity | 67.7% | 853.9 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.499s · Fast | +0.152s slower | 45.8% | 767.9 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.649s · Ok | -0.160s faster | 48.7% | 885.2 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.457s · Fast | parity | 62.8% | 850.8 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.622s · Ok | -0.328s faster | 38.7% | 860.1 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.382s · Fast | +0.054s slower | 67.0% | 842.8 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.240s · Slow | -0.530s faster | 39.3% | 901.5 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.748s · Ok | parity | 60.1% | 937.6 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.714s · Ok | -0.584s faster | 53.6% | 788.2 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.597s · Ok | +0.083s slower | 46.5% | 973.0 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 1.174s · Slow | no baseline | 53.6% | 903.1 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.428s · Fast | no baseline | 60.6% | 824.8 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.328s · Fast | no baseline | 47.3% | 887.8 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.222s · Fast | no baseline | 55.5% | 830.7 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.677s · Ok | no baseline | 54.5% | 861.0 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.239s · Fast | no baseline | 72.9% | 851.2 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 2.632s · Slow | -1.143s faster | 48.1% | 745.2 MB | 02b09eb8f<br>2026-09-24 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.163s · Slow | parity | 17.1% | 838.9 MB | 02b09eb8f<br>2026-09-24 |

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

- [Time to Sent after sending 1000-character text in a 3-person group](charts/group_chat_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/group_chat_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/group_chat_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a 3-person group](charts/group_chat_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/group_chat_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/group_chat_plain_text_delivered_ram.html)

- [Time to Sent after sending a 5-image album in a 3-person group](charts/group_chat_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/group_chat_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/group_chat_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a 3-person group](charts/group_chat_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/group_chat_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/group_chat_album_delivered_ram.html)

- [Time to Sent after sending a GIF in a 3-person group](charts/group_chat_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/group_chat_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/group_chat_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a 3-person group](charts/group_chat_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/group_chat_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/group_chat_gif_delivered_ram.html)

- [Time to Sent after sending 10 texts with 0.5s delay in a 3-person group](charts/group_chat_burst_sent_time.html)

- [CPU usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/group_chat_burst_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/group_chat_burst_sent_ram.html)

- [Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group](charts/group_chat_burst_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/group_chat_burst_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/group_chat_burst_delivered_ram.html)

- [Time to Sent after sending 1000-character text in a 1-on-1 chat](charts/direct_chat_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/direct_chat_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/direct_chat_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a 1-on-1 chat](charts/direct_chat_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/direct_chat_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/direct_chat_plain_text_delivered_ram.html)

- [Time to Sent after sending a 5-image album in a 1-on-1 chat](charts/direct_chat_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/direct_chat_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/direct_chat_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a 1-on-1 chat](charts/direct_chat_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/direct_chat_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/direct_chat_album_delivered_ram.html)

- [Time to Sent after sending a GIF in a 1-on-1 chat](charts/direct_chat_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/direct_chat_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/direct_chat_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a 1-on-1 chat](charts/direct_chat_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/direct_chat_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/direct_chat_gif_delivered_ram.html)

- [Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat](charts/direct_chat_burst_sent_time.html)

- [CPU usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/direct_chat_burst_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/direct_chat_burst_sent_ram.html)

- [Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat](charts/direct_chat_burst_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/direct_chat_burst_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/direct_chat_burst_delivered_ram.html)

### Communities

**Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

- [Time to Sent after sending 1000-character text in a community #general channel](charts/community_general_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/community_general_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/community_general_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a community #general channel](charts/community_general_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/community_general_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/community_general_plain_text_delivered_ram.html)

- [Time to Sent after sending a 5-image album in a community #general channel](charts/community_general_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/community_general_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/community_general_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a community #general channel](charts/community_general_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/community_general_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/community_general_album_delivered_ram.html)

- [Time to Sent after sending a GIF in a community #general channel](charts/community_general_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/community_general_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/community_general_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a community #general channel](charts/community_general_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/community_general_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/community_general_gif_delivered_ram.html)

- [Time to Sent after sending 10 texts with 0.5s delay in a community #general channel](charts/community_general_burst_sent_time.html)

- [CPU usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/community_general_burst_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/community_general_burst_sent_ram.html)

- [Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel](charts/community_general_burst_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/community_general_burst_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/community_general_burst_delivered_ram.html)

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
