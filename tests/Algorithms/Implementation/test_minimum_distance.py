from unittest import TestCase

from src.Algorithms.Implementation.minimum_distance import minimum_distance


class Test(TestCase):
    def test_solve_1(self):
        self.assertEqual(3, minimum_distance([7, 1, 3, 4, 1, 7]))

    def test_solve_2(self):
        self.assertEqual(-1, minimum_distance([1, 2, 3, 4, 10]))
