# Benchmark Results
Automated test suite performance tracking for Windows platform.

## Adding new tests
<details>

1. Edit `./scripts/benchmark_config.toml` and add:

```toml
[[tests]]
test_id = "test_my_feature"
display_name = "My Feature Loading Time"
graph_filename = "my_feature_loading_time.png"
pattern = "test_my_feature"
ylabel = "Load Time (ms)"
```

2. Add your test in this README.md under section `Performance tests`:
```markdown
<summary><b>My Feature Loading Time</b></summary>

![My Feature Loading Timee](./docs/my_feature_loading_time.png)

```
</details>


## Summary Metrics

<summary><b>Pass Rate Trend</b></summary>

![Pass Rate](./docs/pass_rate_trend.png)

<summary><b>Total Test Suite Duration</b></summary>

![Duration](./docs/total_duration.png)

---

## Performance Tests

<summary><b>Wallet Screen Loading Time Performance</b></summary>

![Wallet Loading Time](./docs/wallet_loading_time.png)

<summary><b>Wallet Assets Loading Time Performance</b></summary>

![Wallet Assets Loading Time](./docs/wallet_assets_loading_time.png)

<summary><b>Swap Screen Loading Time Performance</b></summary>

![Swap Loading Time](./docs/swap_loading_time.png)

<summary><b>Community Screen Loading Time Performance</b></summary>

![Community Loading Time](./docs/community_loading_time.png)

---
