# 文件操作的基本方法
f = open('somefile1.txt')
print(f.read(7))  # Welcome
print(f.read(4))  # to
f.close()

f = open('somefile1.txt')
print(f.read())
# Welcome to this file
# There is nothing here except
# This stupid haiku
f.close()

# readline()
f = open('somefile1.txt')
for i in range(3):
    print(str(i) + ': ' + f.readline(), end="")
f.close()
# 0: Welcome to this file
# 1: There is nothing here except
# 2: This stupid haiku['Welcome to this file\n',

# readlines()
import pprint

f = open('somefile1.txt')
pprint.pprint(f.readlines())
f.close()
# ['Welcome to this file\n',
#  'There is nothing here except\n',
#  'This stupid haiku']

# write()
f = open('somefile1.txt', 'w')
f.write('this \nis no \nhaiku')
f.close()
# 文件somefile1.txt内容：
# this
# is no
# haiku

f = open('somefile1.txt')
# 读取所有行
lines = f.readlines()
# 修改第二行
lines[1] = "isn't a\n"
f.close()
f = open('somefile1.txt', 'w')
#写入文件
f.writelines(lines)
f.close()
# 文件somefile1.txt内容：
# this
# isn't a
# haiku
