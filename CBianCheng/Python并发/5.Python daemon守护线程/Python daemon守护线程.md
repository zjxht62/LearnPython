# Python daemon守护线程
当程序中拥有多个线程时，主线程执行结束并不会影响子线程继续执行。换句话说，只有程序中所有线程全部执行完毕后，程序才算真正结束。
```python
import threading
# 主线程执行
for i in range(5):
    print(threading.current_thread().getName() + " " + str(i))

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

```
输出如下，虽然主线程早早得执行完成，但是子线程执行完，程序才算真正结束
```
MainThread 0
MainThread 1
MainThread 2
MainThread 3
MainThread 4
Thread-1 aaa
Thread-1 bbb
Thread-1 ccc
```
除此之外，Python 还支持创建另一种线程，称为守护线程（或后台线程）。此类线程的特点是，当程序中主线程及所有非守护线程执行结束时，未执行完毕的守护线程也会随之消亡（进行死亡状态），程序将结束运行。
> Python 解释器的垃圾回收机制就是守护线程的典型代表，当程序中所有主线程及非守护线程执行完毕后，垃圾回收机制也就没有再继续执行的必要了。

创建守护线程可以在构造函数里直接指定daemon属性为True，或者在调用start()方法之前设置daemon属性，否则会报RuntimeError
```python
import threading


# 线程要执行的方法
def action(*params):
    for p in params:
        print(threading.current_thread().getName() + " " + p)

# 传入的参数
params = ('aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')

# 实例化Thread创建线程，此时处于新建状态

# 在构造函数里指定daemon属性为True，表示线程是守护线程
thread = threading.Thread(target=action, args=params, daemon=True)
# 或者在start()方法之前设置线程的daemon属性
# thread.daemon=True

# 调用start()方法，进入就绪状态
thread.start()
# 主线程执行
for i in range(2):
    print(threading.current_thread().getName() + " " + str(i))
```
执行结果，可以看出，本来子线程应该输出从aaa到fff，但是由于是守护线程，主线程执行完毕后，守护线程也随之消亡
```python
Thread-1 aaaMainThread 0
MainThread 1
```