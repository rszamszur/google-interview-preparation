"""https://leetcode.com/problems/clone-graph"""
import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    """
    Time complexity: O(V + E) where V: vertices, E: edges.
    Space complexity: O(V)

    Args:
        node(Node): A node in a connected undirected graph.

    Returns:
        A deep copy of the graph.

    """
    if not node:
        return None

    ht = dict()
    queue = collections.deque([node])
    visited = set([node])

    while queue:
        vertex = queue.popleft()
        if vertex.val not in ht:
            ht[vertex.val] = Node(vertex.val)

        for neighbor in vertex.neighbors:
            if neighbor.val not in ht:
                ht[neighbor.val] = Node(neighbor.val)

            ht[vertex.val].neighbors.append(
                ht[neighbor.val]
            )

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return ht[node.val]
