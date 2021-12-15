import pytest
from dsa.problems.binary_tree_postorder_traversal import (
    postorder_traversal,
    TreeNode
)
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data, expected", [
    ([1, None, 2, 3], [3, 2, 1]),
    ([1], [1]),
    ([1, 2, 3, 4, 5, None, None], [4, 5, 2, 3, 1])
])
def test_postorder_traversal(tree_data, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert postorder_traversal(root) == expected
