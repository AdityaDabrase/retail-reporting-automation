from __future__ import annotations

import argparse
from pathlib import Path

from src.app.config import PipelineConfig
from src.app.pipeline import run_pipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Retail reporting automation MVP")
    parser.add_argument("--input", default="data/input/retail.csv", help="Input CSV path")
    parser.add_argument("--output", default="data/output", help="Output directory")
    parser.add_argument("--rows", default=500, type=int, help="Rows for fake data generation")
    parser.add_argument("--seed", default=42, type=int, help="Random seed")
    parser.add_argument(
        "--force-generate",
        action="store_true",
        help="Generate fake data even when input CSV exists",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = PipelineConfig(
        input_csv=Path(args.input),
        output_dir=Path(args.output),
        rows=args.rows,
        seed=args.seed,
        force_generate=args.force_generate,
    )

    result = run_pipeline(config)
    print("[SUCCESS] Retail report generated")
    print(f"Input CSV: {result['input_csv']}")
    print(f"Excel:     {result['excel']}")
    print(f"PPT:       {result['ppt']}")
    print(f"Charts:    {result['charts_dir']}")


if __name__ == "__main__":
    main()
