# Desktop benchmark regression report

Generated: 2026-07-20 15:12

**Total flags:** 7

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail |
|------|---------|-------|--------|------|--------|
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.790s | `343b8584a` | 2026-07-20 13:06 | Latest value 1.790s exceeds 1.0s slow threshold |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.770s | `343b8584a` | 2026-07-20 13:06 | Latest value 1.770s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.559s | `343b8584a` | 2026-07-20 13:06 | Latest value 1.559s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 1.367s | `343b8584a` | 2026-07-20 13:06 | Latest value 1.367s exceeds 1.0s slow threshold |
| test_wallet_swap_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.298s | `343b8584a` | 2026-07-20 13:06 | Latest value 1.298s exceeds 1.0s slow threshold |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 4.549s | `50ded3fa4` | 2026-07-20 11:05 | Latest value 4.549s exceeds 1.0s slow threshold |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.148s | `50ded3fa4` | 2026-07-20 11:05 | Latest value 2.148s exceeds 1.0s slow threshold |

## Backlog candidates

_No violations._
