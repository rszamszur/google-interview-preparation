import pytest
from dsa.tree.bst import BinarySearchTree


@pytest.fixture
def bst():
    bst = BinarySearchTree()
    for item in [15, 10, 20, 8, 12, 18, 25, 16, 19, 30]:
        bst.insert(item)

    yield bst


def test_insert():
    bst = BinarySearchTree()
    bst.insert(49)
    bst.insert(79)
    bst.insert(46)
    bst.insert(41)
    bst.insert(64)
    # I'm asserting wheter structure in breadth first order is correct
    assert str(bst) == "[49, 46, 79, 41, 64]"


def test_delete(bst):
    # Delete node with one child
    bst.delete(25)
    assert not bst.find(25)
    assert str(bst) == "[15, 10, 20, 8, 12, 18, 30, 16, 19]"
    # delete leaf node
    bst.delete(19)
    assert not bst.find(19)
    assert str(bst) == "[15, 10, 20, 8, 12, 18, 30, 16]"
    # Delete node with two childs 2x
    bst.delete(20)
    assert not bst.find(20)
    assert str(bst) == "[15, 10, 16, 8, 12, 18, 30]"
    bst.delete(16)
    assert not bst.find(20)
    assert str(bst) == "[15, 10, 18, 8, 12, 30]"


def test_find(bst):
    assert not bst.find(404)
    assert bst.find(15)
    assert bst.find(8)
    assert bst.find(19)
    assert bst.find(16)


def test_min(bst):
    assert bst.min().key == 8
    bst.delete(8)
    assert bst.min().key == 10
    bst.delete(10)
    assert bst.min().key == 12


def test_max(bst):
    assert bst.max().key == 30
    bst.delete(30)
    assert bst.max().key == 25
    bst.delete(25)
    assert bst.max().key == 20


def test_breadth_first(bst):
    order = [15, 10, 20, 8, 12, 18, 25, 16, 19, 30]
    for item in bst:
        assert item.key == order[0]
        order.pop(0)


def test_inorder(bst):
    order = [8, 10, 12, 15, 16, 18, 19, 20, 25, 30]
    for item in bst.inorder():
        assert item.key == order[0]
        order.pop(0)


def test_postorder(bst):
    order = [8, 12, 10, 16, 19, 18, 30, 25, 20, 15]
    for item in bst.postorder():
        assert item.key == order[0]
        order.pop(0)


def test_preorder(bst):
    order = [15, 10, 8, 12, 20, 18, 16, 19, 25, 30]
    for item in bst.preorder():
        assert item.key == order[0]
        order.pop(0)
