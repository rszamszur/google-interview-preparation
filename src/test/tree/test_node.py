from dsa.tree.node import (TreeNode, BinaryTreeNode, GeneralTreeNode)


def test_tree_node():
    node = TreeNode(kwarg1="test", kwarg2=2, name="TreeNode", obj=TreeNode())
    assert node.kwarg1 == "test"
    assert node.kwarg2 == 2
    assert node.name == "TreeNode"
    assert isinstance(node.obj, TreeNode)
    node_eval = eval(repr(node))
    assert node.kwarg1 == node_eval.kwarg1
    assert node.kwarg2 == node_eval.kwarg2
    assert node.name == node_eval.name
    assert isinstance(node.obj, TreeNode) == isinstance(node_eval.obj, TreeNode)


def test_binary_tree_node():
    node = BinaryTreeNode(
        left=0,
        right= 1,
        kwarg1="test",
        kwarg2=2,
        name="BinaryTreeNode",
        obj=TreeNode()
    )
    assert node.left == 0
    assert node.right == 1
    assert node.kwarg1 == "test"
    assert node.kwarg2 == 2
    assert node.name == "BinaryTreeNode"
    assert isinstance(node.obj, TreeNode)
    node_eval = eval(repr(node))
    assert node.left == node_eval.left
    assert node.right == node_eval.right
    assert node.kwarg1 == node_eval.kwarg1
    assert node.kwarg2 == node_eval.kwarg2
    assert node.name == node_eval.name
    assert isinstance(node.obj, TreeNode) == isinstance(node_eval.obj, TreeNode)


def test_general_tree_node():
    node = GeneralTreeNode(
        parent=0,
        children=[],
        kwarg1="test",
        kwarg2=2,
        name="BinaryTreeNode",
        obj=TreeNode()
    )
    assert node.parent == 0
    assert node.children == []
    assert node.kwarg1 == "test"
    assert node.kwarg2 == 2
    assert node.name == "BinaryTreeNode"
    assert isinstance(node.obj, TreeNode)
    node_eval = eval(repr(node))
    assert node.parent == node_eval.parent
    assert node.children == node_eval.children
    assert node.kwarg1 == node_eval.kwarg1
    assert node.kwarg2 == node_eval.kwarg2
    assert node.name == node_eval.name
    assert isinstance(node.obj, TreeNode) == isinstance(node_eval.obj, TreeNode)
