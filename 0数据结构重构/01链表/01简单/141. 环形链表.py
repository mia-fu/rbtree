class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # 快慢指针问题
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        meet = None

        while fast:
            # 快慢指针同时先走一步
            slow = slow.next
            fast = fast.next
            # 判断 如果快指针遇到链尾， 返回空 没有环
            if not fast:
                return False
            # 快指针再走一步
            fast = fast.next
            if fast == slow:
                return True
            # 如果快慢指针相遇，说明有环，返回True
        return False
        # 退出循环，没相遇，说明没环


if __name__ == "__main__":
    l1 = ListNode(5)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)