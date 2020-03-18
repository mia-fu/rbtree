# encoding:utf-8

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    head = ListNode(4)
    p1 = ListNode(5)
    p2 = ListNode(1)
    p3 = ListNode(9)
    # p4 = ListNode(4)
    # p5 = ListNode(5)
    # p6 = ListNode(6)

    head.next = p1
    p1.next = p2
    p2.next = p3
    # p3.next = p4
    # p4.next = p5
    # p5.next = p6

