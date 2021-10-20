from unittest import TestCase

from src.InterviewPreparationKit.GreedyAlgorithms.Medium.greedy_florist import get_min_cost


class Test(TestCase):
    def test_get_min_cost_1(self):
        self.assertEqual(11, get_min_cost(3, [1, 2, 3, 4]))

    def test_get_min_cost_2(self):
        self.assertEqual(13, get_min_cost(3, [2, 5, 6]))

    def test_get_min_cost_3(self):
        self.assertEqual(15, get_min_cost(2, [2, 5, 6]))

    def test_get_min_cost_4(self):
        self.assertEqual(29, get_min_cost(3, [1, 3, 5, 7, 9]))

    def test_get_min_cost_5(self):
        self.assertEqual(163578911, get_min_cost(3,
                                                 [390225, 426456, 688267, 800389, 990107, 439248, 240638, 15991, 874479,
                                                  568754, 729927, 980985, 132244, 488186, 5037, 721765, 251885, 28458,
                                                  23710, 281490, 30935, 897665, 768945, 337228, 533277, 959855, 927447,
                                                  941485, 24242, 684459, 312855, 716170, 512600, 608266, 779912, 950103,
                                                  211756, 665028, 642996, 262173, 789020, 932421, 390745, 433434,
                                                  350262, 463568, 668809, 305781, 815771, 550800]))

    def test_get_min_cost_6(self):
        self.assertEqual(30352414, get_min_cost(34,
                                                [433515, 22221, 540709, 538312, 496949, 902471, 439983, 159332, 417327,
                                                 399306, 817804, 354682, 108825, 970689, 868286, 235070, 18732, 848955,
                                                 994152, 741000, 722232, 564879, 503093, 734475, 174795, 129065, 483929,
                                                 683440, 37645, 670198, 911023, 40334, 329513, 669160, 180034, 285512,
                                                 401190, 629798, 857703, 765572, 174164, 849299, 159367, 62467, 84449,
                                                 523962, 735995, 245666, 832139, 879827, 749840, 315756, 253168, 659252,
                                                 187178]))
