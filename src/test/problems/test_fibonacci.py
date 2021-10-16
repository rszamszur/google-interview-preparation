import pytest
from dsa.problems.fibonacci import (
    fibonacci_recursive,
    fibonacci_top_up,
    fibonacci_bottom_up
)


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (7, 13),
    (10, 55),
])
def test_fibonacci(n, expected):
    assert fibonacci_recursive(n) == expected
    assert fibonacci_bottom_up(n) == expected
    assert fibonacci_top_up(n) == expected
