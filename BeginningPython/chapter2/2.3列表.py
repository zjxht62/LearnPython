# 2.3.1 list()函数
# 使用list函数将序列转为列表
str = "大懒蛋光吃"
print(list(str))

# 2.3.2 基本列表操作
str = "大懒蛋光吃"
strList = list(str)
# 赋值
strList[0] = '小'
print(strList)
# 删除
del strList[0]
print(strList)
# 分片赋值
strList[0:2] = ['粪', '粪']
print(strList)
# 利用分片来插入，同理可用于删除
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print(numbers)

# 2.3.3 列表方法

# append用于追加单个值
lst = [1, 2, 3]
lst.append(4)
lst.append([4, 4, 4])
print(lst)
# [1, 2, 3, 4, [4, 4, 4]]

# count用于统计出现的次数
['to', 'be', 'or', 'not', 'to', 'be'].count('to')

# extend用于一次性追加另外序列中的所有值
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # [1, 2, 3, 4, 5, 6]
print(a)  # [1, 2, 3]
a.extend(b)  # extend会对原列表进行修改 而 + 不会
print(a)  # [1, 2, 3, 4, 5, 6]

# index方法，返回第一个匹配项的索引值
nameList = ['ckx', 'zjx', 'wh', 'zjx']
print(nameList.index('zjx'))  # 1

# insert
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print(numbers)

# pop 移除最后一个元素并返回该元素的值
numbers = [1, 2, 3]
print(numbers.pop())  # 3
print(numbers)  # [1, 2]

# remove 移除第一个匹配项
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print(x)

# reverse将列表元素反向存放
x = [1, 2, 3]
x.reverse()
print(x)

# sort 改变数组但并不返回任何值
x = [1, 2, 53, 3, 4, 1]
y = x.sort()
print(y)  # None
y = x[:]
y.sort()
print(y)

# 高级排序 通过给定比较函数来排序
numbers = [5, 2, 9, 7]
# 可选参数key和reverse
# key
x = ['sadfsd', 'sadf', 'sdafsdfsadf', 'sd']
x.sort(key=len)  # ['sd', 'sadf', 'sadfsd', 'sdafsdfsadf']
# reverse
numbers = [5, 2, 9, 7]
numbers.sort(reverse=True)  # [9, 7, 5, 2]
