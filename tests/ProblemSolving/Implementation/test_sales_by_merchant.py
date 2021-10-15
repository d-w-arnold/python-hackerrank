from unittest import TestCase

from src.ProblemSolving.Implementation.sales_by_merchant import sock_merchant


class Test(TestCase):
    def test_sock_merchant_1(self):
        self.assertEqual(2, sock_merchant(7, [1, 2, 1, 2, 1, 3, 2]))

    def test_sock_merchant_2(self):
        self.assertEqual(3, sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
