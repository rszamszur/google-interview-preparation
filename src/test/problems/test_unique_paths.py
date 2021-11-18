import pytest
from dsa.problems.unique_paths import unique_paths


@pytest.mark.parametrize("m, n, expected", [
    (3, 7, 28),
    (3, 2, 3),
    (3, 3, 6),
])
def test_unique_paths(m, n, expected):
    assert unique_paths(m, n) == expected
