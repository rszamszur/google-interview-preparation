"""https://leetcode.com/problems/longest-palindromic-substring"""


def longest_palindrome(s):
    """
    Time complexity: O(n*log(n)) or O(n^2) not quite sure.
    Space complexity: O(n)

    Args:
        s(str): Given string.

    Returns:
        The longest palindromic substring in s.

    """
    if len(s) < 2:
        return s[0]

    rs = s[::-1]

    for window in reversed(range(2, len(s) + 1)):
        i = 0

        while i + window <= len(s):
            if i == 0:
                end = None
            else:
                end = -i

            if s[i:i + window] == rs[-(i + window):end]:
                return s[i:i + window]

            i += 1

    return s[0]
