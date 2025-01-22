import sys
from pathlib import Path

# Add the project directory to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from etl.extract.extract import extract
from etl.load.load import load
from etl.transform.transform import transform

if __name__ == "__main__":
    print('Starting Extraction...')
    extract()
    print('Starting Transformation...')
    transform()
    print('Starting Loading...')
    load()