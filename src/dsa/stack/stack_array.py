#! /usr/bin/env python
# For this implementation we can use Python array since methods: append(),
# and pop() (for last element) are O(1) time complexity.
#
# NOTE! Although Python lists are implemented with standard "arrays" under the
# hood, its time complexity is the same as for standard array. The largest
# costs come from growing beyond the current allocation size
# (because everything must move), or from inserting or deleting somewhere near
# the beginning (because everything after that must move). If you need to
# add/remove at both ends, consider using a collections.deque instead.
# Wiki: https://wiki.python.org/moin/TimeComplexity


class ArrayStack(object):
    """Stack implementation based on array"""
    # Why slots: https://docs.python.org/3/reference/datamodel.html#slots
    # TLDR: 1. faster attribute access. 2. space savings in memory.
    __slots__ = ("_stack", "_size")

    def __init__(self, size: int):
        """Initialize ArrayStack class object instance."""
        self._stack = []
        self._size = size

    def __str__(self):
        """ArrayStack class __str__ method. Complexity: O(n)"""
        stack = ""

        for item in self._stack:
            stack += str(item)
            stack += "\n"

        return "Top-> {stack}".format(stack=stack).rstrip("\n")

    def __repr__(self):
        """ArrayStack class __repr__ method."""
        return "ArrayStack({size})".format(size=self._size)

    def empty(self):
        """Return if the stack is empty. Complexity: O(1)"""
        return len(self._stack) == 0

    def push(self, value):
        """Insert item at the top of the stack. Complexity: O(1)"""
        if len(self._stack) == self._size:
            raise IndexError("stack overflow")

        self._stack.append(value)

    def pop(self):
        """Remove item at the top of the stack. Complexity: O(1)"""
        try:
            return self._stack.pop()
        except IndexError:
            raise IndexError("pop from empty stack")

    def top(self):
        """Return last at the top of the stack. Complexity: O(1)"""
        if self.empty():
            raise IndexError("top from empty stack")

        return self._stack[-1]
