# encoding:utf-8


def binB(num):
    result = ''
    if num:
        result = binB(num // 2)
        return result + str(num % 2)
    else:
        return result


result = []


def get_digits(n):
    if n > 0:
        result.insert(0, n % 10)
        get_digits(n // 10)
    return result


print(get_digits(12345))




