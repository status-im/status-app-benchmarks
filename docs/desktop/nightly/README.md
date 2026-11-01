# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Nov 01, 2026 · [`af9f8f927`](https://github.com/status-im/status-app/commit/af9f8f927644f80a9e2cf87096bf22e36f57df99)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.577s | 0.961s | 2.961s | af9f8f927 | 2026-11-01 |
| a 5-image album in a 3-person group | 3.719s | 4.288s | 4.855s | af9f8f927 | 2026-11-01 |
| a GIF in a 3-person group | 0.563s | 1.122s | 3.101s | af9f8f927 | 2026-11-01 |
| 10 texts with 0.5s delay in a 3-person group | 0.724s | 1.297s | 3.373s | af9f8f927 | 2026-11-01 |
| 1000-character text in a 1-on-1 chat | 0.707s | 1.076s | 1.499s | af9f8f927 | 2026-11-01 |
| a 5-image album in a 1-on-1 chat | 3.817s | 4.365s | 4.935s | af9f8f927 | 2026-11-01 |
| a GIF in a 1-on-1 chat | 0.622s | 1.136s | 1.583s | af9f8f927 | 2026-11-01 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.798s | 1.405s | 4.273s | af9f8f927 | 2026-11-01 |
| 1000-character text in a community #general channel | 0.570s | 0.945s | 8.167s | af9f8f927 | 2026-11-01 |
| a 5-image album in a community #general channel | 3.994s | 4.905s | 6.746s | af9f8f927 | 2026-11-01 |
| a GIF in a community #general channel | 1.117s | 1.956s | 4.054s | af9f8f927 | 2026-11-01 |
| 10 texts with 0.5s delay in a community #general channel | 1.368s | 2.579s | 5.951s | af9f8f927 | 2026-11-01 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.469s · Fast | +0.097s slower | 65.7% | 712.9 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.334s · Fast | parity | 49.1% | 716.1 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.138s · Fast | parity | 70.6% | 732.6 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.464s · Fast | -0.147s faster | 54.2% | 692.6 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.398s · Fast | parity | 27.0% | 711.8 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.455s · Fast | parity | 50.9% | 720.9 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.323s · Fast | parity | 34.4% | 677.0 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.151s · Slow | +0.263s slower | 45.6% | 742.4 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.357s · Fast | -0.141s faster | 31.6% | 752.2 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.055s · Slow | -0.504s faster | 49.7% | 704.1 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.340s · Fast | -0.228s faster | 29.1% | 863.1 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 2.138s · Slow | no baseline | 59.4% | 710.7 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.191s · Fast | no baseline | 40.0% | 684.7 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.284s · Fast | no baseline | 49.5% | 756.9 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.144s · Fast | no baseline | 55.4% | 774.4 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.165s · Fast | no baseline | 45.7% | 761.1 MB | af9f8f927<br>2026-11-01 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.135s · Fast | no baseline | 57.8% | 766.9 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.577s · Ok | no baseline | 40.6% | 739.4 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.961s · Near ok | no baseline | 10.7% | 739.4 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 2.961s · Slow | no baseline | 5.8% | 731.9 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 3.719s · Slow | no baseline | 10.6% | 741.7 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 4.288s · Slow | no baseline | 5.1% | 749.0 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 4.855s · Slow | no baseline | 1.8% | 749.0 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.563s · Ok | no baseline | 14.3% | 754.6 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 1.122s · Slow | no baseline | 12.1% | 742.7 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 3.101s · Slow | no baseline | 6.8% | 738.0 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.724s · Ok | no baseline | 9.0% | 770.2 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.297s · Slow | no baseline | 6.8% | 768.8 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 3.373s · Slow | no baseline | 4.8% | 770.3 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.707s · Ok | no baseline | 75.3% | 706.4 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 1.076s · Slow | no baseline | 4.5% | 706.5 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 1.499s · Slow | no baseline | 13.4% | 706.5 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.817s · Slow | no baseline | 35.0% | 715.9 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 4.365s · Slow | no baseline | 1.6% | 719.1 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.935s · Slow | no baseline | 1.8% | 719.1 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.622s · Ok | no baseline | 24.9% | 720.2 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.136s · Slow | no baseline | 4.3% | 720.2 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 1.583s · Slow | no baseline | 5.4% | 720.4 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.798s · Ok | no baseline | 19.9% | 726.6 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.405s · Slow | no baseline | 7.6% | 725.0 MB | af9f8f927<br>2026-11-01 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 4.273s · Slow | no baseline | 6.2% | 727.9 MB | af9f8f927<br>2026-11-01 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.570s · Ok | no baseline | 18.2% | 793.4 MB | af9f8f927<br>2026-11-01 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.945s · Near ok | no baseline | 3.6% | 794.8 MB | af9f8f927<br>2026-11-01 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 8.167s · Slow | no baseline | 4.7% | 756.7 MB | af9f8f927<br>2026-11-01 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 3.994s · Slow | no baseline | 7.5% | 774.6 MB | af9f8f927<br>2026-11-01 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 4.905s · Slow | no baseline | 10.5% | 785.1 MB | af9f8f927<br>2026-11-01 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 6.746s · Slow | no baseline | 2.3% | 787.7 MB | af9f8f927<br>2026-11-01 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 1.117s · Slow | no baseline | 4.3% | 772.5 MB | af9f8f927<br>2026-11-01 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.956s · Slow | no baseline | 2.7% | 772.5 MB | af9f8f927<br>2026-11-01 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 4.054s · Slow | no baseline | 3.3% | 772.5 MB | af9f8f927<br>2026-11-01 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.368s · Slow | no baseline | 5.2% | 746.1 MB | af9f8f927<br>2026-11-01 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.579s · Slow | no baseline | 4.6% | 745.0 MB | af9f8f927<br>2026-11-01 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.951s · Slow | no baseline | 4.2% | 741.4 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 1.002s · Slow | +0.518s slower | 33.8% | 714.2 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.497s · Fast | parity | 52.3% | 610.7 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.359s · Fast | parity | 55.9% | 675.4 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.480s · Fast | -0.269s faster | 50.2% | 700.0 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.447s · Fast | parity | 54.3% | 685.6 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.516s · Ok | -0.406s faster | 36.5% | 718.1 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.393s · Fast | parity | 60.0% | 635.1 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 0.896s · Ok | -0.894s faster | 36.3% | 591.7 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.468s · Fast | -0.213s faster | 59.9% | 596.1 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.741s · Ok | -0.626s faster | 41.5% | 712.7 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.885s · Ok | +0.353s slower | 59.5% | 794.7 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.919s · Near ok | no baseline | 52.8% | 683.3 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.786s · Ok | no baseline | 57.4% | 678.4 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 1.955s · Slow | no baseline | 46.7% | 637.7 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 1.340s · Slow | no baseline | 63.0% | 647.8 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.539s · Ok | no baseline | 54.5% | 691.8 MB | af9f8f927<br>2026-11-01 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.172s · Fast | no baseline | 57.9% | 644.6 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.986s · Near ok | +0.761s slower | 39.5% | 785.0 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.498s · Fast | parity | 50.3% | 660.8 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.459s · Fast | +0.112s slower | 51.4% | 726.0 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.533s · Ok | -0.276s faster | 43.7% | 682.5 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.472s · Fast | parity | 67.9% | 651.8 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.402s · Fast | -0.548s faster | 42.9% | 645.4 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.418s · Fast | +0.090s slower | 53.0% | 637.6 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.482s · Slow | -0.288s faster | 55.2% | 688.8 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.522s · Ok | -0.141s faster | 62.1% | 664.2 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.860s · Ok | -0.438s faster | 37.9% | 689.3 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.831s · Ok | +0.317s slower | 66.8% | 799.9 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.612s · Ok | no baseline | 63.5% | 694.5 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.760s · Ok | no baseline | 60.9% | 689.0 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.635s · Ok | no baseline | 56.0% | 737.7 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 1.495s · Slow | no baseline | 60.7% | 698.8 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.445s · Fast | no baseline | 53.3% | 672.1 MB | af9f8f927<br>2026-11-01 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.220s · Fast | no baseline | 62.9% | 645.3 MB | af9f8f927<br>2026-11-01 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 3.630s · Slow | parity | 43.2% | 731.5 MB | af9f8f927<br>2026-11-01 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 3.752s · Slow | +1.650s slower | 35.0% | 748.3 MB | af9f8f927<br>2026-11-01 |

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
