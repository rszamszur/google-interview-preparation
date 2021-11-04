import pytest
from dsa.problems.delete_tree_nodes import delete_tree_nodes, TreeNode
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data, to_delete, expected", [
    ([1, 3, 2, None, 6, 4, None, None, None, 5], [2, 5, 3], [6, 4, 1]),
    ([1, 2, 3, 4, 5, 6, 7], [3, 5], [6, 7, 1, 2, None, 4]),
    ([1, 2, 4, None, 3], [3], [1, 2, 4]),
])
def test_delete_tree_nodes(tree_data, to_delete, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    for node in delete_tree_nodes(root, to_delete):
        assert node.val == expected.pop(0)
