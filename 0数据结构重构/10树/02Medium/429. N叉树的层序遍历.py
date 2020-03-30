# encoding:utf8
# Definition for a Node.


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        # 二叉树的广度遍历
        queue = [root]  # 初始化根节点
        while queue:
            child = []  # 遍历根节点的子节点
            node = []  # 为下一次的循环提供新的数据集
            for item in queue:
                child.append(item.val)
                if item.children:
                    node += item.children
            res.append(child)
            queue = node
        return res


if __name__ == "__main__":
    s = Solution()

    r5 = Node(5)
    r6 = Node(6)
    r1 = Node(3)
    r2 = Node(2)
    r3 = Node(4)
    root = Node(1, r1)
    root = Node(1, r2)
    root = Node(1, r3)

    r1 = Node(3, r5)
    r1 = Node(3, r6)




    r1.children = Node(5)
    r1.children = Node(6)

    print s.levelOrder(root)

