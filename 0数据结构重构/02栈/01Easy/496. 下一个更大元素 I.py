# encoding:utf-8
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = list()
        hashmap = dict()
        for i in nums2:
            while stack and stack[-1] < i:
                hashmap[stack.pop()] = i
            stack.append(i)
        return [hashmap.get(i, -1) for i in nums1]


if __name__ == "__main__":
    num1 = [4, 1, 2]
    num2 = [1, 3, 4, 2]

    s = Solution()
    print s.nextGreaterElement(num1, num2)
