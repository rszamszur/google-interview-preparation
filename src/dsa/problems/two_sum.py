def two_sum(nums, target):
    """https://leetcode.com/problems/two-sum/

    Time complexity: O(n)
    Space complexity: O(n)

    Store every element of the nums array in the map and check if there is an
    element in the dictionary that with the element at current index sums up
    to target.

    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_map = dict(
        zip(nums, range(len(nums)))
    )
    for i, num in enumerate(nums):
        try:
            j = nums_map[target - num]
            if j != i:
                return [i, j]
        except KeyError:
            pass

    return None


def two_sum_brute_force(nums, target):
    """Most obvious yet time complex solution.

    Time complexity: O(n^2)
    Space complexity: O(1)

    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums):
            if i == j:
                continue
            if (n1 + n2) == target:
                return [i, j]

    return None
