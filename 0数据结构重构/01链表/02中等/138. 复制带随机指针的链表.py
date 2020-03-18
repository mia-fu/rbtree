# encoding:utf8

# Definition for a Node.


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        lookup = {}

        def dfs(head):
            if not head:
                return None
            if head in lookup:
                return lookup[head]

            clone = Node(head.val, None, None)
            lookup[head] = clone
            clone.next, clone.random = dfs(head.next), dfs(head.random)
            return clone

        return dfs(head)


if __name__ == "__main__":
    x = Node(7, 13)
    x1 = Node(13, 11, 0)
    x2 = Node(11, 10, 4)
    x3 = Node(10, 1, 2)
    x4 = Node(1, next=None, random=0)

    s = Solution()
    print s.copyRandomList(x)
