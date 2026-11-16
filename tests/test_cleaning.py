import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from roadsafe_cleaning import clean_dataframe


def test_column_names_are_cleaned():
    df = pd.DataFrame({
        "Person Name": ["Piyush"],
        "Age-Value": [20]
    })

    result = clean_dataframe(df)

    assert "person_name" in result.columns
    assert "age_value" in result.columns


def test_duplicate_rows_are_removed():
    df = pd.DataFrame({
        "name": ["A", "A"],
        "age": [20, 20]
    })

    result = clean_dataframe(df)

    assert len(result) == 1


def test_empty_rows_are_removed():
    df = pd.DataFrame({
        "name": ["A", None],
        "age": [20, None]
    })

    result = clean_dataframe(df)

    assert len(result) == 1


def test_spaces_are_removed_from_text():
    df = pd.DataFrame({
        "name": ["  Piyush  "]
    })

    result = clean_dataframe(df)

    assert result.iloc[0]["name"] == "Piyush"