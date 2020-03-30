# encoding:utf8

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        输入: [3,4,-1,1]
        输出: 2
        """
        len_nums = len(nums)
        if len_nums == 0:
            return 1
        # 将数组看做哈希表
        for i in range(len_nums):
            # 遍历数组， 将数组的位置上放在比位置大1的数 比如nums[0] = 1
            while 1 <= nums[i] <= len_nums and nums[i] != nums[nums[i] - 1]:
                # 将i元素上的值， 放在num[num[i] - 1] 的位置上，两个元素互换 如果两个相等，就不用换了
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(len_nums):
            # 如果0的位置上不是1, 返回1
            if nums[i] != i + 1:
                return i + 1

            # 否则则说明数组中的所有数都是出现过的最小正整数，输出比最后一个数大1的
        return nums[len_nums - 1] + 1
        # 如果不是，就交换位置上的两个数

        # 最后遍历一下数组，如果下标不对，那就是返回下标+1


if __name__ == "__main__":
    s = Solution()
    nums = [3,4,-1,1]
    print s.firstMissingPositive(nums)
