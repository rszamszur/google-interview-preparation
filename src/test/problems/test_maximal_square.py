import pytest
from dsa.problems.maximal_square import maximal_square


@pytest.mark.parametrize("matrix, expected", [
    ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4),
    ([["0","1"],["1","0"]], 1)
])
def test_maximal_square(matrix, expected):
    assert maximal_square(matrix) == expected
