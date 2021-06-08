# 前10个斐波那契数列
fib = [0, 1]
for i in range(8):
    fib.append(fib[-2] + fib[-1])
print(fib)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 可以通过callable判断对象是否可调用
import math

x = 1
y = math.sqrt
print(callable(x))  # False
print(callable(y))  # True


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


def test():
    print('just a test')
    return
    print('another test')


x = test()  # 打印出 just a test
print(x)  # None

list = [1, 2, 3]
def replaceList(n):
    n = [4, 5, 6]

replaceList(list)
print(list)  # [1, 2, 3]


# 函数对于参数的改变
def changeStr(s):
    s = "haha"


s1 = '哈哈'
changeStr(s1)
# 还是哈哈，因为字符串以及数和元组是不可变的，你不能修改他们，只能替换
print(s1)


# 但是如果是可变的数据结构就会被修改
list = ['嘿嘿', '呵呵']
def changeList(n):
    n[0] = '哈哈'

changeList(list)
print(list)  # ['哈哈', '呵呵']

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

def hello_1(greeting, name):
    print(f'{greeting}, {name}')

hello_1(name='赵吉祥', greeting='吃了吗')

# 调用时指定关键字参数
def hello(greeting, name):
    print('{}, {}!'.format(greeting, name))


hello(greeting='Fuck you', name='Ford')


# 可以在定义函数时指定默认值
def hello3(greeting='你好', name='世界'):
    print(f'{greeting}, {name}')

hello3() # 你好, 世界
hello3('吃了吗') # 吃了吗, 世界
hello3('吃了吗', '您') # 吃了吗, 您
hello3(name='陌生人') # 你好, 陌生人


def hello_4(name, greeting='Hello', punctuation='!'):
    print('{}, {}{}'.format(greeting, name, punctuation))


hello_4('zjx')
hello_4('Mars', 'Howdy')
hello_4('Mars', 'Howdy', '...')
hello_4('zjx', punctuation='。')
hello_4('zjx', greeting='吃了吗')
hello_4(greeting='吃了吗', name='赵吉祥')
hello_4()
# Traceback (most recent call last):
#   File "E:/zjx/PycharmProjects/LearnPython/BeginningPython/chapter6/chapter6.py", line 150, in <module>
#     hello_4()
# TypeError: hello_4() missing 1 required positional argument: 'name'



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
# 内置函数var可以打印看不见的字典
x = 1
scope = vars()
# 取出x
print(scope['x'])
# 对x进行修改
scope['x'] += 1
print(x)


# 除了全局作用域外，每个函数调用都将创建一个作用域
def foo():
    x = 42


x = 1
foo()  # foo并不会改变全局变量的值，
print(x)

# 函数可以引用全局变量，但是可能导致bug，慎用
external = 'berry'


def combine(parameter):
    print(parameter + external)


combine("Shrub")

# 重新关联全局变量
x = 2


def changeGlobal():
    # 告诉Pythonx是全局变量
    global x
    x = x + 1


changeGlobal()
print(x)


# 嵌套可以用一个函数创建另一个函数
# 像multiplyByFactor这样存储其所在作用域的函数称为闭包。
def multipilier(factor):
    def multiplyByFactor(number):
        return number * factor

    return multiplyByFactor


double = multipilier(2)
print(double(5))

triple = multipilier(3)
print(triple(5))


# 6.6 递归
# 通常递归包含两个部分
# 基线条件：满足这种条件时函数将直接返回一个值
# 递归条件：包含一个或多个调用，这些调用旨在解决问题的一部分
# 关键在于，将问题分解为较小的部分，可以避免递归没完没了，因为问题将被分解成基线条件可以解决的最小问题

# 递归实现阶乘
# 1的阶乘为1。
# 对于大于1的数字n，其阶乘为n  1的阶乘再乘以n。
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(10))


# 二分查找
def search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(seq)
x = search(seq, 12)
print(x)
