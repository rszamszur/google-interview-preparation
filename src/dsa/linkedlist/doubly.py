from .node import DoublyNode


class DoublyLinkedList(object):
    """DoublyLinkedList class implementation."""
    # Why slots: https://docs.python.org/3/reference/datamodel.html#slots
    # TLDR: 1. faster attribute access. 2. space savings in memory.
    __slots__ = ("_head")

    def __init__(self):
        """Initialize DoublyLinkedList class object instance."""
        self._head = None

    def __str__(self):
        """DoublyLinkedList class __str__ method. Complexity: O(n)"""
        values = ""
        node = self._head

        while node:
            values += str(node)

            if node.next:
                values += ", "

            node = node.next

        return "[{values}]".format(values=values)

    def __repr__(self):
        """DoublyLinkedList class __repr__ method."""
        return "{name}()".format(name=self.__class__.__name__)

    def push_front(self, value):
        """Insert item at the head of the list. Complexity: O(1)"""
        node = DoublyNode(value)
        if self._head:
            node.next = self._head
            self._head.prev = node
        self._head = node

    def top_front(self):
        """Return first item. Complexity: O(1)"""
        if self._head:
            return self._head.value

    def pop_front(self):
        """Remove first item. Complexity: O(1)"""
        if self._head:
            node = self._head.next
            if node:
                node.prev = None
            del self._head
            self._head = node

    def push_back(self, value):
        """Insert item at the end of the list. Complexity: O(n)"""
        if self._head:
            node = self._head

            while node.next:
                node = node.next

            node.next = DoublyNode(value)
            node.next.prev = node
        else:
            self._head = DoublyNode(value)

    def top_back(self):
        """Return last item. Complexity: O(n)"""
        if self._head:
            node = self._head

            while node.next:
                node = node.next

            return node.value

    def pop_back(self):
        """Remove last item. Complexity: O(n)"""
        if self._head:
            if not self._head.next:
                del self._head
                self._head = None
            else:
                node = self._head

                while node.next.next:
                    node = node.next

                del node.next
                node.next = None

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

        while node:
            if node.value == value:
                if node.prev:
                    node.prev.next = None
                    if node.next:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                else:
                    self._head = None
                    if node.next:
                        self._head = node.next
                        self._head.prev = None
                del node
                break

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
