from unittest import TestCase

from src.InterviewPreparationKit.DictionariesAndHashmaps.Medium.sherlock_and_anagrams import sherlock_and_anagrams


class Test(TestCase):
    def test_sherlock_and_anagrams_1(self):
        self.assertEqual(4, sherlock_and_anagrams("abba"))

    def test_sherlock_and_anagrams_2(self):
        self.assertEqual(0, sherlock_and_anagrams("abcd"))

    def test_sherlock_and_anagrams_3(self):
        self.assertEqual(3, sherlock_and_anagrams("ifailuhkqq"))

    def test_sherlock_and_anagrams_4(self):
        self.assertEqual(10, sherlock_and_anagrams("kkkk"))

    def test_sherlock_and_anagrams_5(self):
        self.assertEqual(5, sherlock_and_anagrams("cdcd"))
