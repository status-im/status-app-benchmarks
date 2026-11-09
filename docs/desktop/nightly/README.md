# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Nov 09, 2026 · [`518d92d76`](https://github.com/status-im/status-app/commit/518d92d76f11460bffd4d9de67c06ad8fea99b1f)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.582s | 1.014s | 2.324s | 518d92d76 | 2026-11-09 |
| a 5-image album in a 3-person group | 3.024s | 3.610s | 4.184s | 518d92d76 | 2026-11-09 |
| a GIF in a 3-person group | 0.483s | 0.859s | 1.247s | 518d92d76 | 2026-11-09 |
| 10 texts with 0.5s delay in a 3-person group | 0.667s | 1.203s | 3.916s | 518d92d76 | 2026-11-09 |
| 1000-character text in a 1-on-1 chat | 0.658s | 1.058s | 2.446s | 518d92d76 | 2026-11-09 |
| a 5-image album in a 1-on-1 chat | 3.649s | 4.232s | 4.788s | 518d92d76 | 2026-11-09 |
| a GIF in a 1-on-1 chat | 0.506s | 0.939s | 1.363s | 518d92d76 | 2026-11-09 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.705s | 1.284s | 3.882s | 518d92d76 | 2026-11-09 |
| 1000-character text in a community #general channel | 0.643s | 1.014s | 4.572s | 518d92d76 | 2026-11-09 |
| a 5-image album in a community #general channel | 3.960s | 4.660s | 7.117s | 518d92d76 | 2026-11-09 |
| a GIF in a community #general channel | 0.594s | 1.217s | 3.740s | 518d92d76 | 2026-11-09 |
| 10 texts with 0.5s delay in a community #general channel | 1.227s | 2.326s | 5.340s | 518d92d76 | 2026-11-09 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.424s · Fast | parity | 39.3% | 601.9 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.360s · Fast | parity | 50.9% | 601.8 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.143s · Fast | parity | 88.7% | 540.9 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.447s · Fast | -0.164s faster | 61.4% | 562.3 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.407s · Fast | parity | 37.7% | 618.0 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.435s · Fast | parity | 50.0% | 614.2 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.308s · Fast | parity | 39.5% | 610.3 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.541s · Slow | +0.653s slower | 42.7% | 555.6 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.380s · Fast | -0.118s faster | 43.3% | 609.3 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.576s · Ok | -0.983s faster | 33.7% | 551.8 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.403s · Fast | -0.166s faster | 33.7% | 659.8 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 1.599s · Slow | no baseline | 68.2% | 600.2 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.180s · Fast | no baseline | 26.3% | 588.1 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.284s · Fast | no baseline | 44.4% | 537.8 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.128s · Fast | no baseline | 49.1% | 542.7 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.143s · Fast | no baseline | 50.6% | 596.1 MB | 518d92d76<br>2026-11-09 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.132s · Fast | no baseline | 60.2% | 593.9 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.582s · Ok | no baseline | 28.4% | 626.7 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 1.014s · Slow | no baseline | 9.3% | 626.7 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 2.324s · Slow | no baseline | 8.3% | 638.7 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 3.024s · Slow | no baseline | 16.6% | 677.5 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.610s · Slow | no baseline | 1.8% | 656.9 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 4.184s · Slow | no baseline | 5.5% | 656.9 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.483s · Fast | no baseline | 6.2% | 657.8 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.859s · Ok | no baseline | 1.8% | 657.8 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 1.247s · Slow | no baseline | 5.3% | 657.9 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.667s · Ok | no baseline | 5.4% | 653.4 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.203s · Slow | no baseline | 5.4% | 653.2 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 3.916s · Slow | no baseline | 4.0% | 653.3 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.658s · Ok | no baseline | 3.6% | 572.7 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 1.058s · Slow | no baseline | 3.6% | 572.7 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 2.446s · Slow | no baseline | 3.5% | 572.8 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.649s · Slow | no baseline | 21.7% | 590.4 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 4.232s · Slow | no baseline | 1.6% | 600.3 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.788s · Slow | no baseline | 8.5% | 601.0 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.506s · Ok | no baseline | 9.0% | 602.9 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 0.939s · Near ok | no baseline | 8.0% | 603.0 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 1.363s · Slow | no baseline | 3.5% | 602.9 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.705s · Ok | no baseline | 7.2% | 627.3 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.284s · Slow | no baseline | 7.2% | 627.6 MB | 518d92d76<br>2026-11-09 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 3.882s · Slow | no baseline | 6.5% | 630.0 MB | 518d92d76<br>2026-11-09 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.643s · Ok | no baseline | 14.2% | 667.4 MB | 518d92d76<br>2026-11-09 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 1.014s · Slow | no baseline | 9.9% | 667.4 MB | 518d92d76<br>2026-11-09 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 4.572s · Slow | no baseline | 14.8% | 674.0 MB | 518d92d76<br>2026-11-09 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 3.960s · Slow | no baseline | 8.5% | 669.7 MB | 518d92d76<br>2026-11-09 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 4.660s · Slow | no baseline | 2.2% | 675.2 MB | 518d92d76<br>2026-11-09 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 7.117s · Slow | no baseline | 1.9% | 657.3 MB | 518d92d76<br>2026-11-09 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.594s · Ok | no baseline | 2.2% | 657.0 MB | 518d92d76<br>2026-11-09 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.217s · Slow | no baseline | 3.9% | 657.0 MB | 518d92d76<br>2026-11-09 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.740s · Slow | no baseline | 1.6% | 655.5 MB | 518d92d76<br>2026-11-09 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.227s · Slow | no baseline | 4.1% | 652.4 MB | 518d92d76<br>2026-11-09 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.326s · Slow | no baseline | 4.5% | 651.1 MB | 518d92d76<br>2026-11-09 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.340s · Slow | no baseline | 4.6% | 650.3 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 1.212s · Slow | +0.728s slower | 17.9% | 501.8 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.473s · Fast | -0.107s faster | 51.2% | 540.3 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.295s · Fast | -0.107s faster | 44.9% | 524.4 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.483s · Fast | -0.266s faster | 54.6% | 533.2 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.406s · Fast | parity | 33.7% | 541.6 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.502s · Ok | -0.420s faster | 46.7% | 525.2 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.323s · Fast | parity | 32.5% | 525.0 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.491s · Slow | -0.299s faster | 45.1% | 533.2 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.399s · Fast | -0.282s faster | 40.4% | 543.8 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.505s · Ok | -0.862s faster | 37.2% | 529.9 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.524s · Ok | parity | 27.5% | 575.6 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.541s · Ok | no baseline | 49.8% | 511.4 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.547s · Ok | no baseline | 42.9% | 568.7 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.405s · Slow | no baseline | 48.2% | 549.6 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.447s · Fast | no baseline | 31.3% | 562.9 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.483s · Fast | no baseline | 51.3% | 519.9 MB | 518d92d76<br>2026-11-09 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.148s · Fast | no baseline | 52.4% | 535.9 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 1.241s · Slow | +1.016s slower | 16.5% | 535.2 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.473s · Fast | -0.110s faster | 58.1% | 551.9 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.315s · Fast | parity | 52.9% | 540.1 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.498s · Fast | -0.311s faster | 69.3% | 535.8 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.434s · Fast | parity | 62.5% | 577.7 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.475s · Fast | -0.475s faster | 41.5% | 541.9 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.359s · Fast | parity | 56.7% | 546.6 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.153s · Slow | -0.617s faster | 34.1% | 560.4 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.437s · Fast | -0.226s faster | 53.2% | 570.9 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.557s · Ok | -0.741s faster | 43.1% | 540.8 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.502s · Ok | parity | 41.5% | 619.8 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.394s · Fast | no baseline | 58.1% | 559.1 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.648s · Ok | no baseline | 59.9% | 603.3 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.615s · Ok | no baseline | 47.5% | 549.2 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.913s · Near ok | no baseline | 56.7% | 592.0 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.445s · Fast | no baseline | 48.0% | 542.5 MB | 518d92d76<br>2026-11-09 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.170s · Fast | no baseline | 61.1% | 553.2 MB | 518d92d76<br>2026-11-09 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 5.180s · Slow | +1.405s slower | 30.3% | 568.8 MB | 518d92d76<br>2026-11-09 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 3.679s · Slow | +1.577s slower | 32.0% | 665.2 MB | 518d92d76<br>2026-11-09 |

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
