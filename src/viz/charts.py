from __future__ import annotations

from pathlib import Path

import matplotlib
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def create_charts(
    summary_tables: dict[str, pd.DataFrame], output_dir: Path
) -> dict[str, Path]:
    charts_dir = output_dir / "charts"
    charts_dir.mkdir(parents=True, exist_ok=True)

    by_region = summary_tables["by_region"]
    monthly = summary_tables["monthly"]

    region_chart = charts_dir / "revenue_by_region.png"
    plt.figure(figsize=(8, 4.5))
    plt.bar(by_region["region"], by_region["total_revenue"])
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(region_chart, dpi=150)
    plt.close()

    monthly_chart = charts_dir / "monthly_revenue_trend.png"
    plt.figure(figsize=(8, 4.5))
    plt.plot(monthly["month"], monthly["total_revenue"], marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(monthly_chart, dpi=150)
    plt.close()

    return {
        "region_chart": region_chart,
        "monthly_chart": monthly_chart,
    }
