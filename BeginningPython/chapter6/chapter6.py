# 前10个斐波那契数列
fib = [0, 1]
for i in range(8):
    fib.append(fib[-1] + fib[-2])
print(fib)

# 可以通过callable判断对象是否可调用
import math

x = 1
y = math.sqrt
print(callable(x))
print(callable(y))


# 定义函数
def hello(name):
    return 'hello ' + name


print(hello("zjx"))


def fib(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-1] + result[-2])
    return result


print(fib(20))


# 给函数添加文档
# 放在函数开头的字符串称为文档字符串（docstring），将作为函数的一部分存储起来。
def haha():
    """就是打印哈哈而已"""
    print('哈哈 ')


print(haha.__doc__)


# 函数对于参数的改变
def changeStr(s):
    s = "haha"


s1 = '哈哈'
changeStr(s1)
# 还是哈哈，因为字符串以及数和元组是不可变的，你不能修改他们，只能替换
print(s1)


# 但是如果是可变的数据结构就会被修改
def changeList(n):
    n[0] = '哈哈'


l1 = [1, 2, 3]
changeList(l1)
print(l1)

# 举个例子来看函数的作用
storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    return data[label].get(name)


def store(data, fullName):
    names = fullName.split()
    if len(names) == 2:
        names.insert(1, "")
    labels = 'first', 'middle', 'last'

    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(fullName)
        else:
            data[label][name] = [fullName]


mybook = {}
init(mybook)
store(mybook, 'Zhao Jixiang')
store(mybook, 'Da Chou Bao')
print(lookup(mybook, 'middle', ''))


# 调用时指定关键字参数
def hello(greeting, name):
    print('{}, {}!'.format(greeting, name))


hello(greeting='Fuck you', name='Ford')


# 可以在定义函数时指定默认值
def helloWithDefault(greeting='Hello', name='world'):
    print('{}, {}!'.format(greeting, name))


helloWithDefault(name='ckx')


def hello4(name, greeting='Hello', punctuation='!'):
    print('{}, {}{}'.format(greeting, name, punctuation))


hello4('Mars')


# 收集剩余参数
def printParams(*params):
    print(params)


# 剩余参数将被收集到元组中
printParams(1, 2, 3)


def print_params_2(title, *params):
    print(title)
    print(params)


print_params_2('Params', 1, 2, 3)


# 收集中间的参数，这时必须指定后续参数名称
def inTheMiddle(x, *y, z):
    print(x, y, z)


inTheMiddle(1, 2, 3, 4, 5, 6, z=7)


# *不会收集关键字参数
# print_params_2("title", something = 42)
# TypeError: print_params_2() got an unexpected keyword argument 'something'

# 使用**来收集关键字参数，这将返回字典
def printParams3(title, **params):
    print(title, params)


printParams3("我是title", haha='哈哈', heihei='嘿嘿')


# 我是title {'haha': '哈哈', 'heihei': '嘿嘿'}

# 分配参数
# 通过*和**也可以进行相反的操作，将元组和字典解构出来给函数

def add(x, y):
    return x + y


params = (1, 2)
print(add(*params))

params = {'name': 'Sir Robin', 'greeting': 'Well met', 'punctuation': '!'}
hello4(**params)

# 6.5作用域
