import pytest
from dsa.problems.binary_tree_inorder_traversal import (
    inorder_traversal,
    TreeNode
)
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data, expected", [
    ([1, None, 2, 3], [1, 3, 2]),
    ([1], [1]),
    ([1, 2, 3, 4, 5, None, None], [4, 2, 5, 1, 3])
])
def test_inorder_traversal(tree_data, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert inorder_traversal(root) == expected
