# [#22463](https://github.com/status-im/status-app/pull/22463) tests(@e2e): measure send message timing

Automated test suite performance tracking for the Windows desktop app.
Charts show every requested run for this pull request. Each point is one benchmark run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 17, 2026 · [`ee8c63`](https://github.com/status-im/status-app/commit/ee8c632de7bbc5ff1ab1c9927ce8b6ed35713444)

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026). **vs nightly · Sep 17, 2026** is that nightly run — the latest nightly when this PR was measured.

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | vs nightly · Sep 17, 2026 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|----------------------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.628s · Ok | +0.256s slower | -0.112s faster | 82.5% | 762.1 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.649s · Ok | +0.270s slower | +0.131s slower | 71.6% | 843.6 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.151s · Fast | parity | +0.046s slower | 7.2% | 714.4 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.664s · Ok | parity | +0.184s slower | 17.4% | 849.5 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.433s · Fast | parity | parity | 15.2% | 816.7 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.401s · Fast | parity | parity | 24.8% | 774.3 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.427s · Fast | +0.125s slower | +0.132s slower | 21.4% | 794.6 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 0.536s · Ok | -0.352s faster | -0.482s faster | 19.1% | 815.9 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.587s · Ok | +0.089s slower | parity | 24.6% | 909.5 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.965s · Near ok | -0.594s faster | parity | 30.7% | 863.9 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.532s · Ok | parity | +0.121s slower | 21.2% | 943.3 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.212s · Fast | no baseline | +0.058s slower | 34.9% | 698.1 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.179s · Fast | no baseline | parity | 55.5% | 748.0 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.290s · Fast | no baseline | parity | 10.2% | 726.3 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.120s · Fast | no baseline | parity | 32.0% | 714.7 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.220s · Fast | no baseline | parity | 61.3% | 723.1 MB | ee8c63<br>2026-09-17 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.104s · Fast | no baseline | parity | 42.5% | 721.5 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.901s · Near ok | no baseline | — | 8.4% | 780.5 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 2.116s · Slow | no baseline | — | 5.2% | 780.6 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.085s · Slow | no baseline | — | 30.3% | 806.7 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 4.549s · Slow | no baseline | — | 54.7% | 824.1 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.715s · Ok | no baseline | — | 44.5% | 896.8 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 2.929s · Slow | no baseline | — | 53.8% | 897.0 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 0.736s · Ok | no baseline | — | 16.4% | 898.6 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 2.001s · Slow | no baseline | — | 9.1% | 896.9 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 0.526s · Ok | no baseline | — | 18.8% | 810.1 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 2.541s · Slow | no baseline | — | 2.3% | 810.4 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.014s · Slow | no baseline | — | 12.1% | 813.7 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 5.219s · Slow | no baseline | — | 2.7% | 847.5 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 0.503s · Ok | no baseline | — | 2.7% | 902.5 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 2.306s · Slow | no baseline | — | 2.5% | 902.6 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.711s · Ok | no baseline | — | 11.9% | 900.2 MB | ee8c63<br>2026-09-17 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 2.470s · Slow | no baseline | — | 9.6% | 900.3 MB | ee8c63<br>2026-09-17 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.463s · Fast | no baseline | — | 45.7% | 840.4 MB | ee8c63<br>2026-09-17 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 3.747s · Slow | no baseline | — | 5.7% | 840.5 MB | ee8c63<br>2026-09-17 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 5.168s · Slow | no baseline | — | 8.9% | 866.3 MB | ee8c63<br>2026-09-17 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 9.366s · Slow | no baseline | — | 55.9% | 994.6 MB | ee8c63<br>2026-09-17 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.036s · Slow | no baseline | — | 46.6% | 995.0 MB | ee8c63<br>2026-09-17 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.640s · Slow | no baseline | — | 5.4% | 995.1 MB | ee8c63<br>2026-09-17 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 1.126s · Slow | no baseline | — | 9.1% | 970.1 MB | ee8c63<br>2026-09-17 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 4.547s · Slow | no baseline | — | 4.6% | 969.9 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.454s · Fast | parity | +0.182s slower | 35.8% | 878.2 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.856s · Ok | +0.276s slower | +0.314s slower | 75.6% | 867.0 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.703s · Ok | +0.301s slower | parity | 50.3% | 920.7 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.921s · Near ok | +0.172s slower | +0.347s slower | 55.7% | 856.3 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.493s · Fast | parity | +0.086s slower | 66.1% | 824.6 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.559s · Ok | -0.363s faster | parity | 45.4% | 778.1 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.324s · Fast | parity | parity | 42.8% | 751.1 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.395s · Slow | -0.395s faster | -0.292s faster | 45.7% | 863.8 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.641s · Ok | parity | -0.169s faster | 38.0% | 868.5 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.582s · Ok | -0.785s faster | -0.109s faster | 28.1% | 833.1 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.657s · Ok | +0.125s slower | parity | 40.0% | 965.4 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 3.322s · Slow | no baseline | +2.664s slower | 53.1% | 798.0 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.415s · Fast | no baseline | -0.329s faster | 43.1% | 812.0 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.287s · Fast | no baseline | -1.928s faster | 57.8% | 847.5 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.471s · Fast | no baseline | -0.103s faster | 59.8% | 823.3 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 1.060s · Slow | no baseline | +0.361s slower | 70.4% | 859.9 MB | ee8c63<br>2026-09-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.308s · Fast | no baseline | +0.094s slower | 50.0% | 829.3 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.451s · Fast | +0.226s slower | parity | 55.4% | 840.4 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.856s · Ok | +0.273s slower | +0.253s slower | 75.8% | 918.4 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 1.013s · Slow | +0.666s slower | +0.551s slower | 53.1% | 861.6 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.952s · Near ok | +0.143s slower | +0.285s slower | 39.7% | 878.1 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.528s · Ok | +0.093s slower | parity | 59.9% | 878.0 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.481s · Fast | -0.469s faster | parity | 50.9% | 902.4 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.356s · Fast | parity | parity | 70.8% | 833.0 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.919s · Slow | parity | +0.616s slower | 59.1% | 900.1 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.749s · Ok | parity | -0.139s faster | 61.8% | 954.2 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.793s · Ok | -0.505s faster | parity | 51.9% | 839.8 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.613s · Ok | +0.099s slower | -0.252s faster | 57.2% | 1017.5 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.173s · Fast | no baseline | -0.395s faster | 64.5% | 821.1 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.509s · Ok | no baseline | parity | 63.6% | 825.5 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.284s · Fast | no baseline | -0.091s faster | 61.7% | 921.7 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.345s · Fast | no baseline | +0.189s slower | 51.1% | 829.7 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.666s · Ok | no baseline | parity | 53.7% | 845.3 MB | ee8c63<br>2026-09-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.274s · Fast | no baseline | parity | 67.4% | 838.3 MB | ee8c63<br>2026-09-17 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.324s · Slow | parity | +0.457s slower | 51.7% | 830.1 MB | ee8c63<br>2026-09-17 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.165s · Slow | parity | parity | 28.2% | 864.3 MB | ee8c63<br>2026-09-17 |

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
