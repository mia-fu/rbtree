# encoding:utf8
import copy
class Solution(object):

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 需要一个存放结果的二维数组result
        result = [[]]

        # 暂时存放数据的item
        item = []

        self.helper(0, nums, item, result)
        result = [sorted(v) for v in result]
        result = list(set(tuple(t) for t in result))
        result = [list(v) for v in result]
        return result

        # 递归函数
    def helper(self, i, nums, item, result):
        # 设置递归出口
        if i >= len(nums):
            return
        # 需要注意append是浅拷贝，用深拷贝
        item.append(copy.deepcopy(nums[i]))

        result.append(copy.deepcopy(item))

        # 第一次递归
        self.helper(i + 1, nums, item, result)

        # 进行回溯

        item.pop()

        self.helper(i + 1, nums, item, result)


if __name__ == '__main__':
    s = Solution()
    nums = [4, 4, 4, 1, 4]
    print s.subsetsWithDup(nums)


