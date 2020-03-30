# encoding:utf-8

"""
冒泡排序， a表示数组， n表示数组⼤⼩
"""


class Soultion(object):
    def bubbleSort(self,nums):
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

    """
    bubbleSort2为优化改良版的冒泡排序
    """

    def bubbleSort2(self, nums):
        for i in range(len(nums) - 1):
            flag = False
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = True
            if not flag:
                return nums
        return nums


if __name__ == "__main__":
    s = Soultion()
    print s.bubbleSort2([6, 1, 2, 3, 4, 5])