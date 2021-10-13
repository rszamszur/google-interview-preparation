import pytest
from dsa.algorithms.binary_search import (
    binary_search,
    binary_search_recursive
)


@pytest.mark.parametrize("array, querry, expected", [
    ([1, 2, 3], 3, 2),
    ([1, 2, 3, 4, 5, 6, 7, 8], 4, 3),
    ([1, 2, 3, 4, 5, 6, 7, 8], 561, None),
    ([1], 1, 0),
    ([191, 201, 213, 459, 616, 617, 618, 1902, 4000], 1902, 7),
    ([x for x in range(400)], 882, None),
    ([x for x in range(400)], 12, 12),
])
def test_valid_parenthesis(array, querry, expected):
    assert binary_search(array, querry) == expected
    assert binary_search_recursive(array, querry) == expected
