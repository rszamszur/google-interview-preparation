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
        return "{name}({value})".format(
            name=self.__class__.__name__,
            value=self.value
        )
