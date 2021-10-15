from unittest import TestCase

from src.InterviewPreparationKit.StacksAndQueues.Medium.min_max_riddle import riddle


class Test(TestCase):
    def test_riddle_1(self):
        self.assertEqual([12, 3, 3, 1, 1], riddle([6, 3, 5, 1, 12]))

    def test_riddle_2(self):
        self.assertEqual([12, 2, 1, 1], riddle([2, 6, 1, 12]))

    def test_riddle_3(self):
        self.assertEqual([13, 3, 2, 1, 1, 1, 1], riddle([1, 2, 3, 5, 1, 13, 3]))

    def test_riddle_4(self):
        self.assertEqual([7, 6, 4, 4, 3, 2], riddle([3, 5, 4, 7, 6, 2]))
