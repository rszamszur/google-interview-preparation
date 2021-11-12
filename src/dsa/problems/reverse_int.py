"""https://leetcode.com/problems/reverse-integer"""


def reverse_int(x):
    """
    Time complexity: O(log(n))
    Space complexity: O(1)

    Args:
        x(int): Signed 32-bit integer.

    Returns:
        Reversed integer.

    """
    rev_int = ""

    if x < 0:
        rev_int = "-"
        x = abs(x)

    stack = list(str(x))

    while stack:
        rev_int += stack.pop()

    if -(2 ** 31) < int(rev_int) < (2 ** 31) - 1:
        return int(rev_int)

    return 0
