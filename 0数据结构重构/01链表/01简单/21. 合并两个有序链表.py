# encoding:utf-8
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        # 设置临时头结点
        temp_head = ListNode(0)

        # 使用pre指针指向temp_head
        per = temp_head

        while l1 and l2:
            # 如果l1 与 l2 都不为空
            if l1.val < l2.val:
                per.next = l1
                l1 = l1.next
            else:
                per.next = l2
                l2 = l2.next
            per = per.next

        # 如果l1有剩余
        if l1:
            per.next = l1
        if l2:
            per.next = l2
        return temp_head.next


if __name__ == "__main__":
    p10 = ListNode(2)
    p11 = ListNode(3)
    p20 = ListNode(1)
    p21 = ListNode(3)
    p22 = ListNode(4)
    p23 = ListNode(5)
    p10.next = p11

    p20.next = p21
    p21.next = p22
    p22.next = p23

    p = Solution()
    p = p.mergeTwoLists(p10, p20)
    while p:
        print p.val
        p = p.next

