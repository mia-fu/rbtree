# encoding:utf-8

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 存放结果集
        result = []

        def DFS(queens, xy_dif, xy_sum):
            # 深度遍历， 按行来回溯
            # 设置递归出口，如果放置的数量等于皇后的数量，结果集放入，返回
            p = len(queens)
            if p == n:
                result.append(queens)
                return
            # n X n 的棋盘上放棋子，按行遍历
            for q in range(n):
                """
                不在主对角线上： xi-i ≠ xj-j
                不在负对角线上： xi+i ≠ xj+j
                """
                # 皇后不能放在同一列上，用queens来控制
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        DFS([], [], [])
        """
        输出：'Q' 和 '.' 分别代表了皇后和空位
        """

        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]



def main():
    n = int(input("请输入皇后的个数："))
    print("\n请按照如下提示摆放皇后：")
    s = Solution()
    cnt = s.solveNQueens(n)
    print cnt


if __name__ == '__main__':
    main()
