from multiprocessing import Process, Queue
import os, time, random

'''
进程之间相互通信
'''


# 写数据进程执行的代码：
def write(q):
    print('Process to write: {}'.format(os.getpid()))
    for value in ['A', 'B', 'C']:
        print('Put {} to queue...'.format(value))
        q.put(value)
        time.sleep(random.random())
# 读数据进程执行的代码
def read(q):
    print('Process to read: {}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('Get {} from queue.'.format(value))

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()