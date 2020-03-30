#encoding:utf-8


def product(x, *args): #可变函数

    multi = x

    for y in args:

        multi *= y

    return multi


print product(5, 3)
