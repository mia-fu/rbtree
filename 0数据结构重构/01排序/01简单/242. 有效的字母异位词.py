# encoding:utf-8


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 一共26个英文字母， 准备26个桶
        temp = [0 for i in range(26)]

        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        for i in range(s_len):
            temp[ord(s[i]) - ord('a')] += 1
            temp[ord(t[i]) - ord('a')] -= 1

        for i in range(len(temp)):
            if temp[i] != 0:
                return False
        return True


if __name__ == '__main__':
    re = Solution()
    s = "ab"
    t = "a"
    print re.isAnagram(s, t)
