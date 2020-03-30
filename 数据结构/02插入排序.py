# encoding:utf-8

"""
插入排序， a表示数组， n表示数组⼤⼩ 从小到大排序 1，2，3，4，5
"""


class Soultion(object):
    def InsertionSort(self, nums):
        for i in range(1, len(nums)):
            value = nums[i]
            j = i - 1
            while j>=0 and nums[j] > value:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = value
        return nums



if __name__ == "__main__":
    list1 = [4, 5, 6, 1, 3, 2]
    s = Soultion()
    print s.InsertionSort(list1)
