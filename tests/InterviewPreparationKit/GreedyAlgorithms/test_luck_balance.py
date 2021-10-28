from unittest import TestCase

from src.InterviewPreparationKit.GreedyAlgorithms.luck_balance import luck_balance


class Test(TestCase):
    def test_luck_balance_1(self):
        self.assertEqual(10, luck_balance(2, [
            [5, 1],
            [1, 1],
            [4, 0]
        ]))

    def test_luck_balance_2(self):
        self.assertEqual(29, luck_balance(3, [
            [5, 1],
            [2, 1],
            [1, 1],
            [8, 1],
            [10, 0],
            [5, 0]
        ]))

    def test_luck_balance_3(self):
        self.assertEqual(42, luck_balance(5, [
            [13, 1],
            [10, 1],
            [9, 1],
            [8, 1],
            [13, 1],
            [12, 1],
            [18, 1],
            [13, 1]
        ]))

    def test_luck_balance_4(self):
        self.assertEqual(21, luck_balance(2, [
            [5, 1],
            [4, 0],
            [6, 1],
            [2, 1],
            [8, 0]
        ]))
