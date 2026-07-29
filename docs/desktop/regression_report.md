# Desktop benchmark regression report

Generated: 2026-07-29 17:26

**Total flags:** 18

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.329s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 1.329s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.153s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 1.153s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.303s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 1.303s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 1.183s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 1.183s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.394s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 1.394s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_first_open_time_fresh | fresh_user | 12.866s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 12.866s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_first_open_time_wallet_load | wallet_load_user | 24.149s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 24.149s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.638s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 1.638s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load | wallet_load_user | 1.117s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 1.117s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load_alex | wallet_load_alex_user | 1.877s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 1.877s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_fresh | fresh_user | 16.590s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 16.590s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 40.450s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 40.450s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 80.555s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 80.555s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 2.251s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 2.251s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 9.754s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 9.754s exceeds 1.0s slow threshold |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.027s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 3.027s exceeds 1.0s slow threshold |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.138s | `f4cbae9d7f` | 2026-07-29 15:19 | Latest value 2.138s exceeds 1.0s slow threshold |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_send_first_open_time_fresh | fresh_user | 0.600s | `f4cbae9d7f` | 2026-07-29 15:19 | Slow (>1.0s) in 3 of last 5 builds — consider a backlog ticket |
