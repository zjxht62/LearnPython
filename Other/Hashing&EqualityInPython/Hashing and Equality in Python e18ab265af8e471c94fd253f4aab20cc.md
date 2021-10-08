# Hashing and Equality in Python

[identity](Hashing%20and%20Equality%20in%20Python%20e18ab265af8e471c94fd253f4aab20cc/identity%20f8faac3c4b6943a2b57e747fc25c06c9.md)

## TL;DR（太长，不用读）

（TLDR 是指 "Too Long Didn't Read."，通常用于总结冗长的内容）

不要覆盖`__hash__`和`__eq__`方法来强制对象可哈希化。应该使用不可变对象。

## 概述

字典和集合都是非常常用的数据结构，因为它们执行查找操作的时间复杂度都是O(1)，O(1)的时间复杂度依赖于使用”哈希函数“，”哈希函数“具有以下属性：

- 如果：a==b 则：hash(a)== hash(b)
- 如果：hash(a) == hash(b) 则：a 可能等于b
- 如果：hash(a) ≠ hasn(b) 则：a≠b

无论使用何种语言，字典和集合都使用这些假设来实现快速 O(1) 查找。

## 字典概览

Python的字典相当先进和优化，但是要了解为什么上面“哈希函数”所具有的属性如此重要，我们得在高层次上了解他们的工作原理。

存储一个对象：

1. 对key调用`__hash__`方法计算key的hash，如果key不是可哈希的，抛出`TypeError`
2. 将 `(hash_value, key, value)` 存储在位置 `hash_value % len(array)` 的数组中。
3. 如果数组需要调整大小，重新使用先前计算的 hash_values 重新插入所有先前存储的值。

通过key检索对象

1. 对key调用`__hash__`方法计算key的hash，如果key不是可哈希的，抛出`TypeError`
2. 在 `hash(key) % len(array)` 中查找具有匹配 `hash_value` 的条目。如果存在：检查相等性，首先通过[identity](Hashing%20and%20Equality%20in%20Python%20e18ab265af8e471c94fd253f4aab20cc/identity%20f8faac3c4b6943a2b57e747fc25c06c9.md)，然后通过调用`__eq__`方法。

要获得功能上正确的词典，请遵循以下几点：

1. `__eq__`和`__hash__`必须一致：相等的对象必须有相等的哈希值。
2. `__hash__`绝不能改变。一旦插入，对象的哈希值就不会重新计算。
3. 实现了逻辑相等的对象（比如实现`__eq__`方法）必须是不可变的，来保证可哈希性。如果一个对象具有逻辑相等性，更新该对象会改变它的散列，那么就会违反规则2。`dict`、`list`、`set` 本质上都是可变的，因此是不可散列的。 `str`、`bytes`、`frozenset` 和 `tuple` 是不可变的，因此是可散列的

## 深入细节

首先看看如果我们不实现`__hash__`和`__eq__`的时候，对象是如何工作的。

默认情况下，相等性和哈希都依赖于对象的identity，

```python
x = object()
print(f'Hash of x: {hash(x)}')
print(f'id of x: {id(x)}')
print(f'id of x >> 4: {id(x) >> 4}')
print (f'Is x equal to itself? {x == x}')
```

```
Hash of x: 8729258887714
id of x: 139668142203424
id of x >> 4: 8729258887714
Is x equal to itself? True
```

字典和集合假设：如果一个对象与集合或字典中的一个对象具有相同的`identity`，那么两个对象是相等的（比如：我们假设一个对象总是等于它自己），这是一个重要的优化，因为有时调用`__eq__`方法可能会增加开销

```python
class NeverEqual:
    def __eq__(self, other):
        return False

    def __hash__(self):
        return id(self) >> 4  # 请注意，这是有问题的，但仅用于此示例的目的

never_equal = NeverEqual()
print(f'Is never_equal in a set of itself:{never_equal in set([never_equal])}')
# Is never_equal in a set of itself:True
```

虽然上面的代码中`NeverEqual`对象的`__eq__`方法始终返回`False`，但是set会首先用`id`来判断是否是同一个对象。所以返回为`True`。

`__hash__`只在对象被插入dict或set的时候被调用。请注意，即使我们通过插入10000个以上的项目来强制调整set的大小，而且我们检测到了一个逻辑上相同的对象，我们也再也看不到a或b的`__hash__`被调用

```python
class ReportHash:
    def __init__(self, value , name):
        self._value = value
        self._name = name
    def __hash__(self):
        hash_value = hash(self._value)
        print(f'Calling hash for {self._name}:{hash_value}')
        return hash_value
    def __eq__(self, other):
        return isinstance(other, ReportHash) and self._value == other._value
a = ReportHash(42, 'a')
b = ReportHash(37, 'b')
c = ReportHash(42, 'c')
s = {a, b}
for x in range(10000):
    s.add(x)
c in s
```

```
Calling hash for a: 42
Calling hash for b: 37
Calling hash for c: 42
True
```

这就是为什么对象的 `__hash__` 在其生命周期内永远不会改变是绝对重要的。这适用于对象标识（如果 id(a) == id(b) 我们知道 a == b）。

如果 `__hash__`更改，我们可能会遇到字典和集合不再有效并且极难发现错误的情况。

