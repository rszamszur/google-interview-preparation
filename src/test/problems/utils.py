from collections import deque


def assert_trees_equal(tree, tree2):
    queue = deque()
    queue.append((tree, tree2))

    while queue:
        a, b = queue.popleft()
        assert a.val == b.val

        if a.left:
            queue.append((a.left, b.left))

        if a.right:
            queue.append((a.right, b.right))


def recreate_binary_tree(array_data, node_class):
    root = node_class(val=array_data.pop(0))
    queue = deque()
    queue.append(root)

    while array_data:
        parent = queue.popleft()
        left = array_data.pop(0)
        right = array_data.pop(0) if array_data else None

        if left:
            parent.left = node_class(val=left)
            queue.append(parent.left)
        if right:
            parent.right = node_class(val=right)
            queue.append(parent.right)

    return root
