#encoding:utf-8


def int_input(prompt=''):
    while True:
        try:
            int(raw_input(prompt))
            break
        except:
            print ('出错，您输入的不是整数！')


int_input('请输入一个整数：')