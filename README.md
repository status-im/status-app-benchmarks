# Benchmark Results

Automated test suite performance tracking for Windows platform.

**Desktop charts (no GitHub Pages needed):** [docs/desktop/README.md](./docs/desktop/README.md)

**[Interactive dashboard →](https://status-im.github.io/status-app-benchmarks/desktop/)** (requires GitHub Pages — enable in repo Settings → Pages → `master` / `/docs`)

Interactive charts grouped by scenario (community, wallet, swap). Updated nightly by Jenkins.

## Adding new tests

<details>
<summary><b>How to add a new performance test</b></summary>

1. Edit [`./scripts/tests_config.toml`](./scripts/tests_config.toml):

```toml
[[tests]]
test_id = "test_my_feature"
display_name = "My Feature Loading Time Performance"
graph_filename = "my_feature_loading_time.png"
pattern = "test_my_feature"
ylabel = "Load Time (s)"
```

2. Add the test to a scenario page (or create a new one):

```toml
[[pages]]
slug = "my-feature"
title = "My Feature"
description = "Short description shown on the dashboard."
test_ids = ["test_my_feature"]
```

3. Merge the change. Jenkins runs `python scripts/benchmark.py graphs` on the next scheduled run — it writes PNG + interactive HTML charts to `docs/desktop/` and regenerates the GitHub Pages site.

4. **One-time setup:** enable GitHub Pages in repo settings → **Build and deployment** → Source: **Deploy from a branch** → Branch: `master` / folder: **`/docs`**.

</details>

## Android benchmarks

See [`docs/android/README.md`](./docs/android/README.md) for mobile navigation response time charts.

---

Raw CSV history: [`data/`](./data/)
