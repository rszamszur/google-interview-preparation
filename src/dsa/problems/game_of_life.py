"""https://leetcode.com/problems/game-of-life"""
import collections
import itertools


def game_of_life(board):
    """
    Time complexity: O(n^2)
    Space complexityL O(n)

    Args:
        board(List[List[int]]): An m x n grid of cells, where each cell has an
            initial state: live (represented by a 1) or dead
            (represented by a 0).

    """
    queue = collections.deque()

    for i, row in enumerate(board):
        for j, value in enumerate(row):
            live = 0
            neighbors = itertools.product(
                range(max(0, i - 1), min(len(board), i + 2)),
                range(max(0, j - 1), min(len(row), j + 2)),
            )

            for x, y in neighbors:
                if x == i and y == j:
                    continue

                if board[x][y] == 1:
                    live += 1

            if value == 1 and live < 2:
                queue.append((i, j, 0))
            elif value == 1 and live > 3:
                queue.append((i, j, 0))
            elif value == 0 and live == 3:
                queue.append((i, j, 1))

    while queue:
        x, y, value = queue.popleft()
        board[x][y] = value
