"""https://leetcode.com/problems/binary-tree-preorder-traversal"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        root(Optional[TreeNode]): Root of a binary tree.

    Returns:
        The preorder traversal of its nodes' values.

    """
    stack = []

    if root:
        stack.append(root.val)

        if root.left:
            stack += preorder_traversal(root.left)

        if root.right:
            stack += preorder_traversal(root.right)

    return stack
