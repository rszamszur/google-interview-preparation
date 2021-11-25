"""https://leetcode.com/problems/the-skyline-problem"""
import heapq


def get_skyline(buildings):
    """
    Time complexity: O(n * log(n))
    Space complexity: O(n)

    Args:
        buildings(List[List[int]]): Geometric information of each building
            where buildings[i] = [left_i, right_i, height_i]

    Returns:
        The skyline formed by these buildings collectively.

    """
    events = []
    bottom = []

    for left, right, height in buildings:
        events.append((left, -height, right))
        bottom.append((right, 0, None))

    events += bottom
    events.sort()
    skyline = [[0, 0]]
    heap = [(0, float("inf"))]

    for left, neg_height, right in events:
        while heap[0][1] <= left:
            heapq.heappop(heap)

        if neg_height:
            heapq.heappush(heap, (neg_height, right))
        if skyline[-1][1] + heap[0][0]:
            skyline.append([left, -heap[0][0]])

    return skyline[1:]
