#encoding:utf-8
import easygui as g
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')


msg = '请输入我心中所想的数字叭'
title = '猜谜游戏'

number = g.enterbox(msg, title)
number = int(number)

correct = random.randint(1, 10)

while number != correct:
    msg = '你猜错了，重猜'
    g.enterbox(msg, title)
g.msgbox('你猜对了')
