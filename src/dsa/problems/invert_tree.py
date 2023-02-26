"""https://leetcode.com/problems/invert-binary-tree"""
from typing import Optional


# Keeping just for TreeNode reference sake, and tests.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        root: Tree root node.

    Returns:
        Reversed tree

    """
    if not root:
        return root

    invert_tree(root.left)
    invert_tree(root.right)

    root.left, root.right = root.right, root.left
    return root
