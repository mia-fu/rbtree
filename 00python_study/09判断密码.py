#encoding:utf-8
password = 'fsy'

user_in = raw_input("请输入密码：")

time = 3

while time:
    if password == user_in:
        print("输入正确，请进")
        break
    else:
        if user_in.find('*') == 0:
            user_in = raw_input("您输错了，请重新：")
            continue
        user_in = raw_input("您输错了，请重新：")
        time -= 1
        

