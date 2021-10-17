from dsa.tree.traversal.breadth_first import (
    BreadthFirstBinaryTree,
    BreadthFirstGeneralTree,
)
from dsa.tree.node import GeneralTreeNode


def test_breadth_first_binary_tree(binary_tree):
    breadth_first = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i, node in enumerate(BreadthFirstBinaryTree(binary_tree)):
        assert node.index == breadth_first[i]


def test_breadth_first_general_tree(general_tree):
    breadth_first = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for i, node in enumerate(BreadthFirstGeneralTree(general_tree)):
        assert node.index == breadth_first[i]
