"""https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/"""


def min_partitions(n):
    """
    Time complexity: O(len(n))
    Space complexity: O(1)

    Args:
        n (str): Given a string, that represents a positive decimal integer.

    Returns:
        The minimum number of positive deci-binary numbers needed so that they
        sum up to n. A decimal number is called deci-binary if each of its
        digits is either 0 or 1 without any leading zeros. For example, 101
        and 1100 are deci-binary, while 112 and 3001 are not.

    """
    return int(max(n))
