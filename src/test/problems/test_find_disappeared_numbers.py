import pytest
from dsa.problems.find_disappeared_numbers import find_disappeared_numbers


@pytest.mark.parametrize("nums, expected", [
    ([4,3,2,7,8,2,3,1], [5,6]),
    ([1,1], [2]),
])
def test_find_disappeared_numbers(nums, expected):
    assert find_disappeared_numbers(nums) == expected
