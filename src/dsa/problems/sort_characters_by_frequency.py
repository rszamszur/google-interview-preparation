"""https://leetcode.com/problems/sort-characters-by-frequency"""
from collections import Counter


def frequency_sort(s):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        s(str): Given string s.

    Returns:
         The sorted string t in decreasing order based on the frequency of the
         characters.

    """
    result = ""

    for char, count in Counter(s).most_common():
        result += char * count

    return result
