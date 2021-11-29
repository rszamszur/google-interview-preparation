"""https://leetcode.com/problems/accounts-merge"""
from collections import defaultdict, deque


def accounts_merge(accounts):
    """
    Time complexity: O(n * (n * log(n))
    Space complexity: O(n)

    Args:
        accounts(List[List[str]]): Each element accounts[i] is a list of
            strings, where the first element accounts[i][0] is a name, and the
            rest of the elements are emails representing emails of the account.

    Returns:
        Merged accounts in the following format: the first element of each
        account is the name, and the rest of the elements are emails in sorted
        order.

    """
    graph = defaultdict(set)

    for acc in accounts:
        name = acc[0]

        for email in acc[1:]:
            key = "{0:s}::{1:s}".format(name, email)

            if key not in graph:
                graph[key] = set()

            graph[key].update(
                ["{0:s}::{1:s}".format(name, e) for e in acc[1:] if e != email]
            )

    merged = []
    visited = set()

    for node in graph:
        if node in visited:
            continue

        visited.add(node)
        name, email = node.split("::")
        merged.append(["A", email])
        queue = deque([node])

        while queue:
            vertex = queue.popleft()

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    merged[-1].append(neighbor.split("::")[1])

        merged[-1].sort()
        merged[-1][0] = name

    return merged
