# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Oct 17, 2026 · [`ef004cd98`](https://github.com/status-im/status-app/commit/ef004cd984acbd555ef33a529e924a2c6fce5d27)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.480s | 0.840s | 2.257s | ef004cd98 | 2026-10-17 |
| a 5-image album in a 3-person group | 2.965s | 3.596s | 4.866s | ef004cd98 | 2026-10-17 |
| a GIF in a 3-person group | 0.553s | 1.028s | 2.870s | ef004cd98 | 2026-10-17 |
| 10 texts with 0.5s delay in a 3-person group | 0.657s | 1.184s | 2.775s | ef004cd98 | 2026-10-17 |
| 1000-character text in a 1-on-1 chat | 0.528s | 0.960s | 4.450s | ef004cd98 | 2026-10-17 |
| a 5-image album in a 1-on-1 chat | 2.970s | 3.489s | 3.996s | ef004cd98 | 2026-10-17 |
| a GIF in a 1-on-1 chat | 0.543s | 1.024s | 2.049s | ef004cd98 | 2026-10-17 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.680s | 1.245s | 3.502s | ef004cd98 | 2026-10-17 |
| 1000-character text in a community #general channel | 0.452s | 0.780s | 4.007s | ef004cd98 | 2026-10-17 |
| a 5-image album in a community #general channel | 6.604s | 7.366s | 9.064s | ef004cd98 | 2026-10-17 |
| a GIF in a community #general channel | 0.669s | 1.319s | 3.900s | ef004cd98 | 2026-10-17 |
| 10 texts with 0.5s delay in a community #general channel | 1.180s | 2.324s | 5.826s | ef004cd98 | 2026-10-17 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.736s · Ok | +0.364s slower | 57.1% | 837.0 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.355s · Fast | parity | 52.4% | 930.2 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.149s · Fast | parity | 57.1% | 826.1 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.544s · Ok | parity | 51.7% | 814.0 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.395s · Fast | parity | 54.2% | 918.8 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.945s · Near ok | +0.474s slower | 64.4% | 923.0 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.358s · Fast | +0.056s slower | 47.6% | 915.1 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.215s · Slow | +0.327s slower | 46.3% | 916.6 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.349s · Fast | -0.149s faster | 34.1% | 907.5 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.025s · Slow | -0.534s faster | 51.0% | 827.8 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.593s · Ok | parity | 34.3% | 1046.9 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 6.104s · Slow | no baseline | 56.1% | 887.7 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.175s · Fast | no baseline | 39.5% | 878.9 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.266s · Fast | no baseline | 74.2% | 782.7 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.140s · Fast | no baseline | 63.0% | 863.3 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.165s · Fast | no baseline | 78.1% | 874.3 MB | ef004cd98<br>2026-10-17 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.121s · Fast | no baseline | 55.3% | 1020.7 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.480s · Fast | no baseline | 23.8% | 904.5 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.840s · Ok | no baseline | 8.9% | 906.5 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 2.257s · Slow | no baseline | 9.4% | 910.8 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 2.965s · Slow | no baseline | 10.0% | 928.7 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.596s · Slow | no baseline | 3.6% | 940.3 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 4.866s · Slow | no baseline | 3.5% | 941.2 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.553s · Ok | no baseline | 6.2% | 942.0 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 1.028s · Slow | no baseline | 5.4% | 942.0 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 2.870s · Slow | no baseline | 2.9% | 942.0 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.657s · Ok | no baseline | 14.0% | 967.3 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.184s · Slow | no baseline | 5.7% | 968.7 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 2.775s · Slow | no baseline | 6.6% | 970.5 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.528s · Ok | no baseline | 9.9% | 970.5 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 0.960s · Near ok | no baseline | 9.9% | 970.6 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 4.450s · Slow | no baseline | 13.9% | 969.9 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 2.970s · Slow | no baseline | 18.2% | 961.8 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.489s · Slow | no baseline | 0.8% | 950.0 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 3.996s · Slow | no baseline | 1.2% | 950.0 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.543s · Ok | no baseline | 4.5% | 950.6 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.024s · Slow | no baseline | 4.2% | 950.6 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 2.049s · Slow | no baseline | 3.9% | 950.6 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.680s · Ok | no baseline | 15.6% | 944.3 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.245s · Slow | no baseline | 5.1% | 944.4 MB | ef004cd98<br>2026-10-17 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 3.502s · Slow | no baseline | 4.1% | 944.4 MB | ef004cd98<br>2026-10-17 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.452s · Fast | no baseline | 42.9% | 940.1 MB | ef004cd98<br>2026-10-17 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.780s · Ok | no baseline | 1.8% | 931.7 MB | ef004cd98<br>2026-10-17 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 4.007s · Slow | no baseline | 11.0% | 945.6 MB | ef004cd98<br>2026-10-17 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 6.604s · Slow | no baseline | 10.3% | 999.6 MB | ef004cd98<br>2026-10-17 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 7.366s · Slow | no baseline | 3.5% | 1009.2 MB | ef004cd98<br>2026-10-17 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 9.064s · Slow | no baseline | 1.7% | 1015.7 MB | ef004cd98<br>2026-10-17 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.669s · Ok | no baseline | 3.6% | 1016.3 MB | ef004cd98<br>2026-10-17 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.319s · Slow | no baseline | 2.8% | 1015.6 MB | ef004cd98<br>2026-10-17 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.900s · Slow | no baseline | 3.4% | 1015.6 MB | ef004cd98<br>2026-10-17 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.180s · Slow | no baseline | 8.4% | 1004.6 MB | ef004cd98<br>2026-10-17 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.324s · Slow | no baseline | 6.6% | 1003.3 MB | ef004cd98<br>2026-10-17 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.826s · Slow | no baseline | 4.4% | 996.6 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.732s · Ok | +0.248s slower | 42.7% | 828.6 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.489s · Fast | -0.091s faster | 60.3% | 799.9 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.529s · Ok | +0.127s slower | 52.3% | 802.2 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.663s · Ok | parity | 59.4% | 854.9 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.429s · Fast | parity | 64.7% | 842.8 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.499s · Fast | -0.423s faster | 41.9% | 763.1 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.378s · Fast | parity | 61.8% | 860.0 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 0.907s · Near ok | -0.883s faster | 45.1% | 776.3 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.459s · Fast | -0.222s faster | 58.9% | 818.4 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 1.211s · Slow | parity | 62.6% | 813.0 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.899s · Ok | +0.367s slower | 65.9% | 958.5 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.518s · Ok | no baseline | 70.0% | 780.0 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.757s · Ok | no baseline | 59.7% | 889.4 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 2.238s · Slow | no baseline | 58.8% | 916.1 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 1.013s · Slow | no baseline | 54.9% | 876.1 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.644s · Ok | no baseline | 73.6% | 769.0 MB | ef004cd98<br>2026-10-17 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.237s · Fast | no baseline | 59.4% | 864.0 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.622s · Ok | +0.397s slower | 50.0% | 783.8 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.490s · Fast | -0.093s faster | 56.4% | 832.5 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.541s · Ok | +0.194s slower | 47.1% | 817.5 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 1.204s · Slow | +0.395s slower | 62.8% | 804.5 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.441s · Fast | parity | 62.9% | 847.6 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 1.024s · Slow | parity | 45.3% | 883.5 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.374s · Fast | parity | 73.3% | 818.3 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 0.911s · Near ok | -0.859s faster | 40.7% | 852.6 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.499s · Fast | -0.164s faster | 64.4% | 842.9 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 1.213s · Slow | parity | 57.6% | 937.7 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.762s · Ok | +0.248s slower | 66.2% | 988.3 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.600s · Ok | no baseline | 74.8% | 831.4 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.621s · Ok | no baseline | 57.4% | 887.9 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.538s · Ok | no baseline | 65.8% | 785.6 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.801s · Ok | no baseline | 55.9% | 875.6 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.603s · Ok | no baseline | 77.1% | 842.0 MB | ef004cd98<br>2026-10-17 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.241s · Fast | no baseline | 56.7% | 878.9 MB | ef004cd98<br>2026-10-17 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 4.107s · Slow | parity | 43.0% | 948.0 MB | ef004cd98<br>2026-10-17 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 3.619s · Slow | +1.517s slower | 36.7% | 995.9 MB | ef004cd98<br>2026-10-17 |

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

