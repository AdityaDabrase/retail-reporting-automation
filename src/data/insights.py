from __future__ import annotations

import pandas as pd


def generate_insights(
    kpis: dict[str, float], summary_tables: dict[str, pd.DataFrame]
) -> list[str]:
    by_region = summary_tables["by_region"]
    by_category = summary_tables["by_category"]
    by_product = summary_tables["by_product"]

    top_region = by_region.iloc[0]["region"] if not by_region.empty else "N/A"
    top_category = by_category.iloc[0]["category"] if not by_category.empty else "N/A"
    top_product = by_product.iloc[0]["product"] if not by_product.empty else "N/A"

    return [
        f"Total revenue: ${kpis['total_revenue']:,.2f}",
        f"Total orders: {int(kpis['total_orders']):,}",
        f"Total units sold: {int(kpis['total_units']):,}",
        f"Average order value (AOV): ${kpis['average_order_value']:,.2f}",
        f"Top region by revenue: {top_region}",
        f"Top category by revenue: {top_category}",
        f"Top product by revenue: {top_product}",
    ]
