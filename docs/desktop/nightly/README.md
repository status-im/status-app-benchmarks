# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 30, 2026 · [`3e620c9ea`](https://github.com/status-im/status-app/commit/3e620c9ea1dcf232eb43c110b454df679b6afd24)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.438s | 0.819s | 2.028s | 3e620c9ea | 2026-09-30 |
| a 5-image album in a 3-person group | 2.914s | 3.481s | 5.951s | 3e620c9ea | 2026-09-30 |
| a GIF in a 3-person group | 0.684s | 1.282s | 2.516s | 3e620c9ea | 2026-09-30 |
| 10 texts with 0.5s delay in a 3-person group | 0.613s | 1.070s | 3.458s | 3e620c9ea | 2026-09-30 |
| 1000-character text in a 1-on-1 chat | 0.500s | 0.856s | 1.176s | 3e620c9ea | 2026-09-30 |
| a 5-image album in a 1-on-1 chat | 3.065s | 3.560s | 4.054s | 3e620c9ea | 2026-09-30 |
| a GIF in a 1-on-1 chat | 0.552s | 1.005s | 1.381s | 3e620c9ea | 2026-09-30 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.656s | 1.178s | 2.478s | 3e620c9ea | 2026-09-30 |
| 1000-character text in a community #general channel | 0.425s | 0.968s | 2.868s | 3e620c9ea | 2026-09-30 |
| a 5-image album in a community #general channel | 6.380s | 7.151s | 8.775s | 3e620c9ea | 2026-09-30 |
| a GIF in a community #general channel | 0.558s | 1.168s | 3.006s | 3e620c9ea | 2026-09-30 |
| 10 texts with 0.5s delay in a community #general channel | 1.108s | 2.226s | 5.551s | 3e620c9ea | 2026-09-30 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.541s · Ok | +0.169s slower | 45.4% | 737.8 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.495s · Fast | +0.116s slower | 68.8% | 801.1 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.107s · Fast | -0.050s faster | 4.2% | 693.7 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.575s · Ok | parity | 51.7% | 682.1 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.403s · Fast | parity | 25.6% | 751.5 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.266s · Fast | -0.205s faster | 34.2% | 748.4 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.303s · Fast | parity | 30.0% | 807.7 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.587s · Slow | +0.699s slower | 29.4% | 873.9 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.581s · Ok | +0.083s slower | 23.4% | 856.2 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.965s · Near ok | -0.594s faster | 48.6% | 728.8 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.488s · Fast | parity | 20.5% | 909.9 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.138s · Fast | no baseline | 28.9% | 757.7 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.185s · Fast | no baseline | 46.7% | 789.4 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.258s · Fast | no baseline | 26.7% | 702.5 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.128s · Fast | no baseline | 47.4% | 745.0 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.142s · Fast | no baseline | 87.8% | 714.2 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.107s · Fast | no baseline | 47.8% | 730.9 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.438s · Fast | no baseline | 83.0% | 759.0 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.819s · Ok | no baseline | 2.7% | 759.1 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 2.028s · Slow | no baseline | 4.1% | 759.3 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 2.914s · Slow | no baseline | 10.0% | 769.9 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.481s · Slow | no baseline | 1.1% | 782.1 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 5.951s · Slow | no baseline | 4.7% | 827.8 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.684s · Ok | no baseline | 67.5% | 863.8 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 1.282s · Slow | no baseline | 55.8% | 865.8 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 2.516s · Slow | no baseline | 59.6% | 865.9 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.613s · Ok | no baseline | 15.2% | 857.8 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.070s · Slow | no baseline | 4.1% | 857.9 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 3.458s · Slow | no baseline | 6.5% | 858.6 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.500s · Fast | no baseline | 4.2% | 806.0 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 0.856s · Ok | no baseline | 3.1% | 785.9 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 1.176s · Slow | no baseline | 5.0% | 767.1 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.065s · Slow | no baseline | 29.3% | 783.4 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.560s · Slow | no baseline | 0.8% | 789.5 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.054s · Slow | no baseline | 1.2% | 786.3 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.552s · Ok | no baseline | 31.8% | 857.0 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.005s · Slow | no baseline | 15.1% | 910.9 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 1.381s · Slow | no baseline | 2.7% | 901.2 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.656s · Ok | no baseline | 11.3% | 868.1 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.178s · Slow | no baseline | 5.0% | 864.8 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 2.478s · Slow | no baseline | 4.0% | 864.5 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.425s · Fast | no baseline | 35.7% | 816.0 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.968s · Near ok | no baseline | 2.1% | 816.0 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 2.868s · Slow | no baseline | 4.8% | 817.1 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 6.380s · Slow | no baseline | 10.4% | 835.3 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 7.151s · Slow | no baseline | 19.6% | 927.1 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 8.775s · Slow | no baseline | 3.3% | 952.3 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.558s · Ok | no baseline | 2.7% | 947.9 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.168s · Slow | no baseline | 7.6% | 948.0 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.006s · Slow | no baseline | 3.1% | 948.2 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.108s · Slow | no baseline | 7.2% | 948.6 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.226s · Slow | no baseline | 4.4% | 948.5 MB | 3e620c9ea<br>2026-09-30 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.551s · Slow | no baseline | 4.7% | 947.6 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.220s · Fast | -0.264s faster | 57.8% | 937.2 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.540s · Ok | parity | 64.6% | 797.4 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.380s · Fast | parity | 47.2% | 819.8 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 1.091s · Slow | +0.342s slower | 52.0% | 904.7 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.419s · Fast | parity | 44.5% | 795.4 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 1.112s · Slow | +0.190s slower | 35.6% | 775.3 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.339s · Fast | parity | 33.8% | 766.8 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.304s · Slow | -0.486s faster | 46.0% | 947.2 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.651s · Ok | parity | 44.8% | 871.4 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.730s · Ok | -0.637s faster | 47.8% | 848.7 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.600s · Ok | parity | 71.7% | 926.4 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.969s · Near ok | no baseline | 56.5% | 866.5 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.560s · Ok | no baseline | 53.8% | 821.3 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.590s · Slow | no baseline | 61.6% | 862.3 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.498s · Fast | no baseline | 54.8% | 826.4 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.660s · Ok | no baseline | 57.3% | 820.5 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.226s · Fast | no baseline | 58.4% | 772.9 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.797s · Ok | +0.572s slower | 27.3% | 847.9 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.562s · Ok | parity | 70.8% | 799.4 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.670s · Ok | +0.323s slower | 46.0% | 870.8 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.640s · Ok | -0.169s faster | 46.7% | 855.3 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.430s · Fast | parity | 46.5% | 844.8 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.518s · Ok | -0.432s faster | 33.7% | 814.5 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.360s · Fast | parity | 51.0% | 837.4 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.343s · Slow | -0.427s faster | 31.7% | 882.1 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.815s · Ok | +0.152s slower | 66.6% | 932.5 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.747s · Ok | -0.551s faster | 37.2% | 833.6 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.851s · Ok | +0.337s slower | 45.1% | 958.5 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.169s · Fast | no baseline | 46.6% | 825.6 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.479s · Fast | no baseline | 64.1% | 800.9 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.325s · Fast | no baseline | 58.7% | 781.0 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.151s · Fast | no baseline | 66.3% | 785.3 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.552s · Ok | no baseline | 65.3% | 842.0 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.230s · Fast | no baseline | 60.9% | 806.3 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.588s · Slow | parity | 39.4% | 821.8 MB | 3e620c9ea<br>2026-09-30 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.205s · Slow | parity | 9.7% | 857.0 MB | 3e620c9ea<br>2026-09-30 |

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
