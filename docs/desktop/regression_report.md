# Desktop benchmark regression report

Generated: 2026-07-24 07:33

**Total flags:** 17

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_add_account_first_open_time_fresh | fresh_user | 1.093s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 1.093s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_fresh | fresh_user | 1.373s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 1.373s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 2.069s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 2.069s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.899s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 1.899s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.457s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 1.457s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 1.510s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 1.510s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.998s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 1.998s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load | wallet_load_user | 1.248s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 1.248s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load_alex | wallet_load_alex_user | 1.322s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 1.322s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_fresh | fresh_user | 16.402s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 16.402s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 39.150s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 39.150s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 52.066s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 52.066s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 1.946s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 1.946s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 11.603s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 11.603s exceeds 1.0s slow threshold |
| test_wallet_activity_tab_first_open_time_wallet_load | wallet_load_user | 1.052s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 1.052s exceeds 1.0s slow threshold |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 4.167s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 4.167s exceeds 1.0s slow threshold |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.106s | `0c1c2b0287` | 2026-07-24 05:26 | Latest value 2.106s exceeds 1.0s slow threshold |

## Backlog candidates

_No violations._
