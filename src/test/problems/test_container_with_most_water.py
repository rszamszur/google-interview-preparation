import pytest
from dsa.problems.container_with_most_water import max_area


@pytest.mark.parametrize("height, expected", [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1),
    ([4,3,2,1,4], 16),
    ([1,2,1], 2),
    ([2,3,10,5,7,8,9], 36),
])
def test_container_with_most_water(height, expected):
    assert max_area(height) == expected
