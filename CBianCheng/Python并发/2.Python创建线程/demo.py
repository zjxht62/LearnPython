import threading


# # 定义线程要调用的方法，*add可以接收多个以非关键字方式传入的参数
# def action(*add):
#     for arc in add:
#         # 通过getName方法获取当前执行该程序的线程名
#         print(threading.current_thread().getName() + " " + arc)
# 
# my_tuple = ('aaa', 'bbb', 'ccc')
# 
# thread = threading.Thread(target=action, args=my_tuple)
# thread.start()
# 
# # 让主线程也执行工作
# for i in range(5):
#     print(threading.current_thread().getName())

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