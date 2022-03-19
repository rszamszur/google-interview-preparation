"""https://leetcode.com/problems/maximum-frequency-stack"""
import heapq
from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.count = defaultdict(lambda: 0)
        self.heap = []
        self.idx = 0

    def push(self, val):
        """
        Time complexity: O(n)
        Space complexity: O(n)

        Args:
            val(int): Given integer value.

        """
        self.count[val] += 1
        self.idx += 1
        heapq.heappush(self.heap, (-self.count[val], -self.idx, val))

    def pop(self):
        """
        Time complexity: O(n)
        Space complexity: O(n)

        Returns:
            Removes and returns the most frequent element in the stack. If there
             is a tie for the most frequent element, the element closest to the
             stack's top is removed and returned.

        """
        _, _, val = heapq.heappop(self.heap)
        self.count[val] -= 1

        return val
