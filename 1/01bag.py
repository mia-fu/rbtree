# encoding:utf8
def bag(n, c, w, v):
    value =[[0 for j in range(c+1)]for i in range(n)]  # 背包的重量从0到c，物品从0到n-1
    print(value)
    for i in range(0, n):  # i表示第i个物品,我们把第1个物品看作第0个
        for j in range(1, c+1):  # j表示重量为j，从重量为1开始算
            if j < w[i]:  # 背包容量不够，放不下第i个物品
                value[i][j] = value[i-1][j]  # value表示总价值,不放这个物品，肯定就保留前一个物品的总价值
            elif j >= w[i]:
                if value[i][j] < value[i-1][j-w[i]]+v[i]:  # 背包容量足够，价值提升
                    value[i][j] = value[i-1][j-w[i]]+v[i]
                else:
                    value[i][j] = value[i-1][j]  # 背包容量足够，但是价值没有提升
    for x in value:
        print(x)
    return value


def show(n, c, w, value):
    print('max value', value[n-1][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n-1, 0, -1):
        if value[i][j] > value[i-1][j]:  # i代表第i个物品，如果放入第i个物品的价值大于同等重量放入i-1物品的重量，说明选择了物品i
            x[i] = True
            j -= w[i]
    print('items:')
    for i in range(n):
        if x[i]:
            print('no.{}'.format(i+1))


if __name__ =='__main__':
    n = 4
    c = 6
    weight = [2, 3, 4, 5]
    value = [3, 4, 5, 6]
    result = bag(n, c, weight, value)
    show(n, c, weight, result)
