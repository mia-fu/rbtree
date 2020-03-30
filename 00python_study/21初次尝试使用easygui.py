#encoding:utf-8
import easygui as g
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

g.msgbox('欢迎进入第一个界面小游戏')

msg = '你希望玩哪个小游戏呢？'
title = '小游戏互动'

choices = ['飞行棋', '五子棋', '麻将']

choice = g.choicebox(msg, title, choices)

g.msgbox('你的选择是' + str(choice))

msg = '你希望重新开始小游戏嘛？'
title = '请选择'

if g.ccbox(msg, title):
    pass
else:
    sys.exit(0)
