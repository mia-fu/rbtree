# encoding:utf8


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        # 首先生成一个全部为1的列表
        result = [1] * n
        # 0 和 1 不是质数，置为0
        result[0], result[1] = 0, 0
        # 从2开始
        for i in range(2, int(n ** 0.5 + 1)):
            if result[i] == 1:
                # 将i的倍数置为0
                len_result = len(result[i * i:n:i])
                result[i * i:n:i] = [0] * len_result

        return sum(result)


if __name__ == "__main__":
    s = Solution()
    n = 64
    print s.countPrimes(n)
