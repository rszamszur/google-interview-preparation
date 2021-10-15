"""https://leetcode.com/problems/longest-common-prefix/"""


def longest_common_prefix(strs):
    """
    Time complexity: O(S) S -> sum of all characters in all strings
    Space complexity: O(1)

    Args:
        strs(List[str]): array of strings

    Returns:
        The longest common prefix string amongst an array of strings
    """
    prefix = ""
    if len(strs) < 1:
        return prefix

    for i, char in enumerate(min(strs, key=len)):
        if all(char in item[i] for item in strs):
            prefix += char
            continue

        break

    return prefix
