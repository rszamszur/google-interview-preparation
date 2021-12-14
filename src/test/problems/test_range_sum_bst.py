import pytest
from dsa.problems.range_sum_bst import range_sum_bst, TreeNode
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data, low, high, expected", [
    ([10,5,15,3,7,None,18], 7, 15, 32),
    ([10,5,15,3,7,13,18,1,None,6], 6 ,10, 23),
])
def test_range_sum_bst(tree_data, low, high, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert range_sum_bst(root, low, high) == expected
