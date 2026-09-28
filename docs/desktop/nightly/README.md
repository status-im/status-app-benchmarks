# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 28, 2026 · [`3e620c9ea`](https://github.com/status-im/status-app/commit/3e620c9ea1dcf232eb43c110b454df679b6afd24)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.442s | 0.777s | 1.577s | 3e620c9ea | 2026-09-28 |
| a 5-image album in a 3-person group | 2.914s | 3.422s | 3.931s | 3e620c9ea | 2026-09-28 |
| a GIF in a 3-person group | 0.434s | 1.061s | 1.960s | 3e620c9ea | 2026-09-28 |
| 10 texts with 0.5s delay in a 3-person group | 0.611s | 1.086s | 2.436s | 3e620c9ea | 2026-09-28 |
| 1000-character text in a 1-on-1 chat | 0.592s | 1.097s | 3.354s | 3e620c9ea | 2026-09-28 |
| a 5-image album in a 1-on-1 chat | 3.579s | 4.166s | 4.676s | 3e620c9ea | 2026-09-28 |
| a GIF in a 1-on-1 chat | 0.872s | 1.620s | 2.583s | 3e620c9ea | 2026-09-28 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.716s | 1.225s | 1.997s | 3e620c9ea | 2026-09-28 |
| 1000-character text in a community #general channel | 0.534s | 0.947s | 2.630s | 3e620c9ea | 2026-09-28 |
| a 5-image album in a community #general channel | 6.489s | 7.111s | 8.648s | 3e620c9ea | 2026-09-28 |
| a GIF in a community #general channel | 0.579s | 1.139s | 3.079s | 3e620c9ea | 2026-09-28 |
| 10 texts with 0.5s delay in a community #general channel | 1.068s | 2.020s | 5.160s | 3e620c9ea | 2026-09-28 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.503s · Ok | +0.131s slower | 62.1% | 777.8 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.424s · Fast | parity | 72.4% | 798.2 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.145s · Fast | parity | 54.2% | 713.7 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.559s · Ok | parity | 61.9% | 832.2 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.418s · Fast | parity | 7.7% | 785.5 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.312s · Fast | -0.159s faster | 50.7% | 700.1 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.416s · Fast | +0.114s slower | 29.2% | 769.0 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.129s · Slow | +0.241s slower | 64.6% | 872.9 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.646s · Ok | +0.148s slower | 36.2% | 858.3 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.994s · Near ok | -0.565s faster | 29.9% | 764.8 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.471s · Fast | -0.098s faster | 22.4% | 933.0 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.188s · Fast | no baseline | 67.5% | 747.2 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.184s · Fast | no baseline | 47.6% | 813.4 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.501s · Ok | no baseline | 86.1% | 817.3 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.120s · Fast | no baseline | 49.7% | 838.5 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.137s · Fast | no baseline | 47.5% | 765.0 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.109s · Fast | no baseline | 46.5% | 779.5 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.442s · Fast | no baseline | 32.5% | 835.2 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.777s · Ok | no baseline | 7.3% | 835.3 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 1.577s · Slow | no baseline | 17.0% | 864.5 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 2.914s · Slow | no baseline | 12.9% | 872.1 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.422s · Slow | no baseline | 2.1% | 855.5 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 3.931s · Slow | no baseline | 2.6% | 856.7 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.434s · Fast | no baseline | 3.5% | 864.8 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 1.061s · Slow | no baseline | 9.1% | 950.7 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 1.960s · Slow | no baseline | 2.2% | 953.6 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.611s · Ok | no baseline | 16.4% | 933.2 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.086s · Slow | no baseline | 3.7% | 933.4 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 2.436s · Slow | no baseline | 4.2% | 932.2 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.592s · Ok | no baseline | 71.7% | 854.6 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 1.097s · Slow | no baseline | 71.7% | 856.6 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 3.354s · Slow | no baseline | 67.6% | 879.7 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.579s · Slow | no baseline | 56.2% | 910.1 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 4.166s · Slow | no baseline | 62.5% | 896.4 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.676s · Slow | no baseline | 1.5% | 896.6 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.872s · Ok | no baseline | 53.2% | 978.8 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.620s · Slow | no baseline | 60.3% | 979.0 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 2.583s · Slow | no baseline | 4.4% | 979.2 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.716s · Ok | no baseline | 39.4% | 984.3 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.225s · Slow | no baseline | 10.3% | 984.6 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.997s · Slow | no baseline | 12.7% | 985.6 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.534s · Ok | no baseline | 33.2% | 1004.4 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.947s · Near ok | no baseline | 1.0% | 1004.4 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 2.630s · Slow | no baseline | 0.9% | 1004.5 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 6.489s · Slow | no baseline | 8.8% | 1028.8 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 7.111s · Slow | no baseline | 1.0% | 1048.9 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 8.648s · Slow | no baseline | 1.2% | 1128.0 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.579s · Ok | no baseline | 3.1% | 1128.3 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.139s · Slow | no baseline | 3.8% | 1128.3 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.079s · Slow | no baseline | 3.0% | 1128.3 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.068s · Slow | no baseline | 8.8% | 1194.8 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.020s · Slow | no baseline | 4.8% | 1190.7 MB | 3e620c9ea<br>2026-09-28 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.160s · Slow | no baseline | 5.3% | 1192.7 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.481s · Fast | parity | 53.4% | 800.4 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.549s · Ok | parity | 71.8% | 822.6 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.422s · Fast | parity | 40.0% | 867.5 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.544s · Ok | -0.205s faster | 48.2% | 807.3 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.433s · Fast | parity | 30.0% | 776.4 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.365s · Fast | -0.557s faster | 36.8% | 806.3 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.314s · Fast | parity | 36.4% | 777.0 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.842s · Slow | parity | 53.2% | 881.5 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.726s · Ok | parity | 32.7% | 876.3 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.653s · Ok | -0.714s faster | 47.2% | 855.6 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.590s · Ok | parity | 57.1% | 949.1 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 2.548s · Slow | no baseline | 67.1% | 756.7 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.413s · Fast | no baseline | 49.3% | 773.7 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.817s · Slow | no baseline | 68.7% | 780.2 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.552s · Ok | no baseline | 47.2% | 806.1 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.590s · Ok | no baseline | 65.7% | 855.4 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.232s · Fast | no baseline | 73.6% | 785.2 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.855s · Ok | +0.630s slower | 24.1% | 845.0 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.539s · Ok | parity | 71.5% | 896.5 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.514s · Ok | +0.167s slower | 47.2% | 842.7 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.568s · Ok | -0.241s faster | 44.6% | 849.3 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.453s · Fast | parity | 74.4% | 853.0 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 1.015s · Slow | parity | 57.0% | 816.7 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.393s · Fast | +0.065s slower | 73.8% | 848.2 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.488s · Slow | -0.282s faster | 42.0% | 883.4 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.655s · Ok | parity | 38.4% | 909.0 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 1.109s · Slow | parity | 67.5% | 926.0 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 1.532s · Slow | +1.018s slower | 50.5% | 993.2 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 1.051s · Slow | no baseline | 67.1% | 875.3 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.426s · Fast | no baseline | 55.1% | 824.1 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.325s · Fast | no baseline | 65.7% | 894.5 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.165s · Fast | no baseline | 60.1% | 824.4 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.802s · Ok | no baseline | 66.1% | 962.7 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.200s · Fast | no baseline | 63.9% | 822.3 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.239s · Slow | parity | 47.1% | 809.8 MB | 3e620c9ea<br>2026-09-28 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.201s · Slow | parity | 51.6% | 882.3 MB | 3e620c9ea<br>2026-09-28 |

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
