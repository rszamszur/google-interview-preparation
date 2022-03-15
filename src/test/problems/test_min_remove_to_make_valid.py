import pytest
from dsa.problems.min_remove_to_make_valid import min_remove_to_make_valid


@pytest.mark.parametrize("s, expected", [
    ("lee(t(c)o)de)", "lee(t(c)o)de"),
    ("a)b(c)d", "ab(c)d"),
    ("))((", ""),
])
def test_min_remove_to_make_valid(s, expected):
    assert min_remove_to_make_valid(s) == expected
