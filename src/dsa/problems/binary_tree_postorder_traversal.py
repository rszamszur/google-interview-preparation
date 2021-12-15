"""https://leetcode.com/problems/binary-tree-postorder-traversal"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(root):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        root(Optional[TreeNode]): Root of a binary tree.

    Returns:
        The postorder traversal of its nodes' values.

    """
    stack = []

    if root:
        if root.left:
            stack += postorder_traversal(root.left)

        if root.right:
            stack += postorder_traversal(root.right)

        stack.append(root.val)

    return stack
