from multiprocessing import Process
import os

'''
子进程demo
'''
# 子进程要执行的代码
def run_proc(name):
    print("Run child process {} ({})...".format(name, os.getpid()))


if __name__ == '__main__':
    print('Parent process {}.'.format(os.getpid()))
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    # start()方法启动
    p.start()
    # join()方法可以等待子进程结束后再继续往下进行，通常用于进程间的同步
    p.join()
    print('Child process end.')