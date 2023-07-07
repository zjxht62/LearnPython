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


Vector2D = tuple[int, int]


def foo(vector: Vector2D):
    print(vector)


foo(vector=(1, 2))

from typing import NewType

Vector3D = NewType('Vector3D', tuple[int, int, int])


def bar(vector: Vector3D):
    print(vector)


bar(vector=(1, 2, 3))
bar(vector=Vector3D((4, 5, 6)))
