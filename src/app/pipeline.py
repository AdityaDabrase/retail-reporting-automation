from __future__ import annotations

from src.app.config import PipelineConfig
from src.data.fake_data import generate_fake_retail_data
from src.data.insights import generate_insights
from src.data.loader import load_retail_data
from src.data.quality import clean_retail_data, validate_required_columns
from src.data.transform import build_summary_tables, compute_kpis
from src.export.excel_writer import export_excel
from src.export.ppt_writer import export_powerpoint
from src.viz.charts import create_charts


def run_pipeline(config: PipelineConfig) -> dict[str, str]:
    config.input_csv.parent.mkdir(parents=True, exist_ok=True)
    config.output_dir.mkdir(parents=True, exist_ok=True)

    if config.force_generate or not config.input_csv.exists():
        generate_fake_retail_data(config.input_csv, rows=config.rows, seed=config.seed)

    raw_df = load_retail_data(config.input_csv)
    validate_required_columns(raw_df)
    cleaned_df = clean_retail_data(raw_df)

    summary_tables = build_summary_tables(cleaned_df)
    kpis = compute_kpis(cleaned_df)
    insights = generate_insights(kpis, summary_tables)
    charts = create_charts(summary_tables, config.output_dir)

    export_excel(cleaned_df, summary_tables, insights, config.excel_path)
    export_powerpoint(insights, summary_tables, charts, config.ppt_path)

    return {
        "input_csv": str(config.input_csv),
        "excel": str(config.excel_path),
        "ppt": str(config.ppt_path),
        "charts_dir": str(config.output_dir / "charts"),
    }
