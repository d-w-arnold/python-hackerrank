from unittest import TestCase

from src.InterviewPreparationKit.StringManipulation.Medium.special_string_again import sub_str_count


class Test(TestCase):
    def test_sub_str_count_1(self):
        self.assertEqual(12, sub_str_count(8, "mnonopoo"))

    def test_sub_str_count_2(self):
        self.assertEqual(7, sub_str_count(5, "asasd"))

    def test_sub_str_count_3(self):
        self.assertEqual(10, sub_str_count(7, "abcbaba"))

    def test_sub_str_count_4(self):
        self.assertEqual(10, sub_str_count(4, "aaaa"))
