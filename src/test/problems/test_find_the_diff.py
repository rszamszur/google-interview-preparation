import pytest
from dsa.problems.find_the_diff import find_the_diff


@pytest.mark.parametrize("s, t, expected", [
    ("abcd", "abcde", "e"),
    ("", "y", "y"),
    ("a", "aa", "a"),
])
def test_find_the_diff(s, t, expected):
    assert find_the_diff(s, t) == expected
