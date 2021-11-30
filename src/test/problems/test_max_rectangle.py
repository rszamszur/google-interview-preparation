import pytest
from dsa.problems.max_rectangle import max_rectangle


@pytest.mark.parametrize("matrix, expected", [
    ([], 0),
    ([["0"]], 0),
    ([["1"]], 1),
    ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 6),
    ([["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]], 21)
])
def test_max_rectangle(matrix, expected):
    assert max_rectangle(matrix) == expected