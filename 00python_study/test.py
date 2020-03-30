# encoding:utf-8


def load():
    dict1 = {'小付': 'fsy'}
    while 1:
        key = raw_input(
            """
|--- 新建用户：N/n ---|
|--- 登录帐号：E/e ---|
|--- 退出程序：Q/q ---|
|--- 请输入指令代码："""
        )
        if key == 'N' or key == 'n':
            temp_name = raw_input("请输入用户名：")
            try:
                temp_password = raw_input("请输入密码：")
                dict1[temp_name] = temp_password
                print("'注册成功，赶紧试试登录吧^_^'")
                continue
            except:
                temp_name = raw_input("此用户名已经被使用，请重新输入：")

        if key == 'E' or key == 'e':
            temp_name = raw_input("请输入用户名：")
            while temp_name not in dict1:
                temp_name = raw_input("您输入的用户名不存在，请重新输入：")
            temp_password = raw_input("请输入密码：")
            while temp_password not in dict1[temp_name]:
                temp_password = raw_input("您输入的密码错误，请重新输入：")
            print('欢迎进入系统，如要退出，请点右上角的X结束程序！')
            continue
        if key == 'Q' or key == 'q':
            break


load()
