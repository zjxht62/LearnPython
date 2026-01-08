## 4.2创建和使用字典
phonebook = {'Alice': '2341', 'Beth': '9102', "Cecil": '3258'}
print(phonebook['Cecil'])

### 4.2.1 dict函数
# 可以通过dict，用其他映射或者key value这样的序列来建立字典
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)
print(d['name'])
# 也可以通过关键字参数来创建字典
d = dict(name='Gumby', age=42)
print(d)

# 可以创建字典来嵌套字典
dic1 = {"name": "zjx"}
dic2 = {"info": dic1}
print(dic2["info"]['name'])

### 4.2.2基本字典操作
# 字典基本行为和序列类似
# + len(d) 返回键值对的数量
# + d[k] 返回对应key的value
# + d[k]=v 将value关联到key
# + del d[k] 删除key为k的项
# + k in d 检查是否有key为k的项
# 字典和列表的区别
# + key的类型，可能是整型，或其他不可变类型：浮点型、字符串、元组
# + 自动添加 可以给不存在的key关联value，而列表不行
# + 成员资格 k in d检查的是key是否存在，可以根据key找到对应的value

### 4.2.3 字典的格式化字符串
#  通过在%后加上(key)可以方便得处理字典
print("Cecil's phone number is %(Cecil)s." % phonebook)
# 这种方式在模板中非常有用，我觉得感觉有点儿和js里面的解构似的
template = '''<html>
<head><title>{title}</title></head>
<body>
<h1>{title}</h1>
<p>{text}</p>
</body>
'''
data = {"title": "My home page", "text": "欢迎"}
print(template.format_map(data))

# 现代写法（解构）：
data = {"title": "Home", "text": "Welcome"}
print("{title}: {text}".format(**data))

### 4.2.4 字典方法
# clear 清除字典中所有项,
# 对当前字典进行操作，没有返回值
d = {}
d['name'] = 'zjx'
d["age"] = 26
print(d)
d.clear()
print(d)

# copy返回一个具有相同键值对的新字典(浅复制)
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'root'
y['machines'].remove('bar')
print(y)  # {'username': 'root', 'machines': ['foo', 'baz']}
print(x)  # {'username': 'admin', 'machines': ['foo', 'baz']}
# 当在副本中替换值的时候，原始字典不受影响，但是如果对某个值原地修改，原始的字典也会被改变

# 可以使用深拷贝来解决
from copy import deepcopy

d = {}
d['names'] = ['zjx', 'ckx']
c = d.copy()
dc = deepcopy(d)
d['names'].append('dsh')
print(c)
print(dc)  # 不会受到原字典修改的影响

# fromkeys 用给定的key创建新的字典，默认值设置为None
dict.fromkeys(['name', 'age'])  # {'name': None, 'age': None}
# 可以自己指定默认值
dict.fromkeys(["name", "age"], 'undefined')

# get
d = {}
# 对应没有的key返回None
print(d.get('name'))
# 可以设置get不到时候返回的默认值
print(d.get("name", "没有啊"))
# 正常使用
d['name'] = 'zjx'
print(d.get("name"))

# items
# items将所有键值对 可以用for遍历
d = {'title': 'Python Web Site', 'url': 'www.python.org', 'spam': 0}
for item in d.items():
    print(item)

# keys
d = {'title': 'Python Web Site', 'url': 'www.python.org', 'spam': 0}
print(type(d.keys()))

# pop
# 获取对应给定key的值，然后从字典中移除
d = {'x': 1, 'y': 2}
print(d.pop('x'))  # 1
print(d)  # {'y': 2}

# popitem
# 弹出随机的元素
print(d.popitem())
# print(d.popitem()) #空字典调用会抛异常

# setdefault
# 类似get，但是可以在不含给定key的时候设置相应的值
d = {}
print(d.setdefault('name', 'N/A'))  # 获取key对应的value，如果没有就设置成N/A并返回
print(d)

# update
# 利用一个字典项更新另外一个字典
d = {
    'title': 'python website',
    'url': 'http://www.python.org',
    'changed': 'Mar 14'
}
x = {
    'title':'Python Language Website'
}
d.update(x)
print(d)#会将x加入到d字典里，有相同的key则覆盖

# values
#以dict_values类对象的形式返回values
d = {
    'title': 'python website',
    'url': 'http://www.python.org',
    'changed': 'Mar 14'
}
print(type(d.values()))
print(d.values())
