"""https://leetcode.com/problems/car-fleet/submissions/"""


def car_fleet(target, position, speed):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        target(int): Destination, miles away.
        position(List[int]): Current position of cars.
        speed(List[int]): Speed of cars in mph.

    Returns:
        The number of car fleets that will arrive at the destination.

    """
    stack = []

    for pos, speed in sorted(zip(position, speed), reverse=True):
        dist = target - pos
        if not stack:
            stack.append(dist / speed)
        elif dist / speed > stack[-1]:
            stack.append(dist / speed)

    return len(stack)
