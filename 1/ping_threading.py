# encoding:utf8
import os
import threading
import time
from Queue import Queue

# 定义工作线程
WORD_THREAD = 50

# 将需要 ping 的 ip 加入队列
IP_QUEUE = Queue()
ip_list = ['www.baidu.com',
           'www.leetcode-cn.com',
           'www.taobao.com']
for ip in ip_list:
    IP_QUEUE.put(ip)


# 定义一个执行并行 ping 的函数
def ping_threading():
    while not IP_QUEUE.empty():
        ip = IP_QUEUE.get()
        os.system('ping ' + ip)


if __name__ == '__main__':
    threads = []
    start_time = time.time()
    for i in range(WORD_THREAD):
        thread = threading.Thread(target=ping_threading)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print('并行执行所用时间：{0}'.format(time.time() - start_time))
