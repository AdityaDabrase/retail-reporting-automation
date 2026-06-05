from __future__ import annotations

import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


def generate_fake_retail_data(csv_path: Path, rows: int, seed: int = 42) -> None:
    random.seed(seed)

    start_date = datetime(2025, 1, 1)
    regions = ["North", "South", "East", "West"]
    categories = ["Electronics", "Home", "Apparel", "Grocery"]
    products_by_category = {
        "Electronics": ["Laptop", "Phone", "Headphones", "Monitor"],
        "Home": ["Mixer", "Vacuum", "Lamp", "Cookware"],
        "Apparel": ["Jacket", "Jeans", "Shoes", "Shirt"],
        "Grocery": ["Coffee", "Tea", "Snacks", "Cereal"],
    }

    records = []
    for idx in range(rows):
        order_date = start_date + timedelta(days=idx % 365)
        region = random.choice(regions)
        category = random.choice(categories)
        product = random.choice(products_by_category[category])
        units = random.randint(1, 10)
        unit_price = random.choice([15, 25, 40, 60, 90, 120, 180, 250])
        discount_pct = random.choice([0, 0, 0, 5, 10, 15])
        gross_revenue = units * unit_price
        discount_value = gross_revenue * (discount_pct / 100)
        revenue = round(gross_revenue - discount_value, 2)

        records.append(
            {
                "order_id": f"ORD-{100000 + idx}",
                "date": order_date.strftime("%Y-%m-%d"),
                "region": region,
                "category": category,
                "product": product,
                "units": units,
                "unit_price": unit_price,
                "discount_pct": discount_pct,
                "revenue": revenue,
            }
        )

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(records).to_csv(csv_path, index=False)
