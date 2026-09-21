# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** Open the linked interactive charts below, or use the
> [dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) on GitHub Pages.

Full CSV history: [`data/`](../../data/).

> **Baseline note:** A full 2.38.0 (`5f66de`) re-baseline is not available — benchmark user profiles are incompatible with the 2.38.0 binary, and wallet tab tests now wait for tab content. Nightly trend continues; non-tab scenarios still compare to 2.38.0 where valid. When **2.39.0** ships, **2.38.2** becomes the new baseline — see [`BASELINE_2.39.md`](./BASELINE_2.39.md).

**Last run** · Sep 21, 2026 · [`cb9dab193`](https://github.com/status-im/status-app/commit/cb9dab193cb26d11698a3bd3c804db8f9bcffbf4)

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Near ok** · **>1.0s Slow**

Reference parity (where shown) means the latest value is within ±15% of 2.38.0. Wallet tab scenarios show **no baseline** because the e2e test now waits for tab content (Jul 2026).

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | 0.470s · Fast | +0.098s slower | 51.3% | 676.6 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.454s · Fast | +0.075s slower | 64.1% | 811.0 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to open a Wallet account for the first time in the session | 0.153s · Fast | parity | 57.0% | 682.3 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to open the Add account modal for the first time in the session | 0.381s · Fast | -0.230s faster | 17.7% | 693.1 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the Add account modal in the same session | 0.369s · Fast | parity | 19.3% | 743.7 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to open the Receive modal for the first time in the session | 0.389s · Fast | -0.082s faster | 16.4% | 694.2 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the Receive modal in the same session | 0.350s · Fast | +0.048s slower | 24.9% | 753.0 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to open the Send modal for the first time in the session | 1.036s · Slow | +0.148s slower | 40.1% | 788.3 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the Send modal in the same session | 0.673s · Ok | +0.175s slower | 28.1% | 844.7 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to open the Swap modal for the first time in the session | 0.969s · Near ok | -0.590s faster | 49.2% | 806.1 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the Swap modal in the same session | 0.502s · Ok | parity | 23.3% | 917.0 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to open the Assets tab for the first time in the session | 0.136s · Fast | no baseline | 59.5% | 724.9 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the Assets tab in the same session | 0.177s · Fast | no baseline | 41.3% | 728.2 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to open the Collectibles tab for the first time in the session | 0.229s · Fast | no baseline | 34.2% | 736.6 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the Collectibles tab in the same session | 0.120s · Fast | no baseline | 28.4% | 738.3 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to open the History tab for the first time in the session | 0.145s · Fast | no baseline | 62.1% | 703.4 MB | cb9dab193<br>2026-09-21 |
| New user profile | Wallet | Time to reopen the History tab in the same session | 0.121s · Fast | no baseline | 72.6% | 685.8 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 3-person group | 0.563s · Ok | no baseline | 55.5% | 767.2 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 3-person group | 3.153s · Slow | no baseline | 2.1% | 767.5 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 3-person group | 2.992s · Slow | no baseline | 6.8% | 784.1 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 3-person group | 4.220s · Slow | no baseline | 3.3% | 797.8 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 3-person group | 0.595s · Ok | no baseline | 30.5% | 878.5 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 3-person group | 1.560s · Slow | no baseline | 3.7% | 878.5 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 3-person group | 0.793s · Ok | no baseline | 11.1% | 870.3 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group | 3.306s · Slow | no baseline | 3.6% | 870.1 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Sent after sending 1000-character text in a 1-on-1 chat | 0.971s · Near ok | no baseline | 16.9% | 808.5 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Delivered after sending 1000-character text in a 1-on-1 chat | 1.274s · Slow | no baseline | 4.7% | 808.6 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Sent after sending a 5-image album in a 1-on-1 chat | 2.942s · Slow | no baseline | 25.3% | 800.5 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Delivered after sending a 5-image album in a 1-on-1 chat | 3.443s · Slow | no baseline | 1.7% | 806.2 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Sent after sending a GIF in a 1-on-1 chat | 0.520s · Ok | no baseline | 11.1% | 789.4 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Delivered after sending a GIF in a 1-on-1 chat | 1.649s · Slow | no baseline | 7.0% | 821.2 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat | 0.887s · Ok | no baseline | 37.1% | 874.1 MB | cb9dab193<br>2026-09-21 |
| New user profile | Messenger | Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat | 2.659s · Slow | no baseline | 13.1% | 872.4 MB | cb9dab193<br>2026-09-21 |
| New user profile | Communities | Time to Sent after sending 1000-character text in a community #general channel | 0.468s · Fast | no baseline | 17.9% | 830.4 MB | cb9dab193<br>2026-09-21 |
| New user profile | Communities | Time to Delivered after sending 1000-character text in a community #general channel | 2.200s · Slow | no baseline | 4.3% | 830.4 MB | cb9dab193<br>2026-09-21 |
| New user profile | Communities | Time to Sent after sending a 5-image album in a community #general channel | 6.572s · Slow | no baseline | 6.5% | 864.9 MB | cb9dab193<br>2026-09-21 |
| New user profile | Communities | Time to Delivered after sending a 5-image album in a community #general channel | 8.441s · Slow | no baseline | 2.6% | 980.8 MB | cb9dab193<br>2026-09-21 |
| New user profile | Communities | Time to Sent after sending a GIF in a community #general channel | 0.606s · Ok | no baseline | 3.3% | 981.9 MB | cb9dab193<br>2026-09-21 |
| New user profile | Communities | Time to Delivered after sending a GIF in a community #general channel | 3.097s · Slow | no baseline | 8.7% | 981.7 MB | cb9dab193<br>2026-09-21 |
| New user profile | Communities | Time to Sent after sending 10 texts with 0.5s delay in a community #general channel | 1.082s · Slow | no baseline | 8.2% | 964.8 MB | cb9dab193<br>2026-09-21 |
| New user profile | Communities | Time to Delivered after sending 10 texts with 0.5s delay in a community #general channel | 4.489s · Slow | no baseline | 5.0% | 961.9 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open Wallet for the first time after login | 0.546s · Ok | parity | 48.2% | 757.5 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.540s · Ok | parity | 71.1% | 803.6 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open a Wallet account for the first time in the session | 0.280s · Fast | -0.122s faster | 12.1% | 800.4 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Add account modal for the first time in the session | 0.488s · Fast | -0.261s faster | 52.0% | 755.5 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Add account modal in the same session | 0.416s · Fast | parity | 44.7% | 749.0 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Receive modal for the first time in the session | 0.512s · Ok | -0.410s faster | 28.5% | 745.3 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Receive modal in the same session | 0.326s · Fast | parity | 49.0% | 732.3 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Send modal for the first time in the session | 1.209s · Slow | -0.581s faster | 50.5% | 851.1 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Send modal in the same session | 0.754s · Ok | parity | 62.8% | 846.0 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Swap modal for the first time in the session | 0.768s · Ok | -0.599s faster | 32.0% | 852.7 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Swap modal in the same session | 0.696s · Ok | +0.164s slower | 38.7% | 929.2 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Assets tab for the first time in the session | 0.152s · Fast | no baseline | 54.7% | 822.0 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Assets tab in the same session | 1.204s · Slow | no baseline | 49.0% | 830.8 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.297s · Fast | no baseline | 74.3% | 808.4 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the Collectibles tab in the same session | 0.718s · Ok | no baseline | 50.7% | 792.9 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to open the History tab for the first time in the session | 0.622s · Ok | no baseline | 57.3% | 818.5 MB | cb9dab193<br>2026-09-21 |
| Returning user (semi-heavy wallet account) | Wallet | Time to reopen the History tab in the same session | 0.200s · Fast | no baseline | 73.9% | 800.7 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open Wallet for the first time after login | 0.332s · Fast | +0.107s slower | 57.8% | 957.0 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.579s · Ok | parity | 72.2% | 867.8 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open a Wallet account for the first time in the session | 0.487s · Fast | +0.140s slower | 40.4% | 889.4 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Add account modal for the first time in the session | 0.736s · Ok | parity | 57.6% | 939.8 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Add account modal in the same session | 0.479s · Fast | parity | 75.3% | 887.7 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Receive modal for the first time in the session | 0.703s · Ok | -0.247s faster | 32.9% | 797.7 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Receive modal in the same session | 0.359s · Fast | parity | 64.6% | 831.6 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Send modal for the first time in the session | 2.081s · Slow | +0.311s slower | 62.7% | 854.4 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Send modal in the same session | 0.769s · Ok | +0.106s slower | 50.0% | 893.2 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Swap modal for the first time in the session | 0.684s · Ok | -0.614s faster | 44.4% | 806.7 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Swap modal in the same session | 0.868s · Ok | +0.354s slower | 54.7% | 942.4 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Assets tab for the first time in the session | 0.506s · Ok | no baseline | 50.3% | 821.6 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Assets tab in the same session | 0.419s · Fast | no baseline | 61.8% | 777.6 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the Collectibles tab for the first time in the session | 0.353s · Fast | no baseline | 39.0% | 830.8 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the Collectibles tab in the same session | 0.171s · Fast | no baseline | 61.7% | 839.1 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to open the History tab for the first time in the session | 0.610s · Ok | no baseline | 62.0% | 836.5 MB | cb9dab193<br>2026-09-21 |
| Returning user (heavy account from Alex) | Wallet | Time to reopen the History tab in the same session | 0.208s · Fast | no baseline | 66.4% | 790.2 MB | cb9dab193<br>2026-09-21 |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 2.533s · Slow | -1.242s faster | 39.1% | 712.6 MB | cb9dab193<br>2026-09-21 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.170s · Slow | parity | 29.2% | 844.3 MB | cb9dab193<br>2026-09-21 |

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

**Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

- [Time to Sent after sending 1000-character text in a 3-person group](charts/group_chat_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/group_chat_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/group_chat_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a 3-person group](charts/group_chat_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/group_chat_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/group_chat_plain_text_delivered_ram.html)

- [Time to Sent after sending a 5-image album in a 3-person group](charts/group_chat_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/group_chat_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/group_chat_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a 3-person group](charts/group_chat_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/group_chat_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/group_chat_album_delivered_ram.html)

- [Time to Sent after sending a GIF in a 3-person group](charts/group_chat_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/group_chat_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/group_chat_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a 3-person group](charts/group_chat_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/group_chat_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/group_chat_gif_delivered_ram.html)

- [Time to Sent after sending 10 texts with 0.5s delay in a 3-person group](charts/group_chat_burst_sent_time.html)

- [CPU usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/group_chat_burst_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/group_chat_burst_sent_ram.html)

- [Time to Delivered after sending 10 texts with 0.5s delay in a 3-person group](charts/group_chat_burst_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/group_chat_burst_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/group_chat_burst_delivered_ram.html)

- [Time to Sent after sending 1000-character text in a 1-on-1 chat](charts/direct_chat_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/direct_chat_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/direct_chat_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a 1-on-1 chat](charts/direct_chat_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/direct_chat_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/direct_chat_plain_text_delivered_ram.html)

- [Time to Sent after sending a 5-image album in a 1-on-1 chat](charts/direct_chat_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/direct_chat_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/direct_chat_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a 1-on-1 chat](charts/direct_chat_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/direct_chat_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/direct_chat_album_delivered_ram.html)

- [Time to Sent after sending a GIF in a 1-on-1 chat](charts/direct_chat_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/direct_chat_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/direct_chat_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a 1-on-1 chat](charts/direct_chat_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/direct_chat_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/direct_chat_gif_delivered_ram.html)

- [Time to Sent after sending 10 texts with 0.5s delay in a 1-on-1 chat](charts/direct_chat_burst_sent_time.html)

- [CPU usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/direct_chat_burst_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 10 texts with 0.5s delay](charts/direct_chat_burst_sent_ram.html)

- [Time to Delivered after sending 10 texts with 0.5s delay in a 1-on-1 chat](charts/direct_chat_burst_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/direct_chat_burst_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 10 texts with 0.5s delay](charts/direct_chat_burst_delivered_ram.html)

### Communities

**Sent** is the time from pressing Send until the outgoing message shows one tick (published to the network). **Delivered** is the time from pressing Send until two ticks (a recipient acknowledged it); this includes time to Sent.

- [Time to Sent after sending 1000-character text in a community #general channel](charts/community_general_plain_text_sent_time.html)

- [CPU usage while waiting for Sent after sending 1000-character text](charts/community_general_plain_text_sent_cpu.html)

- [RAM usage while waiting for Sent after sending 1000-character text](charts/community_general_plain_text_sent_ram.html)

- [Time to Delivered after sending 1000-character text in a community #general channel](charts/community_general_plain_text_delivered_time.html)

- [CPU usage while waiting for Delivered after sending 1000-character text](charts/community_general_plain_text_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending 1000-character text](charts/community_general_plain_text_delivered_ram.html)

- [Time to Sent after sending a 5-image album in a community #general channel](charts/community_general_album_sent_time.html)

- [CPU usage while waiting for Sent after sending a 5-image album](charts/community_general_album_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a 5-image album](charts/community_general_album_sent_ram.html)

- [Time to Delivered after sending a 5-image album in a community #general channel](charts/community_general_album_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a 5-image album](charts/community_general_album_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a 5-image album](charts/community_general_album_delivered_ram.html)

- [Time to Sent after sending a GIF in a community #general channel](charts/community_general_gif_sent_time.html)

- [CPU usage while waiting for Sent after sending a GIF](charts/community_general_gif_sent_cpu.html)

- [RAM usage while waiting for Sent after sending a GIF](charts/community_general_gif_sent_ram.html)

- [Time to Delivered after sending a GIF in a community #general channel](charts/community_general_gif_delivered_time.html)

- [CPU usage while waiting for Delivered after sending a GIF](charts/community_general_gif_delivered_cpu.html)

- [RAM usage while waiting for Delivered after sending a GIF](charts/community_general_gif_delivered_ram.html)

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
