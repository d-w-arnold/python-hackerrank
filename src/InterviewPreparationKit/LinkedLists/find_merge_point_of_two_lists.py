from typing import Optional


class SinglyLinkedListNode:

    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional[SinglyLinkedListNode] = None


class SinglyLinkedList:

    def __init__(self):
        self.head: Optional[SinglyLinkedListNode] = None
        self.tail: Optional[SinglyLinkedListNode] = None

    def insert_node(self, data) -> None:
        node: SinglyLinkedListNode = SinglyLinkedListNode(data)
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node


def find_merge_node(head1: SinglyLinkedListNode, head2: SinglyLinkedListNode) -> int:
    """
    Find Merge Point of Two Lists problem: https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

    :param head1: A reference to the head of the first list.
    :param head2: A reference to the head of the second list.
    :return: The data value of the node where the lists merge.
    """
    return -2
