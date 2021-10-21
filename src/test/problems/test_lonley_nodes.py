import pytest
from dsa.problems.lonley_nodes import lonley_nodes, TreeNode
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data, expected", [
    ([1, 2, 3, None, 4], [4]),
    ([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2], [6,2]),
    ([11, 99, 88, 77, None, None, 66, 55, None, None, 44, 33, None, None, 22], [77,66,55,44,33,22]),
    ([197], []),
    ([31, None, 78, None, 28], [78,28]),
])
def test_lonley_nodes(tree_data, expected):
    root = recreate_binary_tree(tree_data, TreeNode)
    assert lonley_nodes(root) == expected
