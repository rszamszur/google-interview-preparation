"""https://leetcode.com/problems/candy"""


def candy(ratings):
    """
    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        ratings (List[int]): Assigned a rating value given in the integer array
            ratings.

    Returns:
        The minimum number of candies you need to have to distribute the candies
        to the children.

    """
    l2r = [1] * len(ratings)
    r2l = [1] * len(ratings)

    for i in range(len(ratings) - 1):
        if ratings[i + 1] > ratings[i]:
            l2r[i + 1] = l2r[i] + 1

    for i in reversed(range(len(ratings) - 1)):
        if ratings[i] > ratings[i + 1]:
            r2l[i] = r2l[i + 1] + 1

    count = 0

    for x, y in zip(l2r, r2l):
        count += max(x, y)

    return count
