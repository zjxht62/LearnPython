class A:

    def __method(self):
        print('我是A里面的__method')

    def method(self):
        self.__method()


a = A()
a.method()  # output:我是A里面的__method


class B(A):
    def __method(self):
        print('我是B里面的__method')


b = B()
b.method()  # output:我是A里面的__method，并没有覆盖父类的方法


class C:
    class_var = 10  # 类变量

    def __init__(self, instance_var):
        self.instance_var = instance_var  # 实例变量


c1 = C(1)
# 通过实例可以访问类变量和实例变量
print(c1.instance_var)  # output: 1
print(c1.class_var)  # output: 10
c2 = C(2)
print(c2.instance_var)  # output: 2
print(c2.class_var)  # output: 10

# 直接通过类访问类变量
print(C.class_var)


