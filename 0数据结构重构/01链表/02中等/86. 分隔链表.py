# encoding:utf-8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # 设置两个临时头结点
        more_head = ListNode(0)
        less_head = ListNode(0)

        # 对应指针指向这两个头结点
        more_ptr = more_head
        less_ptr = less_head

        while head:
        # 循环链表head
            if head.val < x:
        # 如果head的值比x小，加入到less指针后
                less_ptr.next = head
        # 连接完成后，less指针指向head
                less_ptr = head
        # 如果head的值比x大，加入more指针后
            else:
                more_ptr.next = head
                more_ptr = head
        # 连接完成 同理
            head = head.next

        less_ptr.next = more_head.next
        # 循环结束后，将less指针的下一个指向more头结点的下一个
        more_ptr.next = None
        # 将more指针的最后一个设置为空

        return less_head.next
        # 返回less头结点的下一个


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)

    x = 3

    s = Solution()

    result = s.partition(head, x)

    while result:
        print result.val
        result = result.next

