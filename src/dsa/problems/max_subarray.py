"""https://leetcode.com/problems/maximum-subarray/"""


def max_subarray(nums):
    """Maximum subarray problem can be solved usin Kadane algorithm:
    https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        nums(List[int]): an integer array

    Returns:
        The largest sum of the contiguous subarray
    """
    numsum = maxsum = nums[0]

    for num in nums[1:]:
        numsum = max(num, numsum + num)
        maxsum = max(maxsum, numsum)

    return maxsum
