import pytest
from dsa.problems.serialize_and_deserialize_binary_tree import Codec, TreeNode
from .utils import recreate_binary_tree, assert_trees_equal


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

    assert_trees_equal(root, deserialized)
