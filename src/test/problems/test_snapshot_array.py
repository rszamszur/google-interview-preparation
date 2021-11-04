from dsa.problems.snapshot_array import SnapshotArray


def test_snapshot_array():
    obj = SnapshotArray(3)
    obj.set(1, 6)
    assert obj.snap() == 0
    assert obj.snap() == 1
    obj.set(1, 19)
    obj.set(0, 4)
    assert obj.get(2, 1) == 0
    assert obj.get(2, 0) == 0
    assert obj.get(0, 1) == 0
    assert obj.get(1, 0) == 6
    assert obj.get(1, 2) == 19
    assert obj.get(0, 2) == 4
    assert obj.snap() == 2
    obj.set(2, 2)
    obj.set(2, 3)
    obj.set(2, 4)
    assert obj.get(2, 3) == 4
