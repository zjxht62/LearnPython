from math import pi
## 3.2 字符串格式化：精简版
#字符串格式化使用字符串格式化操作符，即百分号来实现
format = 'Hello, %s, %s enough fo ya?'
values = ('world', 'hot')
print(format % values)
#使用%s的时候，对应参数应该是字符串类型，如果不是的话会自动调用str方法转换

#格式化浮点数
format = 'Pi保留三位小数: %.3f'
print(format % pi)
