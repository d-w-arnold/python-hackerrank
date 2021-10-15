from unittest import TestCase

from captured_output import captured_output
from src.InterviewPreparationKit.Search.Medium.ice_cream_parlor import what_flavors


class Test(TestCase):
    def test_what_flavors_1(self):
        with captured_output() as (out, err):
            what_flavors([2, 1, 3, 5, 6], 5)
        self.assertEqual("1 3", out.getvalue().strip())

    def test_what_flavor_2(self):
        with captured_output() as (out, err):
            what_flavors([1, 4, 5, 3, 2], 4)
        self.assertEqual("1 4", out.getvalue().strip())

    def test_what_flavor_3(self):
        with captured_output() as (out, err):
            what_flavors([2, 2, 4, 3], 4)
        self.assertEqual("1 2", out.getvalue().strip())
