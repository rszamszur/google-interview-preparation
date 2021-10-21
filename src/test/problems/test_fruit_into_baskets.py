import pytest
from dsa.problems.fruit_into_baskets import total_fruit


@pytest.mark.parametrize("fruits, expected", [
    ([1, 2, 1], 3),
    ([0, 1, 2, 2], 3),
    ([1, 2, 3, 2, 2], 4),
    ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5),
    ([0, 1, 6, 6, 4, 4, 6], 5),
])
def test_total_fruit(fruits, expected):
    assert total_fruit(fruits) == expected
