from dsa.tree.traversal.preorder import (
    PreorderBinaryTree,
    PreorderGeneralTree
)


def test_preorder_binary_tree(binary_tree):
    preorder = [0, 1, 3, 7, 8, 4, 2, 5, 9, 10, 6]
    for i, node in enumerate(PreorderBinaryTree(binary_tree)):
        assert node.index == preorder[i]


def test_preorder_general_tree(general_tree):
    preorder = [0, 1, 4, 5, 2, 6, 7, 3, 8, 10, 11, 9]
    for i, node in enumerate(PreorderGeneralTree(general_tree)):
        assert node.index == preorder[i]