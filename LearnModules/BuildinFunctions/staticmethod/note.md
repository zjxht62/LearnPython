# @staticmethod
将方法转换为静态方法。  

静态方法不接收隐式第一个参数。要声明静态方法，请使用以下习惯用法：
```python
class C:
    @staticmethod
    def f(arg1, arg2, argN): ...
```
可以在类（例如 `C.f()`）或实例（例如 `C().f()`）上调用静态方法。此外，它们可以作为常规函数调用（例如 `f()`）。

Python 中的静态方法类似于 Java 或 C++ 中的静态方法。

就像所有的装饰器一样，staticmethod也可以作为常规的函数来进行调用并对其结果做一些事。
某些情况下，需要从类主体中引用函数并且希望避免自动转换为实例方法（这是必须的）。对于这些情况，请使用这个习惯用法：
```python
def regular_function():
    ...

class C:
    method = staticmethod(regular_function)
```