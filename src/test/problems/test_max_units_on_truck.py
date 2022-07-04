import pytest
from dsa.problems.max_units_on_truck import maximum_units


@pytest.mark.parametrize("box_types, truck_size, expected", [
    ([[1, 3], [2, 2], [3, 1]], 4, 8),
    ([[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91),
    ([[1, 3], [5, 5], [2, 5], [4, 2], [4, 1], [3, 1], [2, 2], [1, 3], [2, 5], [3, 2]], 35, 76),
])
def test_maximum_units(box_types, truck_size, expected):
    assert maximum_units(box_types, truck_size) == expected
