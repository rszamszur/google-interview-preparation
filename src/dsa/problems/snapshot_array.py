"""https://leetcode.com/problems/snapshot-array/"""
import bisect


class SnapshotArray(object):
    # Why slots: https://docs.python.org/3/reference/datamodel.html#slots
    # TLDR: 1. faster attribute access. 2. space savings in memory.
    __slots__ = ("_snapshots", "_snap_id")

    def __init__(self, length):
        """
        Time complexity: O(n)
        Space complexity: O(n)

        Args:
            length(int): Given array length.

        """
        self._snapshots = dict()
        for i in range(length):
            self._snapshots[i] = {0: 0}
        self._snap_id = 0

    def set(self, index, val):
        """
        Time complexity: O(1)
        Space complexity: O(l * s)
        Where l is length of the array and s number of snapshots.

        Args:
            index(int): Given array index.
            val(int): Given value to set.

        """
        self._snapshots[index][self._snap_id] = val

    def snap(self):
        """
        Time complexity: O(1)
        Space complexity: O(1)

        Returns:
            The snapshot id.

        """
        self._snap_id += 1
        return self._snap_id - 1

    def get(self, index, snap_id):
        """
        Time complexity: O(log(n))
        Space complexity: O(?)

        Args:
            index(int): Given array index.
            snap_id(int): Given array snapshot id.

        Returns:
            the value at the given index, at the time we took the snapshot with
            the given snap_id.

        """
        if snap_id not in self._snapshots[index]:
            keys = list(self._snapshots[index].keys())
            prev_id = bisect.bisect_left(
                keys,
                snap_id,
            ) - 1
            snap_id = keys[prev_id]
            del keys
            del prev_id

        return self._snapshots[index][snap_id]
