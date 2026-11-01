# Desktop benchmark flags

Generated: 2026-11-01 06:51

**Total flags:** 40

## Regression

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_community_general_plain_text_delivered_time | default | 8.167s | `af9f8f9276` | 2026-11-01 05:50 | 3 consecutive builds each >=15% above previous (3.001s -> 8.167s) | — |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 1.495s | `af9f8f9276` | 2026-11-01 05:50 | 3 consecutive builds each >=15% above previous (0.492s -> 1.495s) | — |

## Slow builds

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_wallet_send_first_open_time_wallet_load_alex | wallet_load_alex_user | 1.482s | `af9f8f9276` | 2026-11-01 05:50 | Latest value 1.482s exceeds 1.0s slow threshold | — |
| test_wallet_first_open_time_wallet_load | wallet_load_user | 1.002s | `af9f8f9276` | 2026-11-01 05:50 | Latest value 1.002s exceeds 1.0s slow threshold | — |

## Backlog candidates

| Test | Variant | Value | Commit | Date | Detail | Ticket |
|------|---------|-------|--------|------|--------|--------|
| test_community_general_plain_text_delivered_time | default | 8.167s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_album_delivered_time | default | 6.746s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_delivered_time | default | 5.951s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_delivered_time | default | 4.935s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_album_sent_time | default | 4.905s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_delivered_time | default | 4.855s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_sent_time | default | 4.365s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_sent_time | default | 4.288s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_burst_delivered_time | default | 4.273s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_gif_delivered_time | default | 4.054s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_album_visible_time | default | 3.994s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_album_visible_time | default | 3.817s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_second_open_loading_time_member | user_data0-user_account0 | 3.752s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_album_visible_time | default | 3.719s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_status_community_first_open_loading_time_member | user_data0-user_account0 | 3.630s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_burst_delivered_time | default | 3.373s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_gif_delivered_time | default | 3.101s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_plain_text_delivered_time | default | 2.961s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_sent_time | default | 2.579s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_assets_tab_first_open_time_fresh | fresh_user | 2.138s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | [#21694](https://github.com/status-im/status-app/issues/21694) |
| test_community_general_gif_sent_time | default | 1.956s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_collectibles_tab_first_open_time_wallet_load | wallet_load_user | 1.955s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_gif_delivered_time | default | 1.583s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_plain_text_delivered_time | default | 1.499s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_collectibles_tab_time_wallet_load_alex | wallet_load_alex_user | 1.495s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_burst_sent_time | default | 1.405s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_burst_visible_time | default | 1.368s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_collectibles_tab_time_wallet_load | wallet_load_user | 1.340s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_burst_sent_time | default | 1.297s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_send_first_open_time_fresh | fresh_user | 1.151s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_gif_sent_time | default | 1.136s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_gif_sent_time | default | 1.122s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
| test_community_general_gif_visible_time | default | 1.117s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 3 of last 5 builds -- consider a backlog ticket | — |
| test_direct_chat_plain_text_sent_time | default | 1.076s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 5 of last 5 builds -- consider a backlog ticket | — |
| test_wallet_swap_first_open_time_fresh | fresh_user | 1.055s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
| test_group_chat_plain_text_sent_time | default | 0.961s | `af9f8f9276` | 2026-11-01 05:50 | Slow (>1.0s) in 4 of last 5 builds -- consider a backlog ticket | — |
