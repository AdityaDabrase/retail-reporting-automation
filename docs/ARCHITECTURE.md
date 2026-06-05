# Architecture

## Pipeline flow

1. Generate fake retail data (optional)
2. Load and clean CSV
3. Validate required columns and quality checks
4. Compute KPI tables
5. Create charts
6. Generate rule-based insights
7. Export Excel and PowerPoint

## Design principles

- Deterministic metrics first, narrative second
- Offline-first operation
- Modular code for easy extension
- Editable outputs for business users

## Module boundaries

- `src/data/fake_data.py`: synthetic dataset generation
- `src/data/loader.py`: CSV reading + type normalization
- `src/data/quality.py`: data quality checks
- `src/data/transform.py`: KPI and aggregation logic
- `src/data/insights.py`: rule-based business insights
- `src/viz/charts.py`: chart generation
- `src/export/excel_writer.py`: multi-sheet Excel export
- `src/export/ppt_writer.py`: slide deck export
- `src/app/pipeline.py`: orchestration

## Future AI extension

Add a new module `src/ai/insights_generator.py` that receives a compact KPI JSON payload and returns structured narrative fields:
- executive summary
- key insights
- risks
- recommended actions
