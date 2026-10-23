# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Oct 23, 2026 · [`3c8217ee0`](https://github.com/status-im/status-app/commit/3c8217ee050dca77ce29b16613e236d18aca79c7)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.544s | 0.960s | 1.272s | 3c8217ee0 | 2026-10-23 |
| a 5-image album in a 3-person group | 2.860s | 3.372s | 3.875s | 3c8217ee0 | 2026-10-23 |
| a GIF in a 3-person group | 0.466s | 0.953s | 1.962s | 3c8217ee0 | 2026-10-23 |
| 10 texts with 0.5s delay in a 3-person group | 0.686s | 1.249s | 3.375s | 3c8217ee0 | 2026-10-23 |
| 1000-character text in a 1-on-1 chat | 0.665s | 1.066s | 1.401s | 3c8217ee0 | 2026-10-23 |
| a 5-image album in a 1-on-1 chat | 3.007s | 3.533s | 4.093s | 3c8217ee0 | 2026-10-23 |
| a GIF in a 1-on-1 chat | 0.648s | 1.171s | 2.243s | 3c8217ee0 | 2026-10-23 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 0.700s | 1.274s | 3.857s | 3c8217ee0 | 2026-10-23 |
| 1000-character text in a community #general channel | 0.611s | 0.973s | 3.299s | 3c8217ee0 | 2026-10-23 |
| a 5-image album in a community #general channel | 5.169s | 6.171s | 7.921s | 3c8217ee0 | 2026-10-23 |
| a GIF in a community #general channel | 0.582s | 1.228s | 3.328s | 3c8217ee0 | 2026-10-23 |
| 10 texts with 0.5s delay in a community #general channel | 1.162s | 2.274s | 5.914s | 3c8217ee0 | 2026-10-23 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.464s · Fast | +0.092s slower | 62.8% | 752.9 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.349s · Fast | parity | 51.6% | 693.9 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.145s · Fast | parity | 63.9% | 683.4 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.439s · Fast | -0.172s faster | 42.1% | 692.2 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.371s · Fast | parity | 26.2% | 669.7 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.347s · Fast | -0.124s faster | 29.8% | 666.5 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.291s · Fast | parity | 35.7% | 656.6 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.109s · Slow | +0.221s slower | 54.9% | 656.7 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.353s · Fast | -0.145s faster | 29.8% | 680.5 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 1.007s · Slow | -0.552s faster | 51.8% | 757.0 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.542s · Ok | parity | 41.6% | 835.5 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 2.238s · Slow | no baseline | 51.4% | 695.6 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.183s · Fast | no baseline | 30.6% | 670.3 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.271s · Fast | no baseline | 42.5% | 742.5 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.127s · Fast | no baseline | 51.9% | 696.6 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.307s · Fast | no baseline | 75.0% | 840.7 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.111s · Fast | no baseline | 57.9% | 703.0 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.544s · Ok | no baseline | 41.7% | 717.5 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.960s · Near ok | no baseline | 7.3% | 719.4 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 1.272s · Slow | no baseline | 2.0% | 726.9 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 2.860s · Slow | no baseline | 9.5% | 730.6 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.372s · Slow | no baseline | 3.8% | 713.8 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 3.875s · Slow | no baseline | 2.7% | 713.8 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.466s · Fast | no baseline | 3.6% | 713.9 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.953s · Near ok | no baseline | 5.8% | 713.9 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 1.962s · Slow | no baseline | 4.9% | 714.3 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 0.686s · Ok | no baseline | 19.0% | 709.0 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 1.249s · Slow | no baseline | 10.3% | 709.1 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 3.375s · Slow | no baseline | 9.9% | 709.1 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 0.665s · Ok | no baseline | 42.6% | 691.3 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 1.066s · Slow | no baseline | 2.1% | 691.3 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 1.401s · Slow | no baseline | 5.0% | 674.3 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.007s · Slow | no baseline | 19.7% | 699.5 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 3.533s · Slow | no baseline | 2.7% | 700.4 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 4.093s · Slow | no baseline | 7.4% | 703.4 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 0.648s · Ok | no baseline | 13.1% | 693.2 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 1.171s · Slow | no baseline | 10.3% | 697.7 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 2.243s · Slow | no baseline | 5.8% | 701.5 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.700s · Ok | no baseline | 12.8% | 722.9 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 1.274s · Slow | no baseline | 5.2% | 723.6 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 3.857s · Slow | no baseline | 5.0% | 727.4 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.611s · Ok | no baseline | 8.9% | 777.5 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.973s · Near ok | no baseline | 3.6% | 778.2 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 3.299s · Slow | no baseline | 2.6% | 750.8 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 5.169s · Slow | no baseline | 9.7% | 773.2 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 6.171s · Slow | no baseline | 4.8% | 791.4 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 7.921s · Slow | no baseline | 0.8% | 776.0 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 0.582s · Ok | no baseline | 3.4% | 776.6 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 1.228s · Slow | no baseline | 4.8% | 776.1 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.328s · Slow | no baseline | 4.6% | 775.5 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 1.162s · Slow | no baseline | 6.5% | 758.2 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 2.274s · Slow | no baseline | 4.5% | 759.1 MB | 3c8217ee0<br>2026-10-23 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 5.914s · Slow | no baseline | 4.0% | 755.9 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.600s · Ok | +0.116s slower | 32.8% | 839.3 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.478s · Fast | -0.102s faster | 53.8% | 645.9 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.398s · Fast | parity | 45.8% | 602.4 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.530s · Ok | -0.219s faster | 48.3% | 717.3 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.448s · Fast | parity | 58.2% | 639.9 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.466s · Fast | -0.456s faster | 48.0% | 759.9 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.364s · Fast | parity | 62.3% | 642.0 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 0.900s · Ok | -0.890s faster | 34.1% | 719.0 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.457s · Fast | -0.224s faster | 64.5% | 639.6 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.707s · Ok | -0.660s faster | 42.4% | 710.5 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.943s · Near ok | +0.411s slower | 62.0% | 774.9 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 4.416s · Slow | no baseline | 61.4% | 655.2 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.636s · Ok | no baseline | 61.3% | 660.6 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 2.062s · Slow | no baseline | 55.8% | 692.2 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 1.110s · Slow | no baseline | 61.1% | 689.6 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.726s · Ok | no baseline | 66.0% | 687.8 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.205s · Fast | no baseline | 53.4% | 660.1 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.697s · Ok | +0.472s slower | 45.7% | 733.6 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.483s · Fast | -0.100s faster | 63.9% | 664.8 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.378s · Fast | parity | 60.3% | 700.3 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.508s · Ok | -0.301s faster | 60.5% | 671.9 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.448s · Fast | parity | 63.6% | 664.8 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.446s · Fast | -0.504s faster | 44.5% | 695.3 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.371s · Fast | parity | 65.6% | 664.2 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 0.894s · Ok | -0.876s faster | 41.5% | 821.0 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.468s · Fast | -0.195s faster | 64.5% | 681.4 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.636s · Ok | -0.662s faster | 45.7% | 793.2 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.846s · Ok | +0.332s slower | 63.5% | 845.2 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.528s · Ok | no baseline | 67.4% | 671.7 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.659s · Ok | no baseline | 57.4% | 708.1 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.333s · Fast | no baseline | 73.3% | 785.7 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.639s · Ok | no baseline | 58.5% | 743.9 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.651s · Ok | no baseline | 60.5% | 716.2 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.246s · Fast | no baseline | 59.2% | 670.5 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 4.053s · Slow | parity | 41.9% | 703.2 MB | 3c8217ee0<br>2026-10-23 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 3.626s · Slow | +1.524s slower | 21.0% | 770.0 MB | 3c8217ee0<br>2026-10-23 |

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
