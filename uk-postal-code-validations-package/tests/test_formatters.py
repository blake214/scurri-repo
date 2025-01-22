import pytest

from uk_postal_code_validations import (
    formatPostalCode
)

# ============================== Formatter
@pytest.mark.parametrize("input,expected", [
    ("  aA9    9Aa  ", "AA9 9AA"),
])
def test_formatter(input,expected):
    assert formatPostalCode(input) == expected
