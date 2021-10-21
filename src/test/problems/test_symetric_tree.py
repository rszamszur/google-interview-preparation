import pytest
from dsa.problems.symetric_tree import is_symmetric, TreeNode


@pytest.mark.parametrize("recreate_binary_tree, expected", [
    (([1, 2, 2, 3, 4, 4, 3], TreeNode), True),
    (([1, 2, 2, None, 3, None, 3], TreeNode), False),
], indirect=["recreate_binary_tree"])
def test_is_symetric(recreate_binary_tree, expected):
    assert is_symmetric(recreate_binary_tree) == expected
