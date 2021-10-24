import pytest
from dsa.graph import Graph


@pytest.fixture()
def undirected_graph():
    graph = Graph(directed=False)
    graph.add_edge("a", "z")
    graph.add_edge("a", "s")
    graph.add_edge("s", "x")
    graph.add_edge("x", "d")
    graph.add_edge("x", "c")
    graph.add_edge("d", "c")
    graph.add_edge("d", "f")
    graph.add_edge("c", "f")
    graph.add_edge("c", "v")
    graph.add_edge("f", "v")

    yield graph


@pytest.fixture
def directed_graph():
    graph = Graph(directed=True)
    graph.add_edge("a", "z")
    graph.add_edge("a", "s")
    graph.add_edge("s", "x")
    graph.add_edge("x", "d")
    graph.add_edge("x", "c")
    graph.add_edge("d", "c")
    graph.add_edge("d", "f")
    graph.add_edge("c", "f")
    graph.add_edge("c", "v")
    graph.add_edge("f", "v")

    yield graph
