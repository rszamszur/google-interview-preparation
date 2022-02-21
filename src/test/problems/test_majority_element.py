import pytest
from dsa.problems.majority_element import majority_element


@pytest.mark.parametrize("nums, expected", [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([1, 2, 3, 4, 5, 6, 6, 6, 3, 3, 3, 3, 6, 6, 6], 6),
])
def test_majority_element(nums, expected):
    assert majority_element(nums) == expected
