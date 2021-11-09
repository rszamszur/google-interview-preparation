"""https://leetcode.com/problems/palindrome-permutation"""
import collections


def palindrome_permutation(s):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        s(str): Given string.

    Returns:
        True if a permutation of the string could form a palindrome.

    """
    counter = collections.Counter(s)
    odd = 0

    if len(s) % 2 != 0:
        odd = 1

    for char, value in counter.most_common():
        if value % 2 != 0:
            odd -= 1
            if odd < 0:
                return False

    return True
