# Desktop benchmark flags

Generated: 2026-09-30 09:22

**Total flags:** 13

## Regression

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 1.000s | `a4a0c3` | 2026-09-30 07:21 | 3 consecutive builds each >=15% above previous (0.364s -> 1.000s) | — |

## Slow builds

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_assets_tab_first_open_time_wallet_load | wallet_load_user | 7.951s | `a4a0c3` | 2026-09-30 07:21 | Latest value 7.951s exceeds 1.0s slow threshold | — |
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.990s | `a4a0c3` | 2026-09-30 07:21 | Latest value 1.990s exceeds 1.0s slow threshold | — |
| test_wallet_account_first_open_time_wallet_load | wallet_load_user | 1.252s | `a4a0c3` | 2026-09-30 07:21 | Latest value 1.252s exceeds 1.0s slow threshold | — |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 5.229s | `a4a0c3` | 2026-09-30 07:21 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.442s | `a4a0c3` | 2026-09-30 07:21 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.197s | `a4a0c3` | 2026-09-30 07:21 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.818s | `a4a0c3` | 2026-09-30 07:21 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.704s | `a4a0c3` | 2026-09-30 07:21 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_swap_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.475s | `a4a0c3` | 2026-09-30 07:21 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.153s | `a4a0c3` | 2026-09-30 07:21 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_fresh | fresh_user | 1.122s | `a4a0c3` | 2026-09-30 07:21 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.048s | `a4a0c3` | 2026-09-30 07:21 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
