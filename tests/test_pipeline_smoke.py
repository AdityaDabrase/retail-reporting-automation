from pathlib import Path

from src.app.config import PipelineConfig
from src.app.pipeline import run_pipeline


def test_pipeline_generates_outputs(tmp_path: Path) -> None:
    input_csv = tmp_path / "input" / "retail.csv"
    output_dir = tmp_path / "output"

    config = PipelineConfig(
        input_csv=input_csv,
        output_dir=output_dir,
        rows=50,
        seed=1,
        force_generate=True,
    )
    result = run_pipeline(config)

    assert Path(result["input_csv"]).exists()
    assert Path(result["excel"]).exists()
    assert Path(result["ppt"]).exists()
