# Desktop benchmark regression report

Generated: 2026-07-29 06:53

**Total flags:** 15

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_send_first_open_time_fresh | fresh_user | 1.157s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 1.157s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.269s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 1.269s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.617s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 1.617s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.442s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 1.442s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load | wallet_load_user | 1.113s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 1.113s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load_alex | wallet_load_alex_user | 1.234s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 1.234s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_fresh | fresh_user | 16.435s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 16.435s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 40.209s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 40.209s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 56.774s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 56.774s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 1.963s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 1.963s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 16.857s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 16.857s exceeds 1.0s slow threshold |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.531s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 3.531s exceeds 1.0s slow threshold |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.130s | `8b23a3fe3d` | 2026-07-29 04:47 | Latest value 2.130s exceeds 1.0s slow threshold |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 0.794s | `8b23a3fe3d` | 2026-07-29 04:47 | Slow (>1.0s) in 4 of last 5 builds — consider a backlog ticket |
| test_wallet_swap_first_open_time_wallet_load_alex | wallet_load_alex_user | 0.729s | `8b23a3fe3d` | 2026-07-29 04:47 | Slow (>1.0s) in 4 of last 5 builds — consider a backlog ticket |
