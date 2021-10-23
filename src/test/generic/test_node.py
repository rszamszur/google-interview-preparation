from dsa.generic import Node


def test_node():
    node = Node(kwarg1="test", kwarg2=2, name="Node", obj=Node())
    assert node.kwarg1 == "test"
    assert node.kwarg2 == 2
    assert node.name == "Node"
    assert isinstance(node.obj, Node)
    node_eval = eval(repr(node))
    assert node.kwarg1 == node_eval.kwarg1
    assert node.kwarg2 == node_eval.kwarg2
    assert node.name == node_eval.name
    assert isinstance(node.obj, Node) == isinstance(node_eval.obj, Node)
