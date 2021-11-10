import pytest
from dsa.problems.longest_string_chain import longest_string_chain


@pytest.mark.parametrize("words, expected", [
    (["a", "b", "ba", "bca", "bda", "bdca"], 4),
    (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
    (["abcd", "dbqca"], 1),
    (["a", "b", "ba", "bca", "bda", "bdca"], 4),
    (["a", "ab", "ac", "bd", "abc", "abd", "abdd"], 4),
    (["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx",
      "zcpzvh", "zczvh", "gr", "grukmj", "ksqvsq", "gruj", "kssq", "ksqsq",
      "grukkmj", "grukj", "zczpzfvdhx", "gru"], 7),
])
def test_longest_string_chain(words, expected):
    assert longest_string_chain(words) == expected
