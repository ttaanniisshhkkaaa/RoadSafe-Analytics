import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cleaning_utils import clean_common


def test_column_names_are_standardized():
    result = clean_common(pd.DataFrame({"Accident Index": ["A1"]}))
    assert "accident_index" in result.columns


def test_duplicates_are_removed():
    result = clean_common(pd.DataFrame({"id": [1, 1], "value": ["x", "x"]}))
    assert len(result) == 1


def test_blank_values_become_missing():
    result = clean_common(pd.DataFrame({"value": ["", "N/A", "valid"]}))
    assert result["value"].isna().sum() == 2


def test_text_spaces_are_removed():
    result = clean_common(pd.DataFrame({"name": ["  road  "]}))
    assert result.loc[0, "name"] == "road"

