import pytest
from dsa.problems.longest_common_prefix import longest_common_prefix


@pytest.mark.parametrize("strs, expected", [
    (["flower","flow","flight"], "fl"),
    (["dog","racecar","car"], ""),
    (["alpha", "Alpha"], ""),
    (["python3", "python2.7", "python3.10"], "python"),
])
def test_longest_common_prefix(strs, expected):
    assert longest_common_prefix(strs) == expected
