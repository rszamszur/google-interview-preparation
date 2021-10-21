"""https://leetcode.com/problems/decode-string/"""


def decode_string(s):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        s(str): Encoded string.

    Returns:
        Decoded string.

    """
    decoded = ""
    stack = []
    curr_num = ""

    for c in s:
        if c.isdigit():
            curr_num += c
        elif c == "[":
            stack.append([decoded, int(curr_num)])
            decoded = ""
            curr_num = ""
        elif c == "]":
            prev, num = stack.pop()
            decoded = prev + num * decoded
        else:
            decoded += c

    return decoded
