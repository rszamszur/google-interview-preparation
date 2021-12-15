import pytest
from dsa.problems.binary_tree_preorder_traversal import (
    preorder_traversal,
    TreeNode
)
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data, expected", [
    ([1, None, 2, 3], [1, 2, 3]),
    ([1], [1]),
    ([1, 2, 3, 4, 5, None, None], [1, 2, 4, 5, 3]),
])
def test_preorder_traversal(tree_data, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert preorder_traversal(root) == expected
