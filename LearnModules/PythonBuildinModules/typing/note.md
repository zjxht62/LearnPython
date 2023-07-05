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

