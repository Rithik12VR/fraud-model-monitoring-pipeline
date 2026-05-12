from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = BASE_DIR / "data" / "input" / "transactions.csv"
OUTPUT_DIR = BASE_DIR / "data" / "output"

REVIEW_THRESHOLD = 0.70
PSI_BINS = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
