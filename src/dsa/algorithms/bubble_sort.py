"""https://en.wikipedia.org/wiki/Bubble_sort"""


def bubble_sort(array):
    """Boubble sort algorithm implementation.

    Time complexity: O(n^2)
    Space complexity: O(1)

    Args:
        array(List[int]): array of integers to sort

    Returns:
        sorted array
    """
    while True:
        changed = False

        for i in range(len(array) - 1):
            if array[i] <= array[i + 1]:
                continue

            array[i], array[i + 1] = array[i + 1], array[i]
            changed = True

        if not changed:
            break

    return array