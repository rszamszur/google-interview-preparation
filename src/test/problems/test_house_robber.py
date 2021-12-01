import pytest
from dsa.problems.house_robber import rob


@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,1], 4),
    ([2,7,9,3,1], 12),
])
def test_rob(nums, expected):
    assert rob(nums) == expected
