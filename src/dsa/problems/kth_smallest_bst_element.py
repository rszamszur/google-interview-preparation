"""https://leetcode.com/problems/kth-smallest-element-in-a-bst"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root, k):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        root(Optional[TreeNode]): The root of a binary search tree.
        k(int): An integer k.

    Returns:
        The kth smallest value of all the values of the nodes in the tree.

    """
    node = root
    stack = []

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
            continue

        node = stack.pop()
        k -= 1

        if k == 0:
            return node.val

        node = node.right
