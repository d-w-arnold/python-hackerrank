from unittest import TestCase

from src.InterviewPreparationKit.DictionariesAndHashmaps.Medium.count_triplets import count_triplets


class Test(TestCase):
    def test_count_triplets_1(self):
        self.assertEqual(2, count_triplets([1, 4, 16, 64], 4))

    def test_count_triplets_2(self):
        self.assertEqual(2, count_triplets([1, 2, 2, 4], 2))

    def test_count_triplets_3(self):
        self.assertEqual(6, count_triplets([1, 3, 9, 9, 27, 81], 3))

    def test_count_triplets_4(self):
        self.assertEqual(4, count_triplets([1, 5, 5, 25, 125], 5))

    def test_count_triplets_5(self):
        self.assertEqual(161700, count_triplets(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1))
