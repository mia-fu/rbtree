# encoding:utf-8

year = raw_input("请输入一个年份：")
while not year.isdigit():
    print("你输入的不是合法数字")
    year = raw_input("请重新一个年份：")

year = int(year)
if year % 4 == 0:
    if year % 400 == 0:
        print(str(year) + "年是闰年")
    elif year % 100 == 0:
        print(str(year) + "年不是闰年")
    else:
        print(str(year) + "年是闰年")
else:
    print(str(year) + "年不是闰年")