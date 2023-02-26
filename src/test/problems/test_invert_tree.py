import pytest
from dsa.problems.invert_tree import invert_tree, TreeNode
from .utils import recreate_binary_tree, assert_trees_equal


@pytest.mark.parametrize("tree_data, expected", [
    ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
    ([2,1,3], [2,3,1]),
])
def test_invert_tree(tree_data, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert_trees_equal(
        invert_tree(root), recreate_binary_tree(expected, TreeNode)
    )
