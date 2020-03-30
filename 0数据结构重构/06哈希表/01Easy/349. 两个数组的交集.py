# encoding:utf8
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 先比较1和2的长度
        len_num1 = len(nums1)
        len_num2 = len(nums2)

        if len_num1 < len_num2:
            nums1, nums2 = nums2, nums1
            len_num1, len_num2 = len_num2, len_num1

        num_dict = {}
        result = []
        # 遍历将长度长的数组全部放到hash表中，
        for i in range(len_num1):
            num_dict[i] = nums1[i]

        for j in range(len_num2):
            if nums2[j] in num_dict.values():
                result.append(nums2[j])

        return list(set(result))
        # 遍历短数组，将hash表中有的放到list中

if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2]
    nums2 = [1, 1]
    print s.intersection(nums1, nums2)