import pytest
from dsa.problems.validate_bst import (
    validate_bst,
    TreeNode
)
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data, expected", [
    ([2, 1, 3], True),
    ([5, 1, 4, None, None, 3, 6], False),
    ([2, 2, 2], False),
])
def test_validate_bst(tree_data, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert validate_bst(root) == expected
