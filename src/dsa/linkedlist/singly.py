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
      

class SinglyLinkedList(object):
    """SinglyLinkedList class implementation."""
    # Why slots: https://docs.python.org/3/reference/datamodel.html#slots
    # TLDR: 1. faster attribute access. 2. space savings in memory.
    __slots__ = ("head")
    
    def __init__(self):
        """Initialize SinglyLinkedList class object instance."""
        self.head = None

    def __str__(self):
        """SinglyLinkedList class __str__ method. Complexity: O(n)"""
        values = ""
        node = self.head

        while node:
            values += str(node)

            if node.next:
                values += ", "

            node = node.next

        return "[{values}]".format(values=values)

    def __repr__(self):
        """SinglyLinkedList class __repr__ method."""
        return "SinglyLinkedList()"

    def push_front(self, value):
        """Insert item at the head of the list. Complexity: O(1)"""
        node = Node(value)
        node.next = self.head
        self.head = node
        
    def top_front(self):
        """Return first item. Complexity: O(1)"""
        if self.head:
            return self.head.value
    
    def pop_front(self):
        """Remove first item. Complexity: O(1)"""
        if self.head:
            node = self.head.next
            del self.head
            self.head = node

    def push_back(self, value):
        """Insert item at the end of the list. Complexity: O(n)"""
        if self.head:
            node = self.head

            while node.next:
                node = node.next
        
            node.next = Node(value)
        else:
            self.head = Node(value)
    
    def top_back(self):
        """Return last item. Complexity: O(n)"""
        if self.head:
            node = self.head

            while node.next:
                node = node.next

            return node.value

    def pop_back(self):
        """Remove last item. Complexity: O(n)"""
        if self.head:
            if not self.head.next:
                del self.head
                self.head = None
            else:
                node = self.head

                while node.next.next:
                    node = node.next

                del node.next
                node.next = None

    def find(self, value):
        """Return if any item in the list matches value. Complexity: O(n)"""
        node = self.head

        while node:
            if node.value == value:
                return True

            node = node.next

        return False
    
    def erase(self, value):
        """Remove first item that matches value. Complexity: O(n)"""
        node = self.head
        prev = None

        while node:
            if node.value == value:
                if prev:
                    prev.next = node.next
                else:
                    self.head = node.next
                del node
                break

            prev = node
            node = node.next

    def length(self):
        """Return length of the list. Complexity: O(n)"""
        node = self.head
        count = 0

        while node:
            count += 1
            node = node.next

        return count

    def empty(self):
        """Return if the list is empty. Complexity: O(1)"""
        return not self.head
