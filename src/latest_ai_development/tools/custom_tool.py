from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from pathlib import Path

class FileReaderInput(BaseModel):
    file_name: str = Field(..., description="Name of file inside knowledge folder")

class FileReaderTool(BaseTool):
    name: str = "Resume & Job Reader"
    description: str = "Reads resume or job file from knowledge folder"
    args_schema: Type[BaseModel] = FileReaderInput

    def _run(self, file_name: str) -> str:
        # Project root = .../job_fit_agent
        project_root = Path(__file__).resolve().parents[3]
        knowledge_dir = project_root/"knowledge"
        file_path = knowledge_dir/file_name

        if not file_path.exists():
            return f"File {file_name} not found in {knowledge_dir}"

        return file_path.read_text(encoding="utf-8")