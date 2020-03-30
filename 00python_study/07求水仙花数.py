# encoding: utf-8

for i in range(125, 999):
    sum = 0
    cur = i
    while i:
        ge = i % 10
        i = i // 10
        sum += ge ** 3
    if sum == cur:
        print (str(cur) + " ")



