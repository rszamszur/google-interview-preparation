import pytest
from dsa.problems.add_digits import add_digits


@pytest.mark.parametrize("nums, expected", [
    (38, 2),
    (0, 0),
])
def test_add_digits(nums, expected):
    assert add_digits(nums) == expected

