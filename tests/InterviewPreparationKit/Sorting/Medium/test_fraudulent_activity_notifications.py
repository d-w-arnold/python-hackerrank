from unittest import TestCase

from src.InterviewPreparationKit.Sorting.Medium.fraudulent_activity_notifications import activity_notifications


class Test(TestCase):
    def test_activity_notifications_1(self):
        self.assertEqual(1, activity_notifications([10, 20, 30, 40, 50], 3))

    def test_activity_notifications_2(self):
        self.assertEqual(2, activity_notifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))

    def test_activity_notifications_3(self):
        self.assertEqual(0, activity_notifications([1, 2, 3, 4, 4], 4))
