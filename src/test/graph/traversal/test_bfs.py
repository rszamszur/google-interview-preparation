from dsa.graph.traversal import bfs


def test_bfs(directed_graph, undirected_graph):
    expected = ["a", "s", "z", "x", "d", "c", "f", "v"]
    assert sorted(bfs(directed_graph, "a")) == sorted(expected)
    assert sorted(bfs(undirected_graph, "a")) == sorted(expected)
    assert sorted(bfs(undirected_graph, "v")) == sorted(expected)
    assert sorted(bfs(directed_graph, "v")) == ["v"]
    assert sorted(bfs(directed_graph, "d")) == ["c", "d", "f", "v"]
