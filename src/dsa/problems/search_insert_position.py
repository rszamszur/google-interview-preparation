"""https://leetcode.com/problems/search-insert-position"""


def search_insert_position(nums, target):
    """
    Time complexity: O(log(n))
    Space complexity: O(1)

    Args:
        nums(List[int]): A sorted array of distinct integers.
        target(int): A target value.

    Returns:
        The index if the target is found. If not, return the index where it
        would be if it were inserted in order.

    """
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (hi + lo) // 2
        value = nums[mid]

        if target == value:
            return mid
        elif target < value:
            hi = mid - 1
        else:
            lo = mid + 1

    if target > value:
        return mid + 1
    else:
        return mid
