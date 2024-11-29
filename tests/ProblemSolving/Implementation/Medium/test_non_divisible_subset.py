from unittest import TestCase

from src.ProblemSolving.Implementation.Medium.non_divisible_subset import non_divisible_subset


class Test(TestCase):
    def test_non_divisible_subset_1(self):
        self.assertEqual(3, non_divisible_subset(4, [19, 10, 12, 10, 24, 25, 22]))

    def test_non_divisible_subset_2(self):
        self.assertEqual(3, non_divisible_subset(3, [1, 7, 2, 4]))

    def test_non_divisible_subset_3(self):
        self.assertEqual(
            11, non_divisible_subset(7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436])
        )
