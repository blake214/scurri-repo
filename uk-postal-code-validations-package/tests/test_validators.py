import pytest

from uk_postal_code_validations import (
    validationArea,
    validationDistrict,
    validationSector,
    validationUnit,
    validationOutwardCode,
    validationInwardCode,
    validationUKPostalCode
)

# ============================== Area
@pytest.mark.parametrize("input,expected", [
    ("A", True),
    ("AA", True),
    ("AAA", False),
    ("9A", False)
])
def test_validation_area_valid(input,expected):
    assert validationArea(input) == expected

# ============================== District
@pytest.mark.parametrize("input,expected", [
    ("99", True),
    ("9A", True),
    ("A9", False),
    ("AA", False)
])
def test_validation_district_valid(input,expected):
    assert validationDistrict(input) == expected

# ============================== Sector
@pytest.mark.parametrize("input,expected", [
    ("9", True),
    ("10", False),
    ("A", False)
])
def test_validation_sector_valid(input,expected):
    assert validationSector(input) == expected

# ============================== Unit
@pytest.mark.parametrize("input,expected", [
    ("AA", True),
    ("AB", True),
    ("A1", False),
    ("AAA", False),
])
def test_validation_unit_valid(input,expected):
    assert validationUnit(input) == expected

# ============================== Outwards Code
@pytest.mark.parametrize("input,expected", [
    ("A9", True),
    ("A9A", True),
    ("AA9", True),
    ("AA99", True),
    ("AA9A", True),
    ("999", False)
])
def test_validation_outwards_valid(input,expected):
    assert validationOutwardCode(input) == expected

# ============================== Inwards Code
@pytest.mark.parametrize("input,expected", [
    ("9AA", True),
    ("999", False)
])
def test_validation_inwards_valid(input,expected):
    assert validationInwardCode(input) == expected

# ============================== Postal Code
@pytest.mark.parametrize("input,expected", [
    ("AA9 9AA", True),
    ("999 999", False)
])
def test_validation_postal_valid(input,expected):
    assert validationUKPostalCode(input) == expected