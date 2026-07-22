# Desktop benchmark regression report

Generated: 2026-07-22 16:54

**Total flags:** 16

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_send_first_open_time_fresh | fresh_user | 1.507s | `dbde82852` | 2026-07-22 14:48 | Latest value 1.507s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.645s | `dbde82852` | 2026-07-22 14:48 | Latest value 1.645s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 2.049s | `dbde82852` | 2026-07-22 14:48 | Latest value 2.049s exceeds 1.0s slow threshold |
| test_wallet_send_time_wallet_load | wallet_load_user | 1.097s | `dbde82852` | 2026-07-22 14:48 | Latest value 1.097s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.953s | `dbde82852` | 2026-07-22 14:48 | Latest value 1.953s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 1.541s | `dbde82852` | 2026-07-22 14:48 | Latest value 1.541s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.887s | `dbde82852` | 2026-07-22 14:48 | Latest value 1.887s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load | wallet_load_user | 1.286s | `dbde82852` | 2026-07-22 14:48 | Latest value 1.286s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load_alex | wallet_load_alex_user | 1.324s | `dbde82852` | 2026-07-22 14:48 | Latest value 1.324s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_fresh | fresh_user | 16.545s | `dbde82852` | 2026-07-22 14:48 | Latest value 16.545s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 39.837s | `dbde82852` | 2026-07-22 14:48 | Latest value 39.837s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 49.568s | `dbde82852` | 2026-07-22 14:48 | Latest value 49.568s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 1.970s | `dbde82852` | 2026-07-22 14:48 | Latest value 1.970s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 7.651s | `dbde82852` | 2026-07-22 14:48 | Latest value 7.651s exceeds 1.0s slow threshold |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.649s | `dbde82852` | 2026-07-22 14:48 | Latest value 3.649s exceeds 1.0s slow threshold |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.103s | `dbde82852` | 2026-07-22 14:48 | Latest value 2.103s exceeds 1.0s slow threshold |

## Backlog candidates

_No violations._
