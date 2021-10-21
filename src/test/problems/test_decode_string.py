import pytest
from dsa.problems.decode_string import decode_string


@pytest.mark.parametrize("string, expected", [
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ("abc3[cd]xyz", "abccdcdcdxyz"),
    ("10[ab]", "abababababababababab")
])
def test_decode_string(string, expected):
    assert decode_string(string) == expected
