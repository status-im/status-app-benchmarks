# Windows — performance benchmarks

Automated test suite performance tracking for the Windows desktop app.
Charts show data from the last 30 days — each point is one nightly run.
Load-time charts plot the average of runs per build. Lower is better.

> **Viewing charts:** This README renders inline PNG images on GitHub — works without
> GitHub Pages. For interactive charts (hover tooltips, zoom), use the
> [interactive dashboard](https://status-im.github.io/status-app-benchmarks/desktop/) once GitHub Pages is enabled.

Full CSV history: [`data/`](../../data/).

## System info

**Host:** WINDOWS-NODE-01 · **Windows:** Windows Server 2022 Standard 21H2 · **OS build:** 20348.1487 · **CPU:** AMD Ryzen 7 PRO 8700GE w/ Radeon 780M Graphics · **RAM:** 63 GB

## Scenario summary

Latest result for every tested scenario. Speed categories:

**<0.5s Fast** · **0.5–0.9s Ok** · **0.9–1.0s Ok near slow** · **>1.0s Slow**

Reference parity means the latest value is within ±15% of 2.38.0.

| User profile | Area | Scenario | Load time / Speed | vs 2.38.0 | CPU | RAM | Measured |
|--------------|------|----------|-------------------|-----------|-----|-----|----------|
| New user profile | Wallet | Time to open Wallet for the first time after login | — · No data | — | — | — | — · — |
| New user profile | Wallet | Time to reopen Wallet in the same session | 0.464s · Fast | parity | — | — | e05886b4e · 2026-07-17 |
| New user profile | Wallet | Time to open a Wallet account for the first time | — · No data | — | — | — | — · — |
| New user profile | Wallet | Time to open the Add account modal | — · No data | — | — | — | — · — |
| New user profile | Wallet | Time to open the Receive modal | — · No data | — | — | — | — · — |
| New user profile | Wallet | Time to open the Send modal | — · No data | — | — | — | — · — |
| New user profile | Wallet | Time to open the Swap modal | 0.755s · Ok | parity | — | — | e05886b4e · 2026-07-17 |
| New user profile | Wallet | Time to open the Assets tab | — · No data | — | — | — | — · — |
| New user profile | Wallet | Time to open the Collectibles tab | — · No data | — | — | — | — · — |
| New user profile | Wallet | Time to open the Activity tab | — · No data | — | — | — | — · — |
| New user profile | Messenger | Not tested | Not tested | — | — | — | — |
| New user profile | Communities | Not tested | Not tested | — | — | — | — |
| New user profile | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Wallet | Time to open Wallet for the first time after login | — · No data | — | — | — | — · — |
| Returning user (heavy wallet account) | Wallet | Time to reopen Wallet in the same session | 0.680s · Ok | parity | — | — | e05886b4e · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to open a Wallet account for the first time | — · No data | — | — | — | — · — |
| Returning user (heavy wallet account) | Wallet | Time to open the Add account modal | — · No data | — | — | — | — · — |
| Returning user (heavy wallet account) | Wallet | Time to open the Receive modal | — · No data | — | — | — | — · — |
| Returning user (heavy wallet account) | Wallet | Time to open the Send modal | — · No data | — | — | — | — · — |
| Returning user (heavy wallet account) | Wallet | Time to open the Swap modal | 0.829s · Ok | parity | — | — | e05886b4e · 2026-07-17 |
| Returning user (heavy wallet account) | Wallet | Time to open the Assets tab | — · No data | — | — | — | — · — |
| Returning user (heavy wallet account) | Wallet | Time to open the Collectibles tab | — · No data | — | — | — | — · — |
| Returning user (heavy wallet account) | Wallet | Time to open the Activity tab | — · No data | — | — | — | — · — |
| Returning user (heavy wallet account) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (heavy wallet account) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open Wallet for the first time after login | — · No data | — | — | — | — · — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to reopen Wallet in the same session | 0.678s · Ok | parity | — | — | e05886b4e · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open a Wallet account for the first time | — · No data | — | — | — | — · — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Add account modal | — · No data | — | — | — | — · — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Receive modal | — · No data | — | — | — | — · — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Send modal | — · No data | — | — | — | — · — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Swap modal | 0.787s · Ok | parity | — | — | e05886b4e · 2026-07-17 |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Assets tab | — · No data | — | — | — | — · — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Collectibles tab | — · No data | — | — | — | — · — |
| Returning user (medium heavy wallet account from Alex) | Wallet | Time to open the Activity tab | — · No data | — | — | — | — · — |
| Returning user (medium heavy wallet account from Alex) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Communities | Not tested | Not tested | — | — | — | — |
| Returning user (medium heavy wallet account from Alex) | Browser | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Wallet | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Messenger | Not tested | Not tested | — | — | — | — |
| Returning user (Status community member) | Communities | Time to open Status community for the first time after login | 4.269s · Slow | parity | 17.2% | 905.9 MB | e05886b4e · 2026-07-17 |
| Returning user (Status community member) | Communities | Time to reopen Status community in the same session | 2.196s · Slow | parity | 37.2% | 865.6 MB | e05886b4e · 2026-07-17 |
| Returning user (Status community member) | Browser | Not tested | Not tested | — | — | — | — |

## New user profile

Newly created user profile (no-preseeded user data)

### User data profile

- **Stored data:** No pre-seeded data
- **Wallet:** 0 tokens with balance > 0 · 0 NFTs · 0 transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 0 joined communities · 0 spectated communities

### Wallet

**Time to open Wallet for the first time after login**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening Wallet for the first time after login**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening Wallet for the first time after login**

_No data yet — chart will appear after the next nightly benchmark run._

![Time to reopen Wallet in the same session](./wallet_repeat_open_time_fresh.png)

**CPU usage while reopening Wallet in the same session**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while reopening Wallet in the same session**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open a Wallet account for the first time**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening a Wallet account for the first time**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening a Wallet account for the first time**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Add account modal**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Add account modal**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Add account modal**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Receive modal**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Receive modal**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Receive modal**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Send modal**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Send modal**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Send modal**

_No data yet — chart will appear after the next nightly benchmark run._

![Time to open the Swap modal](./wallet_swap_time_fresh.png)

**CPU usage while opening the Swap modal**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Swap modal**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Assets tab**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Assets tab**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Assets tab**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Collectibles tab**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Collectibles tab**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Collectibles tab**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Activity tab**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Activity tab**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Activity tab**

_No data yet — chart will appear after the next nightly benchmark run._

### Messenger

_Not tested for this user profile._

### Communities

_Not tested for this user profile._

### Browser

_Not tested for this user profile._

## Returning user (heavy wallet account)

Returning user with wallet_load profile (~29 MB user data).

### User data profile

- **Stored data:** ~29 MB
- **Wallet:** TBD tokens with balance > 0 · TBD NFTs · TBD transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 0 joined communities · 0 spectated communities

### Wallet

**Time to open Wallet for the first time after login**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening Wallet for the first time after login**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening Wallet for the first time after login**

_No data yet — chart will appear after the next nightly benchmark run._

![Time to reopen Wallet in the same session](./wallet_repeat_open_time_wallet_load.png)

**CPU usage while reopening Wallet in the same session**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while reopening Wallet in the same session**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open a Wallet account for the first time**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening a Wallet account for the first time**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening a Wallet account for the first time**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Add account modal**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Add account modal**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Add account modal**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Receive modal**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Receive modal**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Receive modal**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Send modal**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Send modal**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Send modal**

_No data yet — chart will appear after the next nightly benchmark run._

![Time to open the Swap modal](./wallet_swap_time_wallet_load.png)

**CPU usage while opening the Swap modal**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Swap modal**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Assets tab**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Assets tab**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Assets tab**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Collectibles tab**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Collectibles tab**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Collectibles tab**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Activity tab**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Activity tab**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Activity tab**

_No data yet — chart will appear after the next nightly benchmark run._

### Messenger

_Not tested for this user profile._

### Communities

_Not tested for this user profile._

### Browser

_Not tested for this user profile._

## Returning user (medium heavy wallet account from Alex)

Returning user with wallet_load_alex profile (~16 MB user data).

### User data profile

- **Stored data:** ~16 MB
- **Wallet:** TBD tokens with balance > 0 · TBD NFTs · TBD transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 0 joined communities · 0 spectated communities

### Wallet

**Time to open Wallet for the first time after login**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening Wallet for the first time after login**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening Wallet for the first time after login**

_No data yet — chart will appear after the next nightly benchmark run._

![Time to reopen Wallet in the same session](./wallet_repeat_open_time_wallet_load_alex.png)

**CPU usage while reopening Wallet in the same session**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while reopening Wallet in the same session**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open a Wallet account for the first time**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening a Wallet account for the first time**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening a Wallet account for the first time**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Add account modal**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Add account modal**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Add account modal**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Receive modal**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Receive modal**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Receive modal**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Send modal**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Send modal**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Send modal**

_No data yet — chart will appear after the next nightly benchmark run._

![Time to open the Swap modal](./wallet_swap_time_wallet_load_alex.png)

**CPU usage while opening the Swap modal**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Swap modal**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Assets tab**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Assets tab**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Assets tab**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Collectibles tab**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Collectibles tab**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Collectibles tab**

_No data yet — chart will appear after the next nightly benchmark run._

**Time to open the Activity tab**

_No data yet — chart will appear after the next nightly benchmark run._

**CPU usage while opening the Activity tab**

_No data yet — chart will appear after the next nightly benchmark run._

**RAM usage while opening the Activity tab**

_No data yet — chart will appear after the next nightly benchmark run._

### Messenger

_Not tested for this user profile._

### Communities

_Not tested for this user profile._

### Browser

_Not tested for this user profile._

## Returning user (Status community member)

Returning user with Status community already joined.

### User data profile

- **Stored data:** TBD
- **Wallet:** 0 tokens with balance > 0 · 0 NFTs · 0 transactions
- **Messenger:** 0 1-on-1 chats · 0 group chats
- **Communities:** 1 joined communities · 0 spectated communities

### Wallet

_Not tested for this user profile._

### Messenger

_Not tested for this user profile._

### Communities

![Time to open Status community for the first time after login](./community_first_open_loading_time_member.png)

![Time to reopen Status community in the same session](./community_second_open_loading_time_member.png)

![CPU usage while opening Status community for the first time after login](./community_first_open_cpu_member.png)

![CPU usage while reopening Status community in the same session](./community_second_open_cpu_member.png)

![RAM usage while opening Status community for the first time after login](./community_first_open_ram_member.png)

![RAM usage while reopening Status community in the same session](./community_second_open_ram_member.png)

### Browser

_Not tested for this user profile._

---

Generated by `scripts/benchmark.py graphs` from `data/`. Refreshed nightly by Jenkins.
