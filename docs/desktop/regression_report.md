# Desktop benchmark regression report

Generated: 2026-07-30 17:42

**Total flags:** 15

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_send_first_open_time_fresh | fresh_user | 1.102s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 1.102s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.171s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 1.171s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.214s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 1.214s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.326s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 1.326s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_first_open_time_fresh | fresh_user | 15.364s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 15.364s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_first_open_time_wallet_load | wallet_load_user | 21.541s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 21.541s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load | wallet_load_user | 1.133s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 1.133s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load_alex | wallet_load_alex_user | 1.459s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 1.459s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_fresh | fresh_user | 16.328s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 16.328s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 39.197s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 39.197s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 63.799s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 63.799s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 1.965s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 1.965s exceeds 1.0s slow threshold |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.062s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 3.062s exceeds 1.0s slow threshold |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.152s | `6eedb01da6` | 2026-07-30 15:35 | Latest value 2.152s exceeds 1.0s slow threshold |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 0.207s | `6eedb01da6` | 2026-07-30 15:35 | Slow (>1.0s) in 4 of last 5 builds — consider a backlog ticket |
