import pytest
from dsa.problems.find_duplicates_in_array import find_duplicates


@pytest.mark.parametrize("nums, expected", [
    ([4,3,2,7,8,2,3,1], [2,3]),
    ([1,1,2], [1]),
    ([1,2,3,4], []),
    ([1,2,3,1,2,3], [1,2,3]),
])
def test_find_duplicates(nums, expected):
    assert sorted(find_duplicates(nums)) == expected
