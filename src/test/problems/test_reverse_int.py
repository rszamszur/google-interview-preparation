import pytest
from dsa.problems.reverse_int import reverse_int


@pytest.mark.parametrize("x, expected", [
    (123, 321),
    (-123, -321),
    (120, 21),
    (0, 0),
    (1534236469, 0)
])
def test_reverse_int(x, expected):
    assert reverse_int(x) == expected
