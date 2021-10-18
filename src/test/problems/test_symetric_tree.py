from dsa.problems.symetric_tree import is_symmetric, TreeNode


def test_is_symetric():
    root = TreeNode(val=1)
    n1 = TreeNode(val=2)
    n2 = TreeNode(val=2)
    root.left = n1
    root.right = n2
    n1.left = TreeNode(val=3)
    n2.right = TreeNode(val=3)
    n1.right = TreeNode(val=4)
    n2.left = TreeNode(val=4)

    assert is_symmetric(root)
    assert not is_symmetric(n1)
