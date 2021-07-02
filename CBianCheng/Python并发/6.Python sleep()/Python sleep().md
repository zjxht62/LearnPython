# Python sleep()函数用法：线程睡眠
time模块里面的sleep(secs)函数，可以实现当前执行的线程暂停secs后再继续执行。
就是线程将进入阻塞状态，等到了时间之后，再变成就绪状态，等待CPU的调度。

> sleep() 函数位于 time 模块中，因此在使用前，需先引入 time 模块。


sleep()函数的语法
```
time.sleep(secs) # 其中，secs 参数用于指定暂停的秒数
```

举例:
```python
import threading
import time

# 线程要执行的方法
def action(*params):
    for p in params:
        # 暂停0.1s之后再执行
        time.sleep(0.1)
        print(threading.current_thread().getName() + " " + p)

# 传入的参数
params = ('aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')

# 实例化Thread创建线程
thread = threading.Thread(target=action, args=params)
# 启动
thread.start()

# 主线程执行
for i in range(2):
    print(threading.current_thread().getName() + " " + str(i))
```
执行结果：因为子线程使用了sleep，所以会在执行时被阻塞，导致主线程获得更多的CPU调度
```
MainThread 0
MainThread 1
Thread-1 aaa
Thread-1 bbb
Thread-1 ccc
Thread-1 ddd
Thread-1 eee
Thread-1 fff
```
