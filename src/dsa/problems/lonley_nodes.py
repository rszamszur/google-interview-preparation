"""https://leetcode.com/problems/find-all-the-lonely-nodes"""
from collections import deque


# Keeping just for TreeNode reference sake, and tests.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lonley_nodes(root):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        root(TreeNode): Binary Tree root node.

    Returns:
        Lonley Tree nodes values.

    """
    lonley_nodes = []
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        if node.left and not node.right:
            lonley_nodes.append(node.left.val)
        elif not node.left and node.right:
            lonley_nodes.append(node.right.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return lonley_nodes