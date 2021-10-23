from dsa.tree.node import (BinaryTreeNode, GeneralTreeNode)


def test_binary_tree_node():
    node = BinaryTreeNode(
        left=0,
        right= 1,
        kwarg1="test",
        kwarg2=2,
        name="BinaryTreeNode",
        obj=BinaryTreeNode()
    )
    assert node.left == 0
    assert node.right == 1
    assert node.kwarg1 == "test"
    assert node.kwarg2 == 2
    assert node.name == "BinaryTreeNode"
    assert isinstance(node.obj, BinaryTreeNode)
    node_eval = eval(repr(node))
    assert node.left == node_eval.left
    assert node.right == node_eval.right
    assert node.kwarg1 == node_eval.kwarg1
    assert node.kwarg2 == node_eval.kwarg2
    assert node.name == node_eval.name
    assert isinstance(node.obj, BinaryTreeNode) == isinstance(node_eval.obj, BinaryTreeNode)


def test_general_tree_node():
    node = GeneralTreeNode(
        parent=0,
        children=[],
        kwarg1="test",
        kwarg2=2,
        name="GeneralTreeNode",
        obj=GeneralTreeNode()
    )
    assert node.parent == 0
    assert node.children == []
    assert node.kwarg1 == "test"
    assert node.kwarg2 == 2
    assert node.name == "GeneralTreeNode"
    assert isinstance(node.obj, GeneralTreeNode)
    node_eval = eval(repr(node))
    assert node.parent == node_eval.parent
    assert node.children == node_eval.children
    assert node.kwarg1 == node_eval.kwarg1
    assert node.kwarg2 == node_eval.kwarg2
    assert node.name == node_eval.name
    assert isinstance(node.obj, GeneralTreeNode) == isinstance(node_eval.obj, GeneralTreeNode)
