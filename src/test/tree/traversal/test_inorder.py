from dsa.tree.traversal.inorder import (
    InorderBinaryTree,
    InorderGeneralTree
)
from dsa.tree.node import GeneralTreeNode


def test_inorder_binary_tree(binary_tree):
    inorder = [7, 3, 8, 1, 4, 0, 9, 5, 10, 2, 6]
    for i, node in enumerate(InorderBinaryTree(binary_tree)):
        assert node.index == inorder[i]


def test_inorder_general_tree(general_tree):
    inorder = [4, 1, 5, 6, 2, 7, 0, 10, 8, 11, 3, 9]
    for i, node in enumerate(InorderGeneralTree(general_tree)):
        assert node.index == inorder[i]
