import pytest
from dsa.problems.merge_intervals import merge_intervals


@pytest.mark.parametrize("intervals, expected", [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),
    ([[1,4],[2,3]], [[1,4]]),
])
def test_merge_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected
