from unittest import TestCase

from src.ProblemSolving.Advanced.Medium.find_max_index_prod import solve


class Test(TestCase):
    def test_solve_1(self):
        self.assertEqual(8, solve([5, 4, 3, 4, 5]))
