"""https://leetcode.com/problems/integer-to-roman/"""
import math


def int_to_roman(num):
    """
    Time complexity: O(n*log(n))
    Space complexity: O(n*log(n))

    :type num: int
    :rtype: str
    """
    stack = [
        ("I", 1),
        ("IV", 4),
        ("V", 5),
        ("IX", 9),
        ("X", 10),
        ("XL", 40),
        ("L", 50),
        ("XC", 90),
        ("C", 100),
        ("CD", 400),
        ("D", 500),
        ("CM", 900),
        ("M", 1000),
    ]

    roman = ""
    while num > 0:
        count = math.floor(num / stack[-1][1])
        if count > 0:
            roman += stack[-1][0] * count
            num -= stack[-1][1] * count
        stack.pop()

    return roman