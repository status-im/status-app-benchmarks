# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Oct 24, 2026 · [`e2ed06397`](https://github.com/status-im/status-app/commit/e2ed063972792de05d07cc528c6e11c0d40990fc)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.743s | 1.287s | 4.347s | e2ed06397 | 2026-10-24 |
| a 5-image album in a 3-person group | 2.914s | 3.418s | 3.917s | e2ed06397 | 2026-10-24 |
| a GIF in a 3-person group | 0.489s | 0.909s | 1.297s | e2ed06397 | 2026-10-24 |
| 10 texts with 0.5s delay in a 3-person group | 0.694s | 1.233s | 3.264s | e2ed06397 | 2026-10-24 |
| 1000-character text in a 1-on-1 chat | 0.629s | 1.006s | 1.326s | e2ed06397 | 2026-10-24 |
| a 5-image album in a 1-on-1 chat | 3.005s | 3.513s | 4.030s | e2ed06397 | 2026-10-24 |
| a GIF in a 1-on-1 chat | 0.504s | 1.024s | 4.212s | e2ed06397 | 2026-10-24 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.689s | 1.244s | 2.900s | e2ed06397 | 2026-10-24 |
| 1000-character text in a community #general channel | 0.585s | 0.925s | 2.869s | e2ed06397 | 2026-10-24 |
| a 5-image album in a community #general channel | 5.200s | 5.899s | 9.043s | e2ed06397 | 2026-10-24 |
| a GIF in a community #general channel | 0.636s | 1.298s | 3.257s | e2ed06397 | 2026-10-24 |
| 10 texts with 0.5s delay in a community #general channel | 1.154s | 2.277s | 5.962s | e2ed06397 | 2026-10-24 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.482s · Fast | +0.110s slower | 56.0% | 700.1 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.351s · Fast | parity | 52.6% | 693.0 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.146s · Fast | parity | 86.1% | 665.1 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.431s · Fast | -0.180s faster | 33.4% | 644.3 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.380s · Fast | parity | 33.0% | 670.2 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.442s · Fast | parity | 42.4% | 709.7 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.301s · Fast | parity | 24.4% | 683.4 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.147s · Slow | +0.259s slower | 48.8% | 708.7 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.337s · Fast | -0.161s faster | 19.8% | 663.8 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.995s · Near ok | -0.564s faster | 51.6% | 688.6 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.598s · Ok | parity | 25.5% | 813.2 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.366s · Fast | no baseline | 67.3% | 719.6 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.164s · Fast | no baseline | 38.1% | 670.1 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.296s · Fast | no baseline | 54.2% | 676.4 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.121s · Fast | no baseline | 50.3% | 657.9 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.154s · Fast | no baseline | 53.1% | 729.2 MB | e2ed06397<br>2026-10-24 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.106s · Fast | no baseline | 46.5% | 685.6 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.743s · Ok | no baseline | 62.7% | 736.5 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 1.287s · Slow | no baseline | 56.9% | 742.5 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 4.347s · Slow | no baseline | 7.6% | 747.8 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 2.914s · Slow | no baseline | 13.7% | 763.2 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.418s · Slow | no baseline | 4.2% | 755.5 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 3.917s · Slow | no baseline | 4.2% | 755.5 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.489s · Fast | no baseline | 6.3% | 755.6 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.909s · Near ok | no baseline | 4.5% | 755.6 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 1.297s · Slow | no baseline | 7.3% | 755.6 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.694s · Ok | no baseline | 21.5% | 764.0 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.233s · Slow | no baseline | 5.0% | 763.6 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 3.264s · Slow | no baseline | 7.4% | 763.7 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.629s · Ok | no baseline | 17.8% | 665.1 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 1.006s · Slow | no baseline | 4.2% | 665.1 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 1.326s · Slow | no baseline | 5.0% | 665.2 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.005s · Slow | no baseline | 17.2% | 665.0 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.513s · Slow | no baseline | 1.2% | 665.3 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.030s · Slow | no baseline | 1.7% | 669.9 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.504s · Ok | no baseline | 4.5% | 668.3 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.024s · Slow | no baseline | 5.3% | 668.3 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 4.212s · Slow | no baseline | 6.4% | 684.3 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.689s · Ok | no baseline | 12.1% | 733.9 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.244s · Slow | no baseline | 5.4% | 733.5 MB | e2ed06397<br>2026-10-24 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 2.900s · Slow | no baseline | 5.0% | 739.5 MB | e2ed06397<br>2026-10-24 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.585s · Ok | no baseline | 33.1% | 789.0 MB | e2ed06397<br>2026-10-24 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.925s · Near ok | no baseline | 2.4% | 789.0 MB | e2ed06397<br>2026-10-24 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 2.869s · Slow | no baseline | 11.9% | 791.5 MB | e2ed06397<br>2026-10-24 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 5.200s · Slow | no baseline | 12.7% | 784.2 MB | e2ed06397<br>2026-10-24 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 5.899s · Slow | no baseline | 3.9% | 774.9 MB | e2ed06397<br>2026-10-24 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 9.043s · Slow | no baseline | 1.7% | 777.1 MB | e2ed06397<br>2026-10-24 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.636s · Ok | no baseline | 4.9% | 766.6 MB | e2ed06397<br>2026-10-24 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.298s · Slow | no baseline | 4.1% | 766.6 MB | e2ed06397<br>2026-10-24 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.257s · Slow | no baseline | 3.6% | 770.0 MB | e2ed06397<br>2026-10-24 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.154s · Slow | no baseline | 5.7% | 747.6 MB | e2ed06397<br>2026-10-24 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.277s · Slow | no baseline | 6.4% | 745.8 MB | e2ed06397<br>2026-10-24 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.962s · Slow | no baseline | 4.5% | 743.8 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.463s · Fast | parity | 43.6% | 760.1 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.482s · Fast | -0.098s faster | 59.9% | 655.6 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.400s · Fast | parity | 37.6% | 683.5 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.526s · Ok | -0.223s faster | 61.0% | 648.5 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.439s · Fast | parity | 63.6% | 640.9 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.405s · Fast | -0.517s faster | 48.5% | 717.3 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.369s · Fast | parity | 62.1% | 654.2 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 0.804s · Ok | -0.986s faster | 40.1% | 689.9 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.451s · Fast | -0.230s faster | 62.3% | 643.9 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.619s · Ok | -0.748s faster | 41.2% | 690.6 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 1.010s · Slow | +0.478s slower | 63.1% | 763.4 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 2.750s · Slow | no baseline | 62.5% | 659.8 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.606s · Ok | no baseline | 57.5% | 699.5 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.820s · Slow | no baseline | 70.3% | 742.4 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.914s · Near ok | no baseline | 58.6% | 688.7 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.643s · Ok | no baseline | 62.5% | 704.4 MB | e2ed06397<br>2026-10-24 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.244s · Fast | no baseline | 54.1% | 659.2 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.359s · Fast | +0.134s slower | 40.0% | 650.5 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.499s · Fast | parity | 52.1% | 675.9 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.419s · Fast | +0.072s slower | 60.1% | 672.7 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.561s · Ok | -0.248s faster | 64.1% | 713.1 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.444s · Fast | parity | 59.0% | 670.9 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.587s · Ok | -0.363s faster | 44.7% | 661.1 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.394s · Fast | +0.066s slower | 63.9% | 652.0 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 0.752s · Ok | -1.018s faster | 46.8% | 689.2 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.455s · Fast | -0.208s faster | 64.4% | 661.7 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.661s · Ok | -0.637s faster | 34.1% | 719.6 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.887s · Ok | +0.373s slower | 65.5% | 812.7 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.518s · Ok | no baseline | 60.9% | 667.4 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.606s · Ok | no baseline | 50.2% | 712.6 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.913s · Slow | no baseline | 67.2% | 756.8 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 1.161s · Slow | no baseline | 62.5% | 712.1 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.678s · Ok | no baseline | 64.1% | 719.2 MB | e2ed06397<br>2026-10-24 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.229s · Fast | no baseline | 60.9% | 667.8 MB | e2ed06397<br>2026-10-24 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 5.019s · Slow | +1.244s slower | 63.8% | 707.1 MB | e2ed06397<br>2026-10-24 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 3.571s · Slow | +1.469s slower | 32.3% | 771.8 MB | e2ed06397<br>2026-10-24 |

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
