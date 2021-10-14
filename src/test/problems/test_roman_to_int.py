import pytest
from dsa.problems.roman_to_int import roman_to_int


@pytest.mark.parametrize("roman, expected", [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
    ("MMXXI", 2021),
    ("CDXX", 420),
    ("LXIX", 69),
])
def test_roman_to_int(roman, expected):
    assert roman_to_int(roman) == expected
