"""https://leetcode.com/problems/validate-binary-search-tree"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validate_bst(root):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        root(Optional[TreeNode]): The root of a binary search tree.

    Returns:
        True if it is a valid binary search tree, otherwise false.

    """
    node = root
    stack = []
    last = float("-inf")

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
            continue

        node = stack.pop()

        if last >= node.val:
            return False

        last = node.val
        node = node.right

    return True
