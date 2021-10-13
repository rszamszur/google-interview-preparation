# https://leetcode.com/problems/valid-parentheses/


def valid_parenthesis(s):
    """Time complexity: O(n)"""
    stack = []
    brackets = {
        "{": "}",
        "[": "]",
        "(": ")",
    }
    for char in s:
        if char in brackets:
            stack.append(char)
            continue

        if not stack or brackets[stack.pop()] != char:
            return False

    return not stack
