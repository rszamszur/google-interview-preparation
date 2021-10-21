import pytest
from dsa.problems.find_leaves_of_binary_tree import (
    TreeNode,
    find_leaves_with_bfs,
    find_leaves_with_height
)
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data, expected", [
    ([1, 2, 3, 4, 5], [[3, 4, 5], [2], [1]]),
    ([1], [[1]]),
])
def test_find_leaves_with_bfs(tree_data, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert find_leaves_with_bfs(root) == expected


@pytest.mark.parametrize("tree_data, expected", [
    ([1, 2, 3, 4, 5], [[4, 5, 3], [2], [1]]),
    ([1], [[1]]),
])
def test_find_leaves_with_height(tree_data, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert find_leaves_with_height(root) == expected
