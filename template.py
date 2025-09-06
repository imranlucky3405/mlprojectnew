print("Template script started...")
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

project_name = "mlproject"

# Base directory (C:\mlproject)
base_dir = Path(__file__).parent.resolve()
logging.info(f"Base directory: {base_dir}")

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "pyproject.toml"
]

for filepath in list_of_files:
    filepath = base_dir / filepath  # absolute path
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created (or exists): {filedir}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Empty file created: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")