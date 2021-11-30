"""https://leetcode.com/problems/maximal-rectangle"""


def max_rectangle(matrix):
    """
    Time complexity: O(n^2)
    Space complexity: O(1)

    Args:
        matrix(List[List[str]]): Binary matrix filled with 0's and 1's.

    Returns:
        The area of the largest rectangle containing only 1's.

    """
    area = 0

    for i, row in enumerate(matrix):
        if (len(matrix) - i) * len(matrix[i]) <= area:
            break
        elif "1" not in row:
            continue

        for j, value in enumerate(row):
            if (len(matrix) - i) * len(matrix[i]) - j <= area:
                break
            elif value == "1":
                a = 0
                b = float("inf")

                while j + a < len(row):
                    if matrix[i][j + a] == "0":
                        break

                    curr_b = 0

                    for x in range(i, len(matrix)):
                        if matrix[x][j + a] != "1":
                            break

                        curr_b += 1

                    area = max(area, a * b)
                    b = min(b, curr_b)
                    a += 1

                area = max(area, a * b)

    return area
