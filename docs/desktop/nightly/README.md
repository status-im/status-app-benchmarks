# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Oct 01, 2026 · [`a9bc3de2f`](https://github.com/status-im/status-app/commit/a9bc3de2fafbe5d50174f01c1a10109e44f9da30)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.450s | 0.782s | 3.365s | a9bc3de2f | 2026-10-01 |
| a 5-image album in a 3-person group | 2.947s | 3.517s | 4.909s | a9bc3de2f | 2026-10-01 |
| a GIF in a 3-person group | 0.429s | 0.839s | 2.621s | a9bc3de2f | 2026-10-01 |
| 10 texts with 0.5s delay in a 3-person group | 0.605s | 1.079s | 3.260s | a9bc3de2f | 2026-10-01 |
| 1000-character text in a 1-on-1 chat | 0.486s | 0.838s | 1.150s | a9bc3de2f | 2026-10-01 |
| a 5-image album in a 1-on-1 chat | 3.018s | 3.608s | 4.122s | a9bc3de2f | 2026-10-01 |
| a GIF in a 1-on-1 chat | 0.628s | 1.068s | 2.054s | a9bc3de2f | 2026-10-01 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.635s | 1.143s | 2.676s | a9bc3de2f | 2026-10-01 |
| 1000-character text in a community #general channel | 0.437s | 0.825s | 4.215s | a9bc3de2f | 2026-10-01 |
| a 5-image album in a community #general channel | 5.117s | 5.726s | 9.000s | a9bc3de2f | 2026-10-01 |
| a GIF in a community #general channel | 0.590s | 1.135s | 3.561s | a9bc3de2f | 2026-10-01 |
| 10 texts with 0.5s delay in a community #general channel | 1.214s | 2.258s | 5.536s | a9bc3de2f | 2026-10-01 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.479s · Fast | +0.107s slower | 71.3% | 746.3 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.459s · Fast | +0.080s slower | 47.7% | 790.7 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.158s · Fast | parity | 66.3% | 755.0 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.367s · Fast | -0.244s faster | 18.2% | 698.0 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.375s · Fast | parity | 12.1% | 780.7 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.303s · Fast | -0.168s faster | 27.3% | 717.0 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.285s · Fast | parity | 25.2% | 760.0 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.006s · Slow | parity | 38.5% | 803.5 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.494s · Fast | parity | 17.1% | 902.2 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.251s · Slow | -0.308s faster | 51.8% | 807.2 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.644s · Ok | parity | 23.8% | 939.7 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.144s · Fast | no baseline | 5.4% | 737.7 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.173s · Fast | no baseline | 45.0% | 784.1 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.251s · Fast | no baseline | 31.4% | 793.2 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.113s · Fast | no baseline | 58.6% | 807.8 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.150s · Fast | no baseline | 89.1% | 761.0 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.100s · Fast | no baseline | 45.2% | 738.4 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.450s · Fast | no baseline | 7.5% | 790.2 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.782s · Ok | no baseline | 3.1% | 790.3 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 3.365s · Slow | no baseline | 4.1% | 790.5 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 2.947s · Slow | no baseline | 7.1% | 803.6 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.517s · Slow | no baseline | 1.1% | 814.8 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 4.909s · Slow | no baseline | 7.2% | 854.5 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.429s · Fast | no baseline | 2.7% | 895.7 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.839s · Ok | no baseline | 5.3% | 895.7 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 2.621s · Slow | no baseline | 3.7% | 895.7 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.605s · Ok | no baseline | 17.5% | 884.9 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.079s · Slow | no baseline | 3.8% | 884.5 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 3.260s · Slow | no baseline | 3.9% | 884.5 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.486s · Fast | no baseline | 16.0% | 762.5 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 0.838s · Ok | no baseline | 3.6% | 762.5 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 1.150s · Slow | no baseline | 6.3% | 762.6 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.018s · Slow | no baseline | 11.1% | 775.1 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.608s · Slow | no baseline | 2.8% | 783.4 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.122s · Slow | no baseline | 3.3% | 786.2 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.628s · Ok | no baseline | 20.9% | 869.3 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.068s · Slow | no baseline | 2.7% | 869.4 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 2.054s · Slow | no baseline | 2.3% | 856.2 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.635s · Ok | no baseline | 22.5% | 855.9 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.143s · Slow | no baseline | 3.9% | 856.0 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 2.676s · Slow | no baseline | 3.8% | 856.0 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.437s · Fast | no baseline | 21.8% | 833.3 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.825s · Ok | no baseline | 15.1% | 838.1 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 4.215s · Slow | no baseline | 3.1% | 838.2 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 5.117s · Slow | no baseline | 8.7% | 852.5 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 5.726s · Slow | no baseline | 0.7% | 869.1 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 9.000s · Slow | no baseline | 3.4% | 956.9 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.590s · Ok | no baseline | 3.5% | 957.2 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.135s · Slow | no baseline | 2.7% | 957.1 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.561s · Slow | no baseline | 6.7% | 957.1 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.214s · Slow | no baseline | 6.9% | 946.9 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.258s · Slow | no baseline | 3.7% | 945.9 MB | a9bc3de2f<br>2026-10-01 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.536s · Slow | no baseline | 5.1% | 942.3 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.293s · Fast | -0.191s faster | 51.6% | 799.3 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.554s · Ok | parity | 69.2% | 784.0 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.531s · Ok | +0.129s slower | 29.7% | 829.6 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.635s · Ok | -0.114s faster | 47.4% | 845.7 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.411s · Fast | parity | 34.7% | 782.7 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.512s · Ok | -0.410s faster | 31.9% | 818.8 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.334s · Fast | parity | 37.8% | 780.6 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.941s · Slow | parity | 44.9% | 870.4 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.623s · Ok | parity | 30.2% | 880.6 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.716s · Ok | -0.651s faster | 30.7% | 839.5 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.544s · Ok | parity | 36.1% | 952.5 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 2.251s · Slow | no baseline | 69.2% | 758.8 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.466s · Fast | no baseline | 54.0% | 802.8 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.900s · Slow | no baseline | 48.2% | 779.9 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.520s · Ok | no baseline | 52.3% | 822.7 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.599s · Ok | no baseline | 67.3% | 795.1 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.232s · Fast | no baseline | 77.6% | 791.4 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 1.218s · Slow | +0.993s slower | 33.4% | 873.5 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.542s · Ok | parity | 66.0% | 864.6 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.528s · Ok | +0.181s slower | 48.9% | 899.5 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.455s · Fast | -0.354s faster | 51.5% | 890.2 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.463s · Fast | parity | 66.7% | 847.6 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.551s · Ok | -0.399s faster | 34.6% | 812.5 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.393s · Fast | +0.065s slower | 59.2% | 841.5 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.255s · Slow | -0.515s faster | 59.2% | 865.3 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.775s · Ok | +0.112s slower | 61.0% | 895.0 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.629s · Ok | -0.669s faster | 50.6% | 832.7 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.656s · Ok | +0.142s slower | 64.4% | 995.0 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 1.313s · Slow | no baseline | 61.5% | 846.6 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.450s · Fast | no baseline | 65.7% | 819.6 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.626s · Ok | no baseline | 29.1% | 914.1 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.233s · Fast | no baseline | 55.6% | 841.2 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.615s · Ok | no baseline | 70.4% | 863.4 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.240s · Fast | no baseline | 70.1% | 804.6 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.385s · Slow | parity | 45.8% | 816.4 MB | a9bc3de2f<br>2026-10-01 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.169s · Slow | parity | 15.5% | 892.5 MB | a9bc3de2f<br>2026-10-01 |

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
