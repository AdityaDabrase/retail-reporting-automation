from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = {"date", "region", "category", "product", "units", "revenue"}


def validate_required_columns(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def clean_retail_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.dropna(
        subset=["date", "region", "category", "product", "units", "revenue"]
    ).copy()
    cleaned = cleaned[(cleaned["units"] > 0) & (cleaned["revenue"] >= 0)].copy()
    return cleaned
