"""https://leetcode.com/problems/maximal-square"""


def maximal_square(matrix):
    """
    Time complexity: O(m * n)
    Space complexity: O(1)

    Args:
        matrix(List[List[str]]): m x n binary matrix filled with 0's and 1's.

    Returns:
        Area of the largest square containing only 1's.

    """
    matrix = [[int(val) for val in row] for row in matrix]
    max_a = max(
        max(matrix[0]),
        max(matrix[x][0] for x in range(len(matrix)))
    )

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

                max_a = max(max_a, matrix[i][j])

    return max_a ** 2
