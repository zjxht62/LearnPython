numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 获取第4个到第5个元素
# 含头不含尾
print(numbers[3:5])
# out:[4, 5]

# 访问最后三个元素
print(numbers[-3:])

# 获取前三个元素
print(numbers[:3])

# 控制步长
print(numbers[:7:2])
# out:[1, 3, 5, 7]

# 首先截取包含索引10但是不包含索引5的 之后开始按步长提取
print(numbers[10:2:-2])
# out：[10, 8, 6, 4]