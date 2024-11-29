from unittest import TestCase

from src.Algorithms.Implementation.bigger_is_greater import bigger_is_greater


class Test(TestCase):
    def test_solve_1(self):
        self.assertEqual("abdc", bigger_is_greater("abcd"))

    def test_solve_2(self):
        self.assertEqual("ba", bigger_is_greater("ab"))

    def test_solve_3(self):
        self.assertEqual("no answer", bigger_is_greater("bb"))

    def test_solve_4(self):
        self.assertEqual("hegf", bigger_is_greater("hefg"))

    def test_solve_5(self):
        self.assertEqual("dhkc", bigger_is_greater("dhck"))

    def test_solve_6(self):
        self.assertEqual("hcdk", bigger_is_greater("dkhc"))

    def test_solve_7(self):
        self.assertEqual("lmon", bigger_is_greater("lmno"))

    def test_solve_8(self):
        self.assertEqual("no answer", bigger_is_greater("dcba"))

    def test_solve_9(self):
        self.assertEqual("no answer", bigger_is_greater("dcbb"))

    def test_solve_10(self):
        self.assertEqual("acbd", bigger_is_greater("abdc"))

    def test_solve_11(self):
        self.assertEqual("abdc", bigger_is_greater("abcd"))

    def test_solve_12(self):
        self.assertEqual("fedcbabdc", bigger_is_greater("fedcbabcd"))
