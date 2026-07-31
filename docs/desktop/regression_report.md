# Desktop benchmark regression report

Generated: 2026-07-31 06:56

**Total flags:** 16

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_send_first_open_time_fresh | fresh_user | 1.101s | `512bba730f` | 2026-07-31 04:49 | Latest value 1.101s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.116s | `512bba730f` | 2026-07-31 04:49 | Latest value 1.116s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.168s | `512bba730f` | 2026-07-31 04:49 | Latest value 1.168s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.420s | `512bba730f` | 2026-07-31 04:49 | Latest value 1.420s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.167s | `512bba730f` | 2026-07-31 04:49 | Latest value 1.167s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_first_open_time_fresh | fresh_user | 14.080s | `512bba730f` | 2026-07-31 04:49 | Latest value 14.080s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_first_open_time_wallet_load | wallet_load_user | 20.684s | `512bba730f` | 2026-07-31 04:49 | Latest value 20.684s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load | wallet_load_user | 1.041s | `512bba730f` | 2026-07-31 04:49 | Latest value 1.041s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load_alex | wallet_load_alex_user | 1.316s | `512bba730f` | 2026-07-31 04:49 | Latest value 1.316s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_fresh | fresh_user | 16.462s | `512bba730f` | 2026-07-31 04:49 | Latest value 16.462s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 41.085s | `512bba730f` | 2026-07-31 04:49 | Latest value 41.085s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 69.752s | `512bba730f` | 2026-07-31 04:49 | Latest value 69.752s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 2.070s | `512bba730f` | 2026-07-31 04:49 | Latest value 2.070s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 14.104s | `512bba730f` | 2026-07-31 04:49 | Latest value 14.104s exceeds 1.0s slow threshold |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.598s | `512bba730f` | 2026-07-31 04:49 | Latest value 3.598s exceeds 1.0s slow threshold |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.104s | `512bba730f` | 2026-07-31 04:49 | Latest value 2.104s exceeds 1.0s slow threshold |

## Backlog candidates

_No violations._
