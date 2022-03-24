"""https://leetcode.com/problems/add-two-numbers"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        l1(ListNode): Given non-empty linked lists representing non-negative
            integer.
        l2(ListNode): Given non-empty linked lists representing non-negative
            integer.

    Returns:
        Add the two numbers and return the sum as a linked list.

    """
    node = root = None
    for_next = 0

    while True:
        if l1 and l2:
            for_next, val = divmod((l1.val + l2.val + for_next), 10)
            l1 = l1.next
            l2 = l2.next
        elif l1 and not l2:
            for_next, val = divmod((l1.val + for_next), 10)
            l1 = l1.next
        elif not l1 and l2:
            for_next, val = divmod((l2.val + for_next), 10)
            l2 = l2.next
        else:
            if for_next > 0:
                node.next = ListNode(val=for_next)
            break

        if not node:
            node = ListNode(val=val)
            root = node
        else:
            node.next = ListNode(val=val)
            node = node.next

    return root
