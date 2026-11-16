from pathlib import Path
import sys

# Allow Python to find files inside src/
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from roadsafe_cleaning import clean_csv


RAW_FOLDER = PROJECT_ROOT / "data" / "raw"
PROCESSED_FOLDER = PROJECT_ROOT / "data" / "processed"


FILES = {
    "casualty-2025.csv": "casualty_2025_clean.csv",
    "collision-2025.csv": "collision_2025_clean.csv",
    "vehicle-2025.csv": "vehicle_2025_clean.csv",
}


def main():
    PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)

    for raw_name, processed_name in FILES.items():
        input_file = RAW_FOLDER / raw_name
        output_file = PROCESSED_FOLDER / processed_name

        if not input_file.exists():
            print(f"File not found: {input_file}")
            continue

        clean_csv(input_file, output_file)

    print("Data cleaning completed.")


if __name__ == "__main__":
    main()