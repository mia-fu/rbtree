# encoding:utf8
import heapq


class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []

        # 找最小的k个数，用大根堆实现
        len_arr = len(arr)
        arr_k = [-x for x in arr[:k]]
        # 首先用小根堆模拟大根堆，取负数在堆中放入前k个数
        heapq.heapify(arr_k)

        for i in range(k, len_arr):
            if -arr_k[0] > arr[i]:
                heapq.heappop(arr_k)
                heapq.heappush(arr_k, -arr[i])
        return [-x for x in arr_k]
        # 比较，如果堆顶元素比下一个元素大，那么交换两个元素


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 1]
    k = 2
    print s.getLeastNumbers(nums, k)
