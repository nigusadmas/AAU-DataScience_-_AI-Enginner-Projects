from pathlib import Path

# ===========================
# Project Paths
# ===========================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA = DATA_DIR / "raw" / "used_cars.csv"
PROCESSED_DATA = DATA_DIR / "processed"

MODEL_DIR = BASE_DIR / "models"

OUTPUT_DIR = BASE_DIR / "outputs"
FIGURE_DIR = OUTPUT_DIR / "figures"
REPORT_DIR = OUTPUT_DIR / "reports"
TABLE_DIR = OUTPUT_DIR / "tables"

RANDOM_STATE = 42

TARGET = "price"

TEST_SIZE = 0.2