def valid_parenthesis(s):
    """https://leetcode.com/problems/valid-parentheses/

    Time complexity: O(n)
    Space complexity: O(n)

    :type s: str
    :rtype: bool
    """
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
