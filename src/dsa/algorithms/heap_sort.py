"""
https://en.wikipedia.org/wiki/Heapsort
https://www.cs.usfca.edu/~galles/visualization/HeapSort.html
"""
from dsa.tree.heap import MaxHeap


def heap_sort(array):
    """Heap sort algorithm implementation.

    Time complexity: O(n*log(n))
    Space complexity: O(n)

    Args:
        array(List[int]): Array of integers to sort

    Returns:
        Sorted array
    """
    sorted = []
    heap = MaxHeap(array)

    while not heap.empty():
        sorted.insert(0, heap.pop_max())

    return sorted
