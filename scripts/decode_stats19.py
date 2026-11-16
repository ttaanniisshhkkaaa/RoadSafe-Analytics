"""Decode STATS19 coded values using the official DfT data guide.

The original coded columns are preserved. For each decoded column, a new
column ending in ``_label`` is added.
"""

from pathlib import Path
import re

import pandas as pd


def normalise_column(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(name).strip().lower()).strip("_")


def normalise_code(value) -> str:
    """Make Excel/Pandas codes comparable, e.g. 1 and 1.0 become '1'."""
    if pd.isna(value):
        return "<NA>"
    text = str(value).strip()
    try:
        number = float(text)
        if number.is_integer():
            return str(int(number))
    except ValueError:
        pass
    return text


def load_code_guide(dictionary_file: Path) -> pd.DataFrame:
    guide = pd.read_excel(dictionary_file, sheet_name="2024_code_list")
    guide = guide.rename(columns={
        "table": "dataset",
        "field name": "field",
        "code/format": "code",
        "label": "label",
    })
    guide["field"] = guide["field"].map(normalise_column)
    guide = guide[guide["code"].notna() & guide["label"].notna()].copy()
    guide["code_key"] = guide["code"].map(normalise_code)
    guide["label"] = guide["label"].astype(str).str.strip()
    return guide


def decode_dataset(
    df: pd.DataFrame,
    dataset_name: str,
    guide: pd.DataFrame,
    suffix: str = "_label",
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Add label columns for all coded fields present in one dataset.

    Returns the decoded dataframe and a report of fields that were decoded.
    """
    result = df.copy()
    result.columns = [normalise_column(column) for column in result.columns]
    dataset_guide = guide[guide["dataset"].eq(dataset_name)].copy()
    report = []

    for field in sorted(dataset_guide["field"].unique()):
        if field not in result.columns:
            continue

        lookup = dataset_guide[dataset_guide["field"].eq(field)]
        lookup = lookup.drop_duplicates("code_key").set_index("code_key")["label"]
        result[field + suffix] = result[field].map(
            lambda value: lookup.get(normalise_code(value), pd.NA)
        )
        report.append({
            "dataset": dataset_name,
            "field": field,
            "output_column": field + suffix,
            "mapped_values": int(result[field + suffix].notna().sum()),
        })

    return result, pd.DataFrame(report)


def decode_files(project_root: Path) -> pd.DataFrame:
    """Decode the three cleaned CSV files and save decoded Parquet files."""
    dictionary_file = project_root / "data" / "stats19_data_dictionary.xlsx"
    processed_dir = project_root / "data" / "processed"
    guide = load_code_guide(dictionary_file)

    files = {
        "collision": processed_dir / "collision_2025_clean.csv",
        "vehicle": processed_dir / "vehicle_2025_clean.csv",
        "casualty": processed_dir / "casualty_2025_clean.csv",
    }

    reports = []
    for dataset_name, input_file in files.items():
        if not input_file.exists():
            raise FileNotFoundError(f"Missing cleaned file: {input_file}")
        df = pd.read_csv(input_file, low_memory=False)
        decoded, report = decode_dataset(df, dataset_name, guide)
        output_file = processed_dir / f"{dataset_name}s_2025_decoded.parquet"
        decoded.to_parquet(output_file, index=False)
        reports.append(report)
        print(f"Saved: {output_file}")

    return pd.concat(reports, ignore_index=True)


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    print(decode_files(root).to_string(index=False))
