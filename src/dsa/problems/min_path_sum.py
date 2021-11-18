"""https://leetcode.com/problems/minimum-path-sum"""
import heapq


def min_path_sum_dp(grid):
    """Solution using dynamic programming.

    Time complexity: O(m * n)
    Space complexity: O(1)

    Args:
        grid(List[List[int]]): Matrix m x n filled with non-negative integers.

    Returns:
        Minimal sum of all numbers of a path (One can only move either down or
        right at any point in time) from top left to bottom right.

    """
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if x > 0 and y > 0:
                grid[x][y] = min(
                    grid[x][y] + grid[x - 1][y],
                    grid[x][y] + grid[x][y - 1]
                )
            elif x > 0:
                grid[x][y] = grid[x][y] + grid[x - 1][y]
            elif y > 0:
                grid[x][y] = grid[x][y] + grid[x][y - 1]

    return grid[len(grid) - 1][len(grid[0]) - 1]


def min_path_sum_djikstra(grid):
    """Solution using Djikstra algorithm.

    Time complexity: O(V + E) where V: vertices, E: edges.
    Space complexity: O(V)

    Args:
        grid(List[List[int]]): Matrix m x n filled with non-negative integers.

    Returns:
        Minimal sum of all numbers of a path (One can only move either down or
        right at any point in time) from top left to bottom right.

    """
    heap = [(grid[0][0], 0, 0)]

    while heap:
        cost, x, y = heapq.heappop(heap)

        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return cost

        if x < len(grid) - 1:
            heapq.heappush(heap, (cost + grid[x + 1][y], x + 1, y))
        if y < len(grid[0]) - 1:
            heapq.heappush(heap, (cost + grid[x][y + 1], x, y + 1))
