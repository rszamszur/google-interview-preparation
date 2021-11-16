import pytest
from dsa.problems.move_zeroes import move_zeroes


@pytest.mark.parametrize("nums, expected", [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([1,0,2,0,3,0,4,5,6,0,0,0], [1,2,3,4,5,6,0,0,0,0,0,0]),
])
def test_move_zeroes(nums, expected):
    assert move_zeroes(nums) == expected
