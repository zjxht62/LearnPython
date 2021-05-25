"{foo} {} {bar} {}".format(1, 2, bar=4, foo=3)  # 3 1 4 2

"{foo} {1} {bar} {0}".format(1, 2, foo=3, bar=4)  # 3 2 4 1

full_name = ['trevor', 'zhao']
print('Mr {name[1]}'.format(name=full_name))  # Mr zhao

import math
from math import pi

tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
print(tmpl.format(mod=math))

# 指定转换标志
print("{pi!s} {pi!r} {pi!a}".format(pi="π"))  # π 'π' '\u03c0'

print("The number is {num}".format(num=42))
# The number is 42
print("The number is {num:f}".format(num=42))
# The number is 42.000000
print("The number is {num:b}".format(num=42))
#  The number is 101010


print("{num:10}".format(num=3))  # 3

print("{name:10}".format(name="Trevor"))  # Trevor

print("{pi:10.2f}".format(pi=pi))  # 3.14

print('One googol is {:,}'.format(10 ** 100))
# One googol is 10,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000

# 同时指定其他格式设置元素时，这个逗号应放在宽度和表示精度的句点之间①。
print('One googol is {:10,.5f}'.format(10000))
# One googol is 10,000.00000

# 使用0来填充数字
"{:010.2f}".format(pi)  # 0000003.14

# 指定左对齐、右对齐和居中，可以分别使用<、>和^
print("{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}".format(pi))
# 3.14
#   3.14
#      3.14

print("{:$^15}".format(" WIN BIG "))  # $$$ WIN BIG $$$
print('{0:10.2f}\n{1:10.2f}'.format(pi, -pi))
#      3.14
#     -3.14
print('{0:10.2f}\n{1:=10.2f}'.format(pi, -pi))
#      3.14
#-     3.14

print("{0:-.2}\n{1:-.2}".format(pi, -pi))
#3.1
#-3.1
print("{0:+.2}\n{1:+.2}".format(pi, -pi))
#+3.1
#-3.1

#如果符号说明符指定为空格，那么会在正数前加上空格而不是`+`
print("{0: .2}\n{1: .2}".format(pi, -pi))
#3.1
#-3.1


# 对于二进制、八进制和十六进制转换，将加上一个前缀。
print("{:b}".format(42)) # 101010
print("{:#b}".format(42)) # 0b101010

# 各种十进制数，它要求必须包含小数点
print("{:g}".format(42)) # 42
print("{:#g}".format(42)) # 42.0000
