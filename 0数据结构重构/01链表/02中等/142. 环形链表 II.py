# encoding:utf8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# 快慢指针问题


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        meet = None
        count = 0
        # 记录下相遇节点， 并设一个count 算第几个节点有环

        while fast:
        # 快慢指针各走一步
            fast = fast.next
            slow = slow.next
            if not fast:
        # 判断 如果快指针为空，说明没环
                return None

        # 快指针再走一步
            fast = fast.next
            if fast == slow:
        # 判断 如果快慢指针相遇，记录下相遇节点
                meet = fast
                break

        # 如果没有相遇节点，说明没有环
        while not meet:
            return None

        while meet:
            if meet == head:
                return meet
        #如果有相遇节点，head和meet同时走，相遇即为环的起点
            meet = meet.next
            head = head.next
