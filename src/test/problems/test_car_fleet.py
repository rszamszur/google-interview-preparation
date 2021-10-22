import pytest
from dsa.problems.car_fleet import car_fleet


@pytest.mark.parametrize("target, position, speed, expected", [
    (12, [10,8,0,5,3], [2,4,1,1,3], 3),
    (10, [3], [3], 1),
    (10, [8,3,7,4,6,5], [4,4,4,4,4,4], 6),
])
def test_car_fleet(target, position, speed, expected):
    assert car_fleet(target, position, speed) == expected
