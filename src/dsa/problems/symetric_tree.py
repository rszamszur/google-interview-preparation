"""https://leetcode.com/problems/symmetric-tree"""
from collections import deque


# Keeping just for TreeNode reference sake, and tests.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symetric(root):
    """Check whether Binary Tree it is a mirror of itself.

    Time complexity: O(h) == O(log(n)) where h is the height of the
    Binary Tree. Worst case is O(n) if three is inballanced.
    Space complexity: O(h) == O(log(n)) where h is the height of the
    Binary Tree. Worst case is O(n) if three is inballanced.

    Args:
        root(TreeNode): Root of a binary tree.

    Returns:
        True it is a mirror of itself, False otherwise.

    """
    if not root.left and not root.right:
        return True
    elif not root.left or not root.right:
        return False

    queue = deque()
    queue.appendleft(root.left)
    queue.append(root.right)

    while queue:
        left = queue.popleft()
        right = queue.pop()

        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        queue.appendleft(left.left)
        queue.append(right.right)
        queue.appendleft(left.right)
        queue.append(right.left)

    return True