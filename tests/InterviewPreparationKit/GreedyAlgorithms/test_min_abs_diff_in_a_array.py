from unittest import TestCase

from src.InterviewPreparationKit.GreedyAlgorithms.min_abs_diff_in_a_array import min_abs_diff


class Test(TestCase):
    def test_min_abs_diff_1(self):
        self.assertEqual(2, min_abs_diff([-2, 2, 4]))

    def test_min_abs_diff_2(self):
        self.assertEqual(3, min_abs_diff([3, -7, 0]))

    def test_min_abs_diff_3(self):
        self.assertEqual(1, min_abs_diff([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))

    def test_min_abs_diff_4(self):
        self.assertEqual(3, min_abs_diff([1, -3, 71, 68, 17]))
