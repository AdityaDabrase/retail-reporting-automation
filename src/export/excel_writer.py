from __future__ import annotations

from pathlib import Path

import pandas as pd


def export_excel(
    raw_df: pd.DataFrame,
    summary_tables: dict[str, pd.DataFrame],
    insights: list[str],
    output_path: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        raw_df.to_excel(writer, sheet_name="RawData", index=False)
        summary_tables["by_region"].to_excel(writer, sheet_name="ByRegion", index=False)
        summary_tables["by_category"].to_excel(writer, sheet_name="ByCategory", index=False)
        summary_tables["by_product"].to_excel(writer, sheet_name="ByProduct", index=False)
        summary_tables["monthly"].to_excel(writer, sheet_name="MonthlyTrend", index=False)
        pd.DataFrame({"insight": insights}).to_excel(
            writer, sheet_name="Insights", index=False
        )
