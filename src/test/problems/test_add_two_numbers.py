from dsa.problems.add_two_numbers import add_two_numbers, ListNode


def test_add_two_numbers():
    l1 = ListNode(val=2)
    l1.next = ListNode(val=4)
    l1.next.next = ListNode(val=3)

    l2 = ListNode(val=5)
    l2.next = ListNode(val=6)
    l2.next.next = ListNode(val=4)

    result = add_two_numbers(l1, l2)

    assert result.val == 7
    assert result.next.val == 0
    assert result.next.next.val == 8
