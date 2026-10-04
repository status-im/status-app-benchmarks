# Desktop benchmark flags

Generated: 2026-10-04 07:45

**Total flags:** 37

## Regression

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_first_open_time_wallet_load | wallet_load_user | 0.715s | `c070af64a4` | 2026-10-04 05:44 | 3 consecutive builds each >=15% above previous (0.220s -> 0.715s) | — |

## Slow builds

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_assets_tab_first_open_time_fresh | fresh_user | 4.842s | `c070af64a4` | 2026-10-04 05:44 | Latest value 4.842s exceeds 1.0s slow threshold | [#21694](https://github.com/status-im/status-app/issues/21694) |
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.181s | `c070af64a4` | 2026-10-04 05:44 | Latest value 1.181s exceeds 1.0s slow threshold | — |
| test_direct_chat_plain_text_sent_time | default | 1.156s | `c070af64a4` | 2026-10-04 05:44 | Latest value 1.156s exceeds 1.0s slow threshold | — |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 1.143s | `c070af64a4` | 2026-10-04 05:44 | Latest value 1.143s exceeds 1.0s slow threshold | — |
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 1.103s | `c070af64a4` | 2026-10-04 05:44 | Latest value 1.103s exceeds 1.0s slow threshold | — |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_community_general_album_delivered_time | default | 8.429s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_album_sent_time | default | 5.830s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_plain_text_delivered_time | default | 5.824s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_delivered_time | default | 5.383s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_album_visible_time | default | 5.184s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_delivered_time | default | 4.326s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_delivered_time | default | 3.983s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_sent_time | default | 3.844s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_sent_time | default | 3.489s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_visible_time | default | 3.355s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.180s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_visible_time | default | 3.000s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_gif_delivered_time | default | 2.988s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.147s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_burst_delivered_time | default | 2.136s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_burst_delivered_time | default | 2.113s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_sent_time | default | 2.078s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 2.051s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.627s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_plain_text_delivered_time | default | 1.569s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_gif_delivered_time | default | 1.363s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.321s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_burst_sent_time | default | 1.187s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_gif_delivered_time | default | 1.162s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_burst_sent_time | default | 1.103s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_visible_time | default | 1.094s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_plain_text_delivered_time | default | 1.086s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_gif_sent_time | default | 1.078s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_fresh | fresh_user | 1.063s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.043s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_gif_sent_time | default | 0.955s | `c070af64a4` | 2026-10-04 05:44 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
