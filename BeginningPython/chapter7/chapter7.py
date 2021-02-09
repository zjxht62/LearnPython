# 创建自定义类
# self指向对象本身
class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))


zjx = Person()
zjx.setName('zjx')
zjx.greet()
ckx = Person()
ckx.setName('ckx')
ckx.greet()


##############################################################################
# 7.2.3 属性、函数和方法
# 函数和方法的区别就在于，方法将其第一个参数关联到它所属的实例
class Class:
    def method(self):
        print("我是一个方法", "我有self")


def function():
    print("我是一个函数，没有self")


instance = Class()
# 调用原本的有self的方法
instance.method()  # 我是一个方法 我有self
# 将对象里面的method换成function
instance.method = function
instance.method()  # 我是一个函数，没有self


############################################################################################
# 7.2.4 再谈隐藏
# 默认情况下，可以直接通过对象.属性来访问对象的属性，但是这样的话有些破坏封装
# 可以将属性定义为私有。私有属性不能从外部对象访问，而只能通过getter/setter访问

# 通过在属性或方法名前添加两个下划线来使其成为私有的
class Secretive:
    def __inaccessible(self):
        print("我是私有方法输出的内容")

    def accessible(self):
        print("我来调用私有方法")
        self.__inaccessible()


s = Secretive()
# s.__inaccessible() #AttributeError: 'Secretive' object has no attribute '__inaccessible'
s.accessible()

# 但是是有奇怪的方法来调用的 在类定义中，对所有以两个下划线开头的名称都进行转换，即在开头加上一个下划线和类名
# 比如这里的 __inaccessible() 就变成 _Secretive__inaccessible()
# 直接调用私有方法
s._Secretive__inaccessible()


# 如果你不希望名称被修改，又想发出不要从外部修改属性或方法的信号，可用一个下划线打
# 头。这虽然只是一种约定，但也有些作用。例如， from module import *不会导入以一个下划线
# 打头的名称①。

#############################################################################################
# 7.2.5 类的命名空间
# 在class语句中定义的代码都是在一个特殊的命名空间（类的命名空间）内执行的，而类的所有成员都可以访问这命名空间
# 这里就类似java里的类变量

class MemberCounter:
    members = 0

    def init(self):
        MemberCounter.members += 1


m1 = MemberCounter()
m1.init()
print(MemberCounter.members)  # 1
m2 = MemberCounter()
m2.init()
print(MemberCounter.members)  # 2

# 每个实例都可以访问这个类变量
print(m1.members)  # 2
print(m2.members)  # 2

# 实例变量会遮盖类变量
m1.members = 'two'
print(m1.members)  # two
print(m2.members)  # 2


##################################################################
# 7.2.6 指定超类
# 要指定超类，可以在定义类的时候加上超类名，并用括号括起来
class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


# 继承Filter
class FuckFilter(Filter):
    def init(self):
        self.blocked = ['Fuck']


fuckFilter = FuckFilter()
fuckFilter.init()
seq = ['Fuck', 'you', 'Ford']
seq = fuckFilter.filter(seq)
print(seq)

##########################################################
# 7.2.7 深入探讨继承
# 通过issubclass方法判断是否是一个类的子类
print(issubclass(FuckFilter, Filter))  # True

# 通过__base__属性获得基类信息
print(FuckFilter.__base__)  # <class '__main__.Filter'>

# 通过isinstance()方法判断对象是否是某类的实例
fuckFilter = FuckFilter()
print(isinstance(fuckFilter, FuckFilter))  # True
print(isinstance(fuckFilter, Filter))  # True

# 通过__class__属性获得对象所属的类
print(fuckFilter.__class__)


#####################################################
# 7.2.8 多个超类 多重继承
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print("Hi, my value is", self.value)


class TalkingCalculator(Calculator, Talker):
    pass


tc = TalkingCalculator()
tc.calculate("1 + 2")
tc.talk()  # Hi, my value is 3

# 使用多重继承时，有一点务必注意：如果多个超类以不同的方式实现了同一个方法（即有多个同名方法）
# ，必须在class语句中小心排列这些超类，因为位于前面的类的方法将覆盖位于后面的类的方法。

###############################################################
# 7.2.9 接口和内省
# Python和Java不同，Python不显式得指定对象必须包含哪些方法才能用作参数。
# 不能像Java那样显式编写接口，只能假定这个对象有你需要的方法，或者通过检查来保证

# 通过hasattr函数来判断所需方法是否存在
print(hasattr(tc, 'talk'))  # True
# getattr可以获取属性，并设置默认返回
print(callable(getattr(tc, 'talk', None)))  # True

#################################################
# 7.2.10 抽象基类
# Python官方通过引入abc模块来支持抽象基类
from abc import ABC, abstractmethod


class Talker(ABC):
    # 使用abstractmethod 装饰器来表示这个方法是抽象方法
    @abstractmethod
    def talk(self):
        pass


# 抽象类不能被实例化
# Talker() #TypeError: Can't instantiate abstract class Talker with abstract methods talk

# 继承了抽象基类但是没覆盖方法的类也不行，也是抽象的
class Kingget(Talker):
    pass


# 继承并覆盖方法
class Knigget(Talker):

    def talk(self):
        print("Ni")


knigget = Knigget()
knigget.talk()

# 此时isinstance函数才是有用的，因为确定了是某个抽象基类的实例，所以一定有实现了的抽象方法
k = Knigget()
if isinstance(k, Talker):
    k.talk()


# 为了实现更高级别的多态，只关心对象能做什么，可以将一个类注册为另一个类
class Herring:
    def talk(self):
        print("Blub.")


# h肯定不是Talker的实例
h = Herring()
print(isinstance(h, Talker))  # False

# 将Herring注册成Talker
Talker.register(Herring)
print(isinstance(h, Talker))  # True

# 但是通过注册，无法保证这个类确实实现了需要的方法
class Clam:
    pass

c = Clam()
Talker.register(Clam)
print(issubclass(Clam, Talker)) #True
print(isinstance(c, Talker)) #True
# 但是c并没有talk方法
# c.talk() #AttributeError: 'Clam' object has no attribute 'talk'