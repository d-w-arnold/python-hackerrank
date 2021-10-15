from unittest import TestCase

from captured_output import captured_output
from src.ProblemSolving.Warmup.plus_minus import plus_minus


class Test(TestCase):
    def test_plus_minus_1(self):
        with captured_output() as (out, err):
            plus_minus([1, 1, 0, -1, -1])
        self.assertEqual("0.400000\n0.400000\n0.200000", out.getvalue().strip())

    def test_plus_minus_2(self):
        with captured_output() as (out, err):
            plus_minus([-4, 3, -9, 0, 4, 1])
        self.assertEqual("0.500000\n0.333333\n0.166667", out.getvalue().strip())
