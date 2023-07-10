# age: int = 20
# # 经过一段代码，age被重新赋值为str类型
# age = '20'
#
# print("The age is", age + 1)
#
# a: int = 1
# b: float = 2.43
# c: str = '哈哈'
# d: bool = True

#
# Vector2D = tuple[int, int]
#
#
# def foo(vector: Vector2D):
#     print(vector)
#
#
# foo(vector=(1, 2))
#
# from typing import NewType
#
# Vector3D = NewType('Vector3D', tuple[int, int, int])
#
#
# def bar(vector: Vector3D):
#     print(vector)
#
#
# bar(vector=(1, 2, 3))
# bar(vector=Vector3D((4, 5, 6)))

# from typing import Union
# U = Union[str, int]
# def foo(a:U, b:U) -> list[U]:
#     return [a, b]

# 类型检查通过
# 因为Union[str, int]可以是其中任意一个类型
# 即使你不想让int和str混用
# foo(123, 'aaa')
# foo(19, 39)
# foo('aaa', 'bbb')

# from typing import TypeVar
#
# # 定义泛型T
# # T必须是str或int中的一种
# T = TypeVar('T', str, int)
#
#
# def bar(a: T, b: T) -> list[T]:
#     return [a, b]
#
#
# # 类型检查不通过
# # 函数的参数必须为同一个类型“T”
# bar(123, 'aaa')
# # 通过
# bar(19, 39)
# # 通过
# bar('aaa', 'bbb')

from typing import TypeVar

# 定义泛型 K 和 V
# K 和 V 的具体类型没有限制
K = TypeVar("K")
V = TypeVar("V")


def get_item(key: K, container: dict[K, V]) -> V:
    return container[key]


dict_1 = {"age": 10}
dict_2 = {99: "haha"}

# 类型检查通过，输出：10
print(get_item("age", dict_1))

# 类型检查通过：输出：haha
print(get_item(99, dict_2))

# 类型检查失败
# 因为“name”是字符串，而dict_2的键为int
print(get_item("name", dict_2))
