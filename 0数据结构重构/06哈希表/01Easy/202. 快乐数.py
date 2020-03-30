# encoding:utf8
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 判断快乐数
        # 如果n = 1，说明是快乐数
        result = list()
        while n != 1:
            items = list(str(n))
            sum = 0
            # 如果不是 将n转化为list 遍历 用sum求和，
            for i in items:
                sum += pow(int(i), 2)
            # 将每次求和结果放在result里面
            result.append(sum)
            n = sum
            if len(result) != len(set(result)):
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    n = 19
    print s.isHappy(n)

