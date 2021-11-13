"""https://leetcode.com/problems/trapping-rain-water"""


def trap(height):
    top = float("-inf")
    water = current = 0

    for i, h in enumerate(height):
        if h < top:
            current += top - h
        else:
            water += current
            current = 0
            if i != len(height) - 1:
                top = min(h, max(height[i + 1:]))

    return water
