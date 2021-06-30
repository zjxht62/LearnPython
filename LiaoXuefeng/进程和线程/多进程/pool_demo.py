from multiprocessing import Pool
import os, time, random

'''
使用Pool来创建大量子进程
'''
def long_time_task(name):
    print('Run task {} ({})...'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task {} runs {:0.2f} seconds.'.format(name, (end - start)))


if __name__ == '__main__':
    print('Parent process {}.'.format(os.getpid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    p.close()
    # 会等待所有子进程执行完毕
    p.join()
    print('All subprocesses done.')
