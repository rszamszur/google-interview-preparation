import pytest
from dsa.problems.min_refuel_stops import min_refuel_stops


@pytest.mark.parametrize("target, fuel, stations, expected", [
    (1, 1, [], 0),
    (100, 1, [[10,100]], -1),
    (100, 10, [[10,60],[20,30],[30,30],[60,40]], 2)
])
def test_min_refuel_stops(target, fuel, stations, expected):
    assert min_refuel_stops(target, fuel, stations) == expected
