#! /usr/bin/env python
# In order to have O(1) time complexity of all methods we need to use
# collections.deque class
#
# NOTE! Although Python lists are implemented with standard "arrays" under the
# hood, its time complexity is the same as for standard array. The largest
# costs come from growing beyond the current allocation size
# (because everything must move), or from inserting or deleting somewhere near
# the beginning (because everything after that must move). If you need to
# add/remove at both ends, consider using a collections.deque instead.
# Wiki: https://wiki.python.org/moin/TimeComplexity
from collections import deque


class ArrayQueue(object):
    """Stack implementation based on collections.deque."""

    def __init__(self, size: int):
        """Initialize ArrayQueue class object instance."""
        self._queue = deque(maxlen=size)
        self._size = size

    def __str__(self):
        """ArrayQueue class __str__ method. Complexity: O(n)"""
        queue = ""

        for item in self._queue:
            queue += str(item)
            queue += "\n"

        queue.strip()
        return "Newest -> {queue} <- Oldest".format(queue=queue)

    def __repr__(self):
        """ArrayQueue class __repr__ method."""
        return "ArrayQueue({size})".format(size=self._size)

    def empty(self):
        """Return if the queue is empty. Complexity: O(1)"""
        return len(self._queue) == 0

    def enqueue(self, value):
        """Add an item to the queue. Complexity: O(1)"""
        if len(self._queue) == self._size:
            raise IndexError("queue overflow")

        self._queue.appendleft(value)

    def dequeue(self):
        """Removes an item from the queue. Complexity: O(1)"""
        return self._queue.pop()
