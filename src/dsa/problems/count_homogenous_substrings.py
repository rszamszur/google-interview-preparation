"""https://leetcode.com/problems/count-number-of-homogenous-substrings"""


def count_homogenous_substrings(s):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        s(str): Given string.

    Returns:
        The number of homogenous substrings of s. Since the answer may be too
        large, return it modulo 10^9 + 7.

    """
    result = 0
    sub_len = 1

    for i, char in enumerate(s[1:], start=1):
        if char == s[i - 1]:
            sub_len += 1
            continue

        result += (sub_len * (sub_len + 1) // 2)
        sub_len = 1

    result += (sub_len * (sub_len + 1) // 2)

    return result % ((10 ** 9) + 7)
