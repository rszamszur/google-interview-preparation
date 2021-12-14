import pytest
from dsa.problems.letter_tile_possibilities import letter_tile_possibilities


@pytest.mark.parametrize("tiles, expected", [
    ("AAB", 8),
    ("A", 1),
    ("AAABBC", 188),
])
def test_letter_tile_possibilities(tiles, expected):
    assert letter_tile_possibilities(tiles) == expected
