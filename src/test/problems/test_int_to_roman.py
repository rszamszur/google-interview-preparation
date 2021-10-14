import pytest
from dsa.problems.int_to_roman import int_to_roman


@pytest.mark.parametrize("value, expected", [
    (3, "III"),
    (58, "LVIII"),
    (1994, "MCMXCIV"),
    (2021, "MMXXI"),
    (420, "CDXX"),
    (69, "LXIX"),
])
def test_int_to_roman(value, expected):
    assert int_to_roman(value) == expected
