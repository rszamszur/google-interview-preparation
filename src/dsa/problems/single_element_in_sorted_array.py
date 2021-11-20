"""https://leetcode.com/problems/single-element-in-a-sorted-array"""


def single_non_duplicate(nums):
    """
    Time complexity: O(n/2)
    Space complexity: O(1)

    Args:
        nums(List[int]): A sorted array consisting of only integers where every
            element appears exactly twice, except for one element which appears
            exactly once.

    Returns:
        The single element that appears only once.

    """
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]

    return nums[-1]
