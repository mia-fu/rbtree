# encoding:utf8
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if coins == []:
            return -1
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            temp = [] # 可选方案
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    temp.append(dp[i - coin] + 1)
            if temp != []:
                dp[i] = min(temp)

        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    print s.coinChange(coins, amount)