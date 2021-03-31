# PEP8 -- Python代码样式指南
## <u>简介</u>

这篇文档为Python发行版中的标准库提供了代码编写约定。  

本文档和PEP 257（Docstring约定）是从Guido最初的Python样式指南文章中改编而来，并对Barry的样式指南进行了一些补充[2]。  

此约定可能随着时间的推移而增加新的约定，旧的约定也可能随着语言的进步而过时。

许多项目都有自己的编码规范，为了避免冲突，应该先遵从项目的编码规范

## <u>尽信书则不如无书</u>

Guido的一个核心观点是：代码被阅读的次数远远多于被编写的次数。这篇指南的目的就是提高代码的可读性，并使得各种Python代码保持一致的风格，
正如PEP 20所说，“可读性至关重要”。  

编程指南是关于一致性的。遵守编程指南是重要的。项目内的一致性更重要。一个模块或方法里面的一致性是最重要的。  

然而有时会出现和编码规范相左的时候，比如有时指南推荐的并不适用。当出现疑问的时候，请自己进行判断，参考其他代码和例子，实在不知道就问。

特别是，不要为了遵守PEP而破坏了向后兼容性（backwards compatibility），也就是兼容以前的  

一些情况下可以忽略PEP规范
1. 遵循PEP规范会导致代码可读性下降，甚至让那些熟悉阅读PEP代码的人都看不懂了。
2. 为了和周围其他代码保持一致，虽然这可能是个遵守PEP规范同时清理一些旧代码的机会
3. 有问题的代码在引入规则之前就已经编写完，没有理由修改它
4. 当代码需要和不支持规范建议功能的旧版本Python兼容的时候

## <u>Code Lay-out 代码布局</u>
### <u>Indentation 缩进</u>
每个缩进模块，缩进4个空格  

续行应该与其包裹元素对齐，要么使用圆括号、方括号和花括号内的隐式行连接来垂直对齐，要么使用挂行缩进对齐。当使用挂行缩进时，应该考虑到第一行不应该有参数，以及使用缩进以区分自己是续行。
```python
# 正确示例

# 与左括号对齐
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# 添加4个空格 (也就是增加一级缩进) 来将参数和其他参数区分
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# 挂行缩进应该另起一行
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```
如果if语句的条件部分太长，需要多行书写的话，可以在if后加一个空格，再加一个左括号来创建一个4个空格的缩进来书写条件。这会和同样使用5个空格缩进的代码产生视觉冲突。
PEP不明确指出如何编写，但是可接受的情况如下
```python
# 没有额外的缩进 
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# 添加注释，在能提供语法高亮的编辑器中可以有一些区分
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# 在条件判断的语句添加额外的缩进
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```
在多行中，闭合的}/]/)可以在列表最后一行的第一个非空白字符对齐
```python
my_list = [
    1, 2, 3,
    4, 5, 6
    ]
```
或者可以将其排列在开始多行构造的行的第一个字符下，如下所示：
```python
my_list = [
    1, 2, 3,
    4, 5, 6
]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```
### <u>Tabs or Spaces? 使用Tab还是空格</u>
空格是更好的缩进选择  

Tab只用来和已经用Tab来缩进的代码进行兼容

Python3不允许混用Tab和Space

Tabs和空格混合在一起的Python 2代码应转换为仅使用空格。

当使用-t选项指定Python2解释器的时候，会给出混用Tab和空格的警告。当用参数-tt的时候，警告将变为错误。建议采用这些参数来保证代码一致性。

### <u>Maximum Line Length 最大行长度</u>
限制所有行最多79个字符。

为了使较长的文本块具有较少的结构限制（文档字符串或注释），行长应限制为72个字符。

限制了行的长度，可以并排打开多个文件，查看起来效果更好。

大多数工具中的默认包装会破坏代码的视觉结构，使其更难以理解。 选择这些限制是为了避免在窗口宽度设置为80的编辑器中进行换行，即使在换行时该工具在最后一列中放置了标志符号也是如此。 某些基于Web的工具可能根本不提供动态换行。

一些团队强烈喜欢更长的线长。 对于专门或主要由可以就此问题达成协议的团队维护的代码，可以将行长度限制增加到最多99个字符，前提是注释和文档字符串仍以72个字符包装。

