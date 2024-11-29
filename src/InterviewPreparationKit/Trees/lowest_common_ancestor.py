from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def lca(root: Node, v1: int, v2: int) -> Node:
    """
    Binary Search Tree : Lowest Common Ancestor: https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

    :param root: A pointer to the root node of a binary search tree.
    :param v1: A node.data value.
    :param v2: A node.data value.
    :return: A pointer to the lowest common ancestor node of the two values given.
    """
    if root.data > v1 and root.data > v2:
        return lca(root.left, v1, v2)
    if root.data < v1 and root.data < v2:
        return lca(root.right, v1, v2)
    return root
