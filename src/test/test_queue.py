import pytest
from dsa.queue.queue_array import ArrayQueue
from dsa.queue.queue_linked_list import LinkedListQueue


@pytest.mark.parametrize("queue", [
    ArrayQueue(3),
    LinkedListQueue(),
])
def test_queue(queue):
    assert queue.empty()
    with pytest.raises(IndexError):
        queue.dequeue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    if isinstance(queue, ArrayQueue):
        with pytest.raises(IndexError):
            queue.enqueue(4)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert not queue.empty()
    assert queue.dequeue() == 3
    assert queue.empty()

    obj = eval(repr(queue))
    queue_type = type(queue)
    assert isinstance(queue, queue_type) == isinstance(obj, queue_type)
    assert queue.__dict__ == obj.__dict__
