from unittest import TestCase

from src.Algorithms.Implementation.larrys_array import larrys_array


class Test(TestCase):
    def test_solve_1(self):
        self.assertEqual("YES", larrys_array([1, 6, 5, 2, 4, 3]))

    def test_solve_2(self):
        self.assertEqual("YES", larrys_array([3, 1, 2]))

    def test_solve_3(self):
        self.assertEqual("YES", larrys_array([1, 3, 4, 2]))

    def test_solve_4(self):
        self.assertEqual("NO", larrys_array([1, 2, 3, 5, 4]))
