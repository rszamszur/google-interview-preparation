"""https://leetcode.com/problems/binary-tree-inorder-traversal"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        root(Optional[TreeNode]): Root of a binary tree.

    Returns:
        The inorder traversal of its nodes' values.

    """
    stack = []

    if root:
        if root.left:
            stack += inorder_traversal(root.left)

        stack.append(root.val)

        if root.right:
            stack += inorder_traversal(root.right)

    return stack



