"""https://leetcode.com/problems/area-with-most-water"""


def max_area(height):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        height: List of point at coordinates (index: x, value: y)

    Returns:
        Area of container that contains the most water.

    """
    max_area = 0
    i = 0
    j = len(height) - 1

    while i < j:
        area = (j - i) * min(height[i], height[j])
        max_area = max(max_area, area)

        if height[i] > height[j]:
            j -= 1
        else:
            i += 1

    return max_area
