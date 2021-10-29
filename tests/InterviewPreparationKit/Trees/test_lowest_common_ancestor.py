from typing import Optional
from unittest import TestCase

from src.InterviewPreparationKit.Trees.lowest_common_ancestor import lca, Node


def insert(root: Node, data: int) -> Node:
    if root:
        if data <= root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
        return root
    return Node(data)


def get_root(arr: list) -> Node:
    root: Optional[Node] = None
    for i in arr:
        root = insert(root, i)
    return root


class Test(TestCase):
    def test_lca_1(self):
        self.assertEqual(4, lca(get_root([4, 2, 7, 1, 3, 6]), 1, 7).data)

    def test_lca_2(self):
        self.assertEqual(1, lca(get_root([1, 2]), 1, 2).data)

    def test_lca_3(self):
        self.assertEqual(5, lca(get_root([5, 3, 8, 2, 4, 6, 7]), 7, 3).data)
