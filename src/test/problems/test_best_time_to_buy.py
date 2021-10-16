import pytest
from dsa.problems.best_time_to_buy import best_time_to_buy


@pytest.mark.parametrize("prices, expected", [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
    ([2,4,1], 2),
    ([1, 2], 1),
    ([5, 3, 5, 6, 6, 6], 3),
    ([3,2,6,5,0,3], 4),
    ([11,2,7,1,4], 5),
])
def test_best_time_to_buy(prices, expected):
    assert best_time_to_buy(prices) == expected
