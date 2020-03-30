#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def queen1(A, cur=0):
    cnt = 0

    if cur == len(A):
        print(A)
        return 1

    for col in range(len(A)):
        A[cur], flag = col, True

        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break

        if flag:
            cnt += queen1(A, cur + 1)

    return cnt


def main():
    n = int(input("请输入皇后的个数："))
    print("\n请按照如下提示摆放皇后：")
    cnt = queen1([None] * n)
    print("\n共有%s种摆放方法！" % cnt)


if __name__ == '__main__':
    main()