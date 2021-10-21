import pytest
from dsa.problems.lonley_nodes import lonley_nodes, TreeNode


@pytest.mark.parametrize("recreate_binary_tree, expected", [
    (([1, 2, 3, None, 4], TreeNode), [4]),
    (([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2], TreeNode), [6,2]),
    (([11, 99, 88, 77, None, None, 66, 55, None, None, 44, 33, None, None, 22], TreeNode), [77,66,55,44,33,22]),
    (([197], TreeNode), []),
    (([31, None, 78, None, 28], TreeNode), [78,28]),
], indirect=["recreate_binary_tree"])
def test_lonley_nodes(recreate_binary_tree, expected):
    assert lonley_nodes(recreate_binary_tree) == expected
