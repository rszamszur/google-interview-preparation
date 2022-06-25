"""https://leetcode.com/problems/non-decreasing-array"""


def check_possibility(nums):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        nums (List[int]): Given an array nums with n integers.

    Returns:
        True if it could become non-decreasing by modifying at most one element.

    """
    modified = False
    i = 0

    while i < (len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            i += 1
            continue

        if modified:
            return False

        if i == 0:
            nums[i] = nums[i + 1] - 1
        elif max(nums[:i]) > min(nums[i:]):
            nums[i + 1] = nums[i]
        else:
            nums[i] = nums[i + 1]

        modified = True

    return True
