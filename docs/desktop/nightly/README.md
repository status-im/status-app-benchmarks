# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Oct 06, 2026 · [`f2cacb3e5`](https://github.com/status-im/status-app/commit/f2cacb3e52d6a2fd81dd42cb757051feb2e82778)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.442s | 0.762s | 2.755s | f2cacb3e5 | 2026-10-06 |
| a 5-image album in a 3-person group | 2.996s | 3.612s | 4.874s | f2cacb3e5 | 2026-10-06 |
| a GIF in a 3-person group | 0.402s | 0.832s | 2.294s | f2cacb3e5 | 2026-10-06 |
| 10 texts with 0.5s delay in a 3-person group | 0.622s | 1.109s | 2.737s | f2cacb3e5 | 2026-10-06 |
| 1000-character text in a 1-on-1 chat | 0.622s | 1.021s | 1.418s | f2cacb3e5 | 2026-10-06 |
| a 5-image album in a 1-on-1 chat | 3.332s | 3.831s | 4.330s | f2cacb3e5 | 2026-10-06 |
| a GIF in a 1-on-1 chat | 0.487s | 0.968s | 1.982s | f2cacb3e5 | 2026-10-06 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.708s | 1.259s | 2.312s | f2cacb3e5 | 2026-10-06 |
| 1000-character text in a community #general channel | 0.583s | 1.032s | 2.664s | f2cacb3e5 | 2026-10-06 |
| a 5-image album in a community #general channel | 6.532s | 7.180s | 8.811s | f2cacb3e5 | 2026-10-06 |
| a GIF in a community #general channel | 0.599s | 1.151s | 3.102s | f2cacb3e5 | 2026-10-06 |
| 10 texts with 0.5s delay in a community #general channel | 1.115s | 2.142s | 5.444s | f2cacb3e5 | 2026-10-06 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.489s · Fast | +0.117s slower | 61.8% | 753.0 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.432s · Fast | parity | 66.4% | 835.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.152s · Fast | parity | 51.5% | 774.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.455s · Fast | -0.156s faster | 9.9% | 676.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.386s · Fast | parity | 15.3% | 799.9 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.384s · Fast | -0.087s faster | 31.9% | 814.1 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.298s · Fast | parity | 22.3% | 782.1 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.061s · Slow | +0.173s slower | 43.0% | 707.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.492s · Fast | parity | 29.3% | 781.7 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.031s · Slow | -0.528s faster | 53.1% | 723.3 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.555s · Ok | parity | 41.8% | 917.2 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.137s · Fast | no baseline | 21.3% | 740.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.170s · Fast | no baseline | 44.5% | 794.1 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.230s · Fast | no baseline | 44.6% | 687.5 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.116s · Fast | no baseline | 30.3% | 712.4 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.585s · Ok | no baseline | 44.1% | 801.0 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.104s · Fast | no baseline | 28.4% | 794.3 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.442s · Fast | no baseline | 33.8% | 781.8 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.762s · Ok | no baseline | 6.3% | 782.4 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 2.755s · Slow | no baseline | 4.0% | 782.9 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 2.996s · Slow | no baseline | 12.3% | 784.0 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.612s · Slow | no baseline | 3.3% | 788.1 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 4.874s · Slow | no baseline | 3.4% | 788.2 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.402s · Fast | no baseline | 2.7% | 789.2 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.832s · Ok | no baseline | 2.7% | 789.2 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 2.294s · Slow | no baseline | 3.4% | 789.2 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.622s · Ok | no baseline | 15.5% | 778.8 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.109s · Slow | no baseline | 4.2% | 778.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 2.737s · Slow | no baseline | 3.9% | 778.7 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.622s · Ok | no baseline | 86.1% | 803.4 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 1.021s · Slow | no baseline | 72.8% | 806.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 1.418s · Slow | no baseline | 8.1% | 806.7 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.332s · Slow | no baseline | 31.6% | 822.7 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.831s · Slow | no baseline | 1.6% | 839.5 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.330s · Slow | no baseline | 2.5% | 807.7 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.487s · Fast | no baseline | 22.1% | 777.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 0.968s · Near ok | no baseline | 3.9% | 765.8 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 1.982s · Slow | no baseline | 5.2% | 765.8 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.708s · Ok | no baseline | 30.9% | 765.4 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.259s · Slow | no baseline | 15.5% | 765.7 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 2.312s · Slow | no baseline | 17.2% | 766.3 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.583s · Ok | no baseline | 37.6% | 790.1 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 1.032s · Slow | no baseline | 58.6% | 790.1 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 2.664s · Slow | no baseline | 47.8% | 790.7 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 6.532s · Slow | no baseline | 10.2% | 820.4 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 7.180s · Slow | no baseline | 1.0% | 832.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 8.811s · Slow | no baseline | 2.4% | 832.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.599s · Ok | no baseline | 5.0% | 826.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.151s · Slow | no baseline | 4.9% | 826.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.102s · Slow | no baseline | 8.1% | 826.6 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.115s · Slow | no baseline | 6.7% | 817.4 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.142s · Slow | no baseline | 4.8% | 817.5 MB | f2cacb3e5<br>2026-10-06 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.444s · Slow | no baseline | 4.6% | 816.9 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.906s · Near ok | +0.422s slower | 20.0% | 795.4 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.527s · Ok | parity | 63.8% | 772.2 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.573s · Ok | +0.171s slower | 48.9% | 859.3 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.432s · Fast | -0.317s faster | 32.4% | 756.0 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.401s · Fast | parity | 25.5% | 747.5 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.984s · Near ok | parity | 32.9% | 790.4 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.312s · Fast | parity | 35.7% | 756.0 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.048s · Slow | -0.742s faster | 37.1% | 803.2 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.408s · Fast | -0.273s faster | 27.9% | 758.7 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.680s · Ok | -0.687s faster | 38.7% | 818.2 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.631s · Ok | +0.099s slower | 38.5% | 918.6 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 3.079s · Slow | no baseline | 68.8% | 739.3 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.412s · Fast | no baseline | 53.0% | 774.3 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 2.232s · Slow | no baseline | 56.6% | 786.8 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.446s · Fast | no baseline | 32.6% | 788.5 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.700s · Ok | no baseline | 73.9% | 841.9 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.203s · Fast | no baseline | 66.3% | 807.5 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.996s · Near ok | +0.771s slower | 32.2% | 893.9 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.600s · Ok | parity | 74.3% | 817.5 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.385s · Fast | parity | 17.4% | 794.5 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.587s · Ok | -0.222s faster | 54.3% | 838.0 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.454s · Fast | parity | 67.1% | 833.4 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 1.044s · Slow | parity | 62.6% | 800.9 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.371s · Fast | parity | 67.3% | 791.1 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.705s · Slow | parity | 57.9% | 814.2 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.453s · Fast | -0.210s faster | 65.1% | 837.2 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.834s · Ok | -0.464s faster | 41.2% | 818.7 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.596s · Ok | +0.082s slower | 58.6% | 984.3 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.630s · Ok | no baseline | 55.3% | 833.9 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.721s · Ok | no baseline | 66.1% | 862.3 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.962s · Slow | no baseline | 66.3% | 817.8 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.957s · Near ok | no baseline | 67.7% | 867.0 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.697s · Ok | no baseline | 65.0% | 823.3 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.209s · Fast | no baseline | 65.2% | 832.9 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.190s · Slow | -0.585s faster | 47.4% | 804.4 MB | f2cacb3e5<br>2026-10-06 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.137s · Slow | parity | 11.6% | 859.1 MB | f2cacb3e5<br>2026-10-06 |

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
