from unittest import TestCase

from src.ProblemSolving.Implementation.save_the_prisoner import save_the_prisoner


class Test(TestCase):
    def test_save_the_prisoner_1(self):
        self.assertEqual(3, save_the_prisoner(4, 6, 2))

    def test_save_the_prisoner_2(self):
        self.assertEqual(2, save_the_prisoner(5, 2, 1))

    def test_save_the_prisoner_3(self):
        self.assertEqual(3, save_the_prisoner(5, 2, 2))

    def test_save_the_prisoner_4(self):
        self.assertEqual(6, save_the_prisoner(7, 19, 2))

    def test_save_the_prisoner_5(self):
        self.assertEqual(3, save_the_prisoner(3, 7, 3))

    def test_save_the_prisoner_6(self):
        self.assertEqual(122129406, save_the_prisoner(352926151, 380324688, 94730870))

    def test_save_the_prisoner_7(self):
        self.assertEqual(356482915, save_the_prisoner(715950220, 876882456, 195550680))
