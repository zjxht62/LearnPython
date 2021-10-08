# x = object()
# print(f'Hash of x: {hash(x)}')
# print(f'id of x: {id(x)}')
# print(f'id of x >> 4: {id(x) >> 4}')
# print (f'Is x equal to itself? {x == x}')

# class NeverEqual:
#     def __eq__(self, other):
#         return False
#
#     def __hash__(self):
#         return id(self) >> 4  # 请注意，这是有问题的，但仅用于此示例的目的
#
#
# never_equal = NeverEqual()
# print(f'Is never_equal in a set of itself:{never_equal in set([never_equal])}')

# class ReportHash:
#     def __init__(self, value , name):
#         self._value = value
#         self._name = name
#     def __hash__(self):
#         hash_value = hash(self._value)
#         print(f'Calling hash for {self._name}:{hash_value}')
#         return hash_value
#     def __eq__(self, other):
#         return isinstance(other, ReportHash) and self._value == other._value
# a = ReportHash(42, 'a')
# b = ReportHash(37, 'b')
# c = ReportHash(42, 'c')
# s = {a, b}
# for x in range(10000):
#     s.add(x)
# c in s

class LiesAboutHash:
    def __init__(self, map_value):
        self.map_value = map_value

    def __hash__(self):
        return hash(tuple((k, v) for k, v in self.map_value.items()))

    def __eq__(self, other):
        return isinstance(other,
                          LiesAboutHash) and self.map_value == other.map_value


# d = {'a': 1, 'b': 2, 'c': 3}
# x = LiesAboutHash(d)
# # 使用同一个对象创建一个list和一个set
# l = [x]
# s = set(l)
# print(f'Object is in list: {x in l}')  # True
# print(f'Object is in set: {x in s}')  # True
# print(
#     f'Logically equivalent object is in list: {LiesAboutHash(d) in l}')  # True
# print(
#     f'Logically equivalent object is in set: {LiesAboutHash(d) in s}')  # True
#
# d['a'] = 42
# print(f'Object is in list: {x in l}')  # True
# print(f'Object is in set: {x in s}')  # False
# print(
#     f'Logically equivalent object is in list: {LiesAboutHash(d) in l}')  # True
# print(
#     f'Logically equivalent object is in set: {LiesAboutHash(d) in s}')  # False


# x = [1, 2, 3]
# try:
#     hash(x)
# except TypeError as e:
#     print(f'Exception when trying to hash a list! {e}')
# print(f'hash(tuple(x)):{hash(tuple(x))}')

# x = {1, 2, 3}
# try:
#     hash(x)
# except TypeError as e:
#     print(f'Exception when trying to hash a set! {e}')
# print(f'hash(frozenset(x)): {hash(frozenset(x))}')

# from typing import Tuple
# import attr
# @attr.s(frozen=True, auto_attribs=True)
# class ImmutableThing:
#     x: int
#     y: str
#     computed_field: Tuple[str] = attr.ib(attr.Factory(lambda self: tuple(self.y.split()), takes_self=True), init=False)
#
# thing = ImmutableThing(42, 'hello world')
# print(f'Created an ImmutableThing: {thing}')
# try:
#     thing.x = 99
# except Exception as e:
#     print(f'Caught an error trying to assign to ImmutableThing! {type(e)}')
#
# print(f'hash(thing): {hash(thing)}')
# print(f"ImmutableThing respects logical equality: {thing == ImmutableThing(42, 'hello world')}")
# print(f"ImmutableThing as a dictionary key: {dict(thing='thing is a key')}")

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