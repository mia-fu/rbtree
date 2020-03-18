# encoding:utf8
import copy
class Solution(object):
    def helper(self, i, nums, item, result):
        # 递归结束的条件
        if i >= len(nums):
            return

        item.append(copy.deepcopy(nums[i]))
        # 将数组中的第一个元素放在item中

        result.append(copy.deepcopy(item))
        # 将当前子集item放入result中

        self.helper(i + 1, nums, item, result)
        # 开始第一次递归调用

        # 回溯
        item.pop()

        # 开始第二次递归调用
        self.helper(i + 1, nums, item, result)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 最终结果存在result 列表中
        result = [[]]
        # 回溯时，会产生各个子集的数组
        item = []
        self.helper(0, nums, item, result)
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 6, 7]
    print s.subsets(nums)
