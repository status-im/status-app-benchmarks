# Desktop benchmark flags

Generated: 2026-09-01 08:29

**Total flags:** 11

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 1.183s | `847e196cf1` | 2026-09-01 06:22 | Latest value 1.183s exceeds 1.0s slow threshold | — |
| test_wallet_receive_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.083s | `847e196cf1` | 2026-09-01 06:22 | Latest value 1.083s exceeds 1.0s slow threshold | — |
| test_wallet_activity_tab_first_open_time_wallet_load | wallet_load_user | 1.044s | `847e196cf1` | 2026-09-01 06:22 | Latest value 1.044s exceeds 1.0s slow threshold | — |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 2.582s | `847e196cf1` | 2026-09-01 06:22 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.199s | `847e196cf1` | 2026-09-01 06:22 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.703s | `847e196cf1` | 2026-09-01 06:22 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.480s | `847e196cf1` | 2026-09-01 06:22 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 1.390s | `847e196cf1` | 2026-09-01 06:22 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.108s | `847e196cf1` | 2026-09-01 06:22 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 0.421s | `847e196cf1` | 2026-09-01 06:22 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_assets_tab_first_open_time_wallet_load | wallet_load_user | 0.209s | `847e196cf1` | 2026-09-01 06:22 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
