# encoding:utf-8
import Queue
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = Queue.PriorityQueue()
        for num in nums:
            dp.put(num)
            if dp.qsize() > k:
                dp.get()

        return dp.get()


if __name__ == '__main__':
    nums = [1, 4, 2, 6]
    k = 2

    s = Solution()
    print s.findKthLargest(nums, k)
