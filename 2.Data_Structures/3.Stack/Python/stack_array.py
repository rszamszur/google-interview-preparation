#! /usr/bin/env python


class ArrayStack(object):
    """Stack implementation based on array"""

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

        stack.strip()
        return "Top-> {stack}".format(stack=stack)

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
