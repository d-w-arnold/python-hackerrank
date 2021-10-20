from unittest import TestCase

from captured_output import captured_output
from src.InterviewPreparationKit.Arrays.Medium.new_year_chaos import min_bribes


class Test(TestCase):
    def test_min_bribes_1(self):
        with captured_output() as (out, err):
            min_bribes([1, 2, 3, 5, 4, 6, 7, 8])
        self.assertEqual("1", out.getvalue().strip())

    def test_min_bribes_2(self):
        with captured_output() as (out, err):
            min_bribes([4, 1, 2, 3])
        self.assertEqual("Too chaotic", out.getvalue().strip())

    def test_min_bribes_3(self):
        with captured_output() as (out, err):
            min_bribes([1, 2, 5, 3, 7, 8, 6, 4])
        self.assertEqual("7", out.getvalue().strip())
