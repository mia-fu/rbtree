# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = head
        if i == None or i.next == None:
            return head

        while i.next:
            if i.next.val == i.val:
                i.next = i.next.next
            else:
                i = i.next
        return head


if __name__ == "__main__":
    head = ListNode(1)
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    head.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    s = Solution()
    s.deleteDuplicates(head)

    while head:
        print (head.val),
        if head.next:
            print ("->"),
        head = head.next
