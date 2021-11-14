from src.dsa.problems.iterator_for_combination import CombinationIterator


def test_comination_iterator():
    obj = CombinationIterator("abc", 2)
    assert obj.next() == "ab"
    assert obj.hasNext()
    assert obj.next() == "ac"
    assert obj.hasNext()
    assert obj.next() == "bc"
    assert not obj.hasNext()
