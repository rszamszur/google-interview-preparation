"""https://leetcode.com/problems/count-good-nodes-in-binary-tree"""


# Keeping just for TreeNode reference sake, and tests.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        root(TreeNode): Binary Tree root node.

    Returns:
         The number of good nodes in the binary tree.

    """
    stack = [(root, float("-inf"))]
    good_nodes = 0

    while stack:
        node, max_so_far = stack.pop()
        if max_so_far <= node.val:
            good_nodes += 1

        if node.left:
            stack.append(
                (node.left, max(node.val, max_so_far))
            )

        if node.right:
            stack.append(
                (node.right, max(node.val, max_so_far))
            )

    return good_nodes
