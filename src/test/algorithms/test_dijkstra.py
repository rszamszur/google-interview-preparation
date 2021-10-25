import pytest
from dsa.algorithms.dijkstra import dijkstra


g1 = {
    "A": [["B", 2], ["C", 5]],
    "B": [["A", 2], ["D", 3], ["E", 1], ["F", 1]],
    "C": [["A", 5], ["F", 3]],
    "D": [["B", 3]],
    "E": [["B", 4], ["F", 3]],
    "F": [["C", 3], ["E", 3]],
}

g2 = {
    "B": [["C", 1]],
    "C": [["D", 1]],
    "D": [["F", 1]],
    "E": [["B", 1], ["F", 3]],
    "F": [],
}

g3 = {
    "B": [["C", 1]],
    "C": [["D", 1]],
    "D": [["F", 1]],
    "E": [["B", 1], ["G", 2]],
    "F": [],
    "G": [["F", 1]],
}


@pytest.mark.parametrize("graph, start, end, expected", [
    (g1, "E", "C", 6),
    (g2, "E", "F", 3),
    (g3, "E", "F", 3),
])
def test_dijkstra(graph, start, end, expected):
    dijkstra(graph, start, end) == expected
