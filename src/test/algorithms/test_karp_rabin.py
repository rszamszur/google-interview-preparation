import pytest
from dsa.algorithms.karp_rabin import karp_rabin


@pytest.mark.parametrize("pattern, string, expected", [
    ("Lelo","LeloLelo", 0),
	("Lelo","leloLelo", 4),
	("a","stiojgps", None),
	("o","stiojgps", 3),
	("g","stiojgps", 5),
	("Lelo","garbageLelogarbage", 7),
	("Ricardo", "qwerty _Ricardo_ qwerty", 8)
])
def test_karp_rabin(pattern, string, expected):
    assert karp_rabin(pattern, string) == expected