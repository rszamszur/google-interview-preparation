"""https://leetcode.com/problems/count-complete-tree-nodes"""
import collections


# Keeping just for TreeNode reference sake, and tests.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root):
    """
    Time complexity: O(n)
    Space complexity: O(log(n))

    Args:
        root(TreeNode): Root of a complete binary tree.

    Returns:
        The number of the nodes in the tree.

    """
    if not root:
        return 0

    count = 0
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        count += 1

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return count
