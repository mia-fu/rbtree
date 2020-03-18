# encoding:utf8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 首先计算出l1 和 l2 的长度， 补齐位数
        num1 = 0
        num2 = 0
        per = l1
        while per:
            num1 += 1
            per = per.next
        per = l2

        while per:
            num2 += 1
            per = per.next

        if num1 < num2:
            l1, l2 = l2, l1
            num1, num2 = num2, num1

        diff = num1 - num2

        if diff:
            per = ListNode(0)
            cur = per
            while diff:
                cur.next = ListNode(0)
                diff -= 1
                cur = cur.next
            cur.next = l2
            l2 = per.next



        def listNodeAdd(l1, l2):
            global digit
            digit = 0
            if not l1:
                return

            listNodeAdd(l1.next, l2.next)
            sum = l1.val + l2.val + digit
            if sum >= 10:
                l1.val = sum % 10
                digit = 1
            else:
                l1.val = sum
                digit = 0

        listNodeAdd(l1, l2)
        result = l1
        if digit == 1:
            result = ListNode(1)
            result.next = l1

        return result









if __name__ == "__main__":
    l1 = ListNode(8)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    # l1.next.next.next = ListNode(3)

    l2 = ListNode(2)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    s = Solution()

    count = l1.val + l2.val
    res = s.addTwoNumbers(l1, l2)

    while res:
        print res.val
        res = res.next
