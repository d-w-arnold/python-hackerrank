from unittest import TestCase

from src.Algorithms.Implementation.beautiful_triplets import beautiful_triplets


class Test(TestCase):
    def test_solve_1(self):
        self.assertEqual(3, beautiful_triplets(3, [1, 2, 4, 5, 7, 8, 10]))

    def test_solve_2(self):
        self.assertEqual(2, beautiful_triplets(3, [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]))
