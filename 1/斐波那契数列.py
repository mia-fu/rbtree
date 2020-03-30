# encoding:utf8
def fib(n):
    result = list(range(n+1))

    for i in range(n+1):  # 按顺序从小往大算
        if i < 2:
            result[i] = i
        else:
            result[i] = result[i - 1] + result[i - 2]

    return result[-1]


if __name__ == "__main__":
    result = fib(100)
    print(result)
