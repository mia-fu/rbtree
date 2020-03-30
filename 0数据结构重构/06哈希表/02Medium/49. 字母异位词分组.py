# encoding:utf8

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = [[]]
        str_dict = {}
        # 遍历字符串，用hash表实现
        for s in strs:
            keys = ''.join(sorted(s))
            if keys not in str_dict:
                str_dict[keys] = [s]
            else:
                str_dict[keys].append(s)
        return str_dict.values()
        # 放入hash之前，将每个字符进行排序，如果排序的和表中相等，就是字母异位词


