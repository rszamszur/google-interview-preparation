from singly import SinglyLinkedList


def test_create_read_delete():
    sll = SinglyLinkedList()
    sll.push_front(1)
    sll.push_front(2)
    assert sll.length() == 2
    assert sll.top_front() == 2
    assert sll.top_back() == 1
    sll.pop_front()
    assert sll.top_front() == 1
    assert sll.top_front() == sll.top_back()
    assert sll.length() == 1
    sll.push_back(2)
    assert sll.length() == 2
    assert sll.top_front() == 1
    assert sll.top_back() == 2
    sll.pop_back()
    assert sll.top_front() == 1
    assert sll.top_front() == sll.top_back()
    assert sll.length() == 1


def test_length():
    sll = SinglyLinkedList()
    for x in range(50):
        sll.push_back(x)

    assert sll.length() == 50
    assert sll.top_front() == 0
    assert sll.top_back() == 49

    for x in range(21):
        sll.push_front(x)

    assert sll.length() == 71
    assert sll.top_front() == 20
    assert sll.top_back() == 49


def test_find():
    sll = SinglyLinkedList()
    for x in range(50):
        sll.push_back(x)

    assert sll.find(0)
    assert sll.find(13)
    assert sll.find(49)
    assert not sll.find(50)
    assert not sll.find(-1)


def test_erase():
    sll = SinglyLinkedList()
    for x in range(50):
        sll.push_back(x)

    sll.erase(49)
    sll.erase(0)
    sll.erase(13)
    assert sll.top_back() == 48
    assert sll.top_front() == 1
    assert not sll.find(13)
    assert sll.length() == 47


def test_empty():
    sll = SinglyLinkedList()
    assert sll.empty()
    sll.push_front(1)
    assert not sll.empty()


def test_repr():
    a = SinglyLinkedList()
    b = eval(repr(a))
    assert isinstance(b, SinglyLinkedList)
