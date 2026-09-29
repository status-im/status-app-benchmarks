# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 29, 2026 · [`3e620c9ea`](https://github.com/status-im/status-app/commit/3e620c9ea1dcf232eb43c110b454df679b6afd24)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.433s | 0.765s | 1.063s | 3e620c9ea | 2026-09-29 |
| a 5-image album in a 3-person group | 2.877s | 3.364s | 3.847s | 3e620c9ea | 2026-09-29 |
| a GIF in a 3-person group | 0.476s | 0.953s | 2.692s | 3e620c9ea | 2026-09-29 |
| 10 texts with 0.5s delay in a 3-person group | 0.607s | 1.066s | 2.508s | 3e620c9ea | 2026-09-29 |
| 1000-character text in a 1-on-1 chat | 0.516s | 0.868s | 1.662s | 3e620c9ea | 2026-09-29 |
| a 5-image album in a 1-on-1 chat | 3.040s | 3.531s | 4.016s | 3e620c9ea | 2026-09-29 |
| a GIF in a 1-on-1 chat | 0.458s | 0.961s | 1.343s | 3e620c9ea | 2026-09-29 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.632s | 1.122s | 2.438s | 3e620c9ea | 2026-09-29 |
| 1000-character text in a community #general channel | 0.445s | 0.762s | 2.521s | 3e620c9ea | 2026-09-29 |
| a 5-image album in a community #general channel | 6.359s | 7.120s | 8.727s | 3e620c9ea | 2026-09-29 |
| a GIF in a community #general channel | 0.574s | 1.167s | 3.036s | 3e620c9ea | 2026-09-29 |
| 10 texts with 0.5s delay in a community #general channel | 1.084s | 2.140s | 5.360s | 3e620c9ea | 2026-09-29 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.491s · Fast | +0.119s slower | 67.8% | 738.3 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.429s · Fast | parity | 66.3% | 823.9 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.106s · Fast | -0.051s faster | 53.6% | 688.6 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.485s · Fast | -0.126s faster | 34.4% | 695.0 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.388s · Fast | parity | 17.0% | 774.7 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.287s · Fast | -0.184s faster | 37.1% | 690.7 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.297s · Fast | parity | 24.2% | 740.7 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.036s · Slow | +0.148s slower | 40.5% | 796.8 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.516s · Ok | parity | 20.4% | 893.8 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.976s · Near ok | -0.583s faster | 35.6% | 765.7 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.531s · Ok | parity | 19.9% | 899.7 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.143s · Fast | no baseline | 52.3% | 678.2 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.182s · Fast | no baseline | 46.8% | 693.1 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.264s · Fast | no baseline | 87.8% | 755.6 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.122s · Fast | no baseline | 60.4% | 801.7 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.499s · Fast | no baseline | 21.7% | 747.0 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.106s · Fast | no baseline | 36.5% | 747.1 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.433s · Fast | no baseline | 5.0% | 757.9 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.765s · Ok | no baseline | 3.8% | 757.9 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 1.063s · Slow | no baseline | 5.0% | 758.1 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 2.877s · Slow | no baseline | 14.5% | 775.1 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.364s · Slow | no baseline | 1.2% | 782.0 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 3.847s · Slow | no baseline | 0.8% | 782.0 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.476s · Fast | no baseline | 7.3% | 782.4 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.953s · Near ok | no baseline | 20.4% | 863.0 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 2.692s · Slow | no baseline | 3.5% | 863.9 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.607s · Ok | no baseline | 15.0% | 873.3 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.066s · Slow | no baseline | 4.2% | 873.1 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 2.508s · Slow | no baseline | 4.4% | 875.9 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.516s · Ok | no baseline | 22.4% | 739.1 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 0.868s · Ok | no baseline | 2.1% | 740.0 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 1.662s · Slow | no baseline | 3.8% | 743.6 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.040s · Slow | no baseline | 23.0% | 763.4 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.531s · Slow | no baseline | 0.8% | 742.8 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.016s · Slow | no baseline | 1.2% | 741.0 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.458s · Fast | no baseline | 3.1% | 744.4 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 0.961s · Near ok | no baseline | 10.2% | 826.6 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 1.343s · Slow | no baseline | 8.3% | 826.8 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.632s · Ok | no baseline | 13.4% | 826.9 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.122s · Slow | no baseline | 3.6% | 827.0 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 2.438s · Slow | no baseline | 3.6% | 827.5 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.445s · Fast | no baseline | 32.5% | 807.7 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.762s · Ok | no baseline | 3.1% | 807.7 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 2.521s · Slow | no baseline | 8.4% | 807.8 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 6.359s · Slow | no baseline | 10.7% | 837.1 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 7.120s · Slow | no baseline | 23.3% | 930.7 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 8.727s · Slow | no baseline | 3.5% | 952.9 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.574s · Ok | no baseline | 4.4% | 953.8 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.167s · Slow | no baseline | 2.8% | 953.8 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.036s · Slow | no baseline | 5.8% | 954.0 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.084s · Slow | no baseline | 8.2% | 941.1 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.140s · Slow | no baseline | 4.7% | 939.2 MB | 3e620c9ea<br>2026-09-29 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.360s · Slow | no baseline | 4.9% | 934.9 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.594s · Ok | +0.110s slower | 49.5% | 972.8 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.539s · Ok | parity | 70.8% | 773.1 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.360s · Fast | parity | 27.7% | 803.0 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.663s · Ok | parity | 51.5% | 871.1 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.418s · Fast | parity | 48.5% | 818.3 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.483s · Fast | -0.439s faster | 28.8% | 750.5 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.326s · Fast | parity | 38.9% | 736.9 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 2.155s · Slow | +0.365s slower | 64.6% | 835.9 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.724s · Ok | parity | 37.5% | 831.5 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.575s · Ok | -0.792s faster | 33.4% | 857.7 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.646s · Ok | +0.114s slower | 30.9% | 926.4 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.166s · Fast | no baseline | 49.3% | 794.1 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.662s · Ok | no baseline | 49.0% | 817.5 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.286s · Fast | no baseline | 41.7% | 760.0 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.667s · Ok | no baseline | 54.0% | 805.9 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.698s · Ok | no baseline | 51.6% | 924.7 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.273s · Fast | no baseline | 61.7% | 817.7 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.483s · Fast | +0.258s slower | 26.8% | 845.3 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.576s · Ok | parity | 70.3% | 864.9 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.597s · Ok | +0.250s slower | 41.8% | 828.2 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.544s · Ok | -0.265s faster | 48.1% | 896.0 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.429s · Fast | parity | 49.7% | 850.7 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.426s · Fast | -0.524s faster | 42.3% | 837.8 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.372s · Fast | parity | 50.7% | 808.9 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.820s · Slow | parity | 58.4% | 919.6 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.810s · Ok | +0.147s slower | 64.7% | 939.1 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 1.090s · Slow | -0.208s faster | 58.2% | 843.7 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.733s · Ok | +0.219s slower | 62.8% | 968.7 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.157s · Fast | no baseline | 62.1% | 783.5 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.491s · Fast | no baseline | 67.7% | 801.4 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.452s · Fast | no baseline | 49.9% | 830.5 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.197s · Fast | no baseline | 56.9% | 787.9 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.630s · Ok | no baseline | 62.0% | 791.9 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.220s · Fast | no baseline | 63.5% | 794.7 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 2.791s · Slow | -0.984s faster | 54.4% | 844.2 MB | 3e620c9ea<br>2026-09-29 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.178s · Slow | parity | 42.2% | 894.8 MB | 3e620c9ea<br>2026-09-29 |

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
