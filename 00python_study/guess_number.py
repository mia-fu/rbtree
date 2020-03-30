#encoding:utf-8
import random

guess = raw_input("猜一个数字吧：")

while not guess.isdigit():
    print("你输入的不是合法数字")
    guess = raw_input("请重新输入一个数字")

guess = int(guess)

correct = random.randint(1, 10)
flag = 1
while guess != correct:
    if flag <= correct:
        guess = int(input("猜错了,重猜："))
        if guess == correct:
            print "你猜对了"
            flag = False
            break
        if guess < correct:
            print "你猜小了"
            flag += 1
        else:
            print "你猜大了"
            flag += 1
    else:
        print("你都错了" + str(flag) + "次了，别猜了")
        break

print "结束了"