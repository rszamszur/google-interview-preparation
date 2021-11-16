import pytest
from dsa.problems.count_complete_tree_node import count_nodes, TreeNode
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data, expected", [
    ([1,2,3,4,5,6], 6),
    ([3, 3, None, 4, 2], 4),
    ([3, 1, 4, 3, None, 1, 5], 6),
    ([1], 1),
])
def test_count_nodes(tree_data, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert count_nodes(root) == expected
