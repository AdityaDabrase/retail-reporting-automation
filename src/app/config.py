from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PipelineConfig:
    input_csv: Path
    output_dir: Path
    rows: int = 500
    seed: int = 42
    force_generate: bool = False

    @property
    def excel_path(self) -> Path:
        return self.output_dir / "report.xlsx"

    @property
    def ppt_path(self) -> Path:
        return self.output_dir / "report.pptx"
