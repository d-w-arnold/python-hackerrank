from unittest import TestCase

from src.ProblemSolving.Implementation.breaking_the_records import breaking_records


class Test(TestCase):
    def test_breaking_records_1(self):
        self.assertEqual([1, 1], breaking_records([12, 24, 10, 24]))

    def test_breaking_records_2(self):
        self.assertEqual([2, 4], breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1]))
