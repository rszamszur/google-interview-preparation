from collections import deque

import pytest
from dsa.problems.merge_binary_trees import merge_trees, TreeNode
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree1_data, tree2_data, expected", [
    ([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], [3, 4, 5, 5, 4, None, 7]),
    ([1], [1, 2], [2, 2]),
    ([1, 2, None, 3], [1, None, 2, None, 3], [2, 2, 2, 3, None, None, 3]),
])
def test_merge_trees(tree1_data, tree2_data, expected):
    root1 = recreate_binary_tree(tree1_data, TreeNode)
    root2 = recreate_binary_tree(tree2_data, TreeNode)
    result = merge_trees(root1, root2)
    expected = recreate_binary_tree(expected, TreeNode)

    queue = deque()
    queue.append((result, expected))

    while queue:
        a, b = queue.popleft()
        assert a.val == b.val

        if a.left:
            queue.append((a.left, b.left))

        if a.right:
            queue.append((a.right, b.right))
