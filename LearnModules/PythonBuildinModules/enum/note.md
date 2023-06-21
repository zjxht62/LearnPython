# Enum使用
参考链接： https://docs.python.org/3/howto/enum.html  

Enum（枚举）是一组名称和唯一值的对应关系。他和全局变量类似，但是提供更多的实用可打印形式，分组，类型安全等特性。  

当创建一个由有限值组成的变量的时候，就比较适合使用枚举。比如，星期几：
```python
from enum import Enum
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
```
可见，自定义的枚举类是通过继承Enum类来实现的
> 因为枚举表示常量，所以一般都使用全大写的成员名称

根据枚举得性质，枚举成员的值有时重要有时也不重要，但是无论如何，这个值都可以来获取到对应的成员
```python
Weekday(3)
<Weekday.WEDNESDAY: 3>
```
可见，repr()方法显示了成员的枚举名称，枚举成员名称以及枚举成员的值。成员的str()方法只显示枚举名称和成员名称
```python
print(Weekday.THURSDAY)
Weekday.THURSDAY
```
枚举成员的type是枚举的类型
```python
type(Weekday.SUNDAY)
<enum 'Weekday'>

isinstance(Weekday.FRIDAY, Weekday)
True

```
枚举成员有一个只包含其名称的属性（name）
```python
print(Weekday.THURSDAY.name)
THURSDAY
```
同样也有一个包含枚举成员对应值的属性（value）
```python
print(Weekday.THURSDAY.value)
4
```
与许多将枚举视为名称/值对的语言不同，Python可以为枚举添加行为。比如，datetime.date有两种返回星期几的方法：weekday()和isoweekday()
这两个方法的区别在于一个返回的是0-6，而另一个返回的是1-7。我们可以通过给Weekday枚举添加一个方法，来从实例中提前日期并返回匹配的枚举成员。
```python
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    #
    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())
```
这就可以直接返回今天对应的枚举成员
```python
from datetime import date
Weekday.from_date(date.today())
<Weekday.TUESDAY: 2>
```

如果我们的变量只是需要星期几中的某一个，那么之前的枚举就够了，但是如果我们需要好几个呢？
也许我们正在编写一个函数来绘制一周内的琐事，而且并不想使用列表，那么我们就可以使用不同类型的枚举
```python
from enum import Flag
class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64
```
这回我们继承了`Flag`，而且所有的值都是2的幂
```python
# 可以单独选择周一
frist_week_day = Weekday.MONDAY
frist_week_day
<Weekday.MONDAY: 1>

# 还可以将多个枚举成员合并到一个变量中
weekend = Weekday.SATURDAY | Weekday.SUNDAY
weekend
<Weekday.SATURDAY|SUNDAY: 96>

# 甚至可以迭代含有多个枚举成员的变量
for day in weekend:
    print(day)
    
Weekday.SATURDAY
Weekday.SUNDAY
```
设置一些琐事
```python
chores_for_ethan = {
    'feed the cat': Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
    'do the dishes': Weekday.TUESDAY | Weekday.THURSDAY,
    'answer SO questions': Weekday.SATURDAY,
    }
```
以及显示给定日期的杂务的功能：
```python
def show_chores(chores, day):
    for chore, days in chores.items():
        if day in days:
            print(chore)
```
如果枚举成员的实际值无关紧要，那么可以使用auto()来省点儿事儿。
```python
from enum import auto
class Weekday(Flag):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()
    WEEKEND = SATURDAY | SUNDAY
```
## 编程获取枚举成员以及其属性
```python
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
枚举成员可以这样访问
```python
# 直接使用value在成员中匹配
Color(1)
<Color.RED: 1>
```
如果想直接通过名称获取成员，使用[key]:
```python
Color["RED"]
<Color.RED: 1>
```
获取成员的name或value
```python
member = Color.RED
member.name
'RED'
member.value
1
```
## 重复的枚举成员和枚举值
拥有两个相同枚举成员的枚举是不合法的
```python
class Shape(Enum):
    SQUARE = 2
    SQUARE = 3

Traceback (most recent call last):
...
TypeError: 'SQUARE' already defined as 2
```
然而，枚举成员可以有其他名称的成员与它的值关联，也就是name不同，但是value一样。给定两个具有相同值的条目A和B（并且A先定义），
B是成员A的别名。按值查找 A 的值将返回成员 A。按名称查找 A 将返回成员 A。B 的按名称查找也将返回成员 A：
```python
class Shape(Enum):
    SQUARE=2
    DIAMOND =1
    CIRCLE = 3
    ALIAS_FOR_SQUARE=2
    
Shape.SQUARE
<Shape.SQUARE: 2>
Shape.ALIAS_FOR_SQUARE
<Shape.SQUARE: 2>
Shape(2)
<Shape.SQUARE: 2>
```
## 确保唯一的枚举值
默认情况下，枚举允许多个名称作为同一值的别名。当不需要这种行为时，您可以使用 unique() 装饰器：
```python
from enum import Enum, unique
@unique
class Mistake(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 3

Traceback (most recent call last):
...
ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE
```
## 使用自动生成的值
如果枚举成员的value不重要，可以使用auto
```python
from enum import Enum, auto
class Color(Enum):
    RED=auto()
    GREEN=auto()
    BLUE=auto()
    
[member.value for member in Color]
[1, 2, 3]
```
这些值由 _generate_next_value_() 选择，可以被覆盖：
```python
class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

[member.value for member in Ordinal]
['NORTH', 'SOUTH', 'EAST', 'WEST']
```
> 注意 _generate_next_value_() 方法必须在任何成员之前定义。
## 比较
枚举成员按照身份进行比较
```python
Color.RED is Color.RED
True
Color.RED is Color.BLUE
False
Color.RED is not Color.BLUE
True
```
不支持枚举值之间的有序比较。枚举成员不是整数（但下面的 IntEnum之间可以比较）：
```python
Color.RED < Color.BLUE
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'Color' and 'Color'
```
虽然定义了相等比较：
```python
Color.BLUE == Color.RED
False
Color.BLUE != Color.RED
True
Color.BLUE == Color.BLUE
```
与非枚举值的比较总是不相等（同样，IntEnum 被明确设计为表现不同，见下文）：
```python
Color.BLUE == 2
False
```