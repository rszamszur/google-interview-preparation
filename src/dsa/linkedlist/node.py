from dsa.generic import Node


class SinglyNode(Node):
    """SinglyNode class implementation for singly linkedlist data structure."""

    def __init__(self, value, next=None, **kwargs):
        """Initialize LinkedListNode class object instance."""
        super().__init__(**kwargs)
        self.value = value
        self.next = next

    def __str__(self):
        """Node class __str__ method."""
        return str(self.value)


class DoublyNode(Node):
    """DoublyNode class implementation for doubly linkedlist data structure."""

    def __init__(self, value, next=None, prev=None, **kwargs):
        """Initialize LinkedListNode class object instance."""
        super().__init__(**kwargs)
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        """Node class __str__ method."""
        return str(self.value)
