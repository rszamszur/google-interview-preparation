"""https://leetcode.com/problems/word-search"""


def word_search(board, word):
    """
    Time complexity: O(n*3^l)
    Where n is the number of cells in the board and l is the length of the
    word to be matched.
    Space complexity: O(n)

    Args:
        board(List[List[str]]): m x n grid of characters.
        word(str):

    Returns:
        True if word exists in the grid.

    """
    for m, row in enumerate(board):
        if word[0] not in row:
            continue

        for n, value in enumerate(board[m]):
            if value == word[0]:
                stack = [(m, n, 1, set())]

                while stack:
                    i, j, index, visited = stack.pop()
                    if index >= len(word):
                        return True

                    visited.add((i, j))
                    char = word[index]

                    if i > 0 and board[i - 1][j] == char:
                        if (i - 1, j) not in visited:
                            stack.append((i - 1, j, index + 1, visited.copy()))
                    if i + 1 < len(board) and board[i + 1][j] == char:
                        if (i + 1, j) not in visited:
                            stack.append((i + 1, j, index + 1, visited.copy()))
                    if j > 0 and board[i][j - 1] == char:
                        if (i, j - 1) not in visited:
                            stack.append((i, j - 1, index + 1, visited.copy()))
                    if j + 1 < len(board[0]) and board[i][j + 1] == char:
                        if (i, j + 1) not in visited:
                            stack.append((i, j + 1, index + 1, visited.copy()))

                    del visited

    return False
