"""https://leetcode.com/problems/find-leaves-of-binary-tree"""
from collections import deque


# Keeping just for TreeNode reference sake, and tests.
class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(node):
    bfs = []
    queue = deque()
    node.parent = None
    queue.append(node)

    while queue:
        node = queue.popleft()
        bfs.append(node)

        if node.left:
            node.left.parent = node
            queue.append(node.left)

        if node.right:
            node.right.parent = node
            queue.append(node.right)

    return bfs


def height(node):
    if not node:
        return -1
    else:
        return node.height


def postorder(node):
    stack = []

    if node:
        if node.left:
            stack += postorder(node.left)

        if node.right:
            stack += postorder(node.right)

        if not node.left and not node.right:
            node.height = 0
        else:
            node.height = max(
                height(node.left),
                height(node.right)
            ) + 1

        stack.append(node)

    return stack


def find_leaves_with_height(root):
    """Better implementation using height.

    Time complexity: O(?) O(n) or O(n*log(n))
    Space complexity: O(n)

    Given the root of a binary tree, collect a tree's nodes as if you were
    doing this:
    1) Collect all the leaf nodes.
    2) Remove all the leaf nodes.
    3) Repeat until the tree is empty.

    Args:
        root(TreeNode): Root of binary tree.

    Returns:
        Collected tree nodes.

    """
    result = []

    for node in postorder(root):
        try:
            result[node.height].append(node.val)
        except IndexError:
            result.insert(node.height, [])
            result[node.height].append(node.val)

    return result


def find_leaves_with_bfs(root):
    """Initial implementation

    Time complexity: O(?) n*log(n) or O(n^2), not quite sure
    Space complexity: O(n)

    Given the root of a binary tree, collect a tree's nodes as if you were
    doing this:
    1) Collect all the leaf nodes.
    2) Remove all the leaf nodes.
    3) Repeat until the tree is empty.

    Args:
        root(TreeNode): Root of binary tree.

    Returns:
        Collected tree nodes.

    """
    result = []

    while root.left or root.right:
        leaves = []

        for node in bfs(root):
            if not node.left and not node.right:
                leaves.append(node)

        for i in range(len(leaves)):
            node = leaves[i]

            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None

            leaves[i] = node.val
            del node

        result.append(leaves)

    result.append([root.val])
    return result
