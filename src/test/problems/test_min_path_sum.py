import pytest
from dsa.problems.min_path_sum import min_path_sum_dp, min_path_sum_djikstra


@pytest.mark.parametrize("grid, expected", [
    ([[1,3,1],[1,5,1],[4,2,1]], 7),
    ([[1,2,3],[4,5,6]], 12),
])
def test_min_path_sum_dp(grid, expected):
    assert min_path_sum_dp(grid) == expected


@pytest.mark.parametrize("grid, expected", [
    ([[1,3,1],[1,5,1],[4,2,1]], 7),
    ([[1,2,3],[4,5,6]], 12),
])
def test_min_path_sum_djikstra(grid, expected):
    assert min_path_sum_djikstra(grid) == expected
