import math


class MaxHeap(object):
    """MaxHeap class implementation."""
    __slots__ = ("_heap")

    def __init__(self, array=None):
        """Initialize MaxHeap class object instance."""
        if array:
            self.heapify(array)
        else:
            self._heap = []

    def __str__(self):
        """MaxHeap class __str__ method."""
        return str(self._heap)

    def __repr__(self):
        """MaxHeap class __repr__ method."""
        return "{name}({heap})".format(
            name=self.__class__.__name__,
            heap=self._heap
        )

    def __len__(self):
        """Return lenght. Complexity: O(1)"""
        return len(self._heap)

    def __iter__(self):
        """Iterate over values in heap Breadth First. Complexity: O(n)"""
        return iter(self._heap)

    @property
    def heap(self):
        """Return heap. Complexity: O(1)"""
        return self._heap

    def empty(self):
        """Return if heap is empty. Complexity: O(1)"""
        return len(self._heap) == 0

    def left(self, i):
        """Return left node indice from index i. Complexity: O(1)"""
        if self.is_leaf(i) or (i * 2) + 1 >= len(self._heap):
            return None

        return (i * 2) + 1

    def right(self, i):
        """Return right node indice from index i. Complexity: O(1)"""
        if self.is_leaf(i) or (i * 2) + 2 >= len(self._heap):
            return None

        return (i * 2) + 2

    def is_leaf(self, i):
        """Return if node at index i is leaf. Complexity: O(1)"""
        if len(self._heap) > i >= (len(self._heap) // 2):
            return True

        return False

    def max(self):
        """Return heap max value. Complexity: O(1)"""
        if self._heap:
            return self._heap[0]

    def min(self):
        """Return heap min value. Complexity: O(n)"""
        if self._heap:
            return min(self._heap[(len(self._heap) // 2):])

    def height(self, i):
        """Return node height at index i. Complexity: O(log(n))"""
        return math.ceil(math.log2(i + 2)) - 1

    def push(self, value):
        """Push item to heap. Complexity: O(n)"""
        self._heap.append(value)
        for i in reversed(range(len(self._heap) // 2)):
            self._max_heapify(i)

    def pop_max(self):
        """Pop heap max value and return it. Complexity: O(n)"""
        max_value =  self._heap[0]
        self._heap.pop(0)
        for i in reversed(range(len(self._heap) // 2)):
            self._max_heapify(i)

        return max_value

    def heapify(self, array):
        """Transform provided list to max heap. Complexity: O(n)"""
        self._heap = array
        for i in reversed(range(len(self._heap) // 2)):
            self._max_heapify(i)

    def inorder(self):
        """Heap inorder iterator. Complexity: O(n)"""
        return iter(self._inorder())

    def _inorder(self, i=0):
        """Return heap items in inorder. Complexity: O(n)"""
        inorder = []
        if len(self._heap) > i >= 0:
            if self.left(i):
                inorder += self._inorder(self.left(i))
            inorder.append(self._heap[i])
            if self.right(i):
                inorder += self._inorder(self.right(i))

        return inorder

    def preorder(self):
        """Heap preorder iterator. Complexity: O(n)"""
        return iter(self._preorder())

    def _preorder(self, i=0):
        """Return heap items in preorder. Complexity: O(n)"""
        preorder = []
        if len(self._heap) > i >= 0:
            preorder.append(self._heap[i])
            if self.left(i):
                preorder += self._preorder(self.left(i))
            if self.right(i):
                preorder += self._preorder(self.right(i))

        return preorder

    def postorder(self):
        """Heap postorder iterator. Complexity: O(n)"""
        return iter(self._postorder())

    def _postorder(self, i=0):
        """Return heap items in postorder. Complexity: O(n)"""
        postorder = []
        if len(self._heap) > i >= 0:
            if self.left(i):
                postorder += self._postorder(self.left(i))
            if self.right(i):
                postorder += self._postorder(self.right(i))
            postorder.append(self._heap[i])

        return postorder

    def _max_heapify(self, i):
        """Correct signle violation of max heap property down the tree.
        Compleixty: O(log(n))
        """
        right = self.right(i)
        left = self.left(i)
        max_i = i

        if left and self._heap[left] > self._heap[i]:
            max_i = left
        if right and self._heap[right] > self._heap[max_i]:
            max_i = right

        if i != max_i:
            self._heap[i], self._heap[max_i] = self._heap[max_i], self._heap[i]
            self._max_heapify(max_i)
