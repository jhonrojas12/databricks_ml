import pytest
from utils.validation import validate_dataframe


class DummyDF:
    def __init__(self, columns):
        self.columns = columns


def test_validation_ok():
    df = DummyDF(["feature1", "label"])
    validate_dataframe(df, "label")


def test_validation_missing_target():
    df = DummyDF(["feature1"])
    with pytest.raises(ValueError):
        validate_dataframe(df, "label")