```python
class LiesAboutHash:
    def __init__(self, map_value):
        self.map_value = map_value

    def __hash__(self):
        return hash(tuple((k, v) for k, v in self.map_value.items()))

    def __eq__(self, other):
        return isinstance(other,
                          LiesAboutHash) and self.map_value == other.map_value

d = {'a': 1, 'b': 2, 'c': 3}
x = LiesAboutHash(d)
# 使用同一个对象创建一个list和一个set
l = [x]
s = set(l)
print(f'Object is in list: {x in l}')  # True
print(f'Object is in set: {x in s}')  # True
print(
    f'Logically equivalent object is in list: {LiesAboutHash(d) in l}')  # True
print(
    f'Logically equivalent object is in set: {LiesAboutHash(d) in s}')  # True

# 改变对象中的字典的值，导致hash和插入set时不一致
d['a'] = 42
print(f'Object is in list: {x in l}')  # True
print(f'Object is in set: {x in s}')  # False
print(
    f'Logically equivalent object is in list: {LiesAboutHash(d) in l}')  # True
print(
    f'Logically equivalent object is in set: {LiesAboutHash(d) in s}')  # False
```

上面代码中返回False的原因在于，要实现O(1)的时间复杂度查找字典和集合，需要保证哈希永远不会改变。我们这里是强行和语言做斗争，让hash可变，导致会出现奇奇怪怪的错误

## 那么如何解决呢

我们可以利用一些内置函数，比如`tuple`和`frozenset`，以及一些我们可以使用的第三方库`immutables`和`attrs`

### 内置函数

如果我们有一个`list`需要哈希，我们可以将它转换为`tuple`来保证它是不可变的。

```python
x = [1, 2, 3]
try:
    hash(x)
except TypeError as e:
    print(f'Exception when trying to hash a list! {e}')
print(f'hash(tuple(x)):{hash(tuple(x))}')

# Exception when trying to hash a list! unhashable type: 'list'
# hash(tuple(x)):-2022708474
```

如果我们有一个`set`需要哈希，我们可以将它转换为一个`frozenset`，来保证它是不可变的，同时仍旧保证O(1)的查找时间复杂度

```python
x = {1, 2, 3}
try:
    hash(x)
except TypeError as e:
    print(f'Exception when trying to hash a set! {e}')
print(f'hash(frozenset(x)): {hash(frozenset(x))}')

# Exception when trying to hash a set! unhashable type: 'set'
# hash(frozenset(x)): -2021384008

```

### 类和字典

我们将使用两个高质量的第三方库，`attrs` 和 `immutables`

attrs支持frozen对象，它可以被看做不可变的，所以它是可散列的。attrs还提供了好处，可以让我们不用写很多的模板代码。

```python
from typing import Tuple
import attr
@attr.s(frozen=True, auto_attribs=True)
class ImmutableThing:
    x: int
    y: str
    computed_field: Tuple[str] = attr.ib(attr.Factory(lambda self: tuple(self.y.split()), takes_self=True), init=False)

thing = ImmutableThing(42, 'hello world')
print(f'Created an ImmutableThing: {thing}')
try:
    thing.x = 99
except Exception as e:
    print(f'Caught an error trying to assign to ImmutableThing! {type(e)}')

print(f'hash(thing): {hash(thing)}')
print(f"ImmutableThing respects logical equality: {thing == ImmutableThing(42, 'hello world')}")
print(f"ImmutableThing as a dictionary key: {dict(thing='thing is a key')}")

# Created an ImmutableThing: ImmutableThing(x=42, y='hello world', computed_field=('hello', 'world'))
# Caught an error trying to assign to ImmutableThing! <class 'attr.exceptions.FrozenInstanceError'>
# hash(thing): -1550839745
# ImmutableThing respects logical equality: True
# ImmutableThing as a dictionary key: {'thing': 'thing is a key'}
```

对于 `dict`，我们将使用 `immutables.Map`。 `immutables.Map` 是一个不可变的 Map，因此是 Hashable。任何突变都会一起创建一个新映射，但保持底层映射不变。它的性能明显高于`deepcopy`。

```python
from immutables import Map
d = {'a': 1, 'b': 2, 'c': 3}
try:
    hash(d)
except TypeError as e:
    print(f'Exception when trying to hash a dict! {e}')

m = Map(d)
print(f'hash(m): {hash(m)}')
print(f"Map as a dictionary key: {dict(m='map is a key!')}")
try:
    m['a'] = 42
except TypeError as e:
    print(e)

# Assignment creates a _new_ map!
m_prime = m.set('a', 42)
print(f'm after assignment: {m}')
print(f'm_prime after assignment: {m_prime}')

# Exception when trying to hash a dict! unhashable type: 'dict'
# hash(m): 1444002257
# Map as a dictionary key: {'m': 'map is a key!'}
# 'immutables._map.Map' object does not support item assignment
# m after assignment: immutables.Map({'c': 3, 'b': 2, 'a': 1})
# m_prime after assignment: immutables.Map({'c': 3, 'b': 2, 'a': 42})
```

## 结论

不要试图反抗语言，不然可能出现奇怪的问题。我们可以借助工具使得对象可散列，同时保证正确性和性能。