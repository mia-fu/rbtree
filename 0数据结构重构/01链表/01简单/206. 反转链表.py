# encoding:utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        if head == None:
            return
        while head:
            # 头插法 备份head.next
            temp = head.next
            # head下一个指向新元素
            head.next = new_head
            # new_head指向
            new_head = head
            # head移动到备份的next
            head = temp
        return new_head


if __name__ == "__main__":
    head = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)
    p4 = ListNode(5)

    head.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4

    s = Solution()
    a = s.reverseList(head)

    while a:
        print a.val
        a = a.next
