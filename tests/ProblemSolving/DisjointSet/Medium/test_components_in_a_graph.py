from unittest import TestCase

from src.ProblemSolving.DisjointSet.Medium.components_in_a_graph import components_in_graph


class Test(TestCase):
    def test_components_in_graph_1(self):
        self.assertEqual([2, 3], components_in_graph([
            [1, 5],
            [1, 6],
            [2, 4]
        ]))

    def test_components_in_graph_2(self):
        self.assertEqual([2, 4], components_in_graph([
            [1, 6],
            [2, 7],
            [3, 8],
            [4, 9],
            [2, 6],
        ]))
