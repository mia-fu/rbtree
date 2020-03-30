# encoding:utf-8
import subprocess
import time


def ping_ip():
    start_time = time.time()
    ip_list = ['172.20.10.' + str(i) for i in range(1, 6)]
    for ip in ip_list:
        res = subprocess.call('ping -n 2 -w 5 %s' % ip, stdout=subprocess.PIPE)
        print(ip, True if res == 0 else False)
    print('串行执行所用时间：{0}'.format(time.time() - start_time))


if __name__ == '__main__':
    ping_ip()
