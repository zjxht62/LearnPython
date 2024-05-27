# 命名元祖在Python的collections模块中定义，先import
from collections import namedtuple

# 使用namedtuple函数创建命名元祖类型，并为字段指定名称
Point = namedtuple('Point', ['x', 'y'])
# 这将创建一个名为 Point 的命名元组类型，其中包含 x 和 y 两个字段。然后可以使用这个类型来创建实际的命名元组实例，如下所示：
p = Point(1,2)
# 这将创建一个名为 p 的 Point 实例，其中 x 的值为 1，y 的值为 2。然后可以通过字段名来访问字段值：
print(p.x)
print(p.y)