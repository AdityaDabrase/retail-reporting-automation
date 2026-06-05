from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_retail_data(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["units"] = pd.to_numeric(df["units"], errors="coerce")
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
    return df
