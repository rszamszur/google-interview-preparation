import abc
from collections.abc import Iterable


class AbstractTreeIterator(Iterable, metaclass=abc.ABCMeta):
    """AbstractTreeIterator class implementation."""

    def __init__(self, node):
        """Initialize AbstractTreeIterator class object instance."""
        self._node = node

    def __iter__(self):
        """Class iterator method implementation."""
        return iter(self._order(self._node))

    @abc.abstractmethod
    def _order(self, node):
        """Class abstract method _order definition."""
        pass
