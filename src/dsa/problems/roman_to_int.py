"""https://leetcode.com/problems/roman-to-integer/"""


def roman_to_int(s):
    """
    Time complexity: O(n*log(n))
    Space complexity: O(n*log(n))

    :type s: str
    :rtype: int
    """
    stack = [
        ("I", 1),
        ("V", 5),
        ("IV", 4),
        ("X", 10),
        ("IX", 9),
        ("L", 50),
        ("XL", 40),
        ("C", 100),
        ("XC", 90),
        ("D", 500),
        ("CD", 400),
        ("M", 1000),
        ("CM", 900),
    ]

    value = 0
    while s:
        count = s.count(stack[-1][0])
        if count > 0:
            value += count * stack[-1][1]
            s = s.replace(stack[-1][0], "")
        stack.pop()

    return value
