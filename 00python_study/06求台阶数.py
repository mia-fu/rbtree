#encoding:utf-8
n = 7

flag = False

while not flag:
    if (n % 2 == 1) and (n % 3 == 2) and (n % 5 == 4) and (n % 6 == 5):
        print('台阶数为' + str(n))
        flag = True
    else:
        n += 7


