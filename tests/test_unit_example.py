import pytest

from app import normalize_item


@pytest.mark.parametrize(
    ("input_text", "expected"),
    [
        ("  Apple  ", "apple"),
        ("BaNaNa", "banana"),
        ("", ""),
        (None, ""),
    ],
)
def test_normalize_item(input_text, expected):
    assert normalize_item(input_text) != expected
