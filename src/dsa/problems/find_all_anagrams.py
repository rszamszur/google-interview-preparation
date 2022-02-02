"""https://leetcode.com/problems/find-all-anagrams-in-a-string"""


def find_all_anagrams(s, p):
    """Find all anagrams in a string.

    Time complexity: O(s + p)
    Space complexity: O(s + p)

    Args:
        s(str): String to search in.
        p(str): Anagram pattern to find in provided string.

    Returns:
         An array of all the start indices of p's anagrams in s.

    """
    result = []
    p_hash = sum(hash(char) for char in p)
    rolling_hash = sum(hash(char) for char in s[:len(p)])

    for i in range(len(s) - len(p) + 1):
        if p_hash == rolling_hash:
            result.append(i)

        if i >= len(s) - len(p):
            break

        rolling_hash -= hash(s[i])
        rolling_hash += hash(s[i + len(p)])

    return result
