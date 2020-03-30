# encoding:utf8
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        window = []  # 滑动窗口数组
        max_length = 0  # 最长串长度

        # 遍历字符串
        for c in s:
            # 如果字符不在滑动窗口中，则直接扩展窗口
            if c not in window:
                # 使用当前字符扩展窗口
                window.append(c)
            # 如果字符在滑动窗口中，则
            # 1. 从窗口中移除重复字符及之前的字符串部分
            # 2. 再扩展窗口
            else:
                # 从窗口中移除重复字符及之前的字符串部分，新字符串即为无重复字符的字符串
                window = window[window.index(c) + 1:]
                # 扩展窗口
                window.append(c)

            # 更新最大长度
            max_length = max(len(window), max_length)

        return max_length 

if __name__ == "__main__":
    re = Solution()
    s = "pwwkew"
    print re.lengthOfLongestSubstring(s)






