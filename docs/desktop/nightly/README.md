# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Nov 06, 2026 · [`8249a48a4`](https://github.com/status-im/status-app/commit/8249a48a40313103655bfd0913e07fa216a300d1)

## Send timing

Latest time until the message is **Visible** in the chat, **Sent** (one tick), and **Delivered** (two ticks). Interactive table: [send-timing.html](send-timing.html).

| Scenario | Visible | Sent | Delivered | Commit | Date |
|----------|---------|------|-----------|--------|------|
| 1000-character text in a 3-person group | 0.723s | 1.109s | 1.462s | 8249a48a4 | 2026-11-06 |
| a 5-image album in a 3-person group | 3.031s | 3.679s | 4.354s | 8249a48a4 | 2026-11-06 |
| a GIF in a 3-person group | 0.699s | 1.391s | 1.989s | 8249a48a4 | 2026-11-06 |
| 10 texts with 0.5s delay in a 3-person group | 1.122s | 2.126s | 3.717s | 8249a48a4 | 2026-11-06 |
| 1000-character text in a 1-on-1 chat | 1.064s | 2.000s | 2.924s | 8249a48a4 | 2026-11-06 |
| a 5-image album in a 1-on-1 chat | 3.034s | 4.256s | 6.822s | 8249a48a4 | 2026-11-06 |
| a GIF in a 1-on-1 chat | 1.500s | 2.768s | 3.889s | 8249a48a4 | 2026-11-06 |
| 10 texts with 0.5s delay in a 1-on-1 chat | 2.188s | 4.114s | 6.091s | 8249a48a4 | 2026-11-06 |
| 1000-character text in a community #general channel | 0.847s | 1.543s | 4.264s | 8249a48a4 | 2026-11-06 |
| a 5-image album in a community #general channel | 4.530s | 5.819s | 8.729s | 8249a48a4 | 2026-11-06 |
| a GIF in a community #general channel | 1.349s | 2.768s | 7.163s | 8249a48a4 | 2026-11-06 |
| 10 texts with 0.5s delay in a community #general channel | 2.516s | 5.017s | 10.773s | 8249a48a4 | 2026-11-06 |

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.540s · Ok | +0.168s slower | 38.0% | 612.5 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.350s · Fast | parity | 32.5% | 615.2 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.167s · Fast | parity | 74.4% | 626.9 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.466s · Fast | -0.145s faster | 54.0% | 547.2 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.429s · Fast | parity | 37.1% | 582.6 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.485s · Fast | parity | 43.3% | 546.6 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.362s · Fast | +0.060s slower | 38.0% | 608.8 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.409s · Slow | +0.521s slower | 49.9% | 539.5 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.395s · Fast | -0.103s faster | 31.2% | 567.9 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.601s · Ok | -0.958s faster | 47.5% | 563.7 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.428s · Fast | -0.140s faster | 29.7% | 695.4 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 1.691s · Slow | no baseline | 66.1% | 641.5 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.213s · Fast | no baseline | 41.6% | 647.2 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.267s · Fast | no baseline | 73.5% | 548.8 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.153s · Fast | no baseline | 63.8% | 557.0 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.152s · Fast | no baseline | 48.4% | 549.4 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.140s · Fast | no baseline | 61.4% | 543.5 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 3-person group | 0.723s · Ok | no baseline | 15.1% | 667.5 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 1.109s · Slow | no baseline | 6.2% | 667.6 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 1.462s · Slow | no baseline | 1.7% | 667.6 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 3-person group | 3.031s · Slow | no baseline | 7.7% | 686.5 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 3.679s · Slow | no baseline | 3.0% | 698.4 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 4.354s · Slow | no baseline | 3.7% | 698.6 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 3-person group | 0.699s · Ok | no baseline | 8.5% | 701.6 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 1.391s · Slow | no baseline | 3.7% | 701.7 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 1.989s · Slow | no baseline | 3.4% | 701.7 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 3-person group | 1.122s · Slow | no baseline | 7.9% | 706.3 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 2.126s · Slow | no baseline | 6.7% | 706.7 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 3.717s · Slow | no baseline | 6.5% | 708.4 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Visible after sending 1000-character text in a 1-on-1 chat | 1.064s · Slow | no baseline | 56.4% | 641.4 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 2.000s · Slow | no baseline | 48.7% | 641.8 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 2.924s · Slow | no baseline | 81.5% | 642.1 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Visible after sending a 5-image album in a 1-on-1 chat | 3.034s · Slow | no baseline | 61.2% | 635.0 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 4.256s · Slow | no baseline | 63.6% | 622.5 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 6.822s · Slow | no baseline | 63.3% | 624.9 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Visible after sending a GIF in a 1-on-1 chat | 1.500s · Slow | no baseline | 62.0% | 628.1 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 2.768s · Slow | no baseline | 63.3% | 628.2 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 3.889s · Slow | no baseline | 59.1% | 628.2 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Visible after sending 10 texts with 0.5s delay in a 1-on-1 chat | 2.188s · Slow | no baseline | 61.2% | 613.2 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 4.114s · Slow | no baseline | 61.9% | 612.1 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 6.091s · Slow | no baseline | 61.6% | 612.2 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Communities | Time to Visible after sending 1000-character text in a community #general channel | 0.847s · Ok | no baseline | 58.6% | 633.8 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 1.543s · Slow | no baseline | 56.2% | 634.0 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 4.264s · Slow | no baseline | 59.9% | 634.5 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Communities | Time to Visible after sending a 5-image album in a community #general channel | 4.530s · Slow | no baseline | 43.8% | 654.2 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 5.819s · Slow | no baseline | 59.3% | 662.1 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 8.729s · Slow | no baseline | 59.6% | 663.0 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Communities | Time to Visible after sending a GIF in a community #general channel | 1.349s · Slow | no baseline | 57.5% | 663.6 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 2.768s · Slow | no baseline | 58.1% | 663.8 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 7.163s · Slow | no baseline | 74.0% | 650.1 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Communities | Time to Visible after sending 10 texts with 0.5s delay in a community #general channel | 2.516s · Slow | no baseline | 44.7% | 617.6 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 5.017s · Slow | no baseline | 46.3% | 619.9 MB | 8249a48a4<br>2026-11-06 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 10.773s · Slow | no baseline | 40.5% | 609.3 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 1.290s · Slow | +0.806s slower | 25.3% | 515.7 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.506s · Ok | parity | 48.6% | 570.7 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.232s · Fast | -0.170s faster | 42.6% | 549.0 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.591s · Ok | -0.158s faster | 31.5% | 529.7 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.453s · Fast | parity | 37.8% | 553.1 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.456s · Fast | -0.466s faster | 24.6% | 524.5 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.367s · Fast | parity | 33.4% | 539.5 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.073s · Slow | -0.717s faster | 38.2% | 546.8 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.418s · Fast | -0.263s faster | 31.7% | 557.8 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.574s · Ok | -0.793s faster | 37.6% | 538.2 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.606s · Ok | parity | 31.5% | 613.5 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.306s · Fast | no baseline | 42.7% | 525.7 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 0.546s · Ok | no baseline | 34.2% | 584.8 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 2.006s · Slow | no baseline | 41.2% | 554.1 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.516s · Ok | no baseline | 26.3% | 583.8 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.476s · Fast | no baseline | 50.9% | 534.8 MB | 8249a48a4<br>2026-11-06 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.165s · Fast | no baseline | 54.7% | 524.0 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 1.397s · Slow | +1.172s slower | 26.3% | 526.0 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.503s · Ok | parity | 55.6% | 608.3 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.333s · Fast | parity | 52.4% | 559.5 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.520s · Ok | -0.289s faster | 56.9% | 554.9 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.456s · Fast | parity | 49.9% | 601.3 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.516s · Ok | -0.434s faster | 43.2% | 561.1 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.390s · Fast | +0.062s slower | 60.6% | 568.3 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 1.640s · Slow | parity | 42.8% | 564.5 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.480s · Fast | -0.183s faster | 42.2% | 587.2 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.591s · Ok | -0.707s faster | 44.6% | 562.5 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.537s · Ok | parity | 59.9% | 641.0 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.409s · Fast | no baseline | 68.2% | 526.7 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.618s · Ok | no baseline | 56.1% | 592.9 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.671s · Ok | no baseline | 45.4% | 561.5 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 1.409s · Slow | no baseline | 53.0% | 619.6 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.492s · Fast | no baseline | 48.6% | 542.0 MB | 8249a48a4<br>2026-11-06 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.200s · Fast | no baseline | 69.0% | 562.2 MB | 8249a48a4<br>2026-11-06 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 4.924s · Slow | +1.149s slower | 32.6% | 604.2 MB | 8249a48a4<br>2026-11-06 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 3.805s · Slow | +1.703s slower | 3.5% | 660.9 MB | 8249a48a4<br>2026-11-06 |

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
