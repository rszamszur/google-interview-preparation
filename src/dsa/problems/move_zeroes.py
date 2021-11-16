"""https://leetcode.com/problems/move-zeroes/submissions/"""


def move_zeroes(nums):
    """
    Time complexity: O(n*log(n))
    Space complexity: O(1)

    Args:
        nums(List[int]): An integer array.

    Returns:

    """
    nums.sort(key=bool, reverse=True)
    return nums
