"""https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm"""


def kadane(array):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        nums(List[int]): an integer array

    Returns:
        The largest sum of the contiguous subarray
    """
    current_sum = best_sum = array[0]

    for x in array[1:]:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)

    return best_sum