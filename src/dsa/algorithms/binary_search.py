"""
Binary search works for a sorted array.

Time complexity: O(log(n))
"""


def binary_search(array, query):
    lo = 0
    hi = len(array) - 1

    while lo <= hi:
        mid = (hi + lo) // 2
        value = array[mid]
        if query == value:
            return mid
        elif query > value:
            lo = mid + 1
            continue
        else:
            hi = mid - 1
            continue

    return None


def binary_search_recursive(array, query, start=None, end=None):
    if not start:
        start = 0
    if not end:
        end = len(array) - 1

    if start > end:
        return None

    mid = (end + start) // 2
    value = array[mid]
    if query == value:
        return mid
    elif query > value:
        start = mid + 1
        return binary_search_recursive(array, query, start, end)
    else:
        end = mid - 1
        return binary_search_recursive(array, query, start, end)
