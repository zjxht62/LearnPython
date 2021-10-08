my_list = ['one', 'two', 'three']
# 用fromkeys方法创建字典
my_dict = dict.fromkeys(my_list, [])
# 打印每个列表的id
print(id(my_dict['one']))
print(id(my_dict['two']))
print(id(my_dict['three']))

# 给其中一个列表添加一个元素
my_dict['one'].append('哈哈')
print(my_dict)


# 正确方案
my_dict = {key:[] for key in my_dict}
# 打印每个列表的id
print(id(my_dict['one']))
print(id(my_dict['two']))
print(id(my_dict['three']))
# 给其中一个列表添加一个元素
my_dict['one'].append('哈哈')
print(my_dict)
