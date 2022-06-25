import pytest
from dsa.problems.non_decreasing_array import check_possibility


@pytest.mark.parametrize("nums, expected", [
    ([4, 2, 3], True),
    ([4, 2, 1], False),
    ([5, 7, 1, 8], True),
    ([3, 4, 2, 3], False),
    ([1, 4, 2, 3], True),
])
def test_check_possibility(nums, expected):
    assert check_possibility(nums) == expected
