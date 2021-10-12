import pytest
from stack_array import ArrayStack
from stack_linked_list import LinkedListStack


@pytest.mark.parametrize("stack", [
    ArrayStack(5),
    LinkedListStack()
])
def test_stacks(stack):
    assert stack.empty()
    with pytest.raises(IndexError):
        stack.pop()
        stack.top()

    stack.push(1)
    assert stack.top() == 1
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    assert stack.top() == 5

    if isinstance(stack, ArrayStack):
        with pytest.raises(IndexError):
            stack.push(6)

    stack.pop()
    assert stack.top() == 4
    stack.pop()
    assert stack.top() == 3
    stack.pop()
    assert stack.top() == 2
    stack.pop()
    assert stack.top() == 1
    stack.pop()
    assert stack.empty()

    obj = eval(repr(stack))
    stack_type = type(stack)
    assert isinstance(stack, stack_type) == isinstance(obj, stack_type)
    assert stack.__dict__ == obj.__dict__
