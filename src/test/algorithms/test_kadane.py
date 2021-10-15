import pytest
from dsa.algorithms.kadane import kadane


@pytest.mark.parametrize("array, expected", [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([-2, 1], 1),
    ([10, 11, -20, 100], 101),
    ([1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1], 2),
])
def test_kadane(array, expected):
    assert kadane(array) == expected
