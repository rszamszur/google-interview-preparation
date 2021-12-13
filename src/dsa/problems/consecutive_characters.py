"""https://leetcode.com/problems/consecutive-characters"""


def consecutive_characters(s):
    """
    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        s(str): Given string.

    Returns:
         The maximum length of a non-empty substring that contains only one
         unique character.

    """
    power = cur_power = 1

    for i, char in enumerate(s[1:], start=1):
        if char != s[i - 1]:
            cur_power = 0

        cur_power += 1
        power = max(power, cur_power)

    return power