**Visible** is the time from pressing Send until the outgoing message appears in the chat view, before ticks. **Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

- [Time to Visible after sending 1000-character text in a 3-person group](charts/group_chat_plain_text_visible_time.html)

- [CPU usage while waiting for Visible after sending 1000-character text](charts/group_chat_plain_text_visible_cpu.html)

- [RAM usage while waiting for Visible after sending 1000-character text](charts/group_chat_plain_text_visible_ram.html)

- [Time to Sent after sending 1000-character text in a 3-person group](charts/group_chat_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/group_chat_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/group_chat_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a 3-person group](charts/group_chat_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/group_chat_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/group_chat_plain_text_delivered_ram.html)

- [Time to Visible after sending a 5-image album in a 3-person group](charts/group_chat_album_visible_time.html)

- [CPU usage while waiting for Visible after sending a 5-image album](charts/group_chat_album_visible_cpu.html)

- [RAM usage while waiting for Visible after sending a 5-image album](charts/group_chat_album_visible_ram.html)

- [Time to Sent after sending a 5-image album in a 3-person group](charts/group_chat_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/group_chat_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/group_chat_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a 3-person group](charts/group_chat_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/group_chat_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/group_chat_album_delivered_ram.html)

- [Time to Visible after sending a GIF in a 3-person group](charts/group_chat_gif_visible_time.html)

