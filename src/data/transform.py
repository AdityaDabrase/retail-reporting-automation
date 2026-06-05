from __future__ import annotations

import pandas as pd


def build_summary_tables(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    by_region = (
        df.groupby("region", as_index=False)
        .agg(total_revenue=("revenue", "sum"), total_units=("units", "sum"))
        .sort_values("total_revenue", ascending=False)
    )

    by_category = (
        df.groupby("category", as_index=False)
        .agg(total_revenue=("revenue", "sum"), total_units=("units", "sum"))
        .sort_values("total_revenue", ascending=False)
    )

    by_product = (
        df.groupby("product", as_index=False)
        .agg(total_revenue=("revenue", "sum"), total_units=("units", "sum"))
        .sort_values("total_revenue", ascending=False)
    )

    monthly = (
        df.assign(month=df["date"].dt.to_period("M").astype(str))
        .groupby("month", as_index=False)
        .agg(total_revenue=("revenue", "sum"))
        .sort_values("month")
    )

    return {
        "by_region": by_region,
        "by_category": by_category,
        "by_product": by_product,
        "monthly": monthly,
    }


def compute_kpis(df: pd.DataFrame) -> dict[str, float]:
    total_revenue = float(df["revenue"].sum())
    total_orders = float(df["order_id"].nunique() if "order_id" in df.columns else len(df))
    total_units = float(df["units"].sum())
    average_order_value = total_revenue / total_orders if total_orders else 0.0
    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "total_units": total_units,
        "average_order_value": average_order_value,
    }
