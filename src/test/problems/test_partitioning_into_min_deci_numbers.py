import pytest
from dsa.problems.partitioning_into_min_deci_numbers import min_partitions


@pytest.mark.parametrize("n, expected", [
    ("32", 3),
    ("82734", 8),
    ("27346209830709182346", 9),
])
def test_min_partitions(n, expected):
    assert min_partitions(n) == expected
