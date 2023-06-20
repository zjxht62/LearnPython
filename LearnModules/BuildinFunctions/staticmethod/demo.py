def regular_function():
    print("I'm regular_function")

class C:
    # 通过调用staticmethod方法，将外部方法引用到类的静态方法
    method = staticmethod(regular_function)

if __name__ == '__main__':
    C.method()