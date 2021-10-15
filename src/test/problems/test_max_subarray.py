import pytest
from dsa.problems.max_subarray import max_subarray


@pytest.mark.parametrize("nums, expected", [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([-2, 1], 1),
    ([10, 11, -20, 100], 101),
    ([1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1], 2),
])
def test_max_subarray(nums, expected):
    assert max_subarray(nums) == expected
