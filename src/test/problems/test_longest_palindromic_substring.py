import pytest
from dsa.problems.longest_palindromic_substring import longest_palindrome


@pytest.mark.parametrize("s, expected", [
    ("abb", "bb"),
    ("ccd", "cc"),
    ("babad", "bab"),
    ("a", "a"),
    ("cbbd", "bb"),
    ("xyzmaamabc", "maam"),
    ("aacabdkacaa", "aca"),
])
def test_longest_palindrome(s, expected):
    assert longest_palindrome(s) == expected
