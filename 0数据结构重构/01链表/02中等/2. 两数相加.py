# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        p = ListNode(-1)
        p.next = l1
        head = p
        sum = 0
        while l1 or l2 or sum != 0:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            p.next = ListNode(sum % 10)
            sum = sum // 10
            p = p.next

        return head.next





if __name__ == "__main__":
    l1 = ListNode(5)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    result = s.addTwoNumbers(l1, l2)

    while result:
        print result.val
        result = result.next