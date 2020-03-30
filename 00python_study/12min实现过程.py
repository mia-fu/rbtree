#encoding:utf-8

def get_min(n):
    min_ = n[0]

    for i in n:
        if i < min_:
            min_ = i
    return min_


print get_min((9, 3, 5, 5))
