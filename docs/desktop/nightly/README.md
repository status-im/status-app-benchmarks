# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Nov 03, 2026 · [`9c28b9dd0`](https://github.com/status-im/status-app/commit/9c28b9dd020344baa2854985bf379e19d6f7b77a)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.691s | 1.160s | 1.537s | 9c28b9dd0 | 2026-11-03 |
| a 5-image album in a 3-person group | 3.086s | 3.959s | 5.645s | 9c28b9dd0 | 2026-11-03 |
| a GIF in a 3-person group | 0.735s | 1.431s | 2.849s | 9c28b9dd0 | 2026-11-03 |
| 10 texts with 0.5s delay in a 3-person group | 1.170s | 2.188s | 3.518s | 9c28b9dd0 | 2026-11-03 |
| 1000-character text in a 1-on-1 chat | 0.863s | 1.280s | 1.731s | 9c28b9dd0 | 2026-11-03 |
| a 5-image album in a 1-on-1 chat | 2.862s | 3.527s | 4.201s | 9c28b9dd0 | 2026-11-03 |
| a GIF in a 1-on-1 chat | 0.828s | 1.629s | 2.306s | 9c28b9dd0 | 2026-11-03 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 1.241s | 2.329s | 4.765s | 9c28b9dd0 | 2026-11-03 |
| 1000-character text in a community #general channel | 0.619s | 1.084s | 6.724s | 9c28b9dd0 | 2026-11-03 |
| a 5-image album in a community #general channel | 4.017s | 4.869s | 10.657s | 9c28b9dd0 | 2026-11-03 |
| a GIF in a community #general channel | 0.794s | 1.936s | 4.595s | 9c28b9dd0 | 2026-11-03 |
| 10 texts with 0.5s delay in a community #general channel | 1.769s | 3.512s | 7.942s | 9c28b9dd0 | 2026-11-03 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.471s · Fast | +0.099s slower | 63.9% | 672.8 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.381s · Fast | parity | 54.1% | 762.7 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.172s · Fast | parity | 18.8% | 783.9 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.619s · Ok | parity | 35.4% | 765.4 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.409s · Fast | parity | 36.0% | 746.2 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.491s · Fast | parity | 54.9% | 750.6 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.335s · Fast | parity | 29.9% | 745.2 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.234s · Slow | +0.346s slower | 48.6% | 773.8 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.388s · Fast | -0.110s faster | 27.9% | 731.9 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.058s · Slow | -0.501s faster | 50.1% | 707.5 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.466s · Fast | -0.103s faster | 20.9% | 860.7 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 1.567s · Slow | no baseline | 64.4% | 729.7 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.231s · Fast | no baseline | 35.6% | 694.8 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.289s · Fast | no baseline | 38.0% | 724.2 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.162s · Fast | no baseline | 48.2% | 731.9 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.160s · Fast | no baseline | 38.3% | 713.6 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.153s · Fast | no baseline | 64.5% | 713.0 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.691s · Ok | no baseline | 36.4% | 779.3 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 1.160s · Slow | no baseline | 6.3% | 779.4 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 1.537s · Slow | no baseline | 4.5% | 779.7 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 3.086s · Slow | no baseline | 12.7% | 795.6 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.959s · Slow | no baseline | 4.5% | 803.1 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 5.645s · Slow | no baseline | 3.9% | 802.6 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.735s · Ok | no baseline | 4.8% | 802.7 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 1.431s · Slow | no baseline | 3.0% | 802.7 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 2.849s · Slow | no baseline | 3.7% | 802.7 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 1.170s · Slow | no baseline | 6.2% | 788.9 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 2.188s · Slow | no baseline | 4.6% | 789.0 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 3.518s · Slow | no baseline | 4.4% | 789.0 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.863s · Ok | no baseline | 15.7% | 716.0 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 1.280s · Slow | no baseline | 4.5% | 716.1 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 1.731s · Slow | no baseline | 10.8% | 716.3 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 2.862s · Slow | no baseline | 21.2% | 730.9 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.527s · Slow | no baseline | 4.4% | 740.8 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.201s · Slow | no baseline | 5.7% | 746.1 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.828s · Ok | no baseline | 13.9% | 747.1 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.629s · Slow | no baseline | 11.0% | 747.6 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 2.306s · Slow | no baseline | 10.6% | 752.6 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.241s · Slow | no baseline | 9.0% | 765.0 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 2.329s · Slow | no baseline | 6.5% | 765.9 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 4.765s · Slow | no baseline | 5.5% | 768.0 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.619s · Ok | no baseline | 10.8% | 778.2 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 1.084s · Slow | no baseline | 13.4% | 779.8 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 6.724s · Slow | no baseline | 10.1% | 785.0 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 4.017s · Slow | no baseline | 8.7% | 807.0 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 4.869s · Slow | no baseline | 10.1% | 809.7 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 10.657s · Slow | no baseline | 8.1% | 817.0 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.794s · Ok | no baseline | 6.3% | 816.7 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.936s · Slow | no baseline | 4.9% | 817.3 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 4.595s · Slow | no baseline | 4.4% | 818.7 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.769s · Slow | no baseline | 5.1% | 751.1 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 3.512s · Slow | no baseline | 4.1% | 745.0 MB | 9c28b9dd0<br>2026-11-03 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 7.942s · Slow | no baseline | 4.2% | 737.7 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 1.105s · Slow | +0.621s slower | 32.5% | 742.2 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.516s · Ok | parity | 59.4% | 660.1 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.488s · Fast | +0.086s slower | 45.8% | 662.1 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.597s · Ok | -0.152s faster | 42.2% | 707.9 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.494s · Fast | parity | 58.1% | 674.5 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.412s · Fast | -0.510s faster | 46.4% | 685.9 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.420s · Fast | +0.057s slower | 60.5% | 650.9 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.389s · Slow | -0.401s faster | 57.7% | 692.7 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.512s · Ok | -0.169s faster | 62.7% | 644.9 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.650s · Ok | -0.717s faster | 33.0% | 663.0 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.999s · Near ok | +0.467s slower | 68.6% | 792.4 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.609s · Ok | no baseline | 59.1% | 678.5 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.806s · Ok | no baseline | 59.3% | 675.7 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.793s · Slow | no baseline | 58.2% | 751.9 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 1.468s · Slow | no baseline | 60.1% | 678.9 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.530s · Ok | no baseline | 47.1% | 681.7 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.211s · Fast | no baseline | 53.7% | 641.5 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 1.107s · Slow | +0.882s slower | 57.5% | 788.0 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.529s · Ok | parity | 51.6% | 693.5 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.408s · Fast | +0.061s slower | 63.0% | 694.2 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.622s · Ok | -0.187s faster | 33.9% | 707.1 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.515s · Ok | +0.080s slower | 67.8% | 682.7 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.476s · Fast | -0.474s faster | 39.9% | 685.5 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.458s · Fast | +0.130s slower | 66.2% | 660.9 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.400s · Slow | -0.370s faster | 46.4% | 751.3 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.525s · Ok | -0.138s faster | 60.3% | 704.2 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 1.150s · Slow | parity | 55.4% | 693.7 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.863s · Ok | +0.349s slower | 64.3% | 803.2 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.615s · Ok | no baseline | 65.6% | 691.6 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.830s · Ok | no baseline | 52.3% | 709.0 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 2.027s · Slow | no baseline | 52.1% | 784.3 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 1.284s · Slow | no baseline | 64.5% | 734.8 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.439s · Fast | no baseline | 64.0% | 733.2 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.228s · Fast | no baseline | 56.8% | 676.8 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.761s · Slow | parity | 37.9% | 701.4 MB | 9c28b9dd0<br>2026-11-03 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 3.852s · Slow | +1.750s slower | 18.8% | 831.6 MB | 9c28b9dd0<br>2026-11-03 |

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
