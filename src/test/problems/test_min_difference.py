import pytest
from dsa.problems.min_difference import min_difference


@pytest.mark.parametrize("nums, expected", [
    ([5,3,2,4], 0),
    ([1,5,0,10,14], 1),
    ([6,6,0,1,1,4,6], 2),
    ([1,5,6,14,15], 1),
    ([1,2], 0),
    ([20,66,68,57,45,18,42,34,37,58], 31),
    ([82,81,95,75,20], 1),
])
def test_min_difference(nums, expected):
    assert min_difference(nums) == expected
