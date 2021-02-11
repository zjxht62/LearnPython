# 构造函数
# Python 不同于java 只能有一个构造函数，不支持通过参数重载
# 如果定义了多个，会用最晚定义的那个
from typing import overload, List


class Foobar:

    def __init__(self, value=42):
        self.somevar = value

    # def __init__(self, value1, value2):
    #     self.somevar = value1
    #     self.somevar2 = value2
    #
    # def __init__(self):
    #     self.somevar = 45


f = Foobar()
print(f.somevar)
f = Foobar(99)
print(f.somevar)


# 9.2.1 重写普通方法和特殊的构造函数
class A:
    def hello(self):
        print('Helo from A')


class B(A):

    def hello(self):
        print('Hello from B')


a = A()
a.hello()
b = B()
b.hello()


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃吃吃")
            self.hungry = False
        else:
            print("老子不饿")


b = Bird()
b.eat()
b.eat()


class SongBird(Bird):
    def __init__(self):
        # 调用父类的构造方法
        super().__init__()
        self.sound = '鸟叫'

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()
sb.eat()  # 因为没有调用父类的构造方法，所以没有hungry这个属性


# 9.3 元素访问
# 9.3.1 基本的序列和映射协议

# 创建一个无穷序列
def checkIndex(key):
    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value


s = ArithmeticSequence(1, 2)
print(s[4])  # 9
s[4] = 2
print(s[4])
print(s[5])


# 因为没有实现__del__所以无法删除元素 del s[4]
# 因为是无穷序列 所以也没有__len__方法


# 9.3.2 从list、dict和str派生
# 可以通过继承现有的内置类型
# 实现一个带访问计数器的list

class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super().__getitem__(index)


cl = CounterList(range(10))
print(cl)
print(cl.counter)
print(cl[4] + cl[2])
print(cl.counter)


# 9.5.1 函数property
# 使用property函数，能够让我们将存取方法和直接访问属性绑定起来，实现在用.获取和设置属性时进行校验等操作
class Rectangle():
    def __init__(self):
        self.width = 0
        self.height = 0

    def getSize(self):
        print('我是getSize方法，我被调用了')
        return self.width, self.height

    def setSize(self, size):
        print('我是setSize方法，我被调用了')
        self.width, self.height = size

    size = property(getSize, setSize)


# 没有加property
r = Rectangle()
r.height = 5
r.width = 10
print(r.getSize())
r.setSize((100, 99))
print(r.width)
print(r.height)

# 通过property来将size属性和getter/setter关联
print(r.size)


# 9.5.2 静态方法和类方法
# 静态方法的定义中没有参数self，可直接通过类来调用。
# 类方法的定义中包含类似于self的参数，通常被命名为cls。对于类方法，也可通过对象直接调用，但参数cls将自动关联到类。

class MyClass:

    @staticmethod
    def staticMehtod():
        print('我是静态方法')

    @classmethod
    def classMethod(cls):
        print('我是类方法', cls)


# 无需实例化对象，直接通过类来调用
MyClass.staticMehtod()
MyClass.classMethod()


# 9.5.3 __getattr__  __setattr__等方法
# 这些方法可以拦截对对象属性的所有访问企图，用途之一就是在旧式类中实现特性（在旧式类中，函
# 数property的行为可能不符合预期）。要在属性被访问时执行一段代码，必须使用一些魔法方法。

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, key, value):
        if key == 'size':
            self.width, self.height = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        if item == 'size':
            return self.width, self.height
        else:
            raise AttributeError()


# 9.6 迭代器
# 9.6.1 迭代器协议
# 只要实现了方法__iter__的对象都是可迭代的对象，可以用for in进行迭代
# 方法__iter__返回一个迭代器，它是包含方法__next__的对象，而调用这个方法时可不提供
# 任何参数。当你调用方法__next__时，迭代器应返回其下一个值。如果迭代器没有可供返回的值，
# 应引发StopIteration异常。

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break

# 9.6.2 从迭代器创建序列
class TestIterator:
    value = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
ti = TestIterator()
print(list(ti))
