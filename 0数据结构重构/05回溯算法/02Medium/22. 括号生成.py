# encoding:utf8
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []


        def helper(item, left, right):
            if right == 0 and left == 0:
                result.append(item)

            # 如果还剩有左括号， 左括号-1
            if left > 0:
                helper(item + '(', left - 1, right)

            # 如果还剩右括号，并且剩下的右括号比左括号多，
            if right > 0 and left < right:
                helper(item + ')', left, right - 1)

        helper('', n, n)
        return result


if __name__ == '__main__':
    n = 3

    s = Solution()
    print s.generateParenthesis(n)
