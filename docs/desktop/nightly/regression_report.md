# Desktop benchmark flags

Generated: 2026-08-22 12:11

**Total flags:** 12

## Regression

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_first_open_time_wallet_load_alex | wallet_load_alex_user | 2.039s | `a152a8bd55` | 2026-08-22 10:04 | 3 consecutive builds each >=15% above previous (0.368s -> 2.039s) | — |

## Slow builds

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_first_open_time_wallet_load_alex | wallet_load_alex_user | 2.039s | `a152a8bd55` | 2026-08-22 10:04 | Latest value 2.039s exceeds 1.0s slow threshold | — |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 1.671s | `a152a8bd55` | 2026-08-22 10:04 | Latest value 1.671s exceeds 1.0s slow threshold | — |
| test_wallet_repeat_open_time_wallet_load_alex | wallet_load_alex_user | 1.486s | `a152a8bd55` | 2026-08-22 10:04 | Latest value 1.486s exceeds 1.0s slow threshold | — |
| test_wallet_assets_tab_time_wallet_load_alex | wallet_load_alex_user | 1.280s | `a152a8bd55` | 2026-08-22 10:04 | Latest value 1.280s exceeds 1.0s slow threshold | — |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 1.258s | `a152a8bd55` | 2026-08-22 10:04 | Latest value 1.258s exceeds 1.0s slow threshold | — |
| test_wallet_send_first_open_time_fresh | fresh_user | 1.002s | `a152a8bd55` | 2026-08-22 10:04 | Latest value 1.002s exceeds 1.0s slow threshold | — |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.171s | `a152a8bd55` | 2026-08-22 10:04 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.154s | `a152a8bd55` | 2026-08-22 10:04 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.745s | `a152a8bd55` | 2026-08-22 10:04 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.249s | `a152a8bd55` | 2026-08-22 10:04 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_swap_first_open_time_fresh | fresh_user | 0.985s | `a152a8bd55` | 2026-08-22 10:04 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
