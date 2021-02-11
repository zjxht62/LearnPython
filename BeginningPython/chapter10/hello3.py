def hello():
    print("HelloWorld3")


# 如果这样的话，在import的时候会打印一遍HelloWorld3，我们并不希望模块在import的时候执行测试代码
# hello()

# 通过变量 __name__ 检查模块是作为程序运行还是被导入另一个程序
def test():
    hello()


if __name__ == '__main__':
    test()
