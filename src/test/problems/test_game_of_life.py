import pytest
from dsa.problems.game_of_life import game_of_life


@pytest.mark.parametrize("board, expected", [
    ([[1,1],[1,0]], [[1,1],[1,1]]),
    ([[0,1,0],[0,0,1],[1,1,1],[0,0,0]], [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]),
])
def test_game_of_life(board, expected):
    game_of_life(board)
    assert board == expected
