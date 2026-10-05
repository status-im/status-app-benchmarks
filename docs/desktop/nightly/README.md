# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Oct 05, 2026 · [`4a0b283f9`](https://github.com/status-im/status-app/commit/4a0b283f908d3fef134f2b30eccbc3fd8e39dd47)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.577s | 1.020s | 2.997s | 4a0b283f9 | 2026-10-05 |
| a 5-image album in a 3-person group | 2.930s | 3.522s | 4.065s | 4a0b283f9 | 2026-10-05 |
| a GIF in a 3-person group | 0.507s | 0.929s | 1.830s | 4a0b283f9 | 2026-10-05 |
| 10 texts with 0.5s delay in a 3-person group | 0.609s | 1.082s | 3.202s | 4a0b283f9 | 2026-10-05 |
| 1000-character text in a 1-on-1 chat | 0.503s | 0.934s | 1.779s | 4a0b283f9 | 2026-10-05 |
| a 5-image album in a 1-on-1 chat | 3.038s | 3.526s | 4.018s | 4a0b283f9 | 2026-10-05 |
| a GIF in a 1-on-1 chat | 0.468s | 1.008s | 1.405s | 4a0b283f9 | 2026-10-05 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.666s | 1.204s | 2.861s | 4a0b283f9 | 2026-10-05 |
| 1000-character text in a community #general channel | 0.424s | 0.742s | 2.654s | 4a0b283f9 | 2026-10-05 |
| a 5-image album in a community #general channel | 6.299s | 6.931s | 8.595s | 4a0b283f9 | 2026-10-05 |
| a GIF in a community #general channel | 0.539s | 1.112s | 2.958s | 4a0b283f9 | 2026-10-05 |
| 10 texts with 0.5s delay in a community #general channel | 1.082s | 2.071s | 5.280s | 4a0b283f9 | 2026-10-05 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.483s · Fast | +0.111s slower | 72.3% | 729.3 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.418s · Fast | parity | 63.6% | 796.7 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.146s · Fast | parity | 50.6% | 720.0 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.580s · Ok | parity | 69.1% | 846.2 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.386s · Fast | parity | 32.3% | 772.3 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.358s · Fast | -0.113s faster | 31.6% | 763.2 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.309s · Fast | parity | 37.7% | 782.2 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.113s · Slow | +0.225s slower | 54.9% | 806.2 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.358s · Fast | -0.140s faster | 21.4% | 836.8 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.035s · Slow | -0.524s faster | 56.5% | 768.7 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.400s · Fast | -0.168s faster | 29.3% | 914.0 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 1.831s · Slow | no baseline | 54.8% | 697.3 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.239s · Fast | no baseline | 36.2% | 788.6 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.293s · Fast | no baseline | 59.7% | 864.8 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.134s · Fast | no baseline | 61.6% | 840.1 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.147s · Fast | no baseline | 74.4% | 767.3 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.117s · Fast | no baseline | 53.0% | 750.3 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.577s · Ok | no baseline | 67.5% | 754.9 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 1.020s · Slow | no baseline | 59.5% | 755.0 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 2.997s · Slow | no baseline | 16.9% | 755.0 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 2.930s · Slow | no baseline | 8.7% | 777.9 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.522s · Slow | no baseline | 1.1% | 798.5 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 4.065s · Slow | no baseline | 2.1% | 800.0 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.507s · Ok | no baseline | 5.3% | 784.8 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.929s · Near ok | no baseline | 3.1% | 784.8 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 1.830s · Slow | no baseline | 1.7% | 784.9 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.609s · Ok | no baseline | 18.4% | 788.4 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.082s · Slow | no baseline | 5.2% | 788.4 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 3.202s · Slow | no baseline | 3.7% | 788.5 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.503s · Ok | no baseline | 5.2% | 784.8 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 0.934s · Near ok | no baseline | 4.5% | 848.5 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 1.779s · Slow | no baseline | 4.5% | 810.4 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.038s · Slow | no baseline | 20.0% | 803.1 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.526s · Slow | no baseline | 0.8% | 794.9 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.018s · Slow | no baseline | 2.1% | 795.0 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.468s · Fast | no baseline | 26.6% | 787.1 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.008s · Slow | no baseline | 4.0% | 787.1 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 1.405s · Slow | no baseline | 8.3% | 787.1 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.666s · Ok | no baseline | 17.1% | 787.6 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.204s · Slow | no baseline | 10.5% | 787.8 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 2.861s · Slow | no baseline | 4.1% | 786.8 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.424s · Fast | no baseline | 1.2% | 870.8 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.742s · Ok | no baseline | 2.5% | 872.6 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 2.654s · Slow | no baseline | 1.2% | 877.5 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 6.299s · Slow | no baseline | 10.0% | 872.5 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 6.931s · Slow | no baseline | 4.2% | 878.6 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 8.595s · Slow | no baseline | 2.2% | 878.7 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.539s · Ok | no baseline | 4.9% | 880.2 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.112s · Slow | no baseline | 4.5% | 879.1 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 2.958s · Slow | no baseline | 6.7% | 879.2 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.082s · Slow | no baseline | 7.4% | 859.1 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.071s · Slow | no baseline | 4.1% | 858.0 MB | 4a0b283f9<br>2026-10-05 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.280s · Slow | no baseline | 4.0% | 854.1 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.796s · Ok | +0.312s slower | 37.6% | 737.2 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.530s · Ok | parity | 79.9% | 807.0 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.423s · Fast | parity | 46.1% | 744.2 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.501s · Ok | -0.248s faster | 51.3% | 793.2 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.422s · Fast | parity | 33.7% | 748.2 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.536s · Ok | -0.386s faster | 43.3% | 846.6 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.320s · Fast | parity | 36.1% | 788.9 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.161s · Slow | -0.629s faster | 43.8% | 796.1 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.423s · Fast | -0.258s faster | 46.8% | 755.1 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.629s · Ok | -0.738s faster | 48.5% | 833.0 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.661s · Ok | +0.129s slower | 63.7% | 913.7 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.548s · Ok | no baseline | 65.8% | 830.6 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.511s · Ok | no baseline | 49.2% | 819.9 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 2.283s · Slow | no baseline | 58.5% | 775.0 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.447s · Fast | no baseline | 41.2% | 803.0 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.743s · Ok | no baseline | 63.9% | 810.0 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.195s · Fast | no baseline | 68.0% | 803.2 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.593s · Ok | +0.368s slower | 27.5% | 876.0 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.598s · Ok | parity | 76.0% | 846.7 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.461s · Fast | +0.114s slower | 55.4% | 772.3 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.617s · Ok | -0.192s faster | 34.5% | 863.3 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.459s · Fast | parity | 72.9% | 808.8 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.536s · Ok | -0.414s faster | 38.9% | 842.9 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.361s · Fast | parity | 60.7% | 807.8 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.166s · Slow | -0.604s faster | 49.3% | 760.5 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.428s · Fast | -0.235s faster | 48.7% | 783.1 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.674s · Ok | -0.624s faster | 35.9% | 838.1 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.396s · Fast | -0.118s faster | 50.4% | 946.0 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.480s · Fast | no baseline | 69.9% | 877.1 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.639s · Ok | no baseline | 67.6% | 855.7 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.926s · Slow | no baseline | 60.6% | 862.4 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.862s · Ok | no baseline | 61.3% | 864.2 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.633s · Ok | no baseline | 56.8% | 822.9 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.240s · Fast | no baseline | 78.4% | 856.0 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.347s · Slow | parity | 30.9% | 731.8 MB | 4a0b283f9<br>2026-10-05 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.221s · Slow | parity | 56.1% | 836.5 MB | 4a0b283f9<br>2026-10-05 |

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
