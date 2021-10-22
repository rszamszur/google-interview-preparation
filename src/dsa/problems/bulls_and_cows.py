"""https://leetcode.com/problems/bulls-and-cows"""
from collections import defaultdict


def get_hint(secret, guess):
    """Initial solution

    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        secret:
        guess:

    Returns:

    """
    bulls = []
    cows = 0
    char_map = dict()

    for i, item in enumerate(zip(secret, guess)):
        sc, gc = item
        if sc == gc:
            bulls.append(i)
            continue

        if not sc in char_map:
            char_map[sc] = 0

        char_map[sc] += 1

    for i, c in enumerate(guess):
        if i not in bulls and c in char_map and char_map[c] > 0:
            char_map[c] -= 1
            cows += 1

    return "{bulls}A{cows}B".format(bulls=len(bulls), cows=cows)


def get_hint_one_pass(secret, guess):
    ht = defaultdict(int)
    bulls = cows = 0

    for i, sc in enumerate(secret):
        gc = guess[i]

        if sc == gc:
            bulls += 1
        else:
            cows += int(ht[sc] < 0) + int(ht[gc] > 0)
            ht[sc] += 1
            ht[gc] -= 1

    return "{bulls}A{cows}B".format(bulls=bulls, cows=cows)
