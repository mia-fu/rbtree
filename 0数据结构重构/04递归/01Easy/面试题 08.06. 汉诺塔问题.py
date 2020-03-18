# encoding:utf8
class Solution(object):
    def hanota(self, A, B, C):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :rtype: None Do not return anything, modify C in-place instead.
        """
        self.helper(A, B, C, len(A))
    def helper(self, A, B, C, n):
        if n == 1:
            C.append(A.pop())
            return
        self.helper(A, C, B, n-1)
        C.append(A.pop())
        self.helper(B, A, C, n-1)


if __name__ == '__main__':
    A = [2, 1, 0]
    B = []
    C = []
    s = Solution()
    print s.hanota(A, B, C)