- [CPU usage while waiting for Visible after sending a GIF](charts/group_chat_gif_visible_cpu.html)

- [RAM usage while waiting for Visible after sending a GIF](charts/group_chat_gif_visible_ram.html)

- [Time to Sent after sending a GIF in a 3-person group](charts/group_chat_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/group_chat_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/group_chat_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a 3-person group](charts/group_chat_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/group_chat_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/group_chat_gif_delivered_ram.html)

- [Time to Visible after sending 10 texts with 0.5s delay in a 3-person group](charts/group_chat_burst_visible_time.html)

- [CPU usage while waiting for Visible after sending 10 texts with 0.5s delay](charts/group_chat_burst_visible_cpu.html)

- [RAM usage while waiting for Visible after sending 10 texts with 0.5s delay](charts/group_chat_burst_visible_ram.html)

- [Time to Sent after sending 10 texts with 0.5s delay in a 3-person group](charts/group_chat_burst_sent_time.html)

- [CPU usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/group_chat_burst_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/group_chat_burst_sent_ram.html)

- [Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group](charts/group_chat_burst_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/group_chat_burst_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/group_chat_burst_delivered_ram.html)

- [Time to Visible after sending 1000-character text in a 1-on-1 chat](charts/direct_chat_plain_text_visible_time.html)

- [CPU usage while waiting for Visible after sending 1000-character text](charts/direct_chat_plain_text_visible_cpu.html)

- [RAM usage while waiting for Visible after sending 1000-character text](charts/direct_chat_plain_text_visible_ram.html)

- [Time to Sent after sending 1000-character text in a 1-on-1 chat](charts/direct_chat_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/direct_chat_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/direct_chat_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a 1-on-1 chat](charts/direct_chat_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/direct_chat_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/direct_chat_plain_text_delivered_ram.html)

