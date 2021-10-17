class TreeNode(object):
    """TreeNode class implementation for Tree data structure."""

    def __init__(self, **kwargs):
        """Initialize TreeNode class object instance."""
        self.__dict__.update(kwargs)

    def __str__(self):
        """Node class __str__ method."""
        return str(self.__dict__)

    def __repr__(self):
        """Node class __repr__ method."""
        kwargs = []

        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                kwargs.append(
                    "{key}={value}".format(
                        key=key,
                        value=repr(value)
                    )
                )

        return "{name}({kwargs})".format(
            name=self.__class__.__name__,
            kwargs=", ".join(kwargs)
        )


class BinaryTreeNode(TreeNode):
    """BinaryTreeNode class implementation for BinaryTree data structure."""

    def __init__(self, left=None, right=None, **kwargs):
        """Initialize BinaryTreeNode class object instance."""
        super().__init__(**kwargs)
        self.left = left
        self.right = right


class GeneralTreeNode(TreeNode):
    """GeneralTreeNode class implementation for GeneralTree data structure."""

    def __init__(self, parent=None, children=None, **kwargs):
        """Initialize GeneralTreeNode class object instance."""
        super().__init__(**kwargs)
        self.parent = parent
        self.children = children