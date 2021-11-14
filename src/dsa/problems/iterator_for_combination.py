"""https://leetcode.com/problems/iterator-for-combination"""
import collections
import itertools



class CombinationIterator:
    __slots__ = ("_combinations")

    def __init__(self, characters, characters_len):
        """
        Time complexity: O(r * (n choose r))
        https://stackoverflow.com/questions/53419536/what-is-the-computational-complexity-of-itertools-combinations-in-python
        Space complexity: O((n choose r))

        Args:
            characters(str): String characters of sorted distinct lowercase
                English letters
            characters_len(int): Combination length number.

        """
        self._combinations = collections.deque(
            itertools.combinations(characters, characters_len)
        )

    def next(self):
        """
        Time complexity: O(n)
        String function join costs O(n) where n is Combination length number.
        For deque poping on both sides is constant time.
        Space complexity: O(1)

        Returns:
            The next combination.

        """
        return "".join(self._combinations.popleft())

    def hasNext(self) -> bool:
        """
        Time complexity: O(1)
        Space complexity: O(1)

        Returns:
            True if and only if there exists a next combination.

        """
        return not not self._combinations
