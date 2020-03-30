#encoding:utf-8

name = raw_input('请输入待查找的用户名:')
score = [['mitu', 85], ['fu', 92], ['tian', 99]]

for each in score:
    if each[0] == name:
        print (name + "的得分是：" + str(each[1]))

    elif each[0] != name:
        print("查找的数据不存在")