- [Time to Visible after sending a 5-image album in a 1-on-1 chat](charts/direct_chat_album_visible_time.html)

- [CPU usage while waiting for Visible after sending a 5-image album](charts/direct_chat_album_visible_cpu.html)

- [RAM usage while waiting for Visible after sending a 5-image album](charts/direct_chat_album_visible_ram.html)

- [Time to Sent after sending a 5-image album in a 1-on-1 chat](charts/direct_chat_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/direct_chat_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/direct_chat_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a 1-on-1 chat](charts/direct_chat_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/direct_chat_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/direct_chat_album_delivered_ram.html)

- [Time to Visible after sending a GIF in a 1-on-1 chat](charts/direct_chat_gif_visible_time.html)

- [CPU usage while waiting for Visible after sending a GIF](charts/direct_chat_gif_visible_cpu.html)

- [RAM usage while waiting for Visible after sending a GIF](charts/direct_chat_gif_visible_ram.html)

- [Time to Sent after sending a GIF in a 1-on-1 chat](charts/direct_chat_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/direct_chat_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/direct_chat_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a 1-on-1 chat](charts/direct_chat_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/direct_chat_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/direct_chat_gif_delivered_ram.html)

- [Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat](charts/direct_chat_burst_visible_time.html)

- [CPU usage while waiting for Visible after sending 10 texts with 0.5s delay](charts/direct_chat_burst_visible_cpu.html)

- [RAM usage while waiting for Visible after sending 10 texts with 0.5s delay](charts/direct_chat_burst_visible_ram.html)

- [Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat](charts/direct_chat_burst_sent_time.html)

- [CPU usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/direct_chat_burst_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/direct_chat_burst_sent_ram.html)

- [Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat](charts/direct_chat_burst_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/direct_chat_burst_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/direct_chat_burst_delivered_ram.html)

### Communities

**Visible** is the time from pressing Send until the outgoing message appears in the chat view, before ticks. **Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

- [Time to Visible after sending 1000-character text in a community #general channel](charts/community_general_plain_text_visible_time.html)

- [CPU usage while waiting for Visible after sending 1000-character text](charts/community_general_plain_text_visible_cpu.html)

- [RAM usage while waiting for Visible after sending 1000-character text](charts/community_general_plain_text_visible_ram.html)

- [Time to Sent after sending 1000-character text in a community #general channel](charts/community_general_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/community_general_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/community_general_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a community #general channel](charts/community_general_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/community_general_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/community_general_plain_text_delivered_ram.html)

- [Time to Visible after sending a 5-image album in a community #general channel](charts/community_general_album_visible_time.html)

- [CPU usage while waiting for Visible after sending a 5-image album](charts/community_general_album_visible_cpu.html)

- [RAM usage while waiting for Visible after sending a 5-image album](charts/community_general_album_visible_ram.html)

- [Time to Sent after sending a 5-image album in a community #general channel](charts/community_general_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/community_general_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/community_general_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a community #general channel](charts/community_general_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/community_general_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/community_general_album_delivered_ram.html)

- [Time to Visible after sending a GIF in a community #general channel](charts/community_general_gif_visible_time.html)

- [CPU usage while waiting for Visible after sending a GIF](charts/community_general_gif_visible_cpu.html)

- [RAM usage while waiting for Visible after sending a GIF](charts/community_general_gif_visible_ram.html)

- [Time to Sent after sending a GIF in a community #general channel](charts/community_general_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/community_general_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/community_general_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a community #general channel](charts/community_general_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/community_general_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/community_general_gif_delivered_ram.html)

- [Time to Visible after sending 10 texts with 0.5s delay in a community #general channel](charts/community_general_burst_visible_time.html)

- [CPU usage while waiting for Visible after sending 10 texts with 0.5s delay](charts/community_general_burst_visible_cpu.html)

- [RAM usage while waiting for Visible after sending 10 texts with 0.5s delay](charts/community_general_burst_visible_ram.html)

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
