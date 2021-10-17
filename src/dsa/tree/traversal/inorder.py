from dsa.tree.traversal.base import AbstractTreeIterator


class InorderBinaryTree(AbstractTreeIterator):
    """Inorder Tree iterator class for binary tree."""

    def __init__(self, node):
       """Initialize InorderBinaryTree class object instance."""
       super().__init__(node)

    def _order(self, node):
        """Return inorder nodes for the iterator."""
        stack = []
        if node:
            if node.left:
                stack += self._order(node.left)

            stack.append(node)

            if node.right:
                stack += self._order(node.right)

        return stack


class InorderGeneralTree(AbstractTreeIterator):
    """Inorder Tree iterator class for general tree."""

    def __init__(self, node):
        """Initialize InorderGeneralTree class object instance."""
        super().__init__(node)

    def _order(self, node, left=False):
        """Return inorder nodes for the iterator."""
        stack = []
        if node:
            if node.children:
                for child in node.children[:-1]:
                    stack += self._order(child)

            if left and len(node.children) == 1:
                stack += self._order(node.children[-1])
                stack.append(node)
            else:
                stack.append(node)
                if node.children:
                    stack += self._order(node.children[-1], left=True)

        return stack
