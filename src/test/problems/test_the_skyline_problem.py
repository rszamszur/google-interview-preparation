import pytest
from src.dsa.problems.the_skyline_problem import get_skyline


@pytest.mark.parametrize("buildings, expected", [
    ([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]], [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]),
    ([[0,2,3],[2,5,3]], [[0,3],[5,0]]),
])
def test_get_skyline(buildings, expected):
    assert get_skyline(buildings) == expected
