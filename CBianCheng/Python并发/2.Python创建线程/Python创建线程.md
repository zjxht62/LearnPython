# Python创建线程
Python中和线程相关的模块有两个：
+ _thread：是Python3之前thread模块的重命名，功能比较弱，而且以下划线开头，意味着不建议使用
+ threading：Python3之后的线程模块，功能丰富，使用之。

主要创建线程的两种方式：
1. 使用threading模块中Thread类的构造器创建线程。实例化threading.Thread类，调用实例化对象的start()方法启动线程。
2. 继承threading.Thread类。实例化派生出的类，调用其start()方法。

## 调用Thread类的构造器创建线程
Thread类提供了如下的构造器
```
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)¶
```
要调用Thread的构造函数的时候，一定要使用关键字参数调用，他的参数有：
+ group：应该传None，为了将来实现ThreadGroup类保留的。
+ target：是run()方法运行的可调用的对象。默认是None，意味着什么都不做。
+ name：线程的名字。默认情况下，唯一名称是“Thread-N”的形式，其中 N 是一个小十进制数。
+ args：是要调用的对象的参数元组。默认为 ()。
+ kwargs：是目标调用的关键字参数字典。默认为 {}。
+ deamon：如果不是 None，deamon显式设置线程是否是守护进程。如果为 None（默认值），则从当前线程继承守护进程属性。

如果子类覆盖了构造函数，它必须确保在对线程执行任何其他操作之前调用基类构造函数 (Thread.__init__())。

示例：通过Thread类的构造方法创建线程
```python
import threading

# 定义线程要调用的方法，*add可以接收多个以非关键字方式传入的参数
def action(*add):
    for arc in add:
        # 通过getName方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() + " " + arc)

my_tuple = ('aaa', 'bbb', 'ccc')

thread = threading.Thread(target=action, args=my_tuple)
thread.start()

# 让主线程也执行工作
for i in range(5):
    print(threading.current_thread().getName())

```
> 默认情况下，主线程的名字为 MainThread，用户启动的多个线程的名字依次为 Thread-1、Thread-2、Thread-3、...、Thread-n 等。

执行结果，可以看出两个线程交替运行
```
Thread-1 aaaMainThread

Thread-1 bbb
MainThreadThread-1 ccc

MainThread
MainThread
MainThread

```
> 如果程序中不显式创建任何线程，则所有程序的执行，都将由主线程 MainThread 完成，程序就只能按照顺序依次执行。
## 继承Thread类创建线程类
通过继承来创建线程的时候，子类不应该覆盖run()方法以外的其他的方法（除了构造函数）。换句话说，只覆盖Thread类
的`__init__()`方法和`run()`方法
```python
import threading

# 创建子线程类，继承自 Thread 类
class MyThread(threading.Thread):
    def __init__(self, add):
        super(MyThread, self).__init__()
        # threading.Thread.__init__(self)
        self.add = add

    # 重写run()方法
    def run(self):
        for arc in self.add:
            # 调用 getName() 方法获取当前执行该程序的线程名
            print(threading.current_thread().getName() + " " + arc)

my_tuple = ('aaa', 'bbb', 'ccc')

my_thread = MyThread(my_tuple)
my_thread.start()

# 让主线程也执行工作
for i in range(5):
    print(threading.current_thread().getName())
```
运行结果
```
Thread-1 aaaMainThread

Thread-1 bbbMainThread

Thread-1 ccc
MainThread
MainThread
MainThread
```


