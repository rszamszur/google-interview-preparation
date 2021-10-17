from dsa.tree.traversal.postorder import (
    PostorderBinaryTree,
    PostorderGeneralTree
)


def test_postorder_binary_tree(binary_tree):
    postorder = [7, 8, 3, 4, 1, 9, 10, 5, 6, 2, 0]
    for i, node in enumerate(PostorderBinaryTree(binary_tree)):
        assert node.index == postorder[i]


def test_postorder_general_tree(general_tree):
    postorder = [4, 5, 1, 6, 7, 2, 10, 11, 8, 9, 3, 0]
    for i, node in enumerate(PostorderGeneralTree(general_tree)):
        assert node.index == postorder[i]
