# encoding:utf-8

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)

        if n == 0 or n == 1:
            return intervals


if __name__ == '__main__':
    s = Solution()
    inter = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print s.merge(inter)
