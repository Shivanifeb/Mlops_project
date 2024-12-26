import os
from pathlib import Path 

list_of_files = [
    ".github/workflow/.gitkeep",
    "sec/_init_.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/data_trainer.py",
    "src/components/data_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/logger/logging.py", 
    "src/exception/exception",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",  
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Check if filedir exists and is a file
    if filedir:
        if os.path.exists(filedir) and os.path.isfile(filedir):
            raise FileExistsError(f"A file with the name '{filedir}' already exists. Cannot create directory.")

        # Create directory if it doesn't exist
        os.makedirs(filedir, exist_ok=True)

    # Create an empty file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
