from dsa.problems.max_freq_stack import FreqStack


def test_max_freq_stack():
    stack = FreqStack()
    stack.push(5)
    stack.push(7)
    stack.push(5)
    stack.push(7)
    stack.push(4)
    stack.push(5)
    assert stack.pop() == 5
    assert stack.pop() == 7
    assert stack.pop() == 5
    assert stack.pop() == 4
