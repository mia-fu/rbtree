# encoding:utf8
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """ # 维护一个单调递增栈
        # 主要就是找右边第一个小于i的， 和左边第一个小于i的数，(right_i - left_i - 1) * height[i]
        # 第一个栈顶元素是-1，让第0个元素有左边和右边
        stack = [-1]
        max_res = 0
        for i in range(len(heights)):
            # 如果下一个栈顶元素比现在的小，那这个右边就确定了
            # 这里不用if而是用while，因为要找到左边界
            while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
                # 最大值为 (right_i - left_i - 1) * height[i]
                max_res = max(max_res, heights[stack.pop()] * (i - stack[-1] - 1))
            # 否则就向栈里增加元素
            stack.append(i)
            # print max_res
        # 循环结束，要清理堆栈，此时所有栈中继续存放的元素的右边界c都是结尾len(height)-1，要找到栈里延伸的面积
        for i in range(len(stack)-1):
            max_res = max(max_res, heights[stack.pop()]*(len(heights)-1-stack[-1]))
        return max_res


if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    s = Solution()
    print s.largestRectangleArea(heights)