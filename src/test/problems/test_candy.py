import pytest
from dsa.problems.candy import candy


@pytest.mark.parametrize("ratings, expected", [
    ([1, 0, 2], 5),
    ([1, 2, 2], 4),
    ([29, 51, 87, 87, 72, 12], 12),
    ([12, 4, 3, 11, 34, 34, 1, 67], 16)
])
def test_candy(ratings, expected):
    assert candy(ratings) == expected
