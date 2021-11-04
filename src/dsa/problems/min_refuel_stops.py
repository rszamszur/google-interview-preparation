"""https://leetcode.com/problems/minimum-number-of-refueling-stops"""
import heapq


def min_refuel_stops(target, fuel, stations):
    """
    Time complexity: O(n*log(n))
    Space complexity: O(n)

    Args:
        target(int): Miles away from the starting position.
        fuel(int): Car initial fuel in the tank.
        stations(List[List[int]]): Gas stations along the way.

    Returns:
        The minimum number of refueling stops the car must make in order to
        reach its destination. If it cannot reach the destination, return -1.

    """
    heap = []
    stations.append([target, 0])
    count = prev = 0

    for position, fuel_cap in stations:
        fuel -= position - prev

        while heap and fuel < 0:
            fuel += (heapq.heappop(heap) * -1)
            count += 1

        if fuel < 0:
            return -1

        heapq.heappush(heap, (fuel_cap * -1))
        prev = position

    return count
