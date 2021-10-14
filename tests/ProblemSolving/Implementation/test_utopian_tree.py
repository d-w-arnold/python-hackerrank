from unittest import TestCase

from src.ProblemSolving.Implementation.utopian_tree import utopian_tree


class Test(TestCase):
    def test_utopian_tree_1(self):
        self.assertEqual(1, utopian_tree(0))

    def test_utopian_tree_2(self):
        self.assertEqual(2, utopian_tree(1))

    def test_utopian_tree_3(self):
        self.assertEqual(7, utopian_tree(4))
