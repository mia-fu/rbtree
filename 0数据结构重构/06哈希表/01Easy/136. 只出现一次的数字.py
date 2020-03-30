# encoding:utf8
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        if num_len == 1:
            return nums[0]

        num_dict = {}
        for i in range(num_len):
            if nums[i] in num_dict:
                num_dict.pop(nums[i])
            else:
                num_dict[nums[i]] = 1

        re = list(num_dict.keys())
        return re[0]


if __name__ == "__main__":
    s = Solution()
    nums = [4,1,2,1,2]
    print s.singleNumber(nums)
