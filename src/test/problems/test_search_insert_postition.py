import pytest
from dsa.problems.search_insert_position import search_insert_position


@pytest.mark.parametrize("nums, target, expected", [
    ([1,3,5,6], 5, 2),
    ([1,3,5,6], 2, 1),
    ([1,3,5,6], 7, 4),
    ([1,3,5,6], 0, 0),
    ([1], 0, 0),
])
def test_search_insert_position(nums, target, expected):
    assert search_insert_position(nums, target) == expected
