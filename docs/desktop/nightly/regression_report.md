# Desktop benchmark flags

Generated: 2026-09-25 17:21

**Total flags:** 35

## Regression

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_swap_time_wallet_load | wallet_load_user | 0.959s | `c93fb27ef0` | 2026-09-25 15:20 | 3 consecutive builds each >=15% above previous (0.460s -> 0.959s) | — |

## Slow builds

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_repeat_open_time_wallet_load_alex | wallet_load_alex_user | 2.225s | `c93fb27ef0` | 2026-09-25 15:20 | Latest value 2.225s exceeds 1.0s slow threshold | — |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 1.450s | `c93fb27ef0` | 2026-09-25 15:20 | Latest value 1.450s exceeds 1.0s slow threshold | — |
| test_wallet_receive_first_open_time_wallet_load | wallet_load_user | 1.047s | `c93fb27ef0` | 2026-09-25 15:20 | Latest value 1.047s exceeds 1.0s slow threshold | — |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_community_general_album_delivered_time | default | 8.386s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_album_sent_time | default | 5.740s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_delivered_time | default | 5.432s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_album_visible_time | default | 5.054s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_gif_delivered_time | default | 4.215s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_delivered_time | default | 4.045s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_delivered_time | default | 3.999s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.663s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_sent_time | default | 3.514s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_sent_time | default | 3.512s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_plain_text_delivered_time | default | 3.287s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_gif_delivered_time | default | 3.238s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_burst_delivered_time | default | 3.187s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_plain_text_delivered_time | default | 3.080s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_burst_delivered_time | default | 3.056s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_visible_time | default | 3.014s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_visible_time | default | 2.946s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 2.233s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_sent_time | default | 2.107s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_gif_delivered_time | default | 2.029s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_gif_sent_time | default | 1.418s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.324s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_wallet_load | wallet_load_user | 1.152s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_plain_text_delivered_time | default | 1.148s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_visible_time | default | 1.119s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_burst_sent_time | default | 1.118s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_burst_sent_time | default | 1.056s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_gif_sent_time | default | 1.037s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_gif_sent_time | default | 1.013s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_fresh | fresh_user | 1.009s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_swap_first_open_time_fresh | fresh_user | 0.972s | `c93fb27ef0` | 2026-09-25 15:20 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
