# Desktop benchmark flags

Generated: 2026-10-21 07:42

**Total flags:** 33

## Regression

_No violations._

## Slow builds

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_swap_first_open_time_wallet_load | wallet_load_user | 1.120s | `3498927c33` | 2026-10-21 05:41 | Latest value 1.120s exceeds 1.0s slow threshold | — |
| test_direct_chat_plain_text_sent_time | default | 1.033s | `3498927c33` | 2026-10-21 05:41 | Latest value 1.033s exceeds 1.0s slow threshold | — |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_community_general_album_delivered_time | default | 8.437s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_gif_delivered_time | default | 7.030s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_album_sent_time | default | 6.350s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_delivered_time | default | 6.013s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_album_visible_time | default | 5.393s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_delivered_time | default | 4.575s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_assets_tab_first_open_time_fresh | fresh_user | 4.322s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | [#21694](https://github.com/status-im/status-app/issues/21694) |
| test_direct_chat_album_sent_time | default | 4.059s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 4.045s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_delivered_time | default | 3.972s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_plain_text_delivered_time | default | 3.648s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 3.578s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_visible_time | default | 3.429s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_sent_time | default | 3.422s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_visible_time | default | 2.907s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_burst_delivered_time | default | 2.852s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_burst_delivered_time | default | 2.528s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_plain_text_delivered_time | default | 2.364s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_sent_time | default | 2.341s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 2.242s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_gif_delivered_time | default | 2.064s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_gif_delivered_time | default | 1.986s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_gif_sent_time | default | 1.897s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_burst_sent_time | default | 1.362s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_plain_text_delivered_time | default | 1.286s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_burst_sent_time | default | 1.255s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_visible_time | default | 1.173s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_fresh | fresh_user | 1.134s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.046s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_gif_sent_time | default | 1.014s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_receive_first_open_time_wallet_load_alex | wallet_load_alex_user | 0.516s | `3498927c33` | 2026-10-21 05:41 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
