"""Reusable utilities for RoadSafe Analytics data cleaning."""

import pandas as pd


MISSING_VALUES = ["", " ", "NA", "N/A", "na", "n/a", "NULL", "null", "None", "none", "-", "?"]


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result.columns = (
        result.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    return result


def normalize_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    return result.replace(MISSING_VALUES, pd.NA)


def strip_text_values(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    for column in result.select_dtypes(include=["object", "string"]).columns:
        result[column] = result[column].astype("string").str.strip()
    return result


def remove_empty_and_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    result = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    return result.drop_duplicates().reset_index(drop=True)


def convert_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    for column in result.columns:
        converted = pd.to_numeric(result[column], errors="coerce")
        non_missing = result[column].notna().sum()
        if non_missing and converted.notna().sum() == non_missing:
            result[column] = converted
    return result


def clean_common(df: pd.DataFrame) -> pd.DataFrame:
    result = standardize_column_names(df)
    result = normalize_missing_values(result)
    result = strip_text_values(result)
    result = remove_empty_and_duplicate_rows(result)
    return convert_numeric_columns(result)


def validate_required_columns(df: pd.DataFrame, required_columns: list[str]) -> None:
    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

