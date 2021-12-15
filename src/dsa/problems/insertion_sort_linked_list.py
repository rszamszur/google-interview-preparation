"""https://leetcode.com/problems/insertion-sort-list"""


# Keeping just for ListNode reference sake, and tests.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertion_sort(head):
    """
    Time complexity: O(n^2)
    Space complexity: O(n)

    Args:
        head(Optional[ListNode]): A head of a singly linked list.

    Returns:
        Sort the list using insertion sort, and return the sorted list's head.

    """
    if not head:
        return None

    head_ref = ListNode(val=float("-inf"), next=head)
    last_sorted = head
    node = head.next

    while node:
        if node.val < last_sorted.val:
            prev = head_ref

            while prev.next.val <= node.val:
                prev = prev.next

            last_sorted.next = node.next
            node.next = prev.next
            prev.next = node
        else:
            last_sorted = last_sorted.next

        node = last_sorted.next

    return head_ref.next
