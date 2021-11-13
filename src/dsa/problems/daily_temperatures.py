"""https://leetcode.com/problems/daily-temperatures"""
import collections


def daily_temperatures(temperatures):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        temperatures(List[int]): An array of integers temperatures represents
            the daily temperatures

    Returns:
        An array answer such that answer[i] is the number of days you have to
        wait after the ith day to get a warmer temperature.

    """
    result = [0] * len(temperatures)
    stack = collections.deque()

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev = stack.pop()
            result[prev] = i - prev

        stack.append(i)

    return result
