from dsa.tree.traversal.base import AbstractTreeIterator


class PostorderBinaryTree(AbstractTreeIterator):
    """Postorder Tree iterator class for binary tree."""

    def __init__(self, node):
       """Initialize PostorderBinaryTree class object instance."""
       super().__init__(node)

    def _order(self, node):
        """Return postorder nodes for the iterator."""
        stack = []
        if node:
            if node.left:
                stack += self._order(node.left)

            if node.right:
                stack += self._order(node.right)

            stack.append(node)

        return stack


class PostorderGeneralTree(AbstractTreeIterator):
    """Postorder Tree iterator class for general tree."""

    def __init__(self, node):
        """Initialize PostorderGeneralTree class object instance."""
        super().__init__(node)

    def _order(self, node):
        """Return postorder nodes for the iterator."""
        stack = []
        if node:
            if node.children:
                for child in node.children[:-1]:
                    stack += self._order(child)

            if node.children:
                stack += self._order(node.children[-1])

            stack.append(node)

        return stack
