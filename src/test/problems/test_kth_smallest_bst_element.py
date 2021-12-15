import pytest
from dsa.problems.kth_smallest_bst_element import (
    kth_smallest,
    TreeNode
)
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data, k, expected", [
    ([3, 1, 4, None , 2], 1, 1),
    ([5, 3, 6, 2, 4, None, None, 1], 3, 3)
])
def test_kth_smallest(tree_data, k, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert kth_smallest(root, k) == expected
