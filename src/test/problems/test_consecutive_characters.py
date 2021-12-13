import pytest
from dsa.problems.consecutive_characters import consecutive_characters


@pytest.mark.parametrize("s, expected", [
    ("leetcode", 2),
    ("abbcccddddeeeeedcba", 5),
    ("triplepillooooow", 5),
    ("hooraaaaaaaaaaay", 11),
    ("tourist", 1),
])
def test_consecutive_characters(s, expected):
    assert consecutive_characters(s) == expected
