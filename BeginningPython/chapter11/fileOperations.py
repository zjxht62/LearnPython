#文件操作的基本方法
f = open('somefile1.txt')
print(f.read(7))
print(f.read(4))
f.close()

f = open('somefile1.txt')
print(f.read())
f.close()

#readline()
f = open('somefile1.txt')
for i in range(3):
    print(str(i) + ': ' + f.readline(), end="")
f.close()

#readlines()
import pprint
f = open('somefile1.txt')
pprint.pprint(f.readlines())
f.close()

#write()
f = open('somefile1.txt', 'w')
f.write('this \nis no \nhaiku')
f.close()

f = open('somefile1.txt')
lines = f.readlines()
lines[1] = "isn't a\n"
f.close()
f = open('somefile1.txt', 'w')
f.writelines(lines)
f.close()
