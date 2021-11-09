"""https://leetcode.com/problems/count-square-submatrices-with-all-ones"""
import itertools


def count_squares(matrix):
    """
    Time complexity: O(m * n)
    Space complexity: O(1)

    Args:
        matrix(List[List[int]]): m * n matrix of ones and zeros.

    Returns:
        How many square submatrices have all ones.

    """
    for i in range(1, len(matrix)):
        if 1 not in matrix[i]:
            continue

        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] = 1 + min(
                    matrix[i - 1][j],
                    matrix[i][j - 1],
                    matrix[i - 1][j - 1]
                )

    return sum(itertools.chain(*matrix))
