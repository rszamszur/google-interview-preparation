import pytest
from dsa.problems.top_k_frequent_elements import top_k_frequent


@pytest.mark.parametrize("nums, k, expected", [
    ([1,1,1,2,2,3], 2, [1,2]),
    ([1], 1, [1]),
    ([1,1,2,3,4,55,55,55,55], 3, [55,1,2])
])
def test_top_k_frequent(nums, k, expected):
    assert top_k_frequent(nums, k) == expected
