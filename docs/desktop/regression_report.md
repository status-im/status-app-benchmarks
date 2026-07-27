# Desktop benchmark regression report

Generated: 2026-07-27 18:29

**Total flags:** 16

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_add_account_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.211s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 1.211s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_fresh | fresh_user | 1.256s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 1.256s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.728s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 1.728s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 2.148s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 2.148s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 1.271s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 1.271s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.383s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 1.383s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load | wallet_load_user | 1.240s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 1.240s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load_alex | wallet_load_alex_user | 1.429s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 1.429s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_fresh | fresh_user | 17.506s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 17.506s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 40.064s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 40.064s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 48.217s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 48.217s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 2.310s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 2.310s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 6.345s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 6.345s exceeds 1.0s slow threshold |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.209s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 3.209s exceeds 1.0s slow threshold |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.141s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 2.141s exceeds 1.0s slow threshold |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_swap_first_open_time_fresh | fresh_user | 0.986s | `0b7c6c3241` | 2026-07-27 16:22 | Slow (>1.0s) in 4 of last 5 builds — consider a backlog ticket |
