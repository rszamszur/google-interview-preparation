"""https://leetcode.com/problems/maximum-units-on-a-truck"""


def maximum_units(box_types, truck_size):
    """
    Time complexity: O(n*log(n))
    Space complexity: O(1)

    Args:
        box_types (List[List[int]]):
        truck_size (int):

    Returns:

    """
    box_types = sorted(box_types, key=lambda x: x[1])
    max_units = 0

    while truck_size > 0:
        if not box_types:
            break

        amount, units = box_types.pop()

        amount = min(amount, truck_size)
        max_units += (amount * units)

        truck_size -= amount
        truck_size = max(0, truck_size)

    return max_units
