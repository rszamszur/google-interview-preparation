"""https://leetcode.com/problems/add-digits"""


def add_digits(num):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        num(int): Given an integer num.

    Returns:
        Repeatedly add all its digits until the result has only one digit, and
        return it.

    """
    while num >= 10:
        num = sum([int(char) for char in str(num)])

    return num
