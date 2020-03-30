# encoding:utf-8
import logging
import os
import threading
import time
from Queue import Queue

LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '
logging.basicConfig(level=logging.INFO,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT,
                    filename=r"D:\Python\test.log"
                    )


def ping_list():
    ip_list = ['www.baidu.com',
               'www.leetcode-cn.com',
               'www.taobao.com']
    for ip in ip_list:
        os.system('ping ' + ip)



""""
串行执行
"""""


def ping_ip():
    start_time = time.time()
    ping_list()
    logging.info('串行执行所用时间：{0}'.format(time.time() - start_time))


""""
并行执行
"""""

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
def ping_ip_queue():
    while not IP_QUEUE.empty():
        ip = IP_QUEUE.get()
        os.system('ping ' + ip)


def ping_threading():
    threads = []
    start_time = time.time()
    for i in range(WORD_THREAD):
        thread = threading.Thread(target=ping_ip_queue)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    logging.info('并行执行所用时间：{0}'.format(time.time() - start_time))


if __name__ == '__main__':
    ping_ip()
    ping_threading()
