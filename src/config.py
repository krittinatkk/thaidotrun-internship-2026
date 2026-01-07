# src/config.py
import os
from pathlib import Path
import yaml
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_PATH = DATA_DIR / "raw" / "bkk_data_final.csv"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUTS_DIR = DATA_DIR / "outputs"
REPORTS_DIR = PROJECT_ROOT / "reports"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

# Load YAML config
with open(PROJECT_ROOT / "config" / "settings.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)

# Ensure directories exist
for directory in [PROCESSED_DATA_DIR, OUTPUTS_DIR, REPORTS_DIR]:
    directory.mkdir(exist_ok=True, parents=True)

# Export settings
__all__ = [
    "PROJECT_ROOT", "DATA_DIR", "RAW_DATA_PATH", 
    "PROCESSED_DATA_DIR", "OUTPUTS_DIR", "REPORTS_DIR",
    "NOTEBOOKS_DIR", "CONFIG"
]