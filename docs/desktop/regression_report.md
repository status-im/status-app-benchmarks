# Desktop benchmark regression report

Generated: 2026-07-28 07:42

**Total flags:** 15

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.821s | `cf137ac677` | 2026-07-28 05:35 | Latest value 1.821s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.415s | `cf137ac677` | 2026-07-28 05:35 | Latest value 1.415s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.359s | `cf137ac677` | 2026-07-28 05:35 | Latest value 1.359s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 1.430s | `cf137ac677` | 2026-07-28 05:35 | Latest value 1.430s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.249s | `cf137ac677` | 2026-07-28 05:35 | Latest value 1.249s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load | wallet_load_user | 1.096s | `cf137ac677` | 2026-07-28 05:35 | Latest value 1.096s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load_alex | wallet_load_alex_user | 1.268s | `cf137ac677` | 2026-07-28 05:35 | Latest value 1.268s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_fresh | fresh_user | 17.456s | `cf137ac677` | 2026-07-28 05:35 | Latest value 17.456s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 41.414s | `cf137ac677` | 2026-07-28 05:35 | Latest value 41.414s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 48.217s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 48.217s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 2.450s | `cf137ac677` | 2026-07-28 05:35 | Latest value 2.450s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 6.345s | `0b7c6c3241` | 2026-07-27 16:22 | Latest value 6.345s exceeds 1.0s slow threshold |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.251s | `cf137ac677` | 2026-07-28 05:35 | Latest value 3.251s exceeds 1.0s slow threshold |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.130s | `cf137ac677` | 2026-07-28 05:35 | Latest value 2.130s exceeds 1.0s slow threshold |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_send_first_open_time_fresh | fresh_user | 0.718s | `cf137ac677` | 2026-07-28 05:35 | Slow (>1.0s) in 3 of last 5 builds — consider a backlog ticket |
