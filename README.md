# Benchmark Results

Automated test suite performance tracking for Windows platform.

**Desktop charts (no GitHub Pages needed):** [docs/desktop/README.md](./docs/desktop/README.md)

**[Interactive dashboard →](https://status-im.github.io/status-app-benchmarks/desktop/)**

Interactive charts grouped by scenario (community, wallet, swap). Updated nightly by Jenkins.

## System info (desktop)

Nightly Jenkins runs collect Windows host metadata and pass it to `benchmark.py parse` via `--machine-info`. The dashboard **System info** block reads from `data/run_environment.csv`.

```powershell
powershell -File scripts/collect_machine_info.ps1 -OutputPath machine_info.json
python scripts/benchmark.py parse <dir> `
  --run-id nightly-<commit>-<build> `
  --channel nightly `
  --commit-hash <hash> `
  --date <iso-date> `
  --machine-info machine_info.json
```

See [`scripts/machine_info.example.json`](./scripts/machine_info.example.json) for the JSON shape. Wired in `status-app/scripts/push_benchmark.sh`.

## Channels

Nightly, pull-request, and release results are stored separately and never mixed:

- nightly → [`data/`](./data/)
- PR → `data/desktop/pr/<number>/`
- release → `data/desktop/releases/<series>/` (for example `2.39`)

The manual Jenkins job (`status-app/e2e/manual-benchmark-windows`) publishes PR and RC runs. It does **not** promote a final release into the nightly baseline.

### Promote a final release baseline

After a fully passed final build (for example `2.39.0`, not an RC) is published, promote that run once by hand. Look up `run_id` in `data/desktop/releases/2.39/runs.csv`, then:

```powershell
python scripts/benchmark.py promote-baseline --release-data-dir data/desktop/releases/2.39 --run-id <run_id>
python scripts/benchmark.py graphs --data-dir data --output-dir docs/desktop/nightly --channel nightly --baseline-dir data/desktop/baselines
```

An RC cannot be promoted. Each release series can be promoted only once.

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

</details>

## Android benchmarks

See [`docs/android/README.md`](./docs/android/README.md) for mobile navigation response time charts.

---

Raw CSV history: [`data/`](./data/)
