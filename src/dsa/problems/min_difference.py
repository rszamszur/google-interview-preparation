"""eetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves"""


def min_difference(nums):
    """
    Time complexity: O(log(n))
    Space complexity: O(1)

    Args:
        nums(List[int]): An array of numbers

    Returns:
        The minimum difference between the largest and smallest value of nums
        after perfoming at most 3 moves.

    """
    if len(nums) <= 4:
        return 0

    nums.sort()
    return min(
        (nums[-1] - nums[3]),
        (nums[-2] - nums[2]),
        (nums[-3] - nums[1]),
        (nums[-4] - nums[0]),
    )
