"""https://en.wikipedia.org/wiki/Insertion_sort"""


def insertion_sort(array):
    """Insertion sort algorithm implementation.

    Time complexity: O(n^2)
    Space complexity: O(n)

    Args:
        array(List[int]): Array of integers to sort

    Returns:
        Sorted array.

    """
    for i in range(1, len(array)):
        val = array[i]
        j = i - 1

        while j >=0 and val < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = val

    return array
