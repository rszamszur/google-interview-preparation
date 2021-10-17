from dsa.tree.heap import MaxHeap


def heap_sort(array):
    sorted = []
    heap = MaxHeap(array)

    while not heap.empty():
        sorted.insert(0, heap.pop_max())

    return sorted
