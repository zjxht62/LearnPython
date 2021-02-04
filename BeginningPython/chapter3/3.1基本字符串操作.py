## 3.1基本字符串操作
#字符串是一种序列，所以像索引、分片、in、len等操作都支持
#但是字符串不可变，不能通过分片来改变其值
string = 'abc'
string[len(string):] = 'd'
print(string)
#TypeError: 'str' object does not support item assignment

