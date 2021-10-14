"""https://leetcode.com/problems/asteroid-collision"""


class Solution(object):
    __slots__ = ()

    @staticmethod
    def direction(value):
        if value > 0:
            return 1

        return -1

    def asteroidCollision(self, asteroids):
        """
        Time complexity: O(n)
        Space complexity: O(1)

        :type asteroids: List[int]
        :rtype: List[int]
        """
        offset = 0

        while True:
            if offset < 0:
                offset = 0

            i = offset
            j = 1 + offset

            if j > len(asteroids) - 1:
                break

            if self.direction(asteroids[i]) - self.direction(asteroids[j]) != 2:
                offset += 1
                continue

            if abs(asteroids[i]) - abs(asteroids[j]) == 0:
                asteroids.pop(j)
                asteroids.pop(i)
                offset -= 2
                continue
            elif abs(asteroids[i]) - abs(asteroids[j]) < 0:
                asteroids.pop(i)
                offset -= 1
                continue
            else:
                asteroids.pop(j)
                continue

        return asteroids
