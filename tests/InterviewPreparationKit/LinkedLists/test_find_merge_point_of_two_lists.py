from unittest import TestCase

from src.InterviewPreparationKit.LinkedLists.find_merge_point_of_two_lists import find_merge_node, SinglyLinkedList


def build_linked_list(arr: list) -> SinglyLinkedList:
    linked_list: SinglyLinkedList = SinglyLinkedList()
    for i in arr:
        linked_list.insert_node(i)
    return linked_list


class Test(TestCase):
    def test_find_merge_node_1(self):
        list1: SinglyLinkedList = build_linked_list([1, 2, 3])
        list2: SinglyLinkedList = build_linked_list([1, 2, 3])
        self.assertEqual(2, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_2(self):
        list1: SinglyLinkedList = build_linked_list([1, 2, 3])
        list2: SinglyLinkedList = build_linked_list([1, 3])
        self.assertEqual(3, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_3(self):
        list1: SinglyLinkedList = build_linked_list([9])
        list2: SinglyLinkedList = build_linked_list(
            [2, 6, 6, 2, 5, 3, 2, 2, 9, 3, 10, 4, 1, 5, 9, 9, 5, 1, 8, 1, 6, 6, 9, 6, 8, 10, 10, 8, 3, 8, 1, 7, 6, 7, 8,
             10, 9, 9, 1, 9, 3, 3, 4, 3, 7, 4, 1, 3, 4, 1, 5, 1, 8, 5, 6, 5, 6, 7, 5, 1, 5, 5, 7, 2, 3, 4, 3, 3, 5, 5,
             1, 7, 9])
        self.assertEqual(9, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_4(self):
        list1: SinglyLinkedList = build_linked_list(
            [10, 5, 8, 2, 9, 2, 2, 5, 2, 10, 1, 10, 6, 7, 6, 10, 7, 2, 7, 5, 3, 9, 8, 5, 2, 2, 10, 2, 1, 8, 8, 2, 5, 6,
             3, 3, 9, 5, 10, 2, 6, 10, 1, 1, 8, 7, 3, 6, 8, 9, 10, 1, 9, 8, 7, 2, 1, 8, 6, 3, 6, 3, 4, 2, 10, 7, 4, 8,
             3, 5, 10, 10, 5, 10, 2, 2, 6])
        list2: SinglyLinkedList = build_linked_list(
            [8, 6, 4, 7, 6, 5, 6, 4, 6, 9, 2, 1, 1, 9, 4, 5, 2, 3, 3, 5, 3, 7, 2, 2, 6, 6, 1, 7, 7, 9, 3, 6, 4, 6, 3, 1,
             10, 10, 6, 8, 8, 9, 8, 1, 9, 3, 5, 10, 6, 9, 7, 8, 5, 8, 1, 10, 3, 3, 8, 1, 1, 10, 7, 6, 8, 1, 8, 9, 10, 4,
             6, 8, 2, 4, 8, 1, 8, 4, 10, 3, 4, 8, 2, 8, 5, 4, 9, 7, 7, 6, 10, 9, 8, 6, 10, 5, 10, 2, 2, 6])
        self.assertEqual(10, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_5(self):
        list1: SinglyLinkedList = build_linked_list(
            [6, 2, 5, 5, 7, 3, 4, 9, 8, 3, 1, 5, 8, 2, 10, 1, 10, 3, 10, 4, 7, 8, 3, 3, 6, 2, 3, 5, 9, 7, 1, 4, 1, 7,
             10])
        list2: SinglyLinkedList = build_linked_list(
            [1, 6, 7, 8, 10, 9, 3, 8, 1, 4, 10, 10, 6, 10, 5, 2, 9, 7, 6, 6, 10, 1, 10, 8, 9, 2, 3, 9, 1, 5, 10, 1, 10,
             6, 9, 1, 7, 3, 8, 7, 6, 10, 8, 3, 1, 2, 7, 9, 1, 2, 7, 10, 4, 6, 10, 3, 10, 2, 3, 10, 6, 2, 10, 7, 10, 10,
             8, 6, 2, 7, 4, 9, 6, 1, 2, 8, 4, 8, 7, 6, 1, 3, 8, 5, 10, 7, 7, 1, 10, 4, 9, 8, 3, 1, 5, 8, 2, 10, 1, 10,
             3, 10, 4, 7, 8, 3, 3, 6, 2, 3, 5, 9, 7, 1, 4, 1, 7, 10])
        self.assertEqual(4, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_6(self):
        list1: SinglyLinkedList = build_linked_list(
            [6, 3, 2, 4, 2, 1, 1, 7, 5, 8, 10, 3, 5, 2, 6, 5, 7, 5, 3, 3, 6, 7, 10, 2, 6, 8, 10, 7, 7, 8, 8, 4, 10, 9,
             8, 3, 2, 10, 9, 6, 7, 10, 10, 4, 1, 8, 8, 10, 2, 10, 2, 9, 8, 3, 10, 3, 10, 9, 1, 8, 9, 9, 2, 10, 9, 1, 3,
             10, 10, 3, 7, 9, 3, 9, 4, 5, 6, 1, 4, 9, 2, 7, 8, 9, 9, 7, 3, 10, 8])
        list2: SinglyLinkedList = build_linked_list(
            [8, 8, 6, 1, 7, 4, 1, 1, 6, 2, 4, 2, 10, 8, 2, 3, 4, 7, 5, 10, 6, 8, 6, 5, 8, 7, 3, 3, 6, 10, 8, 5, 7, 3, 7,
             6, 8, 9, 6, 3, 1, 1, 7, 2, 10, 8, 5, 4, 7, 1, 5, 4, 9, 10, 8, 6, 8, 10, 8, 6, 2, 7, 10, 8, 9, 9, 8])
        self.assertEqual(8, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_7(self):
        list1: SinglyLinkedList = build_linked_list(
            [7, 1, 1, 9, 3, 9, 1, 3, 7, 5, 8, 5, 5, 2, 8, 5, 3, 7, 3, 1, 6, 2, 6, 7, 9, 7, 7, 9, 5, 1, 7, 4, 3, 8, 2, 6,
             6, 2, 8, 4, 8, 7, 10])
        list2: SinglyLinkedList = build_linked_list(
            [8, 7, 9, 2, 5, 1, 4, 1, 3, 1, 9, 3, 10, 7, 1, 6, 8, 8, 9, 2, 7, 3, 7, 4, 6, 6, 10, 4, 2, 9, 8, 1, 8, 8, 5,
             2, 9, 8, 2, 3, 1, 3, 5, 10, 1, 5, 5, 8, 4, 6, 2, 10, 8, 8, 6, 8, 5, 5, 2, 8, 5, 3, 7, 3, 1, 6, 2, 6, 7, 9,
             7, 7, 9, 5, 1, 7, 4, 3, 8, 2, 6, 6, 2, 8, 4, 8, 7, 10])
        self.assertEqual(8, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_8(self):
        list1: SinglyLinkedList = build_linked_list([2, 10])
        list2: SinglyLinkedList = build_linked_list(
            [7, 9, 5, 9, 1, 10, 7, 7, 6, 9, 7, 2, 3, 2, 6, 3, 1, 10, 2, 4, 9, 3, 3, 8, 4, 2, 1, 4, 3, 10, 5, 1, 1, 2, 1,
             1, 3, 7, 9, 10, 5, 5, 3, 9, 9, 9, 1, 9, 8, 4, 4, 8, 6, 9, 6, 10, 10, 8, 5, 4, 8, 1, 6, 10, 2, 6, 2, 6, 4,
             10, 6, 10, 4, 10, 8, 4, 10, 10, 3, 9, 4, 8, 7, 9, 6, 4, 10, 7, 1, 4, 2, 10, 7, 7, 9, 10, 4, 10, 6, 9, 10])
        self.assertEqual(10, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_9(self):
        list1: SinglyLinkedList = build_linked_list(
            [8, 5, 2, 7, 10, 2, 7, 2, 10, 2, 2, 8, 2, 7, 1, 4, 4, 2, 9, 5, 1, 5, 4, 2, 5, 7, 1, 2, 6, 2, 4, 5, 8, 7, 2,
             7, 10, 10, 1, 10, 3, 2, 7, 4, 10, 10, 7, 3, 1, 6, 10, 3, 2, 3, 4, 6, 1, 5, 7, 6, 8, 2, 3, 7, 1, 4, 5, 10,
             5, 7, 1, 7, 10, 10, 2, 10, 9, 1, 4])
        list2: SinglyLinkedList = build_linked_list(
            [8, 3, 1, 9, 5, 7, 7, 6, 3, 5, 8, 7, 2, 7, 10, 10, 1, 10, 3, 2, 7, 4, 10, 10, 7, 3, 1, 6, 10, 3, 2, 3, 4, 6,
             1, 5, 7, 6, 8, 2, 3, 7, 1, 4, 5, 10, 5, 7, 1, 7, 10, 10, 2, 10, 9, 1, 4])
        self.assertEqual(5, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_10(self):
        list1: SinglyLinkedList = build_linked_list(
            [10, 7, 5, 8, 9, 10, 2, 8, 4, 9, 9, 2, 10, 8, 4, 9, 8, 6, 3, 8, 3, 7, 10, 1, 4, 6, 7, 1, 8, 2, 3, 9, 10, 10,
             6, 8, 1, 10, 7, 7, 10, 5, 8, 9, 4, 3, 10, 3, 8, 4, 10, 2, 10, 10, 3, 3, 5, 1, 3, 5, 4, 8, 3, 5, 9, 1, 4, 9,
             2, 1, 7, 1, 7, 5, 1, 3, 9, 10, 5, 9, 5, 5, 10, 5, 4])
        list2: SinglyLinkedList = build_linked_list(
            [7, 10, 5, 2, 4, 10, 9, 9, 5, 7, 9, 8, 7, 10, 8, 4, 2, 7, 10, 2, 9, 8, 8, 9, 4, 3, 10, 3, 8, 4, 10, 2, 10,
             10, 3, 3, 5, 1, 3, 5, 4, 8, 3, 5, 9, 1, 4, 9, 2, 1, 7, 1, 7, 5, 1, 3, 9, 10, 5, 9, 5, 5, 10, 5, 4])
        self.assertEqual(8, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_11(self):
        list1: SinglyLinkedList = build_linked_list(
            [8, 8, 9, 8, 4, 4, 1, 3, 6, 5, 4, 1, 7, 4, 9, 1, 2, 9, 10, 8, 8, 10, 3, 1])
        list2: SinglyLinkedList = build_linked_list(
            [2, 5, 6, 2, 10, 10, 1, 7, 9, 8, 3, 4, 1, 5, 9, 5, 8, 10, 3, 1, 10, 3, 2, 9, 3, 1, 8, 2, 6, 9, 7, 9, 5, 4,
             2, 4, 3, 3, 2, 3, 10, 4, 7, 10, 8, 7, 7, 5, 8, 9, 7, 8, 4, 10, 8, 6, 1, 5, 9, 6, 5, 7, 4, 9, 10, 6, 3, 1])
        self.assertEqual(3, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_12(self):
        list1: SinglyLinkedList = build_linked_list([10, 6])
        list2: SinglyLinkedList = build_linked_list(
            [1, 9, 3, 3, 7, 1, 1, 3, 9, 1, 10, 8, 4, 9, 5, 1, 1, 9, 1, 8, 4, 7, 4, 4, 8, 1, 8, 2, 10, 3, 6, 10, 1, 10,
             2, 7, 10, 4, 2, 10, 5, 1, 7, 8, 1, 1, 1, 4, 2, 1, 1, 5, 10, 6, 10, 7, 6, 7, 8, 7, 9, 5, 7, 2, 4, 10, 10, 6,
             4, 1, 5, 8, 3, 2, 7, 6])
        self.assertEqual(6, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_13(self):
        list1: SinglyLinkedList = build_linked_list(
            [7, 9, 5, 10, 1, 1, 9, 7, 1, 5, 2, 7, 3, 9, 8, 9, 7, 9, 5, 8, 8, 10, 3, 9, 6, 10, 1, 9, 9, 6, 3, 7, 6, 7, 6,
             7, 8, 4, 3, 8, 9, 6, 6, 3])
        list2: SinglyLinkedList = build_linked_list(
            [3, 1, 2, 3, 5, 10, 1, 6, 2, 1, 2, 4, 3, 10, 4, 1, 2, 10, 6, 1, 6, 2, 8, 9, 7, 8, 4, 3, 8, 9, 6, 6, 3])
        self.assertEqual(7, find_merge_node(list1.head, list2.head))

    def test_find_merge_node_14(self):
        list1: SinglyLinkedList = build_linked_list(
            [7, 2, 2, 1, 7, 7, 4, 9, 1, 8, 10, 1, 6, 3, 3, 9, 6, 8, 8, 9, 8, 2, 9, 5, 4, 6, 9, 1, 4, 4, 9, 3, 5, 10, 3,
             2, 8, 6, 2, 9, 6, 1, 1, 1, 3, 4, 1, 1, 3, 10, 1, 10, 1, 9, 6, 4, 4, 4, 6, 10, 10, 4, 2, 4, 6, 6, 7, 3, 4,
             8, 3, 9, 10, 4, 1, 5])
        list2: SinglyLinkedList = build_linked_list(
            [1, 5, 1, 10, 5, 2, 3, 6, 7, 8, 1, 3, 6, 10, 2, 1, 3, 7, 6, 9, 4, 1, 2, 3, 3, 2, 5, 8, 4, 9, 8, 6, 3, 10, 5,
             9, 1, 9, 4, 10, 9, 5, 4, 4, 4, 5, 4, 9, 3, 2, 7, 8, 4, 10, 3, 8, 1, 7, 6, 4, 5, 5, 9, 9, 5, 5, 7, 7, 6, 3,
             6, 4, 7, 1, 9, 2, 7, 4, 10, 10, 7, 8, 7, 10, 7, 9, 8, 7, 5, 5, 2, 1, 9, 2, 1, 3, 9, 8, 10, 4, 9, 1, 8, 10,
             1, 6, 3, 3, 9, 6, 8, 8, 9, 8, 2, 9, 5, 4, 6, 9, 1, 4, 4, 9, 3, 5, 10, 3, 2, 8, 6, 2, 9, 6, 1, 1, 1, 3, 4,
             1, 1, 3, 10, 1, 10, 1, 9, 6, 4, 4, 4, 6, 10, 10, 4, 2, 4, 6, 6, 7, 3, 4, 8, 3, 9, 10, 4, 1, 5])
        self.assertEqual(4, find_merge_node(list1.head, list2.head))
