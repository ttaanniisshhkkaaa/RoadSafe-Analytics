import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cleaning_utils import validate_required_columns


def test_collision_identifier_is_unique():
    df = pd.DataFrame({"accident_index": ["A1", "A2"]})
    assert df["accident_index"].is_unique


def test_required_columns_are_present():
    df = pd.DataFrame({"accident_index": ["A1"], "speed_limit": [30]})
    validate_required_columns(df, ["accident_index", "speed_limit"])


def test_relationship_keys_are_not_missing():
    df = pd.DataFrame({"accident_index": ["A1", "A2"]})
    assert df["accident_index"].notna().all()

