# 打开文件
f = open('somefile.txt')

# 通过不同的文件模式来指出要对文件进行的操作
# 这里总结一下w+和r+的不同，w+会删除文件原有的内容，并从头开始写
# r+也是从头开始写，但是会保留原文件未被覆盖的内容
f = open('somefile.txt', 'w+')
f.write("我是w+写入的")
f.close()
# f = open('somefile.txt', 'r+')
# f.write("我是r+写入的")
# f.close()

f = open('somefile.txt', 'r')
print(f.read(4))  # 读取四个字符
print(f.read())  # 读取剩余所有

# 使用seek和tell可以实现在文件中的光标移动，以及获取当前位置
f = open('somefile.txt', 'w')
f.write("01234567890123456789")
print(f.seek(5))  # 5
f.write('Hello, World!')
f.close()

f = open('somefile.txt')
print(f.read())

f = open('somefile.txt')
f.seek(3)
print(f.tell())

# 使用完文件后要记得close
# 传统的处理方式
f = open('somefile.txt', 'w')
try:
    f.write('')
finally:
    f.close()
# 使用with语句来将打开的文件赋给somefile变量，在语句体内，可以进行文件操作，到达结尾时将自动关闭文件
with open("somefile.txt", 'r+') as somefile:
    somefile.read()
    somefile.write("")


# 迭代文件内容
# 定义一个操作
def process(string):
    print('Processing:', string)


# 每次一个字符
with open('somefile1.txt') as f:
    while True:
        char = f.read(1)
        if not char:
            break
        process(char)

#每次一行
with open('somefile1.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        process(line)

#如果文件不太大 可以直接读取全部内容进行迭代
with open('somefile1.txt') as f:
    for char in f.read():
        process(char)

with open('somefile1.txt') as f:
    for line in f.readlines():
        process(line)

#最常见的方法就是直接迭代文件，文件是可迭代的
with open('somefile1.txt') as f:
    for line in f:
        process(line)

#对迭代器做的操作可以用于文件
f = open('somefile1.txt', 'w')
# 使用了print来写入文件，这将自动在提供的字符串后面添加换行符
print('First' ,'line', file=f)
print('Second' ,'line', file=f)
print('Third','and final' ,'line', file=f)
f.close()
lines = list(open('somefile1.txt'))
print(lines)
# 对打开的文件进行序列解包，从而将每行存储到不同的变量中。(实际不常用)
first, second, third = open('somefile1.txt')
print(first)
print(second)
print(third)
