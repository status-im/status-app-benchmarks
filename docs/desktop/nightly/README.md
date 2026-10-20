# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Oct 20, 2026 · [`06073b189`](https://github.com/status-im/status-app/commit/06073b189936902449ab23cded3337fd29ff5374)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.448s | 0.811s | 2.101s | 06073b189 | 2026-10-20 |
| a 5-image album in a 3-person group | 3.006s | 3.654s | 4.232s | 06073b189 | 2026-10-20 |
| a GIF in a 3-person group | 0.530s | 1.004s | 1.401s | 06073b189 | 2026-10-20 |
| 10 texts with 0.5s delay in a 3-person group | 0.670s | 1.205s | 3.034s | 06073b189 | 2026-10-20 |
| 1000-character text in a 1-on-1 chat | 0.670s | 1.246s | 2.401s | 06073b189 | 2026-10-20 |
| a 5-image album in a 1-on-1 chat | 3.585s | 4.409s | 5.079s | 06073b189 | 2026-10-20 |
| a GIF in a 1-on-1 chat | 0.761s | 1.548s | 2.175s | 06073b189 | 2026-10-20 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.964s | 1.650s | 2.851s | 06073b189 | 2026-10-20 |
| 1000-character text in a community #general channel | 0.435s | 0.787s | 5.227s | 06073b189 | 2026-10-20 |
| a 5-image album in a community #general channel | 6.386s | 7.092s | 8.806s | 06073b189 | 2026-10-20 |
| a GIF in a community #general channel | 0.587s | 1.185s | 3.181s | 06073b189 | 2026-10-20 |
| 10 texts with 0.5s delay in a community #general channel | 1.469s | 2.817s | 7.390s | 06073b189 | 2026-10-20 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.468s · Fast | +0.096s slower | 54.3% | 760.8 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.376s · Fast | parity | 55.1% | 821.1 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.160s · Fast | parity | 44.4% | 824.8 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.535s · Ok | parity | 51.8% | 856.8 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.396s · Fast | parity | 67.1% | 921.9 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.965s · Near ok | +0.494s slower | 57.2% | 832.4 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.298s · Fast | parity | 47.4% | 897.2 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.185s · Slow | +0.297s slower | 50.7% | 789.1 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.357s · Fast | -0.141s faster | 27.5% | 808.4 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.002s · Slow | -0.557s faster | 54.2% | 878.0 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.649s · Ok | parity | 35.7% | 1004.9 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 4.428s · Slow | no baseline | 59.4% | 910.6 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.164s · Fast | no baseline | 46.8% | 842.9 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.374s · Fast | no baseline | 62.1% | 783.5 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.138s · Fast | no baseline | 53.9% | 849.1 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.243s · Fast | no baseline | 35.5% | 818.2 MB | 06073b189<br>2026-10-20 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.121s · Fast | no baseline | 66.9% | 907.8 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.448s · Fast | no baseline | 20.5% | 882.0 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.811s · Ok | no baseline | 12.4% | 884.3 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 2.101s · Slow | no baseline | 12.2% | 904.0 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 3.006s · Slow | no baseline | 15.8% | 964.7 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.654s · Slow | no baseline | 8.6% | 983.1 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 4.232s · Slow | no baseline | 6.2% | 986.9 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.530s · Ok | no baseline | 2.7% | 988.1 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 1.004s · Slow | no baseline | 2.2% | 988.1 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 1.401s · Slow | no baseline | 5.3% | 988.1 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.670s · Ok | no baseline | 9.2% | 954.0 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.205s · Slow | no baseline | 4.2% | 954.1 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 3.034s · Slow | no baseline | 4.1% | 954.1 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.670s · Ok | no baseline | 68.2% | 833.3 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 1.246s · Slow | no baseline | 54.2% | 833.3 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 2.401s · Slow | no baseline | 57.6% | 833.6 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.585s · Slow | no baseline | 58.2% | 824.9 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 4.409s · Slow | no baseline | 66.6% | 834.9 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 5.079s · Slow | no baseline | 53.0% | 835.1 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.761s · Ok | no baseline | 57.3% | 836.1 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.548s · Slow | no baseline | 59.4% | 836.2 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 2.175s · Slow | no baseline | 55.2% | 836.2 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.964s · Near ok | no baseline | 48.1% | 882.7 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.650s · Slow | no baseline | 32.3% | 882.5 MB | 06073b189<br>2026-10-20 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 2.851s · Slow | no baseline | 26.9% | 886.5 MB | 06073b189<br>2026-10-20 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.435s · Fast | no baseline | 7.1% | 950.2 MB | 06073b189<br>2026-10-20 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.787s · Ok | no baseline | 1.8% | 958.1 MB | 06073b189<br>2026-10-20 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 5.227s · Slow | no baseline | 29.6% | 944.4 MB | 06073b189<br>2026-10-20 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 6.386s · Slow | no baseline | 11.4% | 954.6 MB | 06073b189<br>2026-10-20 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 7.092s · Slow | no baseline | 4.5% | 963.3 MB | 06073b189<br>2026-10-20 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 8.806s · Slow | no baseline | 5.6% | 963.9 MB | 06073b189<br>2026-10-20 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.587s · Ok | no baseline | 3.9% | 965.7 MB | 06073b189<br>2026-10-20 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.185s · Slow | no baseline | 1.8% | 965.7 MB | 06073b189<br>2026-10-20 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.181s · Slow | no baseline | 7.0% | 966.0 MB | 06073b189<br>2026-10-20 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.469s · Slow | no baseline | 25.2% | 944.2 MB | 06073b189<br>2026-10-20 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.817s · Slow | no baseline | 21.6% | 942.7 MB | 06073b189<br>2026-10-20 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 7.390s · Slow | no baseline | 29.4% | 933.3 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.689s · Ok | +0.205s slower | 45.1% | 765.0 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.472s · Fast | -0.108s faster | 55.6% | 814.9 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.575s · Ok | +0.173s slower | 51.5% | 749.5 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.572s · Ok | -0.177s faster | 62.0% | 751.8 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.464s · Fast | parity | 64.7% | 873.0 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 1.089s · Slow | +0.167s slower | 41.5% | 895.2 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.372s · Fast | parity | 67.1% | 809.7 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.398s · Slow | -0.392s faster | 55.2% | 829.1 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.434s · Fast | -0.247s faster | 62.9% | 818.9 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.721s · Ok | -0.646s faster | 45.5% | 791.1 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.930s · Near ok | +0.398s slower | 62.2% | 991.1 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.540s · Ok | no baseline | 60.8% | 803.7 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.693s · Ok | no baseline | 58.6% | 871.4 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.745s · Slow | no baseline | 62.5% | 913.6 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.893s · Ok | no baseline | 59.1% | 871.8 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.511s · Ok | no baseline | 66.4% | 774.9 MB | 06073b189<br>2026-10-20 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.255s · Fast | no baseline | 55.7% | 872.6 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.673s · Ok | +0.448s slower | 43.5% | 814.5 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.500s · Fast | parity | 59.1% | 834.5 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.580s · Ok | +0.233s slower | 50.4% | 804.5 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.639s · Ok | -0.170s faster | 54.2% | 809.1 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.455s · Fast | parity | 63.1% | 912.3 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.661s · Ok | -0.289s faster | 60.0% | 910.7 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.374s · Fast | parity | 65.9% | 866.8 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 0.896s · Ok | -0.874s faster | 47.9% | 806.3 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.491s · Fast | -0.172s faster | 59.8% | 873.1 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.680s · Ok | -0.618s faster | 47.8% | 811.3 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.910s · Near ok | +0.396s slower | 66.0% | 1007.6 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.534s · Ok | no baseline | 68.5% | 793.1 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.695s · Ok | no baseline | 55.9% | 917.9 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.156s · Slow | no baseline | 65.4% | 808.3 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 1.105s · Slow | no baseline | 63.9% | 922.2 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.670s · Ok | no baseline | 71.2% | 810.5 MB | 06073b189<br>2026-10-20 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.253s · Fast | no baseline | 57.0% | 878.4 MB | 06073b189<br>2026-10-20 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 4.433s · Slow | +0.658s slower | 49.4% | 885.1 MB | 06073b189<br>2026-10-20 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 3.572s · Slow | +1.470s slower | 23.1% | 938.7 MB | 06073b189<br>2026-10-20 |

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
