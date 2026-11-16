"""Cleaning functions for vehicle records."""

import pandas as pd

from cleaning_utils import clean_common


def clean_vehicles(df: pd.DataFrame) -> pd.DataFrame:
    result = clean_common(df)
    key_columns = [column for column in ["accident_index", "vehicle_reference"] if column in result.columns]
    if key_columns:
        result = result.drop_duplicates(subset=key_columns)
    return result.reset_index(drop=True)

