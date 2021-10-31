"""https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

Examples:

graph = {
    "A": [["B", 2], ["C", 5]],
    "B": [["A", 2], ["D", 3], ["E", 1], ["F", 1]],
    "C": [["A", 5], ["F", 3]],
    "D": [["B", 3]],
    "E": [["B", 4], ["F", 3]],
    "F": [["C", 3], ["E", 3]],
}
# E -- 3 --> F -- 3 --> C == 6
shortest_path = dijkstra(graph, "E", "C")

"""
import heapq


def dijkstra(graph, start, end):
    """Dijkstra algorithm implementation.

    Time complexity: O(V + E) where V: vertices, E: edges.
    Space complexity: O(V)

    Args:
        graph(dict): Dictionary of set values.
        start(Any): Start vertex.
        end(Any): Destination vertex.

    Returns:
        The cost of the shortest path between vertices start and end.

    """
    heap = [(0, start)]
    visited = set()

    while heap:
        cost, u = heapq.heappop(heap)

        if u in visited:
            continue

        visited.add(u)
        if u == end:
            return cost

        for v, c in graph[u]:
            if v not in visited:
                heapq.heappush(heap, (cost + c, v))

    return None
