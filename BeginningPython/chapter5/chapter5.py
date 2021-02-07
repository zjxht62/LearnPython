# 可以打印多个参数，会用空格分开
print('Age', 42)  # Age 42

# 自定义分隔符
print("哇", "哈", "哈", sep="_")

# 自定义结束字符串，定义为！所以不会换行
print("fuck", "you", end='!')
print("ford")
# fuck you!ford

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

# 5.4 条件和条件语句
# Python中认为为假的值：False None 0 "" () [] {}
# 各种类型的数值0，空序列，以及空映射都视为假，而其他各种值都视为真
print(True == 1)
print(False == 0)
print(True + False + 12)  # 13

# 可以利用bool函数转换其他值
bool("fuck")
bool(42)
bool('')
bool(0)

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
print(x == y)
print(x is y)
print(x == z)
print(x is z)

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
