# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Oct 02, 2026 · [`085253967`](https://github.com/status-im/status-app/commit/08525396772696fbae59eb89f1b9ee9aa7bfc449)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.476s | 0.830s | 1.559s | 085253967 | 2026-10-02 |
| a 5-image album in a 3-person group | 3.518s | 4.018s | 4.596s | 085253967 | 2026-10-02 |
| a GIF in a 3-person group | 0.479s | 0.888s | 1.258s | 085253967 | 2026-10-02 |
| 10 texts with 0.5s delay in a 3-person group | 0.598s | 1.075s | 2.744s | 085253967 | 2026-10-02 |
| 1000-character text in a 1-on-1 chat | 0.504s | 0.850s | 2.267s | 085253967 | 2026-10-02 |
| a 5-image album in a 1-on-1 chat | 3.330s | 3.820s | 4.306s | 085253967 | 2026-10-02 |
| a GIF in a 1-on-1 chat | 0.623s | 1.074s | 2.028s | 085253967 | 2026-10-02 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.627s | 1.121s | 2.352s | 085253967 | 2026-10-02 |
| 1000-character text in a community #general channel | 0.434s | 0.778s | 2.362s | 085253967 | 2026-10-02 |
| a 5-image album in a community #general channel | 6.385s | 7.044s | 9.115s | 085253967 | 2026-10-02 |
| a GIF in a community #general channel | 0.545s | 1.263s | 3.197s | 085253967 | 2026-10-02 |
| 10 texts with 0.5s delay in a community #general channel | 1.092s | 2.066s | 5.306s | 085253967 | 2026-10-02 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.741s · Ok | +0.369s slower | 66.6% | 768.0 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.372s · Fast | parity | 72.3% | 804.8 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.175s · Fast | parity | 8.3% | 683.5 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.454s · Fast | -0.157s faster | 32.9% | 764.3 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.424s · Fast | parity | 20.0% | 801.5 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.400s · Fast | -0.071s faster | 27.2% | 781.5 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.283s · Fast | parity | 20.7% | 828.6 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.146s · Slow | +0.258s slower | 40.7% | 835.6 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.607s · Ok | +0.109s slower | 25.7% | 848.2 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.218s · Slow | -0.341s faster | 39.9% | 811.9 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.523s · Ok | parity | 21.7% | 917.4 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.134s · Fast | no baseline | 4.7% | 725.3 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.200s · Fast | no baseline | 41.5% | 741.3 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.278s · Fast | no baseline | 36.3% | 691.3 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.115s · Fast | no baseline | 22.9% | 681.3 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.137s · Fast | no baseline | 7.2% | 699.6 MB | 085253967<br>2026-10-02 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.113s · Fast | no baseline | 62.8% | 685.3 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.476s · Fast | no baseline | 97.7% | 778.2 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.830s · Ok | no baseline | 4.5% | 768.0 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 1.559s · Slow | no baseline | 5.3% | 768.3 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 3.518s · Slow | no baseline | 12.8% | 823.6 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 4.018s · Slow | no baseline | 0.4% | 803.8 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 4.596s · Slow | no baseline | 2.3% | 870.3 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.479s · Fast | no baseline | 6.2% | 885.8 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.888s · Ok | no baseline | 4.4% | 886.0 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 1.258s · Slow | no baseline | 7.3% | 886.4 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.598s · Ok | no baseline | 22.0% | 869.1 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.075s · Slow | no baseline | 5.1% | 869.2 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 2.744s · Slow | no baseline | 13.3% | 868.6 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.504s · Ok | no baseline | 2.1% | 790.8 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 0.850s · Ok | no baseline | 3.6% | 792.6 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 2.267s · Slow | no baseline | 9.6% | 798.8 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.330s · Slow | no baseline | 20.5% | 804.9 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.820s · Slow | no baseline | 1.2% | 790.8 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.306s · Slow | no baseline | 2.5% | 790.8 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.623s · Ok | no baseline | 16.9% | 870.7 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.074s · Slow | no baseline | 1.8% | 870.7 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 2.028s · Slow | no baseline | 3.3% | 870.7 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.627s · Ok | no baseline | 15.4% | 868.8 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.121s · Slow | no baseline | 3.3% | 868.8 MB | 085253967<br>2026-10-02 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 2.352s · Slow | no baseline | 3.6% | 868.7 MB | 085253967<br>2026-10-02 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.434s · Fast | no baseline | 41.6% | 803.1 MB | 085253967<br>2026-10-02 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.778s · Ok | no baseline | 8.1% | 803.1 MB | 085253967<br>2026-10-02 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 2.362s · Slow | no baseline | 6.3% | 803.2 MB | 085253967<br>2026-10-02 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 6.385s · Slow | no baseline | 18.5% | 820.2 MB | 085253967<br>2026-10-02 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 7.044s · Slow | no baseline | 4.2% | 849.2 MB | 085253967<br>2026-10-02 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 9.115s · Slow | no baseline | 7.6% | 917.3 MB | 085253967<br>2026-10-02 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.545s · Ok | no baseline | 6.3% | 915.3 MB | 085253967<br>2026-10-02 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.263s · Slow | no baseline | 2.2% | 915.4 MB | 085253967<br>2026-10-02 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.197s · Slow | no baseline | 2.7% | 915.6 MB | 085253967<br>2026-10-02 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.092s · Slow | no baseline | 5.5% | 895.8 MB | 085253967<br>2026-10-02 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.066s · Slow | no baseline | 4.3% | 894.3 MB | 085253967<br>2026-10-02 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.306s · Slow | no baseline | 4.8% | 884.7 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.398s · Fast | -0.086s faster | 29.1% | 826.3 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.561s · Ok | parity | 63.5% | 809.2 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.487s · Fast | +0.085s slower | 46.1% | 766.4 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.509s · Ok | -0.240s faster | 62.9% | 745.6 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.420s · Fast | parity | 52.8% | 751.6 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.974s · Near ok | parity | 43.9% | 769.8 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.326s · Fast | parity | 43.1% | 754.0 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.716s · Slow | parity | 34.3% | 872.0 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.677s · Ok | parity | 47.1% | 866.2 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 1.203s · Slow | parity | 55.1% | 805.0 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.600s · Ok | parity | 50.3% | 899.1 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 2.187s · Slow | no baseline | 65.1% | 753.0 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.439s · Fast | no baseline | 47.5% | 817.5 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.398s · Slow | no baseline | 72.1% | 799.2 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.558s · Ok | no baseline | 51.0% | 789.6 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.732s · Ok | no baseline | 67.5% | 926.8 MB | 085253967<br>2026-10-02 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.206s · Fast | no baseline | 58.3% | 839.7 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.431s · Fast | +0.206s slower | 41.6% | 918.3 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.555s · Ok | parity | 61.9% | 856.1 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.534s · Ok | +0.187s slower | 72.7% | 866.9 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.696s · Ok | parity | 44.4% | 897.6 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.457s · Fast | parity | 70.9% | 868.7 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 1.191s · Slow | +0.241s slower | 61.8% | 832.1 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.394s · Fast | +0.066s slower | 67.5% | 860.4 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.792s · Slow | parity | 52.3% | 920.5 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.730s · Ok | parity | 51.9% | 934.9 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 1.261s · Slow | parity | 61.7% | 932.1 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.543s · Ok | parity | 55.4% | 1001.8 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 1.115s · Slow | no baseline | 57.2% | 872.6 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.452s · Fast | no baseline | 53.8% | 815.4 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.340s · Fast | no baseline | 46.4% | 879.6 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.179s · Fast | no baseline | 58.4% | 829.0 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.664s · Ok | no baseline | 53.6% | 815.3 MB | 085253967<br>2026-10-02 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.226s · Fast | no baseline | 60.6% | 808.7 MB | 085253967<br>2026-10-02 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.253s · Slow | parity | 38.2% | 736.5 MB | 085253967<br>2026-10-02 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.166s · Slow | parity | 10.2% | 867.3 MB | 085253967<br>2026-10-02 |

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
