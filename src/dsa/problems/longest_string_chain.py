"""https://leetcode.com/problems/longest-string-chain"""


def longest_string_chain(words):
    """
    Time complexity: O(n*(log(n) + l^2))
    Where l is the maximum possible length of a word.
    1) Sorting a list of size n takes O(n*(log(n)) time.
    2) Two for loops in which the outer loop runs for O(n) iterations and the
    inner loop runs for O(l^2) iterations in the worst case scenario.
    Space complexity: O(n)

    Args:
        words(List[str]): Array of words where each word consists of lowercase
            English letters.

    Returns:
        The longest possible word chain with words chosen from the given list.

    """
    count = 0
    ht = dict()

    for word in sorted(words, key=len):
        word_ord = sum(ord(c) for c in word)

        for key in list(ht.keys()):
            if len(key) + 1 == len(word):
                char = chr(abs(word_ord - ht[key][1]))

                if key.replace(char, "") == word.replace(char, ""):
                    if word not in ht:
                        ht[word] = [1, word_ord]
                    ht[word][0] = max(ht[word][0], 1 + ht[key][0])
                    count = max(count, ht[word][0])
                    continue
            elif len(key) + 1 > len(word):
                continue
            else:
                del ht[key]

        if word not in ht:
            ht[word] = [1, word_ord]
            count = max(count, 1)

    return count
