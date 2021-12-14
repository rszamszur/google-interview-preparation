import pytest
from dsa.problems.sort_characters_by_frequency import frequency_sort


@pytest.mark.parametrize("s, expected", [
    ("tree", "eetr"),
    ("cccaaa", "cccaaa"),
    ("Aabb", "bbAa"),
])
def test_frequency_sort(s, expected):
    assert frequency_sort(s) == expected
