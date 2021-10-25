"""
For a graph input one can provide either Graph object or dictionary of
lists/sets.

Example usage:
from dsa.graph import Graph


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

bfs = bfs(graph, "a")

"""
from collections import deque


def bfs(graph, start):
    """Graph breadth first search algorithm implementation.

    Time complexity: O(V + E) where V: vertices, E: edges.
    Space complexity: O(V)

    Args:
        graph(dict or Graph): Dictionary of set values.
        start(Any): Start vertex.

    Returns:
        Breadth first search nodes set.

    """
    bfs = [start]
    visited = set([start])
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                bfs.append(neighbor)
                queue.append(neighbor)

    return bfs
