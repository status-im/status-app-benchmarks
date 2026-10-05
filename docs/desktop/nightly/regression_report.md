# Desktop benchmark flags

Generated: 2026-10-05 07:36

**Total flags:** 36

## Regression

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_first_open_time_wallet_load | wallet_load_user | 1.048s | `c070af64a4` | 2026-10-05 05:35 | 3 consecutive builds each >=15% above previous (0.293s -> 1.048s) | — |

## Slow builds

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_collectibles_tab_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.928s | `c070af64a4` | 2026-10-05 05:35 | Latest value 1.928s exceeds 1.0s slow threshold | — |
| test_wallet_assets_tab_time_wallet_load | wallet_load_user | 1.376s | `c070af64a4` | 2026-10-05 05:35 | Latest value 1.376s exceeds 1.0s slow threshold | — |
| test_wallet_first_open_time_wallet_load | wallet_load_user | 1.048s | `c070af64a4` | 2026-10-05 05:35 | Latest value 1.048s exceeds 1.0s slow threshold | — |
| test_wallet_receive_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.043s | `c070af64a4` | 2026-10-05 05:35 | Latest value 1.043s exceeds 1.0s slow threshold | — |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_community_general_album_delivered_time | default | 9.341s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_album_sent_time | default | 6.075s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_delivered_time | default | 5.661s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_delivered_time | default | 5.614s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_album_visible_time | default | 5.252s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_delivered_time | default | 4.222s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_sent_time | default | 3.654s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_sent_time | default | 3.524s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_gif_delivered_time | default | 3.388s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.268s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_gif_delivered_time | default | 3.221s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_visible_time | default | 3.076s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_plain_text_delivered_time | default | 2.959s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_visible_time | default | 2.948s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_burst_delivered_time | default | 2.694s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_burst_delivered_time | default | 2.315s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_sent_time | default | 2.161s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.145s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_plain_text_delivered_time | default | 1.668s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_gif_delivered_time | default | 1.380s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_gif_sent_time | default | 1.297s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 1.272s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.169s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_burst_sent_time | default | 1.151s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_visible_time | default | 1.150s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_burst_sent_time | default | 1.121s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.114s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_plain_text_delivered_time | default | 1.073s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_fresh | fresh_user | 1.023s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.012s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_gif_sent_time | default | 0.985s | `c070af64a4` | 2026-10-05 05:35 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
