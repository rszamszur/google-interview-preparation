import pytest
from dsa.problems.sort_array import sort_array, sort_array_merge_sort


@pytest.mark.parametrize("array, expected", [
    ([1,4,2,3,9,7,10,8,14,16], [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]),
    ([5,6,4,3,3,4,8,11,2,1,40], [1, 2, 3, 3, 4, 4, 5, 6, 8, 11, 40]),
    ([3,1,2], [1,2,3]),
    ([3, 2, 1], [1, 2, 3]),
    ([8, 10, 5, 3, 8], [3, 5, 8, 8, 10]),
    ([101, 12, 4, 3, 2, 0, -10], [-10, 0, 2, 3, 4, 12, 101]),
    ([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3]),
])
def test_sort_array(array, expected):
    assert sort_array(array.copy()) == expected
    assert sort_array_merge_sort(array) == expected
