from dsa.tree.traversal.base import AbstractTreeIterator


class PreorderBinaryTree(AbstractTreeIterator):
    """Preorder Tree iterator class for binary tree."""

    def __init__(self, node):
       """Initialize PreorderBinaryTree class object instance."""
       super().__init__(node)

    def _order(self, node):
        """Return preorder nodes for the iterator."""
        stack = []
        if node:
            stack.append(node)

            if node.left:
                stack += self._order(node.left)

            if node.right:
                stack += self._order(node.right)

        return stack


class PreorderGeneralTree(AbstractTreeIterator):
    """Preorder Tree iterator class for general tree."""

    def __init__(self, node):
        """Initialize PreorderGeneralTree class object instance."""
        super().__init__(node)

    def _order(self, node):
        """Return preorder nodes for the iterator."""
        stack = []
        if node:
            stack.append(node)

            if node.children:
                for child in node.children[:-1]:
                    stack += self._order(child)

            if node.children:
                stack += self._order(node.children[-1])

        return stack
