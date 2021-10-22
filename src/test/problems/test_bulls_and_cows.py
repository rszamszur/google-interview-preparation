import pytest
from dsa.problems.bulls_and_cows import get_hint, get_hint_one_pass


@pytest.mark.parametrize("secret, guess, expected", [
    ("1807", "7810", "1A3B"),
    ("1123", "0111", "1A1B"),
    ("1", "0", "0A0B"),
    ("1", "1", "1A0B"),
    ("1122","2211", "0A4B"),
    ("11", "10", "1A0B"),
])
def test_bulls_and_cows(secret, guess, expected):
    assert get_hint(secret, guess) == expected
    assert get_hint_one_pass(secret, guess) == expected
