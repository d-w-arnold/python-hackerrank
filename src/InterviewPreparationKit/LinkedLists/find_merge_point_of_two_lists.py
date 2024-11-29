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
    if head1.next and head2.next:
        ans = -1
        curr1, curr2 = head1.next, head2.next
        c1_conn = c2_conn = False
        while True:
            if ans == -1:
                if c1_conn == c2_conn and curr1.data == curr2.data:
                    ans = curr1.data
                    continue
                if not curr1.next and not curr2.next:
                    break
                if not curr1.next and not c1_conn:
                    curr1 = head2
                    c1_conn = True
                else:
                    curr1 = curr1.next
                if not curr2.next and not c2_conn:
                    curr2 = head1
                    c2_conn = True
                else:
                    curr2 = curr2.next
            else:
                if curr1.data != curr2.data:
                    ans = -1
                    continue
                elif not curr1.next and not curr2.next:
                    break
                elif not curr1.next or not curr2.next:
                    ans = -1
                    break
                curr1 = curr1.next
                curr2 = curr2.next
        return ans
    elif head1.next:
        while head1:
            if head1.data == head2.data:
                return head1.data
            head1 = head1.next
    else:
        while head2:
            if head2.data == head1.data:
                return head2.data
            head2 = head2.next
    return -1
