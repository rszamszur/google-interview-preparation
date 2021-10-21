import pytest
from dsa.problems.symetric_tree import is_symetric, TreeNode
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data, expected", [
    ([1, 2, 2, 3, 4, 4, 3], True),
    ([1, 2, 2, None, 3, None, 3], False),
])
def test_is_symetric(tree_data, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert is_symetric(root) == expected
