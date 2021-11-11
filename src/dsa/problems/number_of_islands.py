"""https://leetcode.com/problems/number-of-islands"""


def number_of_islands(grid):
    """
    Time compexity: O(m * n)
    Space complexity: O(m * n)

    Args:
        grid(List[List[str]]): Binary grid grid which represents a map of
            '1's (land) and '0's (water).

    Returns:
        The number of islands.

    """
    count = 0
    visited = set()

    for i, row in enumerate(grid):
        if "1" not in row:
            continue

        for j, value in enumerate(row):
            if (i, j) in visited or value == "0":
                continue

            stack = [(i, j)]

            while stack:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.add(vertex)

                    neighbors = []

                    if vertex[0] > 0:
                        neighbors.append((vertex[0] - 1, vertex[1]))
                    if vertex[0] < len(grid) - 1:
                        neighbors.append((vertex[0] + 1, vertex[1]))
                    if vertex[1] > 0:
                        neighbors.append((vertex[0], vertex[1] - 1))
                    if vertex[1] < len(row) - 1:
                        neighbors.append((vertex[0], vertex[1] + 1))

                    for x, y in neighbors:
                        value = grid[x][y]

                        if value == "1":
                            stack.append((x, y))

            count += 1

    return count
