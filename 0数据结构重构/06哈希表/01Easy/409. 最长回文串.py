# encoding:utf8
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # hash表处理
        s_dict = {}
        # 判断是否有中心字符
        flag = 0
        sum_s = 0
        for i in s:
            if i not in s_dict:
                s_dict[i] = 0
            s_dict[i] += 1

        for k in s_dict.keys():
            # 如果字符是偶数个，直接加入
            if s_dict[k] % 2 == 0:
                sum_s += s_dict[k]
            else:
                s_dict[k] -= 1
                sum_s += s_dict[k]
                flag = 1

        return sum_s + flag
        # 如果字符是奇数个，删掉一个，flag= 1说明有中心字符