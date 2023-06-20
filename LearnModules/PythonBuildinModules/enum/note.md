# Enum使用
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