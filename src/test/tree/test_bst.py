import pytest
from dsa.tree.bst import BST
from dsa.tree.node import BinaryTreeNode


@pytest.fixture
def bst():
    bst = BST()
    for item in [15, 10, 20, 8, 12, 18, 25, 16, 19, 30]:
        bst.insert(item)

    yield bst


def test_insert():
    bst = BST()
    node = bst.insert(49)
    assert node.key == 49
    assert isinstance(node, BinaryTreeNode)
    node = bst.insert(79)
    assert node.key == 79
    assert isinstance(node, BinaryTreeNode)
    node = bst.insert(46)
    assert node.key == 46
    assert isinstance(node, BinaryTreeNode)
    node = bst.insert(41)
    assert node.key == 41
    assert isinstance(node, BinaryTreeNode)
    node = bst.insert(64)
    assert node.key == 64
    assert isinstance(node, BinaryTreeNode)
    # I'm asserting wheter structure in breadth first order is correct
    assert str(bst) == "[49, 46, 79, 41, 64]"


def test_delete(bst):
    # Delete node with one child
    node = bst.delete(25)
    assert not bst.find(25)
    assert node.key == 25
    assert isinstance(node, BinaryTreeNode)
    assert str(bst) == "[15, 10, 20, 8, 12, 18, 30, 16, 19]"
    # delete leaf node
    node = bst.delete(19)
    assert not bst.find(19)
    assert node.key == 19
    assert isinstance(node, BinaryTreeNode)
    assert str(bst) == "[15, 10, 20, 8, 12, 18, 30, 16]"
    # Delete node with two childs 2x
    node = bst.delete(20)
    assert not bst.find(20)
    assert node.key == 20
    assert isinstance(node, BinaryTreeNode)
    assert str(bst) == "[15, 10, 16, 8, 12, 18, 30]"
    node = bst.delete(16)
    assert not bst.find(16)
    assert node.key == 16
    assert isinstance(node, BinaryTreeNode)
    assert str(bst) == "[15, 10, 18, 8, 12, 30]"


def test_find(bst):
    assert not bst.find(404)
    node = bst.find(15)
    assert node.key == 15
    assert isinstance(node, BinaryTreeNode)
    node = bst.find(8)
    assert node.key == 8
    assert isinstance(node, BinaryTreeNode)
    node = bst.find(19)
    assert node.key == 19
    assert isinstance(node, BinaryTreeNode)
    node = bst.find(16)
    assert node.key == 16
    assert isinstance(node, BinaryTreeNode)


def test_min(bst):
    node = bst.min()
    assert node.key == 8
    assert isinstance(node, BinaryTreeNode)
    bst.delete(8)
    node = bst.min()
    assert node.key == 10
    assert isinstance(node, BinaryTreeNode)
    bst.delete(10)
    node = bst.min()
    assert node.key == 12
    assert isinstance(node, BinaryTreeNode)


def test_max(bst):
    node = bst.max()
    assert node.key == 30
    assert isinstance(node, BinaryTreeNode)
    bst.delete(30)
    node = bst.max()
    assert node.key == 25
    assert isinstance(node, BinaryTreeNode)
    bst.delete(25)
    node = bst.max()
    assert node.key == 20
    assert isinstance(node, BinaryTreeNode)


def test_breadth_first(bst):
    order = [15, 10, 20, 8, 12, 18, 25, 16, 19, 30]
    for node in bst:
        assert isinstance(node, BinaryTreeNode)
        assert node.key == order[0]
        order.pop(0)


def test_inorder(bst):
    order = [8, 10, 12, 15, 16, 18, 19, 20, 25, 30]
    for node in bst.inorder():
        assert isinstance(node, BinaryTreeNode)
        assert node.key == order[0]
        order.pop(0)


def test_postorder(bst):
    order = [8, 12, 10, 16, 19, 18, 30, 25, 20, 15]
    for node in bst.postorder():
        assert isinstance(node, BinaryTreeNode)
        assert node.key == order[0]
        order.pop(0)


def test_preorder(bst):
    order = [15, 10, 8, 12, 20, 18, 16, 19, 25, 30]
    for node in bst.preorder():
        assert isinstance(node, BinaryTreeNode)
        assert node.key == order[0]
        order.pop(0)
