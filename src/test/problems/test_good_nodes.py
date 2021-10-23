import pytest
from dsa.problems.good_nodes import good_nodes, TreeNode
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data, expected", [
    ([3, 1, 4, 3, None, 1, 5], 4),
    ([3, 3, None, 4, 2], 3),
    ([1], 1),
])
def test_good_nodes(tree_data, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert good_nodes(root) == expected
