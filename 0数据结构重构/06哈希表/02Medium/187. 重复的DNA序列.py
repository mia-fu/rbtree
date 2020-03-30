# encoding:utf8

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []

        res = []
        s_dict = {}
        # 算到倒数第9个数就可以
        for i in range(len(s) - 9):
            # 每次取10个字符，记录下来
            temp = s[i:i + 10]
            s_dict[temp] = s_dict.get(temp, 0) + 1
            # 遍历 如果出现两次，就说明重复
            if s_dict[temp] == 2:
                res.append(temp)
        return res


if __name__ == "__main__":
    re = Solution()
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print re.findRepeatedDnaSequences(s)
