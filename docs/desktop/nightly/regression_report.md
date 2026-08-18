# Desktop benchmark flags

Generated: 2026-08-18 07:37

**Total flags:** 8

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_assets_tab_first_open_time_wallet_load | wallet_load_user | 1.300s | `e348b4caa8` | 2026-08-18 05:30 | Latest value 1.300s exceeds 1.0s slow threshold | — |
| test_wallet_receive_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.071s | `e348b4caa8` | 2026-08-18 05:30 | Latest value 1.071s exceeds 1.0s slow threshold | — |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 4.921s | `e348b4caa8` | 2026-08-18 05:30 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.151s | `e348b4caa8` | 2026-08-18 05:30 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.878s | `e348b4caa8` | 2026-08-18 05:30 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.158s | `e348b4caa8` | 2026-08-18 05:30 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.050s | `e348b4caa8` | 2026-08-18 05:30 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_fresh | fresh_user | 1.007s | `e348b4caa8` | 2026-08-18 05:30 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
