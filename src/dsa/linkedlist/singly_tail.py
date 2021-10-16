from .node import Node


class SinglyTailLinkedList(object):
    """SinglyTailLinkedList class implementation."""
    # Why slots: https://docs.python.org/3/reference/datamodel.html#slots
    # TLDR: 1. faster attribute access. 2. space savings in memory.
    __slots__ = ("_head", "_tail")

    def __init__(self):
        """Initialize SinglyTailLinkedList class object instance."""
        self._head = None
        self._tail = None

    def __str__(self):
        """SinglyTailLinkedList class __str__ method. Complexity: O(n)"""
        values = ""
        node = self._head

        while node:
            values += str(node)

            if node.next:
                values += ", "

            node = node.next

        return "[{values}]".format(values=values)

    def __repr__(self):
        """SinglyTailLinkedList class __repr__ method."""
        return "SinglyTailLinkedList()"

    def push_front(self, value):
        """Insert item at the head of the list. Complexity: O(1)"""
        node = Node(value)
        node.next = self._head
        self._head = node
        if not self._tail:
            self._tail = node

    def top_front(self):
        """Return first item. Complexity: O(1)"""
        if self._head:
            return self._head.value

    def pop_front(self):
        """Remove first item. Complexity: O(1)"""
        if self._head:
            node = self._head.next

            if self._tail == self._head:
                self._tail = node

            del self._head
            self._head = node

    def push_back(self, value):
        """Insert item at the end of the list. Complexity: O(1)"""
        node = Node(value)
        if self._tail:
            self._tail.next = node

        self._tail = node
        if not self._head:
            self._head = node

    def top_back(self):
        """Return last item."""
        if self._tail:
            return self._tail.value

    def pop_back(self):
        """Remove last item. Complexity: O(n)"""
        if self._head:
            if not self._head.next:
                del self._head
                self._head = None
                self._tail = None
            else:
                node = self._head

                while node.next.next:
                    node = node.next

                del node.next
                node.next = None
                self._tail = node

    def find(self, value):
        """Return if any item in the list matches value. Complexity: O(n)"""
        node = self._head

        while node:
            if node.value == value:
                return True

            node = node.next

        return False

    def erase(self, value):
        """Remove first item that matches value. Complexity: O(n)"""
        node = self._head
        prev = None

        while node:
            if node.value == value:
                if prev:
                    prev.next = node.next
                else:
                    self._head = node.next
                if not node.next:
                    self._tail = prev
                del node
                break

            prev = node
            node = node.next

    def length(self):
        """Return length of the list. Complexity: O(n)"""
        node = self._head
        count = 0

        while node:
            count += 1
            node = node.next

        return count

    def empty(self):
        """Return if the list is empty. Complexity: O(1)"""
        return not self._head
