import pytest
from dsa.problems.unique_binary_search_trees import num_trees


@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 2),
    (3, 5),
    (4, 14),
    (5, 42),
    (6, 132),
    (7, 429),
    (8, 1430),
])
def test_num_trees(n, expected):
    assert num_trees(n) == expected
