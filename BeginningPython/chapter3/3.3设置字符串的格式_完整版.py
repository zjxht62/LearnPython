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


print("{num:10}".format(num=3))  #         3

print("{name:10}".format(name="Trevor"))  #Trevor

print("{pi:10.2f}".format(pi=pi))  #      3.14

print( 'One googol is {:,}'.format(10**100))
# One googol is 10,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000

# 同时指定其他格式设置元素时，这个逗号应放在宽度和表示精度的句点之间①。
print( 'One googol is {:10,.5f}'.format(10000))
# One googol is 10,000.00000