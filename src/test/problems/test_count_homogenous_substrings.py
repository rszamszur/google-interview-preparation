import pytest
from dsa.problems.count_homogenous_substrings import count_homogenous_substrings


@pytest.mark.parametrize("s, expected", [
    ("abbcccaa", 13),
    ("xy", 2),
    ("zzzzz", 15),
    ("aaabbbccc", 18),
])
def test_count_homogenous_substrings(s, expected):
    assert count_homogenous_substrings(s) == expected
