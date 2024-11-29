from unittest import TestCase

from src.Algorithms.Implementation.halloween_sale import how_many_games


class Test(TestCase):
    def test_solve_1(self):
        self.assertEqual(6, how_many_games(20, 3, 6, 80))

    def test_solve_2(self):
        self.assertEqual(7, how_many_games(20, 3, 6, 85))
