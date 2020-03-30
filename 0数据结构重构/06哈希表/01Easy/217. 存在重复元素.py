class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_dict = {}
        for n in nums:
            if n in num_dict:
                return True
            else:
                num_dict[n] = 1

        return False