Python标准库是保守的，需要将行数限制为79个字符（文档字符串/注释数限制为72个）。

包装长行的首选方法是在括号，方括号和花括号内使用Python的隐含行连续性。 通过将表达式包装在括号中，可以将长行分成多行。 应优先使用这些，而不是使用反斜杠进行行连续。

有时反斜杠可能仍然合适。 例如，长的多个with语句不能使用隐式连续，因此反斜杠是可以接受的：
```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

### <u>Should a Line Break Before or After a Binary Operator? 是在二元操作符之前还是之后换行</u>
有很久一段儿时间，都是在操作符之后换行的。但是这种方式从两点上破坏了可读性：操作符往往分散在不同的列中，而且操作符和被操作的对象被分隔在了两行里
```python
# Wrong:
# operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```
为了解决可读性的问题，数学家和出版社采用了相反的约定，唐纳德·克努斯（Donald Knuth）在他的《计算机和排版》系列中解释了传统规则：“尽管段落中的公式总是在二元操作符和关系之后换行，但显示的公式总是在二元操作符之前换行” 。

遵循数学的传统通常会导致代码更具可读性：
```python
# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

### <u>Blank Lines 空行</u>
顶级函数和类定义用两个空行分隔

类里面的方法用一个空行分隔

相关的功能组可以用额外的空行（谨慎使用）隔开。一堆相关的单行代码之间的空白行可以省略（例如，一组虚拟实现 dummy implementations）。

在函数中使用空行来区分逻辑段（谨慎使用）。

Python接受control-L（即^L）换页符作为空格；许多工具把这些字符当作页面分隔符，所以你可以在文件中使用它们来分隔相关段落。请注意，一些编辑器和基于Web的代码阅读器可能无法识别control-L为换页，将在其位置显示另一个字形。

### <u>Source File Encoding 源文件编码格式</u>
Python3应使用UTF-8，Python2应使用ASCII

使用ASCII编码的Python2和UTF-8的Python3文件都不应具有编码声明

在标准库里，非默认的编码只应该是为了测试目的，或者当注释或文档中提到的作者包含非ASCII字符的时候。否则，使用\x,\u,\U或\N转义是在包含非ASCII数据时的首选。

对于Python 3.0及更高版本，标准库规定了以下策略（请参阅PEP 3131）：Python标准库中的所有标识符务必使用纯ASCII标识符，并且在可行的情况下应使用英文单词（在许多情况下，使用的缩写和技术术语不是英语）。此外，字符串文字和注释也必须使用ASCII。 唯一的例外是（a）测试非ASCII功能的测试用例，以及（b）作者的姓名。 名称不基于拉丁字母（latin-1，ISO / IEC 8859-1字符集）的作者必须在此字符集中提供其姓名的音译。

鼓励国际化的开源项目采取类似的约定

### <u>Imports 导入</u>
+ imports应该放在独立的行里面
```python
# Corret:
import os
import sys
```
```python
# Wrong:
import os, sys
```
但是从一个module引入多个可以这么写
```python
# Correct:
from subprocess import Popen, PIPE
```

+ imports应该放在文件顶部，在module的注释和文档下方，在模块全局变量和常量上面

imports应该按如下顺序排列
1. 标准库的imports
2. 相关第三方库的imports
3. 本地应用/库的imports
每个组用一个空行分隔

+ 推荐使用绝对路径的imports，可读性更高而且运行起来更好（也能提供更好的错误信息）
```python
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```
然而有时可以使用相对路径导入来替代，特别是处理复杂的模块布局时，绝对导入会太冗长了
```python
from . import sibling
from .sibling import example
```
标准库代码应避免复杂的程序包布局，并始终使用绝对导入。

绝对不要使用隐式相对导入，并且在Python 3中已将其删除。

+ 当从一个包含class的module引入class的时候，可以这么写
```python
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

如果拼写导致名称冲突，那么应该明确拼写
```python
import myclass
import foo.bar.yourclass

# usage:
myclass.Myclass
foo.bar.yourclass.YourClass

```
+ 通配符imports（from <module> import *）应该避免，因为它使得命名空间里名字混乱，混淆了读者和许多自动化工具。通配符导入有一个合理的用例，它是将内部接口重新发布为公共API的一部分

