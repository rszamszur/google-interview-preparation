from src.dsa.graph import bfs_shortest_path


def test_bfs_shortest_path(directed_graph, undirected_graph):
    result = bfs_shortest_path(directed_graph, "x", "f")
    assert result == ["x", "d", "f"] or result == ["x", "c", "f"]
    result = bfs_shortest_path(undirected_graph, "x", "f")
    assert result == ["x", "d", "f"] or result == ["x", "c", "f"]
    assert bfs_shortest_path(directed_graph, "a", "z") == ["a", "z"]
    assert bfs_shortest_path(undirected_graph, "a", "z") == ["a", "z"]
    assert bfs_shortest_path(directed_graph, "z", "a") == None
    assert bfs_shortest_path(undirected_graph, "z", "a") == ["z", "a"]
