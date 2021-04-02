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
## <u>When to Use Trailing Commas 何时用结尾逗号</u>
尾部的逗号通常是可选的，但是在创建一个元素的tuple的时候是必须的。为了清楚起见，建议在创建单个元素的tuple时用括号括起来：
```python
# Correct
FILES = ('setup.cfg',)

# @ Wrong
FILES = 'setup.cfg',
```
其实在结尾的逗号是多余的，但是如果一个list可能会随着时间而新增项目。就需要遵守如下规则：将每个值单独放在一行，同时加上结尾逗号
```python
# Correct:
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )

# Wrong:
FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)
```
## <u>Comments 注释</u>
和代码逻辑不符的注释还不如没有，修改了代码要及时更新注释。

注释要是一个完整的句子。第一个字母大写，除非是一个小写字母开头的标识符

块注释通常由一个或多个完整句子组成的段落组成，每个句子都以句号结尾。

在多句注释中，除了最后一句之后，您应该在句子结尾句后使用两个空格。

确保您的注释清晰明了，并且对于其他使用该语言的使用者来说也很容易理解。

来自非英语国家的Python编码人员：请用英语写您的评论，除非您有120％的把握确保不会说这种语言的人不会阅读该代码。

### <u>Block Comments 块注释</u>
块注释通常用来说明下面的一部分或所有的代码，并和说明的代码缩进到一个级别。块注释的每一行都以＃和一个空格开头（除非注释中的文本是缩进的）。

块注释中的段落由包含单个＃的行分隔。

### <u>Inline Comments 行内注释</u>
谨慎地使用行内注释

行内注释和代码在同一行，应该和代码具有至少两个空格的间距，同时以#加空格开始

行内注释是不必要的，并且如果代码自己能表名其作用，那就不要加。不要这样做：
```python
x = x + 1                 # Increment x

# 但是可能下面这种情况注释是有帮助的
x = x + 1                 # Compensate for border

```
### <u>Documentation Strings 文档字符串</u>
在PEP257中有着写文档字符串的规范

+ 为所有的公共的modules，functions，classes，methods写文档。但是非公共的方法可以不写，但是你应该写个注释，说明这个方法的作用，写在def那一行的下方

+ PEP 257描述了良好的文档字符串约定。请注意，最重要的是，结束多行文档字符串的“”应单独位于一行上：
```python
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
```
+ 对于只有一行的文档字符串，结尾的“””不用换行了：
```python
"""Return an ex-parrot."""
```

## <u>Naming Conventions 命名约定</u>
Python里面的命名有些混乱，所以我们不一定要求完全一致。但是我们推荐下面的命名标准。新的模块和包应该遵守，如果之前的，可能需要保证一致性而不遵守此规则。

### <u>Overriding Principle 覆盖原则</u>
那些在API中作为公共部分暴露给用户的名字应该反应其用途，而不是遵循此规则

### <u>Descriptive:Naming Styles 描述性：命名样式</u>
有多种多样的命名样式，每种都有不同的特点

+ b (单独小写字母)
+ B (单独大写字母)
+ lowercase
+ lower_case_with_underscores
+ UPPERCASE
+ UPPER_CASE_WITH_UNDERSCORES
+ CapitalizedWords (or CapWords, or CamelCase -- so named because of the bumpy look of its letters [4]). This is also sometimes known as StudlyCaps.
+ Note: 当使用CapWords的时候，如果开头的字母组合是大写，那么就全大写， 比如 HTTPServerError 好于 HttpServerError.
+ mixedCase (differs from CapitalizedWords by initial lowercase character!)
+ Capitalized_Words_With_Underscores (ugly!)

还有一种用短的缩写来组织名字的写法。在Python里用的不多，但是还是提一下。比如：os.stat()方法返回一个tuple，里面形如:st_mode，st_size，st_mtime

