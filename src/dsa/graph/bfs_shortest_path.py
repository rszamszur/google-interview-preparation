"""
Example:
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

path = bfs_shortest_path(graph, "x", "f")

"""
from collections import deque


def bfs_shortest_path(graph, start, target):
    """Graph bfs shortest path algorithm implementation.

    Time complexity: O(V + E) where V: vertices, E: edges.
    Space complexity: O(V^2)

    Args:
        graph(dict): Dictionary of set values.
        start(any): Start vertex.

    Returns:
        Breadth first search nodes set.

    """
    if start == target:
        return [start]

    visited = set([start])
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                if neighbor == target:
                    return new_path

                visited.add(neighbor)
                queue.append(new_path)

    return None
