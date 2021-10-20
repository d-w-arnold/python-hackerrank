from unittest import TestCase

from src.ProblemSolving.Warmup.time_conversion import time_conversion


class Test(TestCase):
    def test_time_conversion_1(self):
        self.assertEqual("12:01:00", time_conversion("12:01:00PM"))

    def test_time_conversion_2(self):
        self.assertEqual("00:01:00", time_conversion("12:01:00AM"))

    def test_time_conversion_3(self):
        self.assertEqual("19:05:45", time_conversion("07:05:45PM"))

    def test_time_conversion_4(self):
        self.assertEqual("07:05:45", time_conversion("07:05:45AM"))
