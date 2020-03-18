# encoding:utf8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next




if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    s = Solution()

    res = s.swapPairs(head)
    while res:
        print res.val
        res = res.next
