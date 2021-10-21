"""https://leetcode.com/problems/merge-two-binary-trees"""


# Keeping just for TreeNode reference sake, and tests.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_trees(root1, root2):
    """
    Time complexity: O(m) A total of m nodes need to be traversed. Here, m
    represents the minimum number of nodes from the two given trees.
    Space complexity: O(m) The depth of the recursion tree can go upto m in
    the case of a skewed tree. In average case, depth will be O(log(m)).

    Args:
        root1(TreeNode): root of first binary tree.
        root2(TreeNode): root of second binary tree.

    Returns:
        The merged tree.

    """
    if not root1:
        return root2

    if not root2:
        return root1

    root1.val += root2.val
    root1.left = merge_trees(root1.left, root2.left)
    root1.right = merge_trees(root1.right, root2.right)

    return root1
