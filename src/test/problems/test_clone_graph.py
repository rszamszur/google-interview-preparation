from collections import deque

from src.dsa.problems.clone_graph import clone_graph, Node


def test_clone_graph():
    v2 = Node(2)
    v3 = Node(3)
    v4 = Node(4)
    root = Node(1, neighbors=[v2, v4])
    v2.neighbors = [root, v3]
    v3.neighbors = [v2, v4]
    v4.neighbors = [root, v3]

    copy = clone_graph(root)

    queue = deque([copy])
    visited = set([copy])
    order = [1, 2, 3, 4]

    while queue:
        vertex = queue.popleft()
        assert vertex.val in order
        order.remove(vertex.val)

        for neighbor in vertex.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    assert len(order) == 0
