import pytest
from dsa.problems.task_scheduler import task_scheduler


@pytest.mark.parametrize("tasks, n, expected", [
    (["A","A","A","B","B","B"], 2, 8),
    (["A","A","A","B","B","B"], 0, 6),
    (["A","A","A","A","A","A","B","C","D","E","F","G"], 2, 16),
    (["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2, 12),
])
def test_task_scheduler(tasks, n, expected):
    assert task_scheduler(tasks, n) == expected
