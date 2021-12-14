"""https://leetcode.com/problems/sort-an-array/submissions"""
import heapq


def sort_array(nums):
    """
    Time complexity: O(n*log(n))
    Space complexity: O(n)

    Solved using heap sort algorithm. On coding interview you probably could
    implement whatever sort algo you'd like, but in my opinion heap sort is
    the easiest to implement (provided you can use heapq module).

    Args:
        nums(List[int]): An array of integers.

    Returns:
        The array in ascending order.

    """
    result = []
    heapq.heapify(nums)

    while nums:
        result.append(heapq.heappop(nums))

    return result


def sort_array_merge_sort(nums):
    """Merge sort algorithm implementation.

    Time complexity: O(n*log(n))
    Space complexity: O(n)

    Args:
        nums(List[int]): Array of integers to sort.

    Returns:
        Sorted array.

    """
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        sort_array_merge_sort(left)
        sort_array_merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    return nums
