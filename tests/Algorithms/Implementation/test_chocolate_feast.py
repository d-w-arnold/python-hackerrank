from unittest import TestCase

from src.Algorithms.Implementation.chocolate_feast import chocolate_feast


class Test(TestCase):
    def test_solve_1(self):
        self.assertEqual(9, chocolate_feast(15, 3, 2))

    def test_solve_2(self):
        self.assertEqual(6, chocolate_feast(10, 2, 5))

    def test_solve_3(self):
        self.assertEqual(3, chocolate_feast(12, 4, 4))

    def test_solve_4(self):
        self.assertEqual(5, chocolate_feast(6, 2, 2))

    def test_solve_5(self):
        self.assertEqual(3, chocolate_feast(7, 3, 2))
