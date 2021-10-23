from collections import deque

import pytest
from dsa.problems.serialize_and_deserialize_binary_tree import Codec, TreeNode
from .utils import recreate_binary_tree


@pytest.mark.parametrize("tree_data", [
    [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2],
    [1,2,3,None,None,4,5],
    [1,2,3]
])
def test_serialize_and_deserialize_binary_tree(tree_data):
    root = recreate_binary_tree(tree_data, TreeNode)
    codec = Codec()
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)

    queue = deque()
    queue.append((root, deserialized))

    while queue:
        a, b = queue.popleft()
        assert a.val == b.val

        if a.left:
            queue.append((a.left, b.left))

        if a.right:
            queue.append((a.right, b.right))
