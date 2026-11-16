"""Cleaning functions for collision records."""

import pandas as pd

from cleaning_utils import clean_common


def clean_collisions(df: pd.DataFrame) -> pd.DataFrame:
    result = clean_common(df)
    if "accident_index" in result.columns:
        result = result.drop_duplicates(subset=["accident_index"])
    return result.reset_index(drop=True)

