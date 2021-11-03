import pytest
from dsa.problems.word_search import word_search


@pytest.mark.parametrize("board, list, expected", [
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
    ([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS", True),
])
def test_word_search(board, list, expected):
    assert word_search(board, list) == expected
