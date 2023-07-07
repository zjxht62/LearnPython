# Python类型注解，你需要知道的都在这里了
参考链接：https://www.dusaiphoto.com/article/164/

通常我们在Python中定义的函数都像这样：

```python
def say(name):
    return f'Hello {name}!'
```

但是，有时候我们会看到这样的代码

```python
def say_hi(name: str) -> str:
    return f'Hi {name}'
```

函数定义似乎变得复杂些了：多出来这些 str 、 -> 都是什么意思？有什么作用？

本文将由浅入深，好好聊聊 Python 3.5 之后的**类型注解**。理解它将非常有益于优化你的代码。

## 变量注解
Python是动态语言，其显著的一个特点就是在声明变量的时候，不需要显式得指定其类型。
```python
age = 20
print('The age is: ', age + 1)
# Output:
# The age is:  21
```
虽然我们没有指定age的类型，但是程序在运行时隐式推断出其为`int`类型，因此可以顺利执行`age + 1`操作

除此之外，已经确定类型的变量，可以随时更改其类型，比如：

```python
age = 20
print(type(age))
# Output:# <class 'int'>

age = '20'
print(type(age))
# Output:# <class 'str'>
```
Python 这种动态特性的好处是它非常的自由，大部分时候你不用纠结类型声明、类型转化等麻烦事，可以用很少的代码完成各种骚操作。但是缺点也在这里：
如果你代码某些变量的类型有错，编辑器、IDE等工具无法在早期替你纠错，只能在程序运行阶段才能够暴露问题。

比如下面这个例子：
```python
age = 20
# 经过一段代码，age被重新赋值为str类型
age = '20'

print("The age is", age + 1)
# Output:TypeError: can only concatenate str (not "int") to str
```
尤其是在项目的代码逐渐膨胀的时候，上面这种问题可能会经常出现

因此，在Python3.5中引入了**类型注解**，其作用就是可以声明变量的类型，使得代码不再那么随意，
作为之前写过Java的人来说，这个特性能够让人更好的理解代码，而且使得IDE的提示更加准确

> 类型注解还在快速发展中，因此尽量用较新的 Python 版本去尝试它。

比如上面的代码，就可以用类型注解改写了：

```python
age: int = 20
```
虽然看起来多此一举，但是编辑器可以借此来发现你的不合理的操作。
![img.png](img.png)

很简单，但却带来了巨大的好处：
+ 编辑器可以替你揪出代码中关于类型的错误，避免了程序运行过程中各种奇奇怪怪的 Bug 。
+ 在你编写代码时，编辑器可以提示你对象的类型，免得你或者团队成员忘记了。（程序员通常记性不好）。

注意，Python的类型注解只是给编辑器提供了一个类型检查的机会，不会对实际代码运行过程有影响。也就是说Python和之前一样自由，
即使你用了指定类型之外的类型来赋值，只有不触发错误，程序都能运行下去。

最后，Python 中几种基本的变量类型都得到了支持：

```python
a: int = 1
b: float = 2.43
c: str = '哈哈'
d: bool = True
```
## 函数注解
简单的例子
```python
def say_hi(name:str) -> str:
    return f"Hello {name}!"
```
可以看出，这个函数接受一个字符串类型的参数`name`，并且返回值也是字符串

带默认值的函数像这样书写
```python
def add(first: int = 10, second: float = 5.5) -> float:
    return first + second
```
如果函数没有返回值，那么下面两种写法都可以
```python
def foo():
    pass


def bar() -> None:
    pass
```
参数类型也可以是自定义对象：
```python
class Person:
    def __init__(self, name: str):
        self.name = name


def hello(p: Person) -> str:
    return f"Hello {p.name}"
```
如果要避免循环导入或者注解早于对象定义的情况，可以用字符串代替类型：
```python
def hello(p: 'Person') -> str:
    return f'Hello, {p.name}'


class Person:
    def __init__(self, name: str):
        self.name = name
```
相比于变量类型注解，函数里的类型注解更加常用。
## 容器类型
列表、字典、元祖等包含元素的复合类型，用简单的list、dict、tuple不能说明元素内部的具体类型

因此要用到`typing`模块提供的复合注解功能
```python
from typing import List, Dict, Tuple

# 参数1：int的列表
# 参数2：key为字符串，value为int的字典
# 返回值：包含两个int类型的元祖
def mix(scored: List[int], ages: Dict[str, int]) -> Tuple[int, int]:
    return (0, 0)
```
如果你用的是 Python 3.9+ 版本，甚至连 `typing` 模块都不需要了，内置的容器类型就支持了复合注解：
```python
def mix(scores: list[int], ages: dict[str, int]) -> tuple[int, int]:
    return (0, 0)
```
某些情况下，不需要严格区分参数到底是列表还是元祖。这时就可以将它们的特征抽象为更加泛化的类型（泛型），比如Sequence（序列）
```python
# Python 3.8 之前的版本
from typing import Sequence as Seq1

def foo(seq: Seq1[str]):
    for item in seq:
        print(item)


# Python 3.9+ 也可以这么写
from collections.abc import Sequence as Seq2

def bar(seq: Seq2[str]):
    for item in seq:
        print(item)
```
例子中函数的参数不对容器的类型做具体要求，只要它是个序列（比如列表和元组）就可以。

## 类型别名
有时候类型可能会非常复杂，或者你希望给类型赋一个有意义的名称，那么可以像下面代码这样定义类型的别名
```python
from typing import Tuple

# 类型别名
# Vector2D = Tuple[int, int]
# 3.9以上可以不用import，直接用内建的
Vector2D = tuple[int, int]


def foo(vector: Vector2D):
    print(vector)


foo(vector=(1, 2))
```
`Vector2D `这个名称清晰的表达了这个对象是一个二维的向量。

与类型别名有点类似的，是用 `NewType` 创建自定义类型：
```python
from typing import NewType

Vector3D = NewType('Vector3D', tuple[int, int, int])


def bar(vector: Vector3D):
    print(vector)
```
乍一看感觉跟前面的类型别名差不多，但不同的是`NewType`创建了原始类型的”子类“
```python
# 类型检查成功
# 类型别名和原始类型是等价的
foo(vector=(1, 2))

# 类型检查失败
# NewType创建的是原始类型的“子类”
bar(vector=(1, 2, 3))

# 类型检查成功
# 传入参数必须是 Vector3D 的“实例”
v_3d = Vector3D((4, 5, 6))
bar(vector=v_3d)
```


