# @classmethod注解
@classmethod注解将一个方法转换成类方法。  

类方法接收类（cls）作为隐式第一个参数，就像实例方法接收实例（self）一样。要声明一个类方法，请使用这个习惯用法：

```python
class C:
    @classmethod
    def f(cls, arg1, arg2): ...
```
既可以在类上调用类方法（`C.f()`)，也可以在实例上调用类方法（`C().f()`），即使在实例上调用类方法，实例也会被忽略，只保留类对象。
如果为派生类调用类方法，那么cls传入的就是派生类对象。

Python中的类方法与Java或C++中的静态方法不同，Python中提供了`@staticmethod`来实现静态方法。
