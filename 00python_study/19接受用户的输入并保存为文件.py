#encoding:utf-8

file_name = raw_input('请输入文件名：')
file_name = 'E://' + file_name

print('请输入内容【单独输入‘:w’保存退出】')

f = open(file_name, 'w')


while True:
    a = raw_input()
    if a != ':w':
        f.write('%s\n' % a)
    else:
        break
f.close()


