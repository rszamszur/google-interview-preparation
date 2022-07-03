import pytest
from dsa.problems.max_cake_area import max_cake_area


@pytest.mark.parametrize("h, w, hc, vc, expected", [
    (5, 4, [1, 2, 4], [1, 3], 4),
    (5, 4, [3, 1], [1], 6),
    (5, 4, [3], [3], 9),
])
def test_max_cake_area(h, w, hc, vc, expected):
    assert max_cake_area(h, w, hc, vc) == expected
