# Desktop benchmark flags

Generated: 2026-08-12 14:52

**Total flags:** 13

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_assets_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.226s | `4acdfba962` | 2026-08-12 12:45 | Latest value 1.226s exceeds 1.0s slow threshold | — |
| test_wallet_receive_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.035s | `4acdfba962` | 2026-08-12 12:45 | Latest value 1.035s exceeds 1.0s slow threshold | — |
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 1.011s | `4acdfba962` | 2026-08-12 12:45 | Latest value 1.011s exceeds 1.0s slow threshold | — |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 59.102s | `4acdfba962` | 2026-08-12 12:45 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 45.455s | `4acdfba962` | 2026-08-12 12:45 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_collectibles_tab_first_open_time_fresh | fresh_user | 15.618s | `4acdfba962` | 2026-08-12 12:45 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | [#21732](https://github.com/status-im/status-app/issues/21732) |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.124s | `4acdfba962` | 2026-08-12 12:45 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.224s | `4acdfba962` | 2026-08-12 12:45 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 2.051s | `4acdfba962` | 2026-08-12 12:45 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.553s | `4acdfba962` | 2026-08-12 12:45 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.228s | `4acdfba962` | 2026-08-12 12:45 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.034s | `4acdfba962` | 2026-08-12 12:45 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_fresh | fresh_user | 1.022s | `4acdfba962` | 2026-08-12 12:45 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
