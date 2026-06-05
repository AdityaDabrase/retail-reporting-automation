# Retail Reporting Automation MVP

Python-only project that turns retail CSV data into:
- cleaned analysis-ready datasets,
- KPI tables and charts,
- editable Excel reports (`.xlsx`),
- editable PowerPoint decks (`.pptx`).

This project includes fake data generation so you can test end-to-end immediately.

## Project structure

```text
retail-reporting-automation/
  data/
    input/
    output/
  docs/
    ARCHITECTURE.md
    LINKEDIN_POST.md
  src/
    app/
      config.py
      pipeline.py
    cli/
      main.py
    data/
      fake_data.py
      loader.py
      quality.py
      transform.py
      insights.py
    export/
      excel_writer.py
      ppt_writer.py
    viz/
      charts.py
  requirements.txt
  run_report.py
```

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run_report.py --force-generate
```

## Outputs

After execution, check:
- `data/input/retail.csv` (generated if missing or forced),
- `data/output/report.xlsx`,
- `data/output/report.pptx`,
- `data/output/charts/*.png`.

## Use your own dataset

Your CSV should include these columns:
- `date`
- `region`
- `category`
- `product`
- `units`
- `revenue`

Run:

```bash
python run_report.py --input data/input/my_retail.csv --output data/output
```

## AI direction

The current MVP generates deterministic, rule-based insights.  
You can later plug in an LLM for narrative generation while keeping metrics computed by Python.
