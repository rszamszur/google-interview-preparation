"""An example of Graph represenation using adjacency list implemented with
dictionary of lists/sets."""
from dsa.graph import Graph, bfs_shortest_path
from dsa.graph.traversal import bfs


# Using just dictionary
graph = {
    'a': {'z', 's'},
    'z': {'a'},
    's': {'x', 'a'},
    'x': {'d', 'c', 's'},
    'd': {'f', 'c', 'x'},
    'c': {'d', 'v', 'x', 'f'},
    'f': {'d', 'c', 'v'},
    'v': {'f', 'c'}
}

print(bfs(graph, "a"))
print(bfs_shortest_path(graph, "x", "f"))

# Using custom Graph class implementation
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

print(graph)
print(bfs(graph, "a"))
print(bfs_shortest_path(graph, "x", "f"))