### <u>Module Level Dunder Names 模块级别的双下划綫命名</u>
模块级别的“dunders”（比如具有双下划线变量名，例如：__name__,__author__）应该在module的文档字段之后，但是在任何import声明之前（from __future__ 除外）。
Python要求来自__future__的imports必须在模块里的其他代码之前出现，但文档字段例外
```python
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL  #这里是__future__的引用

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

## <u>String Quotes String的引号</u>
在Python里，单引号和双引号作用相同。PEP并没有对此进行约定。提一个小要求，如果字符串包括单引号，那么就用双引号包裹它，反之同理。这样可以提高可读性，同时不用转义

对于三引号字符串，请始终使用双引号字符以与PEP 257中的docstring约定一致。

## <u>Whitespace in Expressions and Statements 语句和表达式里的空格</u>
### <u>Pet Peeves 讨厌的毛病</u>
以下情况请避免使用多余的空格
+ 紧靠在括号，方括号或大括号内，不要加空格：
```python
# Correst:
spam(ham[1], {eggs: 2})

# Wrong:
spam( ham[ 1 ], { eggs: 2 })
```
+ 在结尾逗号和右括号之间不要有空格：
```python
# Correct:
foo = (0,)

# Wrong:
foo = (0, )
```
+ 紧跟在逗号，分号和冒号之前不要有空格：
```python
# Correct:
if x == 4: print x, y; x, y = y, x

# Wrong:
if x == 4 : print x , y ; x , y = y , x
```
+ 但是，在切片操作里，冒号的作用类似于二元操作符，而且两侧都有相等数量的空格，把它看做一个优先级最低的运算符处理。
在扩展的切片操作里，两个冒号必须应用相同的间距。
例外：省略slice参数时，将省略空格：
```python
# Correct:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

# Wrong:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```
+ 函数名和参数列表之间不要有空格
```python
# Correct:
spam(1)

# Wrong:
spam (1)
```
+ 在开始进行索引或切片操作之前不要有空格
```python
# Correct
dct['key'] = lst[index]

# Wrong:
dct ['key'] = lst [index]
```
+ 赋值（或其他）运算符周围有多个空格，以使其与另一个对齐：
```python
# Correct:
x = 1
y = 2
long_variable = 3

# Wrong:
x             = 1 
y             = 2 
long_variable = 3
```

### <u>Other Recommendations 其他的建议</u>
+ 在任何地方避免结尾的空格，因为它通常是不可见的，而且可能造成混淆，比如：反斜杠后跟一个空格和一个换行符不算作行继续标记。
+ 始终将这些二进制运算符的两边都用一个空格括起来：赋值（=），扩展赋值（+=，-=等），比较（==，<，>，=，<>，<=，> = ，in，not in，is，is not），布尔值（and，or，not）。
+ 如果使用优先级不同的运算符，请考虑在优先级最低的运算符周围添加空格。 使用您自己的判断； 但是，永远不要使用一个以上的空格，并且在二进制运算符的两边总是具有相同数量的空格：
```python
# Correct:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# Wrong:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```
+ 函数注释硬功使用冒号的常规规则，如果存在 -> 那么应该在两侧加上空格
```python
# Correct:
def munge(input: AnyStr): ...
def munge() -> PosInt: ...

# Wrong:
def munge(input:AnyStr): ...
def munge()->PosInt: ...
```
+ 在方法的参数列表中使用关键字传值的时候，以及定义方法默认参数的时候都不应该有空格
```python
# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Wrong:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```
+ 但是，当将参数注释与默认值组合时，请在=符号周围使用空格：
```python
# Correct:
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

# Wrong:
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
```
+ 通常不建议使用复合语句（同一行上的多个语句）：
```python
# Correct:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

# Wrong:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()
```
+ 虽然有时可以将if / for / while的小主体放在同一行上是可以的，但对于多子句的语句则永远不要这样做。也要避免折叠这么长的线！
```python
# Wrong:
if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()

# Wrong:
if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)

if foo == 'blah': one(); two(); three()
```