"""Parse machine / OS info from collect_machine_info.ps1 JSON."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Optional

import pandas as pd

RUN_ENVIRONMENT_FIELDS = ('hostname', 'windows_version', 'os_build', 'cpu', 'ram_gb')
RUN_ENVIRONMENT_CSV = 'run_environment.csv'


def parse_machine_info(machine_info_file: Optional[Path]) -> Dict[str, str]:
    """Read system metadata from JSON (see machine_info.example.json)."""
    if machine_info_file is None or not machine_info_file.exists():
        return {}
    try:
        data = json.loads(machine_info_file.read_text(encoding='utf-8'))
    except json.JSONDecodeError as error:
        print(f'Warning: Failed to parse machine info JSON {machine_info_file}: {error}')
        return {}
    if not isinstance(data, dict):
        return {}
    return {
        field: str(data[field]).strip()
        for field in RUN_ENVIRONMENT_FIELDS
        if data.get(field) is not None and str(data[field]).strip()
    }


def load_run_environment(data_dir: Path) -> pd.DataFrame:
    path = data_dir / RUN_ENVIRONMENT_CSV
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(
        path,
        parse_dates=['date'],
        dtype={field: str for field in RUN_ENVIRONMENT_FIELDS},
    ).sort_values('date')
