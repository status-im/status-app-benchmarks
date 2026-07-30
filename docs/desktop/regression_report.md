# Desktop benchmark regression report

Generated: 2026-07-30 07:47

**Total flags:** 17

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.610s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 1.610s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.631s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 1.631s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.315s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 1.315s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_first_open_time_fresh | fresh_user | 14.119s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 14.119s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_first_open_time_wallet_load | wallet_load_user | 22.402s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 22.402s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.526s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 1.526s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load | wallet_load_user | 1.126s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 1.126s exceeds 1.0s slow threshold |
| test_wallet_assets_tab_time_wallet_load_alex | wallet_load_alex_user | 1.472s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 1.472s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_fresh | fresh_user | 16.599s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 16.599s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 40.546s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 40.546s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 60.579s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 60.579s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 1.905s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 1.905s exceeds 1.0s slow threshold |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 27.102s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 27.102s exceeds 1.0s slow threshold |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.574s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 3.574s exceeds 1.0s slow threshold |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.163s | `cd4b4e1aa0` | 2026-07-30 05:40 | Latest value 2.163s exceeds 1.0s slow threshold |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 0.758s | `cd4b4e1aa0` | 2026-07-30 05:40 | Slow (>1.0s) in 3 of last 5 builds — consider a backlog ticket |
| test_wallet_swap_first_open_time_wallet_load_alex | wallet_load_alex_user | 0.721s | `cd4b4e1aa0` | 2026-07-30 05:40 | Slow (>1.0s) in 3 of last 5 builds — consider a backlog ticket |
