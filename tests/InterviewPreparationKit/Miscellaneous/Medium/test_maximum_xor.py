from unittest import TestCase

from src.InterviewPreparationKit.Miscellaneous.Medium.maximum_xor import max_xor


class Test(TestCase):
    def test_max_xor_1(self):
        self.assertEqual([3, 7, 3], max_xor([0, 1, 2], [3, 7, 2]))

    def test_max_xor_2(self):
        self.assertEqual([7, 7], max_xor([5, 1, 7, 4, 3], [2, 0]))

    def test_max_xor_3(self):
        self.assertEqual([22, 7], max_xor([1, 3, 5, 7], [17, 6]))
