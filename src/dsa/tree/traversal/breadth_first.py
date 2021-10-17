from collections import deque
from dsa.tree.traversal.base import AbstractTreeIterator


class BreadthFirstBinaryTree(AbstractTreeIterator):
    """Breadth First Tree iterator class for binary tree."""

    def __init__(self, node):
       """Initialize BreadthFirstBinaryTree class object instance."""
       super().__init__(node)

    def _order(self, node):
        """Return breadth first nodes for the iterator."""
        order = [node]
        queue = deque()
        queue.append(node)

        while queue:
            node = queue.popleft()

            if node.left:
                order.append(node.left)
                queue.append(node.left)

            if node.right:
                order.append(node.right)
                queue.append(node.right)

        return order


class BreadthFirstGeneralTree(AbstractTreeIterator):
    """Breadth First Tree iterator class for general tree."""

    def __init__(self, node):
        """Initialize BreadthFirstGeneralTree class object instance."""
        super().__init__(node)

    def _order(self, node):
        """Return breadth first nodes for the iterator."""
        order = [node]
        queue = deque()
        queue.append(node)

        while queue:
            node = queue.popleft()

            if node.children:
                for child in node.children:
                    order.append(child)
                    queue.append(child)

        return order
