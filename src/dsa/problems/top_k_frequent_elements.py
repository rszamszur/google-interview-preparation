"""https://leetcode.com/problems/top-k-frequent-elements"""
from collections import Counter


def top_k_frequent(nums, k):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        nums(List[int]): An integer array.
        k(int): An integer k.

    Returns:
        The k most frequent elements. You may return the answer in any order.

    """
    return list(
        [x[0] for x in Counter(nums).most_common(k)]
    )
