# 构造函数
# Python 不同于java 只能有一个构造函数，不支持通过参数重载
# 如果定义了多个，会用最晚定义的那个
from typing import overload, List


class Foobar:

    def __init__(self, value=42):
        self.somevar = value


#     def __init__(self, value1, value2):
#         self.somevar = value1
#         self.somevar2 = value2
#
#     def __init__(self):
#         self.somevar = 45
#
#
f = Foobar()
print(f.somevar)  # 45
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
def check_key(key):
    # 如果key的类型不对，应抛出TypeError
    if not isinstance(key, int):
        raise TypeError
    # 如果key的值不合法，应抛出IndexError
    if key < 0:
        raise IndexError


class ArithmeticSequence:

    def __init__(self, start=0, step=1):
        """
        初始化这个算术序列
        start -序列中的第一个值
        step -两个相邻值的差
        changed -一个字典，包含用户修改后的值
        """
        self.start = start
        self.step = step
        # 用一个字典保存修改的元素
        self.changed = {}

    def __getitem__(self, key):
        check_key(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        check_key(key)
        self.changed[key] = value

    # 因为是无穷序列，所以没有实现__len__
    # 因为不允许进行修改，所以没实现__del__


arithmetic_seq = ArithmeticSequence(1, 2)
print(arithmetic_seq[0])  # 1
print(arithmetic_seq[1])  # 3
print(arithmetic_seq[2])  # 5
print(arithmetic_seq[3])  # 7
print(arithmetic_seq[4])  # 9
arithmetic_seq[4] = 999
print(arithmetic_seq[4])  # 999


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
print(cl)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(cl.counter)  # 0
print(cl[4] + cl[2])  # 6
print(cl.counter)  # 2 调用了两次__getitem__方法


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


r = Rectangle()
r.width = 10
r.height = 5

print(r.size)  # (10, 5)
r.size = 150, 100
print(r.width)  # 150


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
MyClass.staticMehtod()  # 我是静态方法
MyClass.classMethod()  # 我是类方法 <class '__main__.MyClass'>


### 9.5.3 __getattr__  __setattr__等方法
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
        print(f)  # 1597
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
print(list(ti))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 9.7 生成器
# 生成器是一种使用普遍函数语法定义的迭代器
# 包含yield语句的函数都被称为生成器。每次使用yield生成一个值后，函数都将冻结，即在此停止执行，等待被重新唤醒
# 被重新唤醒之后，函数将从停止的地方开始继续执行
nested = [[1, 2], [3, 4], [5]]


def flatten(nested):
    for sublist in nested:
        for ele in sublist:
            yield ele


print(list(flatten(nested)))  # [1, 2, 3, 4, 5]



# 通过递归来实现嵌套列表展开
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flatten([[1], 2, 3, 4, [5, [6, 7], 8]])))


# 9.7.3 通用生成器
# ： 生成器的函数和生成器的迭代器。生成器的函数
# 是由def语句定义的，其中包含yield。生成器的迭代器是这个函数返回的结果。用不太准确的话
# 说，这两个实体通常被视为一个，通称为生成器。

# 9.7.4 生成器的方法
# 在生成器开始运行后，可使用生成器和外部之间的通信渠道向它提供值。这个通信渠道包含
# 如下两个端点。
# 1.外部世界：外部世界可访问生成器的方法send，这个方法类似于next， 但接受一个参数（要发送的“消息”，可以是任何对象）。
# 2.生成器：在挂起的生成器内部， yield可能用作表达式而不是语句。换而言之，当生成器重新运行时， yield返回一个值——通过send从外部世界发送的值。如果使用的是next，yield将返回None。
def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new


r = repeater(42)
print(r.__next__())
print(r.send("Hello, world"))
print(r.__next__())
print(r.__next__())

# 生成器还包含另外两个方法。
# 方法throw：用于在生成器中（ yield表达式处）引发异常，调用时可提供一个异常类型、一个可选值和一个traceback对象。
# 方法close：用于停止生成器，调用时无需提供任何参数
