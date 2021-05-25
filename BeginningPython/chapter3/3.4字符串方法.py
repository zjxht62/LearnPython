## 3.4 字符串方法
# string模块包含了常见的常量和函数
import string

# 包含0~9的字符串
print(string.digits)
# 包含所有字母
print(string.ascii_letters)
# 包含所有小写字母
print(string.ascii_lowercase)
# 所有可打印字符
print(string.printable)
# 所有标点符号
print(string.punctuation)

print("The Middle by Jimmy Eat World".center(39))
#     The Middle by Jimmy Eat World
print("The Middle by Jimmy Eat World".center(39, "*"))
#*****The Middle by Jimmy Eat World*****

### 3.4.1 find
# 返回子串最左边的索引值，没找到返回-1
title = "Monty Python's Flying Cirus"
print(title.find("Python"))  # 6
print(title.find("zjx"))  # -1

# find可以指定查找的范围
subject = "$$$ Get rich now!!! $$$"
print(subject.find("$$$")) # 0
# 只提供起始点
print(subject.find('$$$', 1)) # 20
# 提供起始点和终点，同样是含头不含尾
print(subject.find("!!!", 0, 10)) # -1

### 3.4.2 join
# join用来在队列里添加元素
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))  # 1+2+3+4+5

dirs = ['home', 'admin', 'logs', 'jmcs']
print('/'.join(dirs))

### 3.4.3 lower
# 返回字符串的小写字母版
string = "ABC"
print(string.lower())

### 3.4.4 replace
# 查找并替换所有匹配项
string = "wa ha ha ha hei hei"
print(string.replace("ha", "hei"))

### 3.4.5 split
# 根据分隔符将字符串分为序列
string = "1,2,3,4,5"
print(string.split(","))

### 3.4.6 strip
# 去除字符串两侧的空格
# 可以对用户输入进行处理，去掉多余的空格
string = "    sdafs   "
print(string.strip())

string = "*** SPAM * for * everyone!!! ***".strip(' *!')
print(string) # SPAM * for * everyone

### 3.4.7 translate
# translate方法只处理单个字符，同时进行多个替换
# 举例：将所有的c=>k s=>z
string = "this is an incredible test"
# 定义一张转换表
table = str.maketrans('cs', 'kz')
print(string.translate(table))

## 3.5 小结
