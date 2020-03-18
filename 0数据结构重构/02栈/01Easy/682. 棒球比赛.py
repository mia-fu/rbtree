class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == '+':
                stack.append(int(stack[-1] + stack[-2]))
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(int(stack[-1]) * 2)
            else:
                stack.append(int(op))
        return sum(stack)


if __name__ == '__main__':
    ops = ["5","-2","4","C","D","9","+","+"]
    s = Solution()
    print s.calPoints(ops)
