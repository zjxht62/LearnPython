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


