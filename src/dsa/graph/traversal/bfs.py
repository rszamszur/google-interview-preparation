from collections import deque


def breadth_first_search(graph, start):
    """Graph breadth first search algorithm implementation.

    Time complexity: O(V + E) where V: vertices, E: edges.
    Space complexity: O(V)

    Args:
        graph(dict): Dictionary of set values.
        start(any): Start vertex.

    Returns:
        Breadth first search nodes set.

    """
    explored = set()
    queue = deque
    queue.append(start)
    explored.add(start)

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in explored:
                explored.add(neighbor)
                queue.append(neighbor)

    return explored