此外，还可以识别出以下使用前划线或下划线的特殊形式（通常可以将它们与任何大小写惯例结合使用）：
+ _single_leading_underscore: 表名弱的内部使用。 举例： from M import * 不会引入下划线开头的对象
+ single_trailing_underscore_: 此约定是为了避免和Python关键字发生冲突
```python
tkinter.Toplevel(master, class_='ClassName')
```
+ __double_leading_underscore: 当命名类的一个属性, 调用名称处理(inside class FooBar, __boo becomes _FooBar__boo; see below).用于标记那些不能被子类覆盖的方法
+ __double_leading_and_trailing_underscore__: 用户命名空间内的魔法属性和方法. E.g. __init__, __import__ or __file__. 不要发明类似的名称; 按照文档使用.
  
### <u>Descriptive:Naming Styles 说明性：命名约定</u>
#### <u>Names to Avoid 避免使用的名称</u>
不要用小写的l、大写的O、大写的I，这三个在一些字体里看着容易混

#### <u>ASCII Compatibility ASCII兼容性</u>
标准库中使用的标识符必须与PEP 3131的策略部分中所述的ASCII兼容。

#### <u>Package and Module Names 模块名和包名</u> 
模块名应该全小写，可以用下划线增加可读性。尽管在包名中不推荐使用下划线，但是也应该使用全小写的名称

当用C或C ++编写的扩展模块具有随附的Python模块提供更高级别的接口（例如，面向对象的接口）时，C / C ++模块具有一个下划线（例如_socket）。

#### <u>Class Names 类名</u> 
类名通常应使用CapWords约定。

如果这个接口主要被用作可调用的函数，那么可以使用函数的命名约定

请注意，内置名称有一个单独的约定：大多数内置名称是单个单词（或两个单词一起运行），而CapWords约定仅用于异常名称和内置常量。

#### <u>Type Variable Names 类型变量命名</u> 
在PEP 484中引入的类型变量的名称通常应使用CapWord，而不是使用短名称：T，AnyStr，Num。建议将后缀_co或_contra分别添加到用于声明协变或反变行为的变量中：
```python
from typing import TypeVar

VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)
```

#### <u>Exception Names 异常名</u> 
异常也是一个类，所以应采用类名的约定。同时以Exception或Error结尾来表示它是一个异常或错误

#### <u>Global Variable Names 全局变量名</u> 
（我们希望这些变量只能在一个模块内使用。）约定与函数的约定大致相同。

为了通过 from M import * 而使用的module，应该使用__all__机制来防止导出全局变量，或使用较早的约定在此类全局变量前加下划线（您可能需要这样做以表明这些全局变量是“非公共模块” ”）。

#### <u>Function and Variable Names 函数名和变量名</u> 
函数名应该使用小写，同时用下划线增加可读性。

变量名应该和函数名遵守一样的约定。

仅在已经是主流样式（例如threading.py）的上下文中才允许使用blendingCase，以保持向后兼容性。

#### <u>Function and Method Arguments 函数和方法的参数名</u> 
实例方法第一个参数应该是self。

类方法的第一个参数应该是cls。

如果函数的参数名称和保留关键字冲突了，最好在后面加一个下划线，比如class_（但是最好换一个名字来避免冲突)

#### <u>Method Names and Instance Variables 方法名和实例变量</u> 
使用函数命名规则：小写字母，必要时用下划线分隔单词，提高可读性。

仅仅对非公共方法和实例变量使用前下划线

为了避免名称与子类冲突，请使用两个前下划线来调用Python的名称处理规则。

Python用类名来修饰这些名称：如果Foo类具有名为__a的属性，则Foo .__ a不能访问它。 （坚持的用户仍然可以通过调用Foo._Foo__a来获得访问权限。）通常，应仅使用双引号下划线来避免名称与设计为子类的类中的属性发生冲突。

#### <u>Constants 常量</u>
常量一般用全大写字母定义，同时可以用下划线增加可读性。例如：MAX_OVERFLOW，TOTAL

#### <u>Designing for Inheritance 为了继承考虑</u>
一定要考虑类的方法和实例变量到底应该是公有的还是非公有的。如果不确定，选择非公有的，之后变成公有的比较简单。

