# 第10章 开箱即用
## 10.1 模块
使用import可以导入外部模块
```python
import math
math.sin(0)
```
### 10.1.1 模块就是程序
任何Python程序都可以作为模块导入
```python
# hello.py
print('Hello, world!')
```
需要告诉解释器去哪里查找这个模块，可执行如下命令
```shell
>>> import sys
>>> sys.path.append('C:/python')
```
上面的命令告诉解释器，除了通常查找的位置之外，还应该到目录`C:\python`去查找这个模块，之后就
可以导入这个模块了
```shell
>>> import hello
Hello, world!
```
> 注意：当导入模块的时候，除了源代码的.py文件，还有一个名为__pycache__的子目录。这个里面包含的是
> 处理过的文件。Python能够更高效地处理他们，如果.py文件没有变化，那么导入模块的时候将导入处理后的文件，
> 否则将重新生成处理后的文件。

导入这个模块的时候会执行其中的代码。但是如果再次导入，什么事情都不会发生。
```shell
>>> import hello
```
因为模块并不是用来执行操作的，而是用来定义变量、函数、类等。鉴于定义只需要做一次，因此导入模块多次和导入一次的效果相同。
> 为何只导入一次
> 
> 如果两个模块彼此导入对方，就会出现无穷导入，如果第二次导入时什么都不会发生，这种循环将被打破。
> 
> 如果一定要重新加载模块，可使用模块importlib中的函数reload，它接受一个参数（要重新加载的模块），并返回重新加载的模块。如果在程序运行时修改了模块，并希望这种修改反映到程序中，这将很有用。

### 10.1.2 模块是用来下定义的
1. 在模块中定义函数  
```python
# 定义一个有函数的模块 
# hello2.py
def hello():
    print("Hello, world!")

# other.py
import hello2
hello2.hello()
```
通过模块，可以实现代码的重用，在多个程序中使用他们。

2. 在模块中添加测试代码  

由于模块在被导入的时候会被执行，所以需要进行特殊处理。
关键是检查模块是作为程序运行还是被导入到另一个程序。需要使用变量`__name__`
```shell
>>> __name__
'__main__'
>>> hello3.__name__
'hello3'
```
在主程序中（包括解释器的交互式提示符），变量__name__的值是'__main__'，而
在导入的模块中，这个变量被设置为该模块的名称。
```python
# 一个包含有条件地执行的测试代码的模块
# hello4.py
def hello():
    print('Hello, world!')

def test():
    hello()

if __name__ == '__main__':
    test()    
```
   
### 10.1.3 让模块可用
1. 将模块放在正确的位置  

将模块放在Python解释器寻找的路径下面，就可以导入模块。
```shell
# 查看Python的搜索路径
import sys, pprint
pprint.pprint(sys.path)
['/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev',
 '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display',
 '/Applications/PyCharm.app/Contents/plugins/python/helpers/third_party/thriftpy',
 '/Applications/PyCharm.app/Contents/plugins/python/helpers/pydev',
 '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python38.zip',
 '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8',
 '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/lib-dynload',
 '/Users/zjx/PycharmProjects/LearnPython/venv/lib/python3.8/site-packages',
 '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend',
 '/Users/zjx/PycharmProjects/LearnPython']
```
目录site-packages是存放模块的最佳的选择。
2. 告诉解释器到哪里去找  

有时，将模块放到查找路径并不是一个很好的解决方案。比如会有如下问题：
+ 不希望Python解释器的目录里充斥着自己编写的模块
+ 没有必要的权限，无法将文件放置到搜索路径下
+ 想将模块放在其他的地方

可以通过**环境变量**`PYTHONPATH`来告诉解释器去哪里查找，做法是将**模块所在的目录**包含在`PYTHONPATH`环境变量中

### 10.1.4 包
为了组织模块，可以将他们编组为包（package）。包是一个目录，要想让Python将目录视为包，那么目录必须包含文件`__init__.py`。  
如果像导入普通模块那样导入包，那么文件`__init__.py`的内容就是包的内容。

例如，有个名为`constants`的包，文件`constants/__init__.py`包含语句`PI=3.14`，那么就可以这样
```python
import constants
print(constants.PI)
```
包支持嵌套

## 10.2 探索模块
### 10.2.1 模块包含什么
1. 使用dir  

函数dir将列出对象的所有属性，对于模块，它列出所有的函数、类、变量等。
```python
import copy
#使用dir，列出对象的所有属性，通过列表推导式可以过滤掉非外部使用的
print([n for n in dir(copy) if not n.startswith("_")])
# ['Error', 'copy', 'deepcopy', 'dispatch_table', 'error']
```

2. 变量__all__

变量__all__是在copy模块里设置的
```python
# 摘自copy.py
__all__ = ["Error", "copy", "deepcopy"]
```   
```python
print(copy.__all__)
# ['Error', 'copy', 'deepcopy']
```
__all__旨在定义模块的公有接口。具体地说，它告诉解释器从这个模块导入所有 的名称意味着什么。
```python
from copy import *
# 上面的import语句只能得到__all__里面列出的3个函数
```
要导入PyStringMap，必须显式地:导入copy并使用 copy.PyStringMap;或者使用from copy import PyStringMap。  

如果不设置__all__，则会在以import *方式导入时， 导入所有不以下划线打头的全局名称。

### 10.2.2 使用help获取帮助
```shell
import copy
help(copy.copy)
Help on function copy in module copy:
copy(x)
    Shallow copy operation on arbitrary Python objects.
    
    See the module's __doc__ string for more info.
```
在帮助信息中，还提到了模块的__doc__字符串。__doc__字符串是什么呢?你可能还记得，第6章提到了文档字符串。 文档字符串就是在函数开头编写的字符串，用于对函数进行说明，而函数的属性__doc__可能包含这个字符串。
```shell
print(copy.copy.__doc__)
Shallow copy operation on arbitrary Python objects.
    See the module's __doc__ string for more info.
```
相比于直接查看文档字符串，使用help的优点是可获取更多的信息，如函数的特征标(即它接受的参数)。

### 10.2.3 文档
通过__doc__属性，可以快速查看函数的描述
```shell
print(range.__doc__)
range(stop) -> range object
range(start, stop[, step]) -> range object
Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
```

### 10.2.4 使用源码
有时需要查看源码来理解模块，通过模块的属性`__file__`可以查看到文件的路径
```shell
print(copy.__file__)
/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/copy.py
```

## 10.3 标准库：一些深受欢迎的模块
