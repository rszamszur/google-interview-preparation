"""https://leetcode.com/problems/find-all-duplicates-in-an-array"""
import collections


def find_duplicates(nums):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        nums(List[int]): An integer array.

    Returns:
        An array of all the integers that appears twice.

    """
    return [x[0] for x in collections.Counter(nums).items() if x[1] > 1]
