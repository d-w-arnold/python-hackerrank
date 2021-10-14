from unittest import TestCase

from src.ProblemSolving.Implementation.number_line_jumps import kangaroo


class Test(TestCase):
    def test_kangaroo_1(self):
        self.assertEqual("YES", kangaroo(2, 1, 1, 2))

    def test_kangaroo_2(self):
        self.assertEqual("YES", kangaroo(0, 3, 4, 2))

    def test_kangaroo_3(self):
        self.assertEqual("NO", kangaroo(1, 2, 3, 2))

    def test_kangaroo_4(self):
        self.assertEqual("NO", kangaroo(0, 2, 5, 3))
