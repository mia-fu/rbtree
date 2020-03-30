# encoding: utf-8


def hanoi(n, x, y, z):
    if n == 1:
        print (x, ' --> ', z)
    else:
        # 将前 n - 1 个盘子从x移动到y上
        hanoi(n-1, x, z, y)
        # 将最后一个盘子从x移动到z上
        print (x, ' --> ', z)
        # 将前 n - 1 个盘子从y移动到z上，完成
        hanoi(n-1, y, x, z)


print hanoi(4, 'X', 'Y', 'Z')
