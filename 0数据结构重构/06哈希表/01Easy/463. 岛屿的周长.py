# encoding:utf8


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        # 一个方框的边长为4， 遍历行和列，

        # 如果该块的上下左右有1， 就-1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 4
                    # 判断上
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        count -= 1
                    # 判断下
                    if i + 1 < len(grid) and grid[i + 1][j] == 1:
                        count -= 1
                    # 判断左
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        count -= 1
                    # 判断右
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                        count -= 1
        return count


if __name__ == "__main__":
    s = Solution()
    grid = [[1,0]]
    print s.islandPerimeter(grid)