# encoding:utf8
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 拼接数组，求连续子数组的最大和
        len_A = len(A)
        max = A[0]
        A = A + A # 环形条件限制
        for i in range(len(A)):
            sum = 0
            j = 1
            while (j - i) < len(A):
                sum += A[j]
                # 在这一步做了裁剪，如果到这部分仍然是小于的，直接跳过这个l；
                # 同时为了防止全负情况或a[0]
                #为负的情况，做了个简单sum校验

                if sum < 0 and sum < max:
                    break
                if sum > max:
                    max = sum
                j += 1
        return max


if __name__ == "__main__":
    s = Solution()
    A = [-2,-3,-1]
    print s.maxSubarraySumCircular(A)
