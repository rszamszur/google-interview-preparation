from dsa.generic import Node


class BinaryTreeNode(Node):
    """BinaryTreeNode class implementation for BinaryTree data structure."""

    def __init__(self, left=None, right=None, **kwargs):
        """Initialize BinaryTreeNode class object instance."""
        super().__init__(**kwargs)
        self.left = left
        self.right = right


class GeneralTreeNode(Node):
    """GeneralTreeNode class implementation for GeneralTree data structure."""

    def __init__(self, parent=None, children=None, **kwargs):
        """Initialize GeneralTreeNode class object instance."""
        super().__init__(**kwargs)
        self.parent = parent
        self.children = children
