import pytest
from dsa.tree.heap import MaxHeap


@pytest.mark.parametrize("array, expected", [
    ([1,2,3,4,5,6], [6,5,3,4,2,1]),
    ([],[]),
    ([1, 2, 3], [3, 2, 1]),
    ([1,4,2,3,9,7,10,8,14,16], [16, 14, 10, 8, 9, 7, 2, 1, 3, 4])
])
def test_heapify(array, expected):
    heap = MaxHeap()
    heap.heapify(array)
    assert heap.heap == expected


@pytest.mark.parametrize("array, expected", [
    ([1,2,3,4,5,6], [6,5,3,4,2,1]),
    ([],[]),
    ([1, 2, 3], [3, 2, 1]),
    ([1, 4, 2, 3, 9, 7, 10, 8, 14, 16], [16, 14, 10, 8, 9, 7, 2, 1, 3, 4])
])
def test_init_heapify(array, expected):
    heap = MaxHeap(array)
    assert heap.heap == expected


def test_empty():
    heap = MaxHeap()
    assert heap.empty()
    heap.push(1)
    assert not heap.empty()


def test_left():
    heap = MaxHeap([1,2,3,4,5,6])
    assert not heap.left(5)
    assert not heap.left(4)
    assert not heap.left(3)
    assert heap.left(2) == 5
    assert heap.left(1) == 3


def test_right():
    heap = MaxHeap([1, 2, 3, 4, 5, 6])
    assert not heap.right(5)
    assert not heap.right(4)
    assert not heap.right(3)
    assert not heap.right(2)
    assert heap.right(1) == 4


def test_leaf():
    heap = MaxHeap([16, 14, 10, 8, 9, 7, 2, 1, 3, 4])
    assert not heap.is_leaf(4)
    assert heap.is_leaf(5)
    assert heap.is_leaf(6)
    assert heap.is_leaf(7)
    assert heap.is_leaf(8)
    assert heap.is_leaf(9)


def test_max():
    heap = MaxHeap([1,2,3,4,5,6])
    assert heap.max() == 6
    heap.push(8)
    assert heap.max() == 8
    heap.push(81)
    assert heap.max() == 81


def test_min():
    heap = MaxHeap([1, 2, 3, 4, 5, 6])
    assert heap.min() == 1
    heap.push(0)
    assert heap.min() == 0
    heap.push(-2)
    assert heap.min() == -2


def test_height():
    heap = MaxHeap([16, 14, 10, 8, 9, 7, 2, 1])
    assert heap.height(0) == 0
    assert heap.height(1) == 1
    assert heap.height(2) == 1
    assert heap.height(3) == 2
    assert heap.height(4) == 2
    assert heap.height(5) == 2
    assert heap.height(6) == 2
    assert heap.height(7) == 3


def test_push():
    heap = MaxHeap()
    heap.push(2)
    heap.push(3)
    heap.push(7)
    heap.push(4)
    heap.push(10)
    assert heap.heap == [10, 7, 3, 2, 4]


def test_pop_max():
    heap = MaxHeap([16, 14, 10, 8, 9, 7, 2, 1])
    assert heap.pop_max() == 16
    assert heap.pop_max() == 14
    assert heap.pop_max() == 10
    assert heap.pop_max() == 9
    assert heap.pop_max() == 8
    assert heap.pop_max() == 7
    assert heap.pop_max() == 2
    assert heap.pop_max() == 1
    assert heap.empty()


def test_inorder():
    heap = MaxHeap([16, 14, 10, 8, 9, 7, 2, 1])
    inorder = [1, 8, 14, 9, 16, 7, 10, 2]
    for i, item in enumerate(heap.inorder()):
        assert item == inorder[i]


def test_preorder():
    heap = MaxHeap([16, 14, 10, 8, 9, 7, 2, 1])
    preorder = [16, 14, 8, 1, 9, 10, 7, 2]
    for i, item in enumerate(heap.preorder()):
        assert item == preorder[i]


def test_postorder():
    heap = MaxHeap([16, 14, 10, 8, 9, 7, 2, 1])
    postorder = [1, 8, 9, 14, 7, 2, 10, 16]
    for i, item in enumerate(heap.postorder()):
        assert item == postorder[i]


def test_eval():
    heap = MaxHeap([1, 2, 3, 4, 5, 6])
    heap_eval = eval(repr(heap))
    assert heap.heap == heap_eval.heap
