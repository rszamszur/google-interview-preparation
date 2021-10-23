from dsa.graph.node import GraphNode


def test_graph_node():
    neighbors = set()
    neighbors.add(GraphNode(name="Neighbor"))
    node = GraphNode(
        neighbors=neighbors,
        kwarg1="test",
        kwarg2=2,
        name="GraphNode",
        obj=GraphNode()
    )
    assert node.kwarg1 == "test"
    assert node.kwarg2 == 2
    assert node.name == "GraphNode"
    assert len(node.neighbors) == 1
    for item in node.neighbors:
        assert isinstance(item, GraphNode)
        assert item.name == "Neighbor"
    assert isinstance(node.obj, GraphNode)
    node_eval = eval(repr(node))
    assert node.kwarg1 == node_eval.kwarg1
    assert node.kwarg2 == node_eval.kwarg2
    assert node.name == node_eval.name
    assert isinstance(node.obj, GraphNode) == isinstance(node_eval.obj, GraphNode)
    for item in node_eval.neighbors:
        assert isinstance(item, GraphNode)
        assert item.name == "Neighbor"