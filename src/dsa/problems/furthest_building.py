"""https://leetcode.com/problems/furthest-building-you-can-reache"""
import heapq


def furthest_building(heights, bricks, ladders):
    """
    Time complexity: O(n*log(n))
    Space complexity: O(n)

    Args:
        heights (List[int]): Given array heights representing the heights of
            buildings.
        bricks (int): Given number of bricks.
        ladders (int): Given number of ladders.

    Returns:
        The furthest building index (0-indexed) you can reach if you use the
        given ladders and bricks optimally.

    """
    heap = []

    for i in range(len(heights) - 1):
        hop = heights[i] - heights[i + 1]

        if hop >= 0:
            continue

        heapq.heappush(heap, abs(hop))

        if len(heap) > ladders:
            bricks -= heapq.heappop(heap)

        if bricks < 0:
            return i

    return len(heights) - 1
