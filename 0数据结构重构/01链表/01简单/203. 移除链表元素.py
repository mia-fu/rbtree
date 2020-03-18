# encoding:utf-8

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):

        p = ListNode(-1)
        # 因为要删除的可能是链表的第一个元素，所以用一个h节点来做处理
        # 最后只要返回h的下一个节点即可
        p.next, h = head, p
        # 注意遍历的条件是p.next不为空
        while p.next:
            # 如果p的下一个节点的值==val
            # P就指向下下一个，这就删掉了指定的节点
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return h.next


if __name__ == "__main__":
    head = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(6)
    p3 = ListNode(3)
    # p4 = ListNode(4)
    # p5 = ListNode(5)
    # p6 = ListNode(6)

    head.next = p1
    p1.next = p2
    p2.next = p3
    # p3.next = p4
    # p4.next = p5
    # p5.next = p6

    val = 6
    s = Solution()
    a = s.removeElements(head, val)

    while a:
        print a.val
        a = a.next
