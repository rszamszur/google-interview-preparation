import pytest
from dsa.algorithms.heap_sort import heap_sort


@pytest.mark.parametrize("array, expected", [
    ([1,4,2,3,9,7,10,8,14,16], [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]),
    ([5,6,4,3,3,4,8,11,2,1,40], [1, 2, 3, 3, 4, 4, 5, 6, 8, 11, 40]),
    ([3,1,2], [1,2,3]),
])
def test_heap_sort(array, expected):
    assert heap_sort(array) == expected
