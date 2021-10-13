import pytest
from dsa.problems.two_sum import two_sum
from dsa.problems.two_sum import two_sum_brute_force


@pytest.mark.parametrize("nums, target, expected", [
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1]),
    ([1,2,3,4], 80, None),
])
def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected
    assert two_sum_brute_force(nums, target) == expected
