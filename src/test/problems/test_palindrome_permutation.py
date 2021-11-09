import pytest
from dsa.problems.palindrome_permutation import palindrome_permutation


@pytest.mark.parametrize("s, expected", [
    ("code", False),
    ("ccd", True),
    ("carerac", True),
    ("aabbccc", True),
    ("aacabdkacaa", False),
])
def test_palindrome_permutation(s, expected):
    assert palindrome_permutation(s) == expected