公共的属性是你声明给用你的类的客户用的，你应该做好向后兼容。非公有的属性是指不打算给第三方使用的属性。你不保证非公有的属性不会修改，甚至删除。

我们不用private这个词，因为在Python里没有真正的private

还有一类属性是子类API的一部分（通常在其他语言里叫做protected)。有些类设计时就是为了被继承，来扩展或修改类的行为。当设计这种类的时候，谨慎决定哪些属性是公共属性，哪些是子类API的一部分，哪些只在基类中使用

根据上面的思想，下面是符合Python逻辑的指导：
+ Public的属性不应该以下划线开头

+ 如果你的公有的属性名和保留字冲突，那在结尾加一个下划线。这比缩写或拼写错误更好。（但是，尽管有此规则，但对于任何已知是类的变量或参数，尤其是类方法的第一个参数，“ cls”是首选的拼写。）

+ 对于简单的公共数据属性，最好只暴露出属性名，不要有复杂的getter/setter方法。请记住，如果您发现简单的数据属性需要增强行为（比如在获取值的时候进行部分处理），那么Python为这种情况提供了一个方法。在这种情况下，使用properties将功能实现隐藏在简单的数据属性访问语法之后。  
note1：Properties只用于新式类。  
note2：尽力避免功能行为的副作用。  
note3：避免用属性处理复杂的运算，调用属性表示法时，人们会觉得背后逻辑相对简单。

+ 如果你希望你的类被子类化，而且你有的属性不想让子类用，考虑以双下划线开头命名。这将触发Python的名字修改规则，会将类名加在属性名前（比如__method()变成_A__method())。这有助于避免属性名称冲突，如果子类无意中包含名称相同的属性。   
注1：注意改编名称仅用于简单类名，如果一个子类使用相同的类名和属性名，仍然会有名字冲突。  
注2：名称改编会带来一定的不便，如调试和__getattr__()。然而，名称改编算法有良好的文档，也容易手工执行。  
注3：不是每个人都喜欢名称改编。尝试平衡避免意外的名称冲突和高级调用者的可能。

#### <u>Public and Internal Interfaces 公有接口和内部接口</u>
只需要在公共的接口保证向后兼容性。因此，重要的是让用户能够清楚地区分公共接口和内部接口。

除非文档明确声明它们是临时接口或内部接口不受通常的向后兼容性保证，否则已说明文件的接口被视为公共接口。 所有未记录的接口都应假定为内部接口。

为了更好地支持检查，模块应该使用__all__属性来指出公有API的名称。设置__all__为空的话意味着意味着没有公有的API。

即使适当地设置了__all__，内部接口（包，模块，类，函数，属性或其他名称）仍应以单个下划线作为前缀。

一个接口被认为是内部接口，如果它包含任何命名空间（包，模块，或类）被认为是内部的。

导入名被认为是实现细节。其它模块必须不依赖间接访问这个导入名，除非他们是一个明确的记录包含模块的API的一部分，例如os.path或包的__init__模块，从子模块暴露功能。

## <u>Programming Recommendations 编程建议</u>
+ 应该以不损害Python其他实现（PyPy，Jython，IronPython，Cython，Psyco等）的方式编写代码。  
例如，对于形式为+ = b或a = a + b的语句，请不要依赖CPython有效地实现就地字符串连接。 即使在CPython中，这种优化也是脆弱的（仅适用于某些类型），并且在不使用引用计数的实现中根本不存在这种优化。 在库的性能敏感部分中，应改用''.join（）形式。 这将确保在各种实现方式中串联发生在线性时间内。
 
+  与单例（如None）的比较应该始终使用is or not，永远不要使用等于运算符。  
同时注意，如果你想写的是 if x is not None，那就别写 if x，在测试是否将默认为None的变量或参数设置为其他值时。另一个值可能具有在布尔上下文中可能为false的类型（例如空列表等）！参见例子：none_test.py