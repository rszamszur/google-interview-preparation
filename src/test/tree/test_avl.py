import pytest
from dsa.tree.avl import AVL
from dsa.tree.node import BinaryTreeNode


@pytest.fixture
def avl():
    avl = AVL()
    for value in [10, 11, 12, 9, 8, 14, 13, 6, 7, 5]:
        avl.insert(value)

    yield avl


def test_insert(avl):
    bfs = [(11, 3), (7, 2), (13, 1), (6, 1), (9, 1), (12, 0), (14, 0), (5, 0),
           (8, 0), (10, 0)]

    for node in avl:
        assert node.key == bfs[0][0]
        assert node.height == bfs[0][1]
        bfs.pop(0)


def test_delete(avl):
    node = avl.delete(12)
    assert node.key == 12
    assert node.height == 0
    assert isinstance(node, BinaryTreeNode)
    node = avl.delete(14)
    assert node.key == 14
    assert node.height == 0
    assert isinstance(node, BinaryTreeNode)

    bfs = [(7, 3), (6, 1), (11, 2), (5, 0), (9, 1), (13, 0), (8, 0), (10, 0)]

    for node in avl:
        assert node.key == bfs[0][0]
        assert node.height == bfs[0][1]
        bfs.pop(0)
