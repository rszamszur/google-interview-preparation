"""https://leetcode.com/problems/time-based-key-value-store"""


class TimeMap(object):
    __slots__ = ("_storage")

    def __init__(self):
        self._storage = {}

    def set(self, key, value, timestamp):
        """
        Time complexity: O(1)
        Space complexity: O(n)

        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self._storage:
            self._storage[key] = []

        self._storage[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        Time complexity: O(log(n))
        Space complexity: O(n)

        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self._storage:
            return ""

        vals = self._storage[key]

        if vals[-1][0] <= timestamp:
            return vals[-1][1]
        elif vals[0][0] > timestamp:
            return ""

        lo = 0
        hi = len(vals) - 1

        while lo <= hi:
            mid = (hi + lo) // 2
            value = vals[mid][0]
            if timestamp == value:
                return vals[mid][1]
            elif timestamp > value:
                lo = mid + 1
                continue
            else:
                hi = mid - 1
                continue

        return vals[lo - 1][1]
