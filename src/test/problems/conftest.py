from collections import deque

import pytest


@pytest.fixture(scope="function")
def recreate_binary_tree(request):
    input = request.param[0]
    node_class = request.param[1]
    root = node_class(val=input.pop(0))
    queue = deque()
    queue.append(root)

    while input:
        parent = queue.popleft()
        left = input.pop(0)
        right = input.pop(0)

        if left:
            parent.left = node_class(val=left)
            queue.append(parent.left)
        if right:
            parent.right = node_class(val=right)
            queue.append(parent.right)

    yield root
