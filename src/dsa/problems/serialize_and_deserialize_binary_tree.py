"""https://leetcode.com/problems/serialize-and-deserialize-binary-tree/"""
from collections import deque


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        Time complexity: O(n)
        Space complexity: O(n)

        Args:
            root(TreeNode): Root of binary tree.

        Returns:
            Serialized binary tree into string.

        """
        if not root:
            return ""

        bfs = []
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node:
                bfs.append(node.val)
            else:
                bfs.append(None)
                continue

            queue.append(node.left)
            queue.append(node.right)

        return ";".join([str(x) for x in bfs[:-2]])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        Time complexity: O(n)
        Space complexity: O(n)

        Args:
            data(str): Serializerd binary tree into string.

        Returns:
            The root of deserialized binary tree.

        """
        if not data:
            return None

        bfs = [int(x) if x != "None" else None for x in data.split(";")]
        root = TreeNode(bfs.pop(0))
        queue = deque()
        queue.append(root)

        while bfs:
            parent = queue.popleft()
            left = bfs.pop(0)
            right = bfs.pop(0) if bfs else None

            if left is not None:
                parent.left = TreeNode(left)
                queue.append(parent.left)
            if right is not None:
                parent.right = TreeNode(right)
                queue.append(parent.right)

        return root
