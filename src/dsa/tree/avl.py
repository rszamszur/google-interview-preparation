from dsa.tree.bst import BST


class AVL(BST):

    def __init__(self):
        super().__init__()

    def _update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def _left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if not y.parent:
            self._root = y
        else:
            self._update_node_parent(node=y, parent=x, value=y)

        x.right = y.left
        if x.right:
            x.right.parent = x

        y.left = x
        x.parent = y
        self._update_height(x)
        self._update_height(y)

    def _right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if not y.parent:
            self._root = y
        else:
            self._update_node_parent(node=y, parent=x, value=y)

        x.left = y.right
        if x.left:
            x.left.parent = x

        y.right = x
        x.parent = y
        self._update_height(x)
        self._update_height(y)

    def _rebalance(self, node):
        while node:
            self._update_height(node)

            if self.height(node.left) >= 2 + self.height(node.right):
                if self.height(node.left.left) >= self.height(node.left.right):
                    self._right_rotate(node)
                else:
                    self._left_rotate(node.left)
                    self._right_rotate(node)
            elif self.height(node.right) >= 2 + self.height(node.left):
                if self.height(node.right.right) >= self.height(node.right.left):
                    self._left_rotate(node)
                else:
                    self._right_rotate(node.right)
                    self._left_rotate(node)

            node = node.parent

    def height(self, node):
        if not node:
            return -1
        else:
            return node.height

    def insert(self, key):
        node = super().insert(key)
        self._rebalance(node)
        return node

    def delete(self, key):
        node = super().delete(key)
        self._rebalance(node.parent)
        return node
