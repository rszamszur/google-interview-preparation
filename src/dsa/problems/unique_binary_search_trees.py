"""https://leetcode.com/problems/unique-binary-search-trees"""
import math


def num_trees(n):
    """
    Solved with math using Catalan number:
    https://en.wikipedia.org/wiki/Catalan_number
    Time complexity: O(1)
    Space complexity: O(1)

    Args:
        n(int): Integer n.

    Returns:
        The number of structurally unique binary search trees which has exactly
        n nodes of unique values from 1 to n.

    """
    return int(
        (math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n)))
    )
