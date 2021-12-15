import pytest
from dsa.problems.insertion_sort_linked_list import insertion_sort, ListNode


@pytest.mark.parametrize("vals, expected", [
    ([4, 2, 1, 3], [1, 2, 3, 4]),
    ([3, 2, 1], [1, 2, 3]),
    ([8, 10, 5, 3, 8], [3, 5, 8, 8, 10]),
    ([101, 12, 4, 3, 2, 0, -10], [-10, 0, 2, 3, 4, 12, 101]),
    ([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3]),
])
def test_insertion_sort(vals, expected):
    head = ListNode(val=vals.pop(0))
    node = head

    while vals:
        node.next = ListNode(val=vals.pop(0))
        node = node.next

    sorted_ll = insertion_sort(head)

    while sorted_ll:
        assert sorted_ll.val == expected.pop(0)
        sorted_ll = sorted_ll.next
