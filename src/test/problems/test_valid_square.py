import pytest
from dsa.problems.valid_square import valid_square


@pytest.mark.parametrize("p1, p2, p3, p4, expected", [
    ([0, 0], [1, 1], [1, 0], [0, 1], True),
    ([0, 0], [1, 1], [1, 0], [0, 12], False),
    ([1, 0], [-1, 0], [0, 1], [0, -1], True),
    ([6987,-473], [6985,-473], [6986,-472], [6986,-474], True),
    ([1134,-2539], [492,-1255], [-792,-1897], [-150,-3181], True),
    ([0, 0], [0, 0], [0, 0], [0, 0], False),
])
def test_valid_square(p1, p2, p3, p4, expected):
    assert valid_square(p1, p2, p3, p4) == expected
