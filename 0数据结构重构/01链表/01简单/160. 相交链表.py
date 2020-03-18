# encoding:utf-8

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pA = headA
        pB = headB
        len_A = 0
        len_B = 0
        # 让两个链表走到链表末尾，求出链表长度
        while pA:
            pA = pA.next
            len_A += 1
        while pB:
            pB = pB.next
            len_B += 1

        pA = headA
        pB = headB
        # 得到两个链表长度的差值，让链表长的先走差值部分
        diff = len_A - len_B

        while diff != 0:
            if diff > 0:
                pA = pA.next
                diff -= 1
            if diff < 0:
                pB = pB.next
                diff += 1

        # 设置一个循环，判断两个链表是否相等，不等两个指针同时向前走， 直到找到
        while pA != pB:
            pA = pA.next
            pB = pB.next
        return pA


if __name__ == '__main__':
    headA = ListNode(4)
    a1 = ListNode(1)
    a2 = ListNode(8)
    a3 = ListNode(4)
    a4 = ListNode(5)

    headB = ListNode(5)
    b1 = ListNode(0)
    b2 = ListNode(1)
    b3 = ListNode(8)
    b4 = ListNode(4)
    b5 = ListNode(5)

    headA.next = a1
    a1.next = a2
    a2.next = a3
    a3.next = a4

    headB.next = b1
    b1.next = b2
    b2.next = b3
    b3.next = b4
    b4.next = b5

    s = Solution()
    a = s.getIntersectionNode(headA, headB)
    print a

