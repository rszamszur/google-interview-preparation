"""https://leetcode.com/problems/house-robber"""


def rob(nums):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        nums(List[int]): An integer array nums representing the amount of money
            of each house

    Returns:
         The maximum amount of money you can rob tonight without alerting the
         police.

    """
    rob = not_rob = 0

    for num in nums:
        rob, not_rob = not_rob + num, max(rob, not_rob)

    return max(rob, not_rob)
