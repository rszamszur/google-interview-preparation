"""https://leetcode.com/problems/delete-nodes-and-return-forest"""


# Keeping just for TreeNode reference sake, and tests.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder(node):
    """
    Time complexity: O(log(n)) if tree is balanced, otherwise O(n)
    Space complexity: O(n)

    Args:
        self:
        node(TreeNode): Binary tree root.

    Returns:
        TreeNode's in postorder.

    """
    stack = []

    if node:
        if node.left:
            stack += postorder(node.left)

        if node.right:
            stack += postorder(node.right)

        stack.append(node)

    return stack


def delete_tree_nodes(root, to_delete):
    """
    Time complexity: O(log(n)) if tree is balanced, otherwise O(n)
    Space complexity: O(n)

    Args:
        root(TreeNode): Binary tree root.
        to_delete(List[int]): List of nodes to delete.

    Returns:
        The roots of the trees in the remaining forest.

    """
    forest = []

    for node in postorder(root):
        if node.right and node.right.val in to_delete:
            node.right = None
        if node.left and node.left.val in to_delete:
            node.left = None

        if node.val in to_delete:
            if node.left:
                forest.append(node.left)

            if node.right:
                forest.append(node.right)

            del node
        elif node.val == root.val:
            forest.append(node)

    return forest
