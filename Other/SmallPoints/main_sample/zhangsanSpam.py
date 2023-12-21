import spam
spam.spam1()
spam.spam1()
spam.spam2('郭老板')
spam.spam3('郭老板')
spam.spam4('郭老板')

# 在zhangsanSpam.py里通过import spam导入spam.py，会执行一遍spam.py里的所有代码。
# 这里面有张三想要的几个spam()函数的定义，但是他不想要的骂黄老板的代码也跟着运行了。