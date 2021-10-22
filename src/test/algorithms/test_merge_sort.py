import pytest
from dsa.algorithms.merge_sort import merge_sort


@pytest.mark.parametrize("array, expected", [
    ([3, 2, 1], [1, 2, 3]),
    ([8, 10 ,5, 3, 8], [3, 5, 8, 8, 10]),
    ([101, 12, 4, 3, 2, 0, -10], [-10, 0, 2, 3, 4, 12, 101]),
    ([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3]),
])
def test_merge_sort(array, expected):
    assert merge_sort(array) == expected
