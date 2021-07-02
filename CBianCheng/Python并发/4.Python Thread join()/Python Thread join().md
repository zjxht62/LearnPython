# Python Thread join()
如果想让某个线程先执行，可以调用该线程对象的join()方法。我感觉join可以理解为插队，想让哪个线程插队，就在他身上调用join()方法
```
thread.join( [timeout] )
```
其中，thread 为 Thread 类或其子类的实例化对象；timeout 参数作为可选参数，其功能是指定 thread 线程最多可以霸占 CPU 资源的时间（以秒为单位），如果省略，则默认直到 thread 执行结束（进入死亡状态）才释放 CPU 资源。
```python
import threading

# 线程要执行的方法
def action(*params):
    for p in params:
        print(threading.current_thread().getName() + " " + p)

# 传入的参数
params = ('aaa', 'bbb', 'ccc')

# 实例化Thread创建线程，此时处于新建状态
thread = threading.Thread(target=action, args=params)
# 调用start()方法，进入就绪状态
thread.start()
thread.join()

# 主线程执行
for i in range(5):
    print(threading.current_thread().getName() + " " + str(i))
```
执行结果
```
Thread-1 aaa
Thread-1 bbb
Thread-1 ccc
MainThread 0
MainThread 1
MainThread 2
MainThread 3
MainThread 4

```