"""https://leetcode.com/problems/unique-paths/submissions"""
from math import factorial


def unique_paths(m, n):
    """
    Time complexity: O(1)
    Space complexity: O(1)

    Args:
        m(int): First dimension of matrix.
        n(int): Second dimension of matrix.

    Returns:
        Possible unique paths.

    """
    return factorial((m - 1) + (n - 1)) / (factorial(m - 1) * factorial(n - 1))
