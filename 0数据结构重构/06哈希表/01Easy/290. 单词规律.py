# encoding:utf8

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_dict = {}
        str_list = str.split()

        if len(pattern) != len(str_list):
            return False

        for i, j in zip(pattern, str_list):
            # 如果字典中没有abba，对应str加入字典中
            if i not in str_dict:
                str_dict[i] = j
            elif i in str_dict and str_dict[i] != j:
                return False

        if len(set(str_dict.values())) != len(str_dict.values()):
            return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    pattern = "abba"
    str = "dog cat cat dog"
    print s.wordPattern(pattern, str)
