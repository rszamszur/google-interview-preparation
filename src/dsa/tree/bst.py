from dsa.tree.node import BinaryTreeNode
from dsa.tree.traversal import (
    BreadthFirstBinaryTree,
    InorderBinaryTree,
    PreorderBinaryTree,
    PostorderBinaryTree
)


class BST(object):
    """BinarySearchTree class implementation."""

    def __init__(self):
        """Initialize BinarySearchTree class object instance."""
        self._root = None

    def __str__(self):
        """Class custom __str__ method implementation.

        Returns:
            str: BinarySearchTree in breadth first traversal order.
        """
        bst = []

        for node in BreadthFirstBinaryTree(self._root):
            bst.append(node.key)

        return str(bst)

    def __repr__(self):
        """Class custom __repr__ method implementation.

        Returns:
            str: BinarySearchTree string object.

        """
        return "{name}()".format(name=self.__class__.__name__)

    def __iter__(self):
        """Iterate over BinarySearchTree values in Breadth First traversal.

        Time Complexity: O(n)
        Space complexity: O(n) -> Allocating iterator array memory

        Returns:
            Breadth First traversal iterator.

        """
        if self._root:
            return iter(BreadthFirstBinaryTree(self._root))

    def __contains__(self, item):
        """Implementation of membership test operators.

        Time compleixty: O(h) == O(log(n)) where h is the height of the
        BinarySearchTree. Worst case is O(n) if three is inballanced.
        Space complexity: O(1)

        Args:
            item: Value to test.

        Returns:
            True if value in BinarySearchTree, false otherwise.

        """
        return not not self.find(item)

    def insert(self, key):
        """Insert key into BinarySearchTree.

        Time compleixty: O(h) == O(log(n)) where h is the height of the
        BinarySearchTree. Worst case is O(n) if three is inballanced.
        Space complexity: O(1)

        Args:
            key(int): Key to insert.

        Returns
            BinaryTreeNode: Inserted node.

        """
        if not self._root:
            self._root = BinaryTreeNode(key=key, parent=None)
            return self._root

        node = self._root
        parent = node

        while node:
            parent = node

            if key < node.key:
                node = node.left
            else:
                node = node.right

        if key < parent.key:
            parent.left = BinaryTreeNode(key=key, parent=parent)
            return parent.left
        else:
            parent.right = BinaryTreeNode(key=key, parent=parent)
            return parent.right

    def find(self, key):
        """Find node in BinarySearchTree that matches provided key.

        Time compleixty: O(h) == O(log(n)) where h is the height of the
        BinarySearchTree. Worst case is O(n) if three is inballanced.
        Space complexity: O(1)

        Args:
            key(int): Key to find.

        Returns
            BinaryTreeNode: Node if found, otherwise None.

        """
        node = self._root

        while node:
            if key == node.key:
                return node

            if key < node.key:
                node = node.left
            else:
                node = node.right

        return None

    def delete(self, key):
        """Delete node from BinarySearchTree that matches provided key.

        Time compleixty: O(h) == O(log(n)) where h is the height of the
        BinarySearchTree. Worst case is O(n) if three is inballanced.
        Space complexity: O(1)

        Args:
            key(int): Key to delete.

        Returns
            BinaryTreeNode: Deleted node.

        Raises:
            KeyError: If key to delete doesn't exist.

        """
        node = self.find(key)

        if not node:
            raise KeyError(key)

        if not node.left and not node.right:
            if node == self._root:
                self._root = None
            else:
                self._update_node_parent(
                    node=node,
                    parent=node,
                )

            return node
        elif node.left and node.right:
            successor = self.min(node)
            node.key, successor.key = successor.key, node.key
            self._update_node_parent(
                node=successor,
                parent=successor,
            )

            return successor
        else:
            if node.left:
                child = node.left
            else:
                child = node.right

            if node == self._root:
                self._root = child
            else:
                self._update_node_parent(
                    node=node,
                    parent=node,
                    value=child,
                )

            child.parent = node.parent
            return node

    def max(self, node=None):
        """Returns maximum value in BinarySearchTree.

        Time compleixty: O(h) == O(log(n)) where h is the height of the
        BinarySearchTree. Worst case is O(n) if three is inballanced.
        Space complexity: O(1)

        Args:
            node(BinaryTreeNode): Node from which to start.

        Returns:
            BinaryTreeNode: Maximum value.

        Raises:
            ValueError: If BinarySearchTree is empty Tree.

        """
        if not node:
            if not self._root:
                raise ValueError("max() arg is an empty BinaryTreeNode")

            node = self._root

        while node.right:
            node = node.right

        return node

    def min(self, node=None):
        """Returns minimum value in BinarySearchTree.

        Time compleixty: O(h) == O(log(n)) where h is the height of the
        BinarySearchTree. Worst case is O(n) if three is inballanced.
        Space complexity: O(1)

        Args:
            node(BinaryTreeNode): Node from which to start.

        Returns:
            BinaryTreeNode: Minimum value.

        Raises:
            ValueError: If BinarySearchTree is empty Tree.

        """
        if not node:
            if not self._root:
                raise ValueError("min() arg is an empty BinaryTreeNode")

            node = self._root

        while node.left:
            node = node.left

        return node

    def inorder(self):
        """Iterate over BinarySearchTree nodes in inorder traversal.

        Time complexity: O(n)
        Space complexity: O(n) -> Allocating iterator array memory

        Returns:
            Inorder traversal iterator.

        """
        if self._root:
            return iter(InorderBinaryTree(self._root))

    def preorder(self):
        """Iterate over BinarySearchTree nodes in preorder traversal.

        Time complexity: O(n)
        Space complexity: O(n) -> Allocating iterator array memory

        Returns:
            Preorder traversal iterator.

        """
        if self._root:
            return iter(PreorderBinaryTree(self._root))

    def postorder(self):
        """Iterate over BinarySearchTree nodes in postorder traversal.

        Time complexity: O(n)
        Space complexity: O(n) -> Allocating iterator array memory

        Returns:
            Postorder traversal iterator.

        """
        if self._root:
            return iter(PostorderBinaryTree(self._root))

    def _update_node_parent(self, node, parent, value=None):
        """Class utility method for updating node parent with provided value.

        Time complexity: O(1)
        Space complexity: O(1)

        Args:
            node(BinaryTreeNode): Node which parent to update
            value(BinaryTreeNode): Value to update with

        """
        if node.parent.left == node:
            node.parent.left = value
        else:
            node.parent.right = value
