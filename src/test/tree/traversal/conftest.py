import pytest
from dsa.tree.node import (BinaryTreeNode, GeneralTreeNode)


@pytest.fixture
def binary_tree():
    root = BinaryTreeNode(index=0)
    root.left = BinaryTreeNode(index=1)
    root.right = BinaryTreeNode(index=2)
    root.left.left = BinaryTreeNode(index=3)
    root.left.right = BinaryTreeNode(index=4)
    root.right.left = BinaryTreeNode(index=5)
    root.right.right = BinaryTreeNode(index=6)
    root.left.left.left = BinaryTreeNode(index=7)
    root.left.left.right = BinaryTreeNode(index=8)
    root.right.left.left = BinaryTreeNode(index=9)
    root.right.left.right = BinaryTreeNode(index=10)
    yield root


@pytest.fixture
def general_tree():
    root = GeneralTreeNode(children=[], index=0)
    for i in range(1, 4):
        root.children.append(
            GeneralTreeNode(parent=root, children=[], index=i)
        )
    for i in range(4, 6):
        root.children[0].children.append(
            GeneralTreeNode(parent=root.children[0], children=[], index=i)
        )
    for i in range(6, 8):
        root.children[1].children.append(
            GeneralTreeNode(parent=root.children[1], children=[], index=i)
        )
    root.children[2].children.append(
        GeneralTreeNode(parent=root.children[2], children=[], index=8)
    )
    root.children[2].children.append(
        GeneralTreeNode(parent=root.children[2], children=[], index=9)
    )
    root.children[2].children[0].children.append(
        GeneralTreeNode(parent=root.children[2].children[0], children=[], index=10)
    )
    root.children[2].children[0].children.append(
        GeneralTreeNode(parent=root.children[2].children[0], children=[], index=11)
    )
    yield root
