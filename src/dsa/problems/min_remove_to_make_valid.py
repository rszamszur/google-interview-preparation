"""https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses"""


def min_remove_to_make_valid(s):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        s(str): Given a string s of '(' , ')' and lowercase English characters.

    Returns:
        Remove the minimum number of parentheses ( '(' or ')', in any positions
        ) so that the resulting parentheses string is valid and return any
        valid string.

    """
    s = list(s)
    stack = []

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                s[i] = ""

    while stack:
        s[stack.pop()] = ""

    return "".join(s)
