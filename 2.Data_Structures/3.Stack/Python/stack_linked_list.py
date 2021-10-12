#! /usr/bin/env python


class Node(object):
    """Node class implementation for linked list."""

    def __init__(self, value):
        """Initialize Node class object instance."""
        self.value = value
        self.next = None

    def __str__(self):
        """Node class __str__ method."""
        return str(self.value)

    def __repr__(self):
        """Node class __repr__ method."""
        return "Node({value})".format(value=self.value)


class LinkedListStack(object):
    """Stack implementation based on linked list"""

    def __init__(self):
        """Initialize LinkedListStack class object instance."""
        self._top = None

    def __str__(self):
        """LinkedListStack class __str__ method. Complexity: O(n)"""
        stacks = ""
        node = self._top

        while node:
            stacks += str(node)

            if node.next:
                stacks += "\n"

            node = node.next

        return "Top-> {stacks}".format(stacks=stacks)

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
