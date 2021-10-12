import pytest
from dsa.linkedlist.singly import SinglyLinkedList
from dsa.linkedlist.singly_tail import SinglyTailLinkedList
from dsa.linkedlist.doubly import DoublyLinkedList


@pytest.mark.parametrize("linked_list", [
    SinglyLinkedList,
    SinglyTailLinkedList,
    DoublyLinkedList,
])
def test_create_read_delete(linked_list):
    obj = linked_list()
    obj.push_front(1)
    obj.push_front(2)
    obj.push_front(3)
    assert obj.length() == 3
    assert obj.top_front() == 3
    assert obj.find(2)
    assert obj.top_back() == 1
    obj.pop_front()
    obj.pop_front()
    assert obj.top_front() == 1
    assert obj.top_front() == obj.top_back()
    assert obj.length() == 1
    obj.push_back(2)
    obj.push_back(3)
    assert obj.length() == 3
    assert obj.top_front() == 1
    assert obj.find(2)
    assert obj.top_back() == 3
    obj.pop_back()
    obj.pop_back()
    assert obj.top_front() == 1
    assert obj.top_front() == obj.top_back()
    assert obj.length() == 1
    obj.pop_back()
    assert obj.length() == 0
    obj.push_front(1)
    obj.pop_front()
    assert obj.length() == 0


@pytest.mark.parametrize("linked_list", [
    SinglyLinkedList,
    SinglyTailLinkedList,
    DoublyLinkedList,
])
def test_length(linked_list):
    obj = linked_list()
    for x in range(50):
        obj.push_back(x)

    assert obj.length() == 50
    assert obj.top_front() == 0
    assert obj.top_back() == 49

    for x in range(21):
        obj.push_front(x)

    assert obj.length() == 71
    assert obj.top_front() == 20
    assert obj.top_back() == 49


@pytest.mark.parametrize("linked_list", [
    SinglyLinkedList,
    SinglyTailLinkedList,
    DoublyLinkedList,
])
def test_find(linked_list):
    obj = linked_list()
    for x in range(50):
        obj.push_back(x)

    assert obj.find(0)
    assert obj.find(13)
    assert obj.find(49)
    assert not obj.find(50)
    assert not obj.find(-1)


@pytest.mark.parametrize("linked_list", [
    SinglyLinkedList,
    SinglyTailLinkedList,
    DoublyLinkedList,
])
def test_erase(linked_list):
    obj = linked_list()
    for x in range(5):
        obj.push_back(x)

    obj.erase(4)
    obj.erase(0)
    obj.erase(2)
    assert obj.top_back() == 3
    assert obj.top_front() == 1
    assert not obj.find(2)
    assert obj.length() == 2
    assert str(obj) == "[1, 3]"
    obj.erase(1)
    assert obj.length() == 1
    obj.erase(3)
    assert obj.length() == 0
    obj.erase(3)
    assert obj.length() == 0


@pytest.mark.parametrize("linked_list", [
    SinglyLinkedList,
    SinglyTailLinkedList,
    DoublyLinkedList,
])
def test_empty(linked_list):
    obj = linked_list()
    assert obj.empty()
    obj.push_front(1)
    assert not obj.empty()


@pytest.mark.parametrize("linked_list", [
    SinglyLinkedList,
    SinglyTailLinkedList,
    DoublyLinkedList,
])
def test_repr(linked_list):
    a = linked_list()
    b = eval(repr(a))
    assert isinstance(b, linked_list)
