"""https://leetcode.com/problems/merge-intervals"""


def merge_intervals(intervals):
    """
    Time complexity: O(n*log(n))
    Space complexity: O(n)

    Args:
        intervals(List[List[int]]):  An array of intervals where
            intervals[i] = [start_i, end_i]

    Returns:
        An array of the non-overlapping intervals that cover all the intervals
        in the input.

    """
    result = []
    current = []

    for interval in sorted(intervals):
        if not current:
            current = interval
            continue

        if interval[0] <= current[1]:
            current[1] = max(interval[1], current[1])
        else:
            result.append(current)
            current = interval

    if current:
        result.append(current)

    return result
