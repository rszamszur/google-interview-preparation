#! /usr/bin/env python
from collections.abc import Set


class HashTableNode(object):
    """HashTableNode class implementation for chaining."""
    # Why slots: https://docs.python.org/3/reference/datamodel.html#slots
    # TLDR: 1. faster attribute access. 2. space savings in memory.
    __slots__ = ("value", "key", "next")

    def __init__(self, key, value):
        """Initialize Node class object instance."""
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        """Node class __str__ method."""
        return str(self.value)

    def __repr__(self):
        """Node class __repr__ method."""
        return "Node(key={key}, value={value})".format(
            value=self.value,
            key=self.key,
        )


class HashTable(Set):
    # Why slots: https://docs.python.org/3/reference/datamodel.html#slots
    # TLDR: 1. faster attribute access. 2. space savings in memory.
    __slots__ = ("_size", "_table")

    def __init__(self, size):
        self._size = size
        self._table = [None] * size

    def __str__(self):
        visualise = ""
        for index, item in enumerate(self._table):
            visualise += "#{id}|".format(id=index)
            if not item:
                visualise += "None"

            while item:
                visualise += repr(item)

                if item.next:
                    visualise += " -> "

                item = item.next

            visualise += "\n"

        return str(visualise.rstrip("\n"))

    def __repr__(self):
        return "HashTable({size})".format(size=self.size)

    def __contains__(self, key):
        for item in self.keys():
            if item.key == key:
                return True

        return False

    def __iter__(self):
        return iter(self.items())

    def __len__(self):
        return len(self._table)

    def __getitem__(self, key):
        index = hash(key) & (self._size - 1)

        if not self._table[index]:
            raise KeyError(key)

        node = self._table[index]

        if node.next and node.key != key:
            node = node.next

            while node.key != key:
                node = node.next

        return node.value

    def __setitem__(self, key, value):
        # Use Python builtin hash method, and apply a mask.
        index = hash(key) & (self._size - 1)

        # Handle colisions
        if self._table[index]:
            node = self._table[index]

            while node:
                # Handle update
                if node.key == key:
                    node.value = value
                    return
                node = node.next

            node.next = HashTableNode(key=key, value=value)
        else:
            self._table[index] = HashTableNode(key=key, value=value)

    def __delitem__(self, key):
        # Use Python builtin hash method, and apply a mask.
        index = hash(key) & (self._size - 1)

        if not self._table[index]:
            raise KeyError(key)

        node = self._table[index]
        if node.next and node.key != key:
            node = node.next

            while node.key != key:
                node = node.next

        del node
        self._table[index] = None

    def keys(self):
        keys = []

        for item in [x for x in self._table if x]:
            while item:
                keys.append(item.key)
                item = item.next

        return keys

    def values(self):
        values = []

        for item in [x for x in self._table if x]:
            while item:
                values.append(item.value)
                item = item.next

        return values

    def items(self):
        keys = []
        values = []

        for item in [x for x in self._table if x]:
            while item:
                keys.append(item.key)
                values.append(item.value)
                item = item.next

        return zip(keys, values)
