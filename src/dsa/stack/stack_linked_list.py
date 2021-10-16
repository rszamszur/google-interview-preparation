from dsa.linkedlist.node import Node


class LinkedListStack(object):
    """Stack implementation based on linked list"""
    # Why slots: https://docs.python.org/3/reference/datamodel.html#slots
    # TLDR: 1. faster attribute access. 2. space savings in memory.
    __slots__ = ("_top")

    def __init__(self):
        """Initialize LinkedListStack class object instance."""
        self._top = None

    def __str__(self):
        """LinkedListStack class __str__ method. Complexity: O(n)"""
        stack = ""
        node = self._top

        while node:
            stack += str(node)

            if node.next:
                stack += "\n"

            node = node.next

        return "Top-> {stack}".format(stack=stack)

    def __repr__(self):
        """LinkedListStack class __repr__ method."""
        return "LinkedListStack()"

    def empty(self):
        """Return if the stack is empty. Complexity: O(1)"""
        return not self._top

    def push(self, value):
        """Insert item at the top of the stack. Complexity: O(1)"""
        node = Node(value)
        node.next = self._top
        self._top = node

    def pop(self):
        """Remove item at the top of the stack. Complexity: O(1)"""
        if not self._top:
            raise IndexError("pop from empty stack")

        node = self._top.next
        del self._top
        self._top = node

    def top(self):
        """Return last at the top of the stack. Complexity: O(1)"""
        if not self._top:
            raise IndexError("top from empty stack")

        return self._top.value
