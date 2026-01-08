from math import pi

## 3.2 字符串格式化：精简版
# 字符串格式化使用字符串格式化操作符，即百分号来实现
format = 'Hello, %s, %s enough fo ya?'
values = ('world', 'hot')
print(format % values)
# 使用%s的时候，对应参数应该是字符串类型，如果不是的话会自动调用str方法转换

# 格式化浮点数
format = 'Pi保留三位小数: %.3f'
print(format % pi)

from string import Template

tmpl = Template("Hello, $who! $what enough for ya?")
print(tmpl.substitute(who='zjx',
                      what='Dusty'))  # Hello, zjx! Dusty enough for ya?

# 直接将参数按顺序输出
print("{}, {} and {}".format('first', 'second', 'third'))
# first, second and third

# 通过索引来访问
print("{0} {1} {2} {3} {0} {1}".format('to', 'be', 'or', 'not'))
# to be or not to be

# 使用命名字段
print("{name} is approximately {value:.2f}.".format(value=pi, name="兀"))
# 兀 is approximately 3.14.

# 当变量与替换字段同名，可以进行简写
from math import e

# 最常用
print(f"Euler's constant is roughly {e}")
# Euler's constant is roughly 2.718281828459045
