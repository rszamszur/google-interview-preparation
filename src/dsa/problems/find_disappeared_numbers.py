"""https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array"""


def find_disappeared_numbers(nums):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        nums(List[int]): Array nums of n integers.

    Returns:
        An array of all the integers in the range [1, n] that do not appear
        in nums.

    """
    return list(
        set(range(1, len(nums) + 1)).difference(set(nums))
    )
