import threading


# 线程要执行的方法
def action(*params):
    for p in params:
        print(threading.current_thread().getName() + " " + p)

# 传入的参数
params = ('aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff')

# 实例化Thread创建线程，此时处于新建状态
thread = threading.Thread(target=action, args=params, daemon=True)
# 调用start()方法，进入就绪状态
thread.start()
# 主线程执行
for i in range(2):
    print(threading.current_thread().getName() + " " + str(i))


