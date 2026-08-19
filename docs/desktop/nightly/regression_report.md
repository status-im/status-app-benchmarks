# Desktop benchmark flags

Generated: 2026-08-19 08:18

**Total flags:** 9

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_assets_tab_first_open_time_wallet_load | wallet_load_user | 1.405s | `6d4aa0faf8` | 2026-08-19 06:10 | Latest value 1.405s exceeds 1.0s slow threshold | — |
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 1.044s | `6d4aa0faf8` | 2026-08-19 06:10 | Latest value 1.044s exceeds 1.0s slow threshold | — |
| test_wallet_swap_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.006s | `6d4aa0faf8` | 2026-08-19 06:10 | Latest value 1.006s exceeds 1.0s slow threshold | — |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 4.912s | `6d4aa0faf8` | 2026-08-19 06:10 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.139s | `6d4aa0faf8` | 2026-08-19 06:10 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.673s | `6d4aa0faf8` | 2026-08-19 06:10 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.189s | `6d4aa0faf8` | 2026-08-19 06:10 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.103s | `6d4aa0faf8` | 2026-08-19 06:10 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_fresh | fresh_user | 1.071s | `6d4aa0faf8` | 2026-08-19 06:10 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
