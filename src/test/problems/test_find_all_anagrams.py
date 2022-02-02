import pytest
from dsa.problems.find_all_anagrams import find_all_anagrams


@pytest.mark.parametrize("s, p, expected", [
    ("af", "be", []),
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2]),
])
def test_fibonacci(s, p, expected):
    assert find_all_anagrams(s, p) == expected
