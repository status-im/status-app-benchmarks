# Desktop benchmark regression report

Generated: 2026-07-23 13:46

**Total flags:** 17

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_add_account_first_open_time_wallet_load | wallet_load_user | 1.201s | `e05186176a` | 2026-07-23 11:39 | Latest value 1.201s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.967s | `e05186176a` | 2026-07-23 11:39 | Latest value 1.967s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.839s | `e05186176a` | 2026-07-23 11:39 | Latest value 1.839s exceeds 1.0s slow threshold |
| test_wallet_send_time_wallet_load_alex | wallet_load_alex_user | 1.042s | `e05186176a` | 2026-07-23 11:39 | Latest value 1.042s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.484s | `e05186176a` | 2026-07-23 11:39 | Latest value 1.484s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 1.082s | `e05186176a` | 2026-07-23 11:39 | Latest value 1.082s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load_alex | wallet_load_alex_user | 2.342s | `e05186176a` | 2026-07-23 11:39 | Latest value 2.342s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load | wallet_load_user | 1.161s | `e05186176a` | 2026-07-23 11:39 | Latest value 1.161s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load_alex | wallet_load_alex_user | 1.227s | `e05186176a` | 2026-07-23 11:39 | Latest value 1.227s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_fresh | fresh_user | 17.396s | `e05186176a` | 2026-07-23 11:39 | Latest value 17.396s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 39.540s | `e05186176a` | 2026-07-23 11:39 | Latest value 39.540s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 48.873s | `e05186176a` | 2026-07-23 11:39 | Latest value 48.873s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 1.828s | `e05186176a` | 2026-07-23 11:39 | Latest value 1.828s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 10.768s | `e05186176a` | 2026-07-23 11:39 | Latest value 10.768s exceeds 1.0s slow threshold |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 4.172s | `e05186176a` | 2026-07-23 11:39 | Latest value 4.172s exceeds 1.0s slow threshold |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.096s | `e05186176a` | 2026-07-23 11:39 | Latest value 2.096s exceeds 1.0s slow threshold |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_send_first_open_time_fresh | fresh_user | 0.894s | `e05186176a` | 2026-07-23 11:39 | Slow (>1.0s) in 4 of last 5 builds — consider a backlog ticket |
