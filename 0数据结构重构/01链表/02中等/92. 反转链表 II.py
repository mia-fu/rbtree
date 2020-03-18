# encoding:utf8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        pre = res

        # 找到 m-1 个节点 m-1的下一个最终指向n
        for i in range(1, m):
            pre = pre.next

        mNode = pre.next
        cur = pre.next
        for j in range(m, n + 1):
            temp = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = temp

        mNode.next = cur
        # m节点的下一个最终指向n+1
        return res.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    m = 2
    n = 4

    s = Solution()
    res = s.reverseBetween(head, m, n)

    while res:
        print res.val
        res = res.next
