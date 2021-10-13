#! /usr/bin/env python


class Node(object):
    """Node class implementation for linked list."""
    # Why slots: https://docs.python.org/3/reference/datamodel.html#slots
    # TLDR: 1. faster attribute access. 2. space savings in memory.
    __slots__ = ("value", "next")

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


class LinkedListQueue(object):
    """Queue implementation based on linked list"""
    # Why slots: https://docs.python.org/3/reference/datamodel.html#slots
    # TLDR: 1. faster attribute access. 2. space savings in memory.
    __slots__ = ("_head", "_tail")

    def __init__(self):
        """Initialize LinkedListQueue class object instance."""
        self._head = None
        self._tail = None

    def __str__(self):
        """LinkedListQueue class __str__ method. Complexity: O(n)"""
        queue = ""
        node = self._head

        while node:
            queue += str(node)

            if node.next:
                queue += "\n"

            node = node.next

        return "Newest -> {queue} <- Oldest".format(queue=queue)

    def __repr__(self):
        """LinkedListQueue class __repr__ method."""
        return "LinkedListQueue()"

    def empty(self):
        """Return if the queue is empty. Complexity: O(1)"""
        return not self._head

    def enqueue(self, value):
        """Add an item to the queue. Complexity: O(1)"""
        node = Node(value)
        if self._tail:
            self._tail.next = node

        self._tail = node
        if not self._head:
            self._head = node

    def dequeue(self):
        """Removes an item from the queue. Complexity: O(1)"""
        if self._head:
            node = self._head.next

            if self._tail == self._head:
                self._tail = node

            dequeued = self._head.value
            del self._head
            self._head = node

            return dequeued

        raise IndexError("dequeue from empty queue")
