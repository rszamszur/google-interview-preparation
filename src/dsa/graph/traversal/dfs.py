"""
For a graph input one can provide either Graph object or dictionary of
lists/sets.

Examples:
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

dfs = dfs(graph, "a")

"""
from collections import deque


def dfs(graph, start):
    """Graph depth first search algorithm implementation.

    Time complexity: O(V + E) where V: vertices, E: edges.
    Space complexity: O(V)

    Args:
        graph(dict or Graph): Dictionary of set values.
        start(Any): Start vertex.

    Returns:
        Depth first search nodes.

    """
    dfs = []
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            dfs.append(vertex)
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return dfs
