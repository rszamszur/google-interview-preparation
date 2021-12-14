"""https://leetcode.com/problems/range-sum-of-bst/"""
from collections import deque


# Keeping just for TreeNode reference sake, and tests.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def range_sum_bst(root, low, high):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        root(Optional[TreeNode]): Root node of a binary search tree.
        low(int): Given integer low.
        high(int): Given integer high.

    Returns:

    """
    result = 0
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if low <= node.val <= high:
            result += node.val

        if node.left and node.val > low:
            queue.append(node.left)
        if node.right and node.val < high:
            queue.append(node.right)

    return result
