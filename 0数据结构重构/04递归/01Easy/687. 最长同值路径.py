# encoding:utf8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        

if __name__ == '__main__':
    root = TreeNode(5)
    root.right = TreeNode(4)
    root.left = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)