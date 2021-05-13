from pip._vendor.distlib.compat import raw_input

# name = raw_input("What's your name?")
# print("Hello, " + name)

# str函数和repr函数
# str主要用来给终端用户输出一些内容
# repr则用于调试，他展示的是解释器看到的文本，比如字符串是带有引号包裹的

print(repr("Hello,\nworld!"))
# 'Hello,\nworld!'
print(str("Hello,\nworld!"))
# Hello,
# world!



# input和raw_input
# input()要求用户输入的是合法的python表达式，比如要输入字符串，那么就需要带上引号才行，就像是"hello"
# raw_input()函数则会将用户输入的原始数据放到字符串里
# 但是在python3里整合了，只有input()函数了
# name = input("请输入姓名")
# print(name)

# 定义长字符串 使用三引号 可以使用反斜线来忽略换行
print('''哇哈哈\
爱呵呵
哎嘿嘿''')
# out: 哇哈哈爱呵呵
# 哎嘿嘿

# 原始字符串
# 原始字符串不会把反斜线当成特殊字符 但是原始字符串的结尾不能是反斜线\
# 当 r 或者 R 前缀存在的时候，在反斜杠依旧用来转义后面的字符，但是反斜杠本身会保留在字符串中
# 所有 r'Let\'s go!' 包含 L e t \ ' s g o !
# 但是 r'Let\'s go!\' 包含 L e t \ ' s g o ! \ ' 导致没有最后用来配对的单引号
print(r'C:\nowhere\zjx')
print(r'Let\'s go!')
# out: Let\'s go!

print(r'C:\Program Files\foo\bar' '\\')

# Unicode字符串 python3里所有字符串都是Unicode字符串
print(u'Hello,world!')
