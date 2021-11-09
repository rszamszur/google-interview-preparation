import pytest
from dsa.problems.count_square_submatrices import count_squares


@pytest.mark.parametrize("matrix, expected", [
    ([[0,1,1,1],[1,1,1,1],[0,1,1,1]], 15),
    ([[1,0,1],[1,1,0],[1,1,0]], 7),
    ([[1,1,0,0,1],[1,0,1,1,1],[1,1,1,1,1],[1,0,1,0,1],[0,0,1,0,1]], 19),
    ([[1,0,1,0,1],[1,0,0,1,1],[0,1,0,1,1],[1,0,0,1,1]], 14),
])
def test_count_squares(matrix, expected):
    assert count_squares(matrix) == expected
