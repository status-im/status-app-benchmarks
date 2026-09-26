# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 26, 2026 · [`3e620c9ea`](https://github.com/status-im/status-app/commit/3e620c9ea1dcf232eb43c110b454df679b6afd24)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.429s | 0.827s | 1.192s | 3e620c9ea | 2026-09-26 |
| a 5-image album in a 3-person group | 2.930s | 3.433s | 3.918s | 3e620c9ea | 2026-09-26 |
| a GIF in a 3-person group | 0.439s | 0.839s | 1.231s | 3e620c9ea | 2026-09-26 |
| 10 texts with 0.5s delay in a 3-person group | 0.638s | 1.110s | 2.725s | 3e620c9ea | 2026-09-26 |
| 1000-character text in a 1-on-1 chat | 0.502s | 0.922s | 1.270s | 3e620c9ea | 2026-09-26 |
| a 5-image album in a 1-on-1 chat | 3.351s | 3.844s | 4.339s | 3e620c9ea | 2026-09-26 |
| a GIF in a 1-on-1 chat | 0.722s | 1.101s | 1.489s | 3e620c9ea | 2026-09-26 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.659s | 1.154s | 1.895s | 3e620c9ea | 2026-09-26 |
| 1000-character text in a community #general channel | 0.446s | 0.796s | 2.471s | 3e620c9ea | 2026-09-26 |
| a 5-image album in a community #general channel | 6.587s | 7.417s | 9.086s | 3e620c9ea | 2026-09-26 |
| a GIF in a community #general channel | 0.559s | 1.165s | 3.089s | 3e620c9ea | 2026-09-26 |
| 10 texts with 0.5s delay in a community #general channel | 1.104s | 2.128s | 5.479s | 3e620c9ea | 2026-09-26 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.477s · Fast | +0.105s slower | 55.3% | 694.9 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.484s · Fast | +0.105s slower | 58.2% | 813.5 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.105s · Fast | -0.052s faster | 39.4% | 770.4 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.477s · Fast | -0.134s faster | 30.0% | 707.5 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.387s · Fast | parity | 15.9% | 772.8 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.414s · Fast | parity | 47.6% | 848.1 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.430s · Fast | +0.128s slower | 22.2% | 806.2 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.014s · Slow | parity | 42.6% | 828.0 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.653s · Ok | +0.155s slower | 23.3% | 833.2 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.031s · Slow | -0.528s faster | 56.3% | 779.9 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.557s · Ok | parity | 32.8% | 894.1 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.138s · Fast | no baseline | 67.2% | 693.1 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.176s · Fast | no baseline | 51.1% | 741.9 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.254s · Fast | no baseline | 73.7% | 717.2 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.130s · Fast | no baseline | 56.0% | 709.6 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.158s · Fast | no baseline | 53.9% | 706.3 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.118s · Fast | no baseline | 53.2% | 693.3 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.429s · Fast | no baseline | 22.5% | 783.9 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.827s · Ok | no baseline | 1.8% | 784.0 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 1.192s · Slow | no baseline | 5.4% | 784.3 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 2.930s · Slow | no baseline | 7.1% | 797.4 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.433s · Slow | no baseline | 20.3% | 878.4 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 3.918s · Slow | no baseline | 1.7% | 841.8 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.439s · Fast | no baseline | 1.8% | 836.6 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.839s · Ok | no baseline | 2.1% | 917.7 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 1.231s · Slow | no baseline | 6.2% | 917.7 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.638s · Ok | no baseline | 14.1% | 885.5 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.110s · Slow | no baseline | 4.6% | 883.5 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 2.725s · Slow | no baseline | 4.3% | 880.5 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.502s · Ok | no baseline | 5.4% | 794.1 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 0.922s · Near ok | no baseline | 1.8% | 794.2 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 1.270s · Slow | no baseline | 7.2% | 794.2 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.351s · Slow | no baseline | 27.9% | 779.8 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.844s · Slow | no baseline | 1.9% | 784.3 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.339s · Slow | no baseline | 2.9% | 784.6 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.722s · Ok | no baseline | 14.1% | 866.9 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.101s · Slow | no baseline | 2.7% | 867.1 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 1.489s · Slow | no baseline | 2.7% | 867.2 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.659s · Ok | no baseline | 21.3% | 876.0 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.154s · Slow | no baseline | 4.6% | 874.3 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.895s · Slow | no baseline | 3.9% | 872.9 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.446s · Fast | no baseline | 66.5% | 810.8 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.796s · Ok | no baseline | 6.2% | 810.8 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 2.471s · Slow | no baseline | 2.2% | 801.3 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 6.587s · Slow | no baseline | 6.5% | 827.8 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 7.417s · Slow | no baseline | 13.3% | 928.8 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 9.086s · Slow | no baseline | 5.0% | 944.3 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.559s · Ok | no baseline | 2.5% | 945.5 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.165s · Slow | no baseline | 5.9% | 945.5 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.089s · Slow | no baseline | 3.4% | 945.5 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.104s · Slow | no baseline | 7.0% | 932.8 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.128s · Slow | no baseline | 4.8% | 930.1 MB | 3e620c9ea<br>2026-09-26 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.479s · Slow | no baseline | 4.8% | 928.7 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.396s · Fast | -0.088s faster | 37.0% | 812.9 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.548s · Ok | parity | 73.0% | 804.0 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.415s · Fast | parity | 31.3% | 812.8 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.632s · Ok | -0.117s faster | 52.5% | 862.1 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.399s · Fast | parity | 40.1% | 798.0 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.386s · Fast | -0.536s faster | 25.8% | 786.0 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.330s · Fast | parity | 37.1% | 778.6 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.216s · Slow | -0.574s faster | 32.2% | 873.2 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.635s · Ok | parity | 35.9% | 875.7 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.659s · Ok | -0.708s faster | 63.5% | 772.5 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.557s · Ok | parity | 49.0% | 885.8 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 2.520s · Slow | no baseline | 65.6% | 823.2 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.439s · Fast | no baseline | 48.1% | 821.6 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.346s · Fast | no baseline | 57.6% | 838.0 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.321s · Fast | no baseline | 47.5% | 809.8 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.673s · Ok | no baseline | 73.6% | 797.7 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.229s · Fast | no baseline | 44.2% | 803.5 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.584s · Ok | +0.359s slower | 57.9% | 911.7 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.577s · Ok | parity | 70.7% | 863.0 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.774s · Ok | +0.427s slower | 49.2% | 834.4 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.482s · Fast | -0.327s faster | 56.2% | 841.4 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.460s · Fast | parity | 64.4% | 856.7 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.571s · Ok | -0.379s faster | 48.7% | 848.6 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.408s · Fast | +0.080s slower | 66.2% | 831.4 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.852s · Slow | parity | 68.1% | 888.6 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.796s · Ok | +0.133s slower | 58.5% | 901.1 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.728s · Ok | -0.570s faster | 43.4% | 922.8 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.745s · Ok | +0.231s slower | 66.9% | 992.5 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.391s · Fast | no baseline | 79.2% | 851.5 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.441s · Fast | no baseline | 56.7% | 804.4 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.329s · Fast | no baseline | 82.4% | 804.8 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.152s · Fast | no baseline | 76.7% | 793.3 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.585s · Ok | no baseline | 63.9% | 840.4 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.246s · Fast | no baseline | 62.0% | 834.5 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.002s · Slow | -0.773s faster | 43.1% | 789.2 MB | 3e620c9ea<br>2026-09-26 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.147s · Slow | parity | 10.2% | 838.8 MB | 3e620c9ea<br>2026-09-26 |

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
