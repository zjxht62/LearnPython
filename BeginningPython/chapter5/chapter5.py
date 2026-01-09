# 可以打印多个参数，会用空格分开
print('Age', 42)  # Age 42

# 自定义分隔符
print("哇", "哈", "哈", sep="_")

# 自定义结束字符串，定义为！所以不会换行
print("fuck", "you", end='!')
print("ford")
print('haha')
# fuck you!ford
# haha

# 序列解包:将一个序列（或任何可迭代对象）解包，并将得到的值存储到一系列变量里
# 同时赋值
x, y, z = 1, 2, 3
print(x, y, z)
# 可以用来交换值
x, y = y, x
print(x, y, z)

values = 1, 2, 3
x, y, z = values
print(x)

# 和js里结构感觉很像，但是这里不要求名称必须对应
person = {"name": 'zjx', "girlfriend": 'ckx'}
key, value = person.popitem()
print(key, value)

# 利用*来收集剩余参数
x, y, *z = [1, 2, 3, 4]
print(z)  # [3, 4]
# 也可以收集中间的参数
x, *y, z = [1, 2, 3, 4, 5]
print(y)  # [2, 3, 4]
# 即使收集到的参数数量为1，返回的也是一个列表
x, y, *z = [1, 2, 3]
print(x, y, z)  # 1 2 [3]

### 链式赋值
x = y = 1

### 增强赋值
x = 2
x += 1
x *= 2
print(x)

fnord = 'foo'
fnord += 'bar'
fnord *= 2
print(fnord)

# 5.4 条件和条件语句
# Python中认为为假的值：False None 0 "" () [] {}
# 各种类型的数值0，空序列，以及空映射都视为假，而其他各种值都视为真
print(True == 1)
print(False == 0)
print(True + False + 12)  # 13

# 可以利用bool函数转换其他值
print(bool("fuck"))
print(bool(42))
print(bool(''))
print(bool(0))

# if示例
num = int(input(('Enter a number')))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

name = input("What's your name?")
if name.endswith('Gumby'):
    if name.startswith("Mr."):
        print('Hello, Mr.Gumby')
    elif name.startswith("Mrs."):
        print('Hello, Mrs. Gumby')
    else:
        print('Hello, Gumby')
else:
    print("Hello Stranger")

# is 和 == is来判断是否是相同的对象 ==来判断值是否相等
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y) #True
print(x is y) #True
print(x == z) #True
print(x is z) #False



# 布尔运算符 and or not
# 布尔运算符只做必要的运算 x and y 只要x为false 那么立即返回false
# 如果x为假，那么这个表达式将返回x，否则返回y
# 对于运算符or，情况亦如此。在表达式x or y中，如果x为真，就返回x，否则返回y。
# 请注意，这意味着位于布尔运算符后面的代码（如函数调用）可能根本不会执行。

# 5.4.7 断言
age = -1
# assert age > 0, 'The age must be realistic'

# 5.5 循环
# while循环
x = 1
while x < 101:
    print(x)
    x += 1

name = ''
while not name:
    name = input('Enter your name:')
print(f'hello{ name}!')

# for循环
# 可以使用for循环遍历可迭代的对象
words = ['fuck', 'you', 'haha']
for w in words:
    print(w)

# 利用range()函数创建范围
print(list(range(0, 10)))

for num in range(1, 101):
    print(num)

d = {"x": 1, 'y': 2, 'z': 3}
for key, value in d.items():
    print(key, "对应的value是", value)

for key in d:
    print(key, '对应的值', d[key])

# 使用zip函数 缝合两个序列 如果长度不同，将取更短者的长度
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
# 将返回一个由元组组成的list  [('anne', 12), ('beth', 45), ('george', 32), ('damon', 102)]
newList = list(zip(names, ages))
for name, age in newList:
    print('名字是', name, '年龄', age)

# 迭代时获取索引
strings = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1']
for index, string in enumerate(strings):
    if 'c' in string:
        strings[index] = '哈'

# break
from math import sqrt

# 从99开始以步长为-1迭代,找到小于100的最大平方值（乘数与自己相乘的结果）
for n in range(99, 0, -1):
    root = sqrt(n)
    print(root)
    if root == int(root):
        print(n)
        break

# continue用来跳出当前循环开始下次循环

# 循环中的else语句 它仅在没有调用break时才执行
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find it")

# 5.6 简单推导
# 生成从0到9的平方组成的列表
print([x * x for x in range(10)])  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 打印那些能被3整除的平方值
print([x * x for x in range(10) if x % 3 == 0])  # [0, 9, 36, 81]

print([(x, y) for x in range(3) for y in range(3)])
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 将girls和boys的首字母配对
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print([b + "+" + g for b in boys for g in girls if b[0] == g[0]])
# ['chris+clarice', 'arnold+alice', 'bob+bernice']

letterGirls = {}
for girl in girls:
    # 建立字典，key为首字母，value默认为[]，之后添加girl全名
    letterGirls.setdefault(girl[0], []).append(girl)
    print("输出每次的letterGirls", letterGirls)
print([b + "+" + g for b in boys for g in letterGirls[b[0]]])

# 使用圆括号并不能实现元组推导，而是创建生成器
# 然而可以使用花括号执行字典推导
squares = {i: "{} squared is {}".format(i, i ** 2) for i in range(10)}
print(squares[8])

# 5.7 pass del 和exec
# pass可以用作占位符，表示什么都不做
if name == 'Ralph Auldus Melish':
    print('Welcome')
elif name == 'Enid':
    # 还未完成
    pass
elif name == 'Bill Gates':
    print('Access Denied')

# 使用del删除
dit1 = {'x': 1, 'y': 2}
dit2 = dit1
dit1 = None
dit2 = None
# Python解释器将进行垃圾回收 因为没有对象引用它了

x = 1
del x
# print(x)
#NameError: name 'x' is not defined

#exec和eval执行字符串及计算结果
#exec
exec("print('hello world')")
# 执行的同时传入命名空间防止污染其他代码
from math import sqrt
scope = {}
exec("sqrt = 1", scope)
print(sqrt(4))

#eval计算用字符串表示的Python表达式的值，并返回结果（exec什么都不返回，因为它本身是条语句）。
print(eval(input("请输入表达式")))
#也可以提供命名空间
