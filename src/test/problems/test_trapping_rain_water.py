import pytest
from dsa.problems.trapping_rain_water import trap


@pytest.mark.parametrize("height, expected", [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
    ([4,2,3], 1),
    ([1,2,3,4,5,4,3,3,4,2,1,0,2,3,4,5,5,4], 24)
])
def test_trap(height, expected):
    assert trap(height) == expected
