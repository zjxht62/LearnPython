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

上面的命令告诉解释器，除了通常查找的位置之外，还应该到目录`C:\python`去查找这个模块，之后就 可以导入这个模块了

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

由于模块在被导入的时候会被执行，所以需要进行特殊处理。 关键是检查模块是作为程序运行还是被导入到另一个程序。需要使用变量`__name__`

```shell
>>> __name__
'__main__'
>>> hello3.__name__
'hello3'
```

在主程序中（包括解释器的交互式提示符），变量__name__的值是'__main__'，而 在导入的模块中，这个变量被设置为该模块的名称。

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

# 使用dir，列出对象的所有属性，通过列表推导式可以过滤掉非外部使用的
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


在帮助信息中，还提到了模块的__doc__字符串。__doc__字符串是什么呢?你可能还记得，第6章提到了文档字符串。
文档字符串就是在函数开头编写的字符串，用于对函数进行说明，而函数的属性__doc__可能包含这个字符串。


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

在安装Python之后，就会获得很多有用的模块。

### 10.3.1 sys

模块sys能访问与Python解释器相关的变量和函数。

|函数/变量|描述|
|---|---|
|argv| 命令行参数，包括脚本名|
|exit([arg])|退出当前程序，可通过可选参数指定返回值或错误信息|
|modules|一个字典，将模块名映射到加载的模块|
|path|一个列表，包含要在其中查找模块的目录的名称|
|platform|一个平台标识符，如sunos5或win32|
|stdin|标准输入流----一个类似于文件的对象|
|stdout|标准输出流----一个类似于文件的对象|
|stderr|标准错误流----一个类似于文件的对象|

变量sys.argv包含传递给Python解释器的参数，其中包括脚本名

函数sys.exit退出当前程序。可以向他提供一个整数，指出程序是否成功，这是一种UNIX约定。在大多数情况下，使用该参数的默认值（0，表示成功）即可。也可向它提供一个字符串，这个字符串将成为错误消息，对用户找出程序终止的原因很有帮助。在这种情况下，程序退出时将显示指定的错误消息以及一个表示失败的编码。

```python
# 如果默认或是None，那默认exit code是0
sys.exit()  # Process finished with exit code 0

# 如果是integer，将此integer作为exit code
sys.exit(5)

# 如果是其他对象，会将他先print出来，exit code将是1
sys.exit('娃哈哈')
```

映射sys.modules将模块名映射到模块（仅限于当前已导入的模块）。

```python
print(sys.modules)
# {'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, '_imp': <module '_imp' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'nt': <module 'nt' (built-in)>, '_thread': <module '_thread' (built-in)>, '_weakref': <module '_weakref' (built-in)>, 'winreg': <module 'winreg' (built-in)>, 'time': <module 'time' (built-in)>, 'zipimport': <module 'zipimport' (frozen)>, '_codecs': <module '_codecs' (built-in)>, 'codecs': <module 'codecs' from 'E:\\Programs\\Python\\Python38-32\\lib\\codecs.py'>, 'encodings.aliases': <module 'encodings.aliases' from 'E:\\Programs\\Python\\Python38-32\\lib\\encodings\\aliases.py'>, 'encodings': <module 'encodings' from 'E:\\Programs\\Python\\Python38-32\\lib\\encodings\\__init__.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from 'E:\\Programs\\Python\\Python38-32\\lib\\encodings\\utf_8.py'>, '_signal': <module '_signal' (built-in)>, '__main__': <module '__main__' from 'E:/zjx/PycharmProjects/LearnPython/BeginningPython/chapter10/chapter10.py'>, 'encodings.latin_1': <module 'encodings.latin_1' from 'E:\\Programs\\Python\\Python38-32\\lib\\encodings\\latin_1.py'>, '_abc': <module '_abc' (built-in)>, 'abc': <module 'abc' from 'E:\\Programs\\Python\\Python38-32\\lib\\abc.py'>, 'io': <module 'io' from 'E:\\Programs\\Python\\Python38-32\\lib\\io.py'>, '_stat': <module '_stat' (built-in)>, 'stat': <module 'stat' from 'E:\\Programs\\Python\\Python38-32\\lib\\stat.py'>, 'genericpath': <module 'genericpath' from 'E:\\Programs\\Python\\Python38-32\\lib\\genericpath.py'>, 'ntpath': <module 'ntpath' from 'E:\\Programs\\Python\\Python38-32\\lib\\ntpath.py'>, 'os.path': <module 'ntpath' from 'E:\\Programs\\Python\\Python38-32\\lib\\ntpath.py'>, '_collections_abc': <module '_collections_abc' from 'E:\\Programs\\Python\\Python38-32\\lib\\_collections_abc.py'>, 'os': <module 'os' from 'E:\\Programs\\Python\\Python38-32\\lib\\os.py'>, '_sitebuiltins': <module '_sitebuiltins' from 'E:\\Programs\\Python\\Python38-32\\lib\\_sitebuiltins.py'>, '_locale': <module '_locale' (built-in)>, '_bootlocale': <module '_bootlocale' from 'E:\\Programs\\Python\\Python38-32\\lib\\_bootlocale.py'>, '_codecs_cn': <module '_codecs_cn' (built-in)>, '_multibytecodec': <module '_multibytecodec' (built-in)>, 'encodings.gbk': <module 'encodings.gbk' from 'E:\\Programs\\Python\\Python38-32\\lib\\encodings\\gbk.py'>, 'types': <module 'types' from 'E:\\Programs\\Python\\Python38-32\\lib\\types.py'>, 'importlib._bootstrap': <module 'importlib._bootstrap' (frozen)>, 'importlib._bootstrap_external': <module 'importlib._bootstrap_external' (frozen)>, 'warnings': <module 'warnings' from 'E:\\Programs\\Python\\Python38-32\\lib\\warnings.py'>, 'importlib': <module 'importlib' from 'E:\\Programs\\Python\\Python38-32\\lib\\importlib\\__init__.py'>, 'importlib.machinery': <module 'importlib.machinery' from 'E:\\Programs\\Python\\Python38-32\\lib\\importlib\\machinery.py'>, 'importlib.abc': <module 'importlib.abc' from 'E:\\Programs\\Python\\Python38-32\\lib\\importlib\\abc.py'>, '_operator': <module '_operator' (built-in)>, 'operator': <module 'operator' from 'E:\\Programs\\Python\\Python38-32\\lib\\operator.py'>, 'keyword': <module 'keyword' from 'E:\\Programs\\Python\\Python38-32\\lib\\keyword.py'>, '_heapq': <module '_heapq' (built-in)>, 'heapq': <module 'heapq' from 'E:\\Programs\\Python\\Python38-32\\lib\\heapq.py'>, 'itertools': <module 'itertools' (built-in)>, 'reprlib': <module 'reprlib' from 'E:\\Programs\\Python\\Python38-32\\lib\\reprlib.py'>, '_collections': <module '_collections' (built-in)>, 'collections': <module 'collections' from 'E:\\Programs\\Python\\Python38-32\\lib\\collections\\__init__.py'>, '_functools': <module '_functools' (built-in)>, 'functools': <module 'functools' from 'E:\\Programs\\Python\\Python38-32\\lib\\functools.py'>, 'contextlib': <module 'contextlib' from 'E:\\Programs\\Python\\Python38-32\\lib\\contextlib.py'>, 'importlib.util': <module 'importlib.util' from 'E:\\Programs\\Python\\Python38-32\\lib\\importlib\\util.py'>, 'zope': <module 'zope' (namespace)>, 'enum': <module 'enum' from 'E:\\Programs\\Python\\Python38-32\\lib\\enum.py'>, '_sre': <module '_sre' (built-in)>, 'sre_constants': <module 'sre_constants' from 'E:\\Programs\\Python\\Python38-32\\lib\\sre_constants.py'>, 'sre_parse': <module 'sre_parse' from 'E:\\Programs\\Python\\Python38-32\\lib\\sre_parse.py'>, 'sre_compile': <module 'sre_compile' from 'E:\\Programs\\Python\\Python38-32\\lib\\sre_compile.py'>, 'copyreg': <module 'copyreg' from 'E:\\Programs\\Python\\Python38-32\\lib\\copyreg.py'>, 're': <module 're' from 'E:\\Programs\\Python\\Python38-32\\lib\\re.py'>, 'token': <module 'token' from 'E:\\Programs\\Python\\Python38-32\\lib\\token.py'>, 'tokenize': <module 'tokenize' from 'E:\\Programs\\Python\\Python38-32\\lib\\tokenize.py'>, 'linecache': <module 'linecache' from 'E:\\Programs\\Python\\Python38-32\\lib\\linecache.py'>, 'traceback': <module 'traceback' from 'E:\\Programs\\Python\\Python38-32\\lib\\traceback.py'>, 'sitecustomize': <module 'sitecustomize' from 'E:\\Program Files\\JetBrains\\PyCharm 2021.1.2\\plugins\\python\\helpers\\pycharm_matplotlib_backend\\sitecustomize.py'>, 'site': <module 'site' from 'E:\\Programs\\Python\\Python38-32\\lib\\site.py'>, 'hello': <module 'hello' from 'E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10\\hello.py'>, 'hello2': <module 'hello2' from 'E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10\\hello2.py'>, 'hello3': <module 'hello3' from 'E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10\\hello3.py'>, 'pprint': <module 'pprint' from 'E:\\Programs\\Python\\Python38-32\\lib\\pprint.py'>, 'constants': <module 'constants' from 'E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10\\constants\\__init__.py'>, 'constants.haha': <module 'constants.haha' from 'E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10\\constants\\haha.py'>, 'constants.heihei': <module 'constants.heihei' from 'E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10\\constants\\heihei.py'>, '_weakrefset': <module '_weakrefset' from 'E:\\Programs\\Python\\Python38-32\\lib\\_weakrefset.py'>, 'weakref': <module 'weakref' from 'E:\\Programs\\Python\\Python38-32\\lib\\weakref.py'>, 'copy': <module 'copy' from 'E:\\Programs\\Python\\Python38-32\\lib\\copy.py'>, '_opcode': <module '_opcode' (built-in)>, 'opcode': <module 'opcode' from 'E:\\Programs\\Python\\Python38-32\\lib\\opcode.py'>, 'dis': <module 'dis' from 'E:\\Programs\\Python\\Python38-32\\lib\\dis.py'>, 'collections.abc': <module 'collections.abc' from 'E:\\Programs\\Python\\Python38-32\\lib\\collections\\abc.py'>, 'inspect': <module 'inspect' from 'E:\\Programs\\Python\\Python38-32\\lib\\inspect.py'>, 'pkgutil': <module 'pkgutil' from 'E:\\Programs\\Python\\Python38-32\\lib\\pkgutil.py'>, 'platform': <module 'platform' from 'E:\\Programs\\Python\\Python38-32\\lib\\platform.py'>, 'urllib': <module 'urllib' from 'E:\\Programs\\Python\\Python38-32\\lib\\urllib\\__init__.py'>, 'urllib.parse': <module 'urllib.parse' from 'E:\\Programs\\Python\\Python38-32\\lib\\urllib\\parse.py'>, 'pydoc': <module 'pydoc' from 'E:\\Programs\\Python\\Python38-32\\lib\\pydoc.py'>}

```

变量sys.path在本章前面讨论过，它是一个字符串列表，其中的每个字符串都是一个目录名， 执行import语句时将在这些目录中查找模块

```python
import pprint

pprint.pprint(sys.path)

['E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10',
 'E:\\zjx\\PycharmProjects\\LearnPython',
 'E:\\Program Files\\JetBrains\\PyCharm '
 '2021.1.2\\plugins\\python\\helpers\\pycharm_display',
 'E:\\Programs\\Python\\Python38-32\\python38.zip',
 'E:\\Programs\\Python\\Python38-32\\DLLs',
 'E:\\Programs\\Python\\Python38-32\\lib',
 'E:\\Programs\\Python\\Python38-32',
 'E:\\Programs\\Python\\Python38-32\\lib\\site-packages',
 'E:\\Program Files\\JetBrains\\PyCharm '
 '2021.1.2\\plugins\\python\\helpers\\pycharm_matplotlib_backend',
 'C:/python']
```

变量sys.platform（一个字符串）是运行解释器的平台名称。可能表示的是操作系统的名称，也可能是表示其他平台类型（如Java虚拟机）的名称（如java1.4.0）----如果你运行的是Jython

```python
print(sys.platform)  # win32
```


变量sys.stdin、 sys.stdout和sys.stderr是类似于文件的流对象，表示标准的UNIX概念： 标准输入、标准输出和标准错误。简单地说， Python从sys.stdin获取输入（例如，用于input中），
并将输出打印到sys.stdout。

demo:按相反顺序打印命令行参数

```python
import sys

print(' '.join(reversed(sys.argv[1:])))
```

```shell
$ python reverseargs.py one two three
three two one
```

### 10.3.2 os
模块os让你能够访问多个操作系统服务。除此之外，os和它的子模块os.path还包含多个查看、创建和删除目录及文件的函数，以及一些操作路径的函数（例如，
os.path.split和os.path.join让你在大多数情况下都可 忽略os.pathsep）

|函数/变量|描述|
|---|---|
|environ|包含环境变量的映射|
|system(command)|在子shell中执行操作系统命令|
|sep|路径中使用的分隔符|
|pathsep|分隔不同路径的分隔符|
|linesep|行分隔符（'\n'、'\r'或'\r\n'）|
|urandom(n)|返回n个字节的强加密随机数据|

映射os.environ包含环境变量，这个映射也可用于修改环境变量，但并非所有的平台都支持这样做。

```python
print(os.environ)
# environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'ANDROID_HOME': 'E:\\android-sdk-windows', 'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming', 'CATALINA_BASE': 'E:\\apache-tomcat-9.0.2', 'CATALINA_HOME': 'E:\\apache-tomcat-9.0.2', 'CHOCOLATEYINSTALL': 'C:\\ProgramData\\chocolatey', 'CHOCOLATEYLASTPATHUPDATE': '132560301740133164', 'CIRRUS_UNINSTALL_EXE': 'E:\\Program Files\\DLP\\dlp3.0\\unins000.exe', 'CLASSPATH': '.;C:\\Program Files\\Java\\jdk1.8.0_241\\lib\\dt.jar;C:\\Program Files\\Java\\jdk1.8.0_241\\lib\\tools.jar;', 'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-RMO2H0L', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'ERLANG_HOME': 'E:\\Program Files\\erl10.3', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Administrator', 'IDEA_INITIAL_DIRECTORY': 'E:\\Program Files\\JetBrains\\PyCharm 2021.1.2\\bin', 'INTELLIJ IDEA': 'E:\\Program Files\\JetBrains\\IntelliJ IDEA 2020.2.4\\bin;', 'ITEST_HOME': 'E:\\itestInstalDir\\itest', 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk1.8.0_241', 'JMETER_HOME': 'E:\\zjx\\Jmeter\\Jmeter', 'LANG': 'zh_CN', 'LOCALAPPDATA': 'C:\\Users\\Administrator\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-RMO2H0L', 'MAVEN_HOME': 'E:\\apache-maven-3.0.5', 'MOZ_PLUGIN_PATH': 'E:\\PROGRAM FILES (X86)\\FOXIT SOFTWARE\\FOXIT READER\\plugins\\', 'NUMBER_OF_PROCESSORS': '4', 'NVM_HOME': 'C:\\Users\\Administrator\\AppData\\Roaming\\nvm', 'NVM_SYMLINK': 'E:\\Program Files\\nodejs', 'ONEDRIVE': 'C:\\Users\\Administrator\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;E:\\Program Files\\Git\\bin;E:\\Program Files\\TortoiseGit\\bin;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;E:\\apache-maven-3.0.5\\bin\\;E:\\android-sdk-windows\\platform-tools;E:\\android-sdk-windows\\tools;E:\\MinGW\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\npm;E:\\Program Files\\erl10.3\\bin;E:\\aliyun;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Java\\jdk1.8.0_241\\bin;C:\\Program Files\\Java\\jdk1.8.0_241\\jre\\bin;C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin;E:\\zjx\\Jmeter\\Jmeter\\bin;C:\\ProgramData\\chocolatey\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\nvm;E:\\Program Files\\nodejs;E:\\allure-2.13.8\\bin;C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\;C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\;E:\\Programs\\Python\\Python38-32\\Scripts\\;E:\\Programs\\Python\\Python38-32\\;C:\\Program Files\\MySQL\\MySQL Shell 8.0\\bin\\;C:\\Users\\Administrator\\AppData\\Local\\Microsoft\\WindowsApps;E:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Users\\Administrator\\AppData\\Local\\Programs\\Fiddler;E:\\Program Files (x86)\\Atmel\\Flip 3.4.7\\bin;C:\\Users\\Administrator\\AppData\\Local\\Microsoft\\WindowsApps;E:\\Program Files\\JetBrains\\IntelliJ IDEA 2020.2.4\\bin;;C:\\Users\\Administrator\\AppData\\Roaming\\nvm;E:\\Program Files\\nodejs;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW', 'PROCESSOR_ARCHITECTURE': 'x86', 'PROCESSOR_ARCHITEW6432': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 142 Stepping 9, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '8e09', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files (x86)', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\;C:\\Program Files\\Intel\\;C:\\Program Files\\Intel\\Wired Networking\\', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'E:\\zjx\\PycharmProjects\\LearnPython;E:\\Program Files\\JetBrains\\PyCharm 2021.1.2\\plugins\\python\\helpers\\pycharm_matplotlib_backend;E:\\Program Files\\JetBrains\\PyCharm 2021.1.2\\plugins\\python\\helpers\\pycharm_display', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'ULTRAMON_LANGDIR': 'C:\\Program Files\\UltraMon\\Resources\\cn', 'USERDOMAIN': 'DESKTOP-RMO2H0L', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-RMO2H0L', 'USERNAME': 'Administrator', 'USERPROFILE': 'C:\\Users\\Administrator', 'VS140COMNTOOLS': 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\Common7\\Tools\\', 'WINDIR': 'C:\\WINDOWS'})

# 获取名为JAVA_HOME的环境变量
print(os.environ['JAVA_HOME'])
# C:\Program Files\Java\jdk1.8.0_241
```

函数os.system用于运行外部程序。还有其他用于执行外部程序的函数，如execv和popen。前
者退出Python解释器，并将控制权交给被执行的程序，而后者创建一个到程序的连接（这个连接 类似于文件）。
> 提示 请参阅模块subprocess，它融合了模块os.system以及函数execv和popen的功能

变量os.sep是用于路径名中的分隔符。 在UNIX（以及macOS的命令行Python版本）中，标准
分隔符为/。在Windows中，标准分隔符为\\（这种Python语法表示单个反斜杠）。 （在有些平台中，
os.altsep包含替代路径分隔符，如Windows中的/。）

```python
print(repr(os.sep))  # '\\'
```


可使用os.pathsep来组合多条路径， 就像PYTHONPATH中那样。 pathsep用于分隔不同的路径名： 在UNIX/macOS中为:
，而在Windows中为;。

变量os.linesep是用于文本文件中的行分隔符：在UNIX/OS X中为单个换行符（\n），在 Windows中为回车和换行符（\r\n）。

函数urandom使用随系统而异的“真正”（至少是强加密）随机源。如果平台没有提供这样的 随机源，将引发NotImplementedError异常。

### 10.3.3 fileinput

模块fileinput让你能够轻松地迭代一系列文本文件中的所有行。如果这样调用脚本

```shell
python some_script.py file1.txt file2.txt file3.txt
```

就能够依次迭代文件file1.txt到file3.txt中的行。
你还可在UNIX管道中对使用UNIX标准命令cat提供给标准输入（sys.stdin）的行进行迭代。

```shell
$ cat file.txt | python some_script.py
```

如果使用模块fileinput，在UNIX管道中使用cat调用脚本的效果将与以命令行参数的方式向脚本提供文件名一样。

|函数/变量|描述|
|---|---|
|input([files[, inplace[, backup]]])|帮助迭代多个输入流中的行|
|filename()|返回当前文件的名称|
|lineno()| 返回（累计的）当前行号|
|filelineno()| 返回在当前文件中的行号|
|isfirstline()| 检查当前行是否是文件中的第一行|
|isstdin()| 检查最后一行是否来自sys.stdin|
|nextfile()| 关闭当前文件并移到下一个文件|
|close()| 关闭序列|


fileinput.input是其中最重要的函数，它返回一个可在for循环中进行迭代的对象。如果要
覆盖默认行为（确定要迭代哪些文件），可以序列的方式向这个函数提供一个或多个文件名。还
可将参数inplace设置为True（inplace=True），这样将就地进行处理。对于你访问的每一行，都
需打印出替代内容，这些内容将被写回到当前输入文件中。就地进行处理时，可选参数backup用 于给从原始文件创建的备份文件指定扩展名。

函数fileinput.filename返回当前文件（即当前处理的行所属文件）的文件名。

函数fileinput.lineno返回当前行的编号。这个值是累计的，因此处理完一个文件并接着处 理下一个文件时，不会重置行号，而是从前一个文件最后一行的行号加1开始。

函数fileinput.filelineno返回当前行在当前文件中的行号。每次处理完一个文件并接着处 理下一个文件时，将重置这个行号并从1重新开始。

函数fileinput.isfirstline在当前行为当前文件中的第一行时返回True，否则返回False。

函数fileinput.isstdin在当前文件为sys.stdin时返回True，否则返回False。

函数fileinput.nextfile关闭当前文件并跳到下一个文件，且计数时忽略跳过的行。这在你 知道无需继续处理当前文件时很有用。

函数fileinput.close关闭整个文件链并结束迭代。

demo:给Python脚本添加行号

```python
# 给python脚本结尾增加行号                            
import fileinput

for line in fileinput.input(inplace=True):
    line = line.rstrip()
    num = fileinput.lineno()
    print('{:<50} # {:2d}'.format(line, num))
```

### 10.3.4 集合、堆和双端队列

1. 集合  
   集合是由内置类set实现的，所以无需导入模块sets

```shell
set(range(10))
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

可使用序列（或其他可迭代对象）来创建集合，也可以用花括号显式地指定。但是不能用花括号来创建空集合，因为那样会创建一个空字典。

```shell
type({})
<class 'dict'>
```

集合主要用于成员资格检查，因此将忽略 重复的元素:

```shell
 >>> {0, 1, 2, 3, 0, 1, 2, 3, 4, 5}
{0, 1, 2, 3, 4, 5}
```

与字典一样，集合中元素的排列顺序是不确定的，因此不能依赖于这一点。

```shell
>>> {'fee', 'fie', 'foe'} 
{'foe', 'fee', 'fie'}
```

除此之外，还可以执行各种标准集合操作（比如交集和并集）计算并集可以对一个集合调用方法union，或者使用按位或操作符`|`

```shell
a = {1, 2, 3}
b = {2, 3, 4}
a.union(b)
{1, 2, 3, 4}
a | b
{1, 2, 3, 4}
```

一些其他的方法

```shell
# 取交集
c = a & b
c
{2, 3}

# 判断是否是子集
c.issubset(a)
True
c <= a
True

# 判断是否是超集
c.issuperset(a)
False
c >= a
False

# 取交集
a.intersection(b)
{2, 3}
a & b
{2, 3}

# 差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
a.difference(b)
{1}
a - b
{1}

# 两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
a.symmetric_difference(b)
{1, 4}
a ^ b
{1, 4}

# 拷贝一个集合
a.copy()
{1, 2, 3}
a.copy() is a
False
```

集合是可变的，因此不能用作字典中的键。另一个问题是，集合只能包含不可变(可散列)
的值，因此不能包含其他集合。由于在现实世界中经常会遇到集合的集合，因此这可能是个问题。 所幸还有frozenset类型，它表示不可变(可散列)的集合。

```shell
>>> a = set()
>>> b = set()
>>> a.add(b)
Traceback (most recent call last):
File "<stdin>", line 1, in ? TypeError: set objects are unhashable >>> a.add(frozenset(b))
```

构造函数frozenset创建给定集合的副本。在需要将集合作为另一个集合的成员或字典中的键时，frozenset很有用。

2. 堆  
   
堆是一种优先队列。

优先队列让你能够以任意顺序添加对象，并随时(可能是在两次添加对象之间)找出(并删除)最小的元素。


Python没有独立的堆类型，而只有一个包含一些堆操作函数的模块。这个模块名为 heapq(其中的q表示队列)，它包含6个函数(如表10-5所示)
，其中前4个与堆操作直接相关。必须使用列表来表示堆对象本身。

|函数|描述|
|---|---|
|heappush(heap, x)|将x压入堆中|
|heappop(heap)|从堆中弹出最小的元素|
|heapify(heap)|让列表具备堆特征|
|heapreplace(heap, x)|弹出最小的元素，并将x压入堆中|
|nlargest(n, iter)|返回iter中n个最大的元素|
|nsmallest(n, iter)|返回iter中n个最小的元素|


函数heappush用于在堆中添加一个元素。请注意，不能将它用于普通列表，而只能用于使用各种堆函数创建的列表。原因是元素的顺序很重要(
虽然元素的排列顺序看起来有点随意，并没有严格地排序)。

```shell
from heapq import *
from random import shuffle
data = list(range(10))
heap = []
for n in data:
    heappush(heap, n)
    
heap
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
heappush(heap, 0.5)
heap
[0, 0.5, 2, 3, 1, 5, 6, 7, 8, 9, 4]
```

元素的排列顺序并不像看起来那么随意。它们虽然不是严格排序的，但必须保证一点:位置i处的元素总是大于位置i // 2处的元素(反过来说就是小于位置2 * i和2
* i + 1处的元素)。这是底层堆算法的基础，称为**堆特征(heap property)**。

函数heappop弹出最小的元素(总是位于索引0处)，并确保剩余元素中最小的那个位于索引0 处(保持堆特征)
。虽然弹出列表中第一个元素的效率通常不是很高，但这不是问题，因为heappop 会在幕后做些巧妙的移位操作。

```shell
heappop(heap)
0

heappop(heap)
0.5

heap
[1, 3, 2, 7, 4, 5, 6, 9, 8]
```


函数heapify通过执行尽可能少的移位操作将列表变成合法的堆(即具备堆特征)。如果你的
堆并不是使用heappush创建的，应在使用heappush和heappop之前使用这个函数。

```shell
>>> heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2] >>> heapify(heap)
>>> heap
[0, 1, 5, 3, 2, 7, 9, 8, 4, 6]
```


函数heapreplace用得没有其他函数那么多。它从堆中弹出最小的元素，再压入一个新元素。
相比于依次执行函数heappop和heappush，这个函数的效率更高。

```shell
>>> heapreplace(heap, 0.5)
0
>>> heap
[0.5, 1, 5, 3, 2, 7, 9, 8, 4, 6]
>>> heapreplace(heap, 10)
0.5
>>> heap
[1, 2, 5, 3, 6, 7, 9, 8, 4, 10]
```


nlargest(n, iter)和nsmallest(n, iter)，:分别用于找出可迭代对象iter中最大和最小的n个元素。这种任务也可通过先排序(
如使用函数sorted)再切片来完成，但堆算法的速度更快，使用的内存更少(而且使用起来也更容易)。

3. 双端队列

在需要按添加元素的顺序进行删除时，双端队列很有用。在模块collection中，包含类型deque以及其他几个集合类型。

双端队列也是从可迭代对象创建的。

```python
from collections import deque

q = deque(range(5))
q.append(5)
q.appendleft(6)
q
# deque([6, 0, 1, 2, 3, 4, 5])
q.pop()
# 5
q.popleft()
# 6

q
# deque([0, 1, 2, 3, 4])
q.rotate(3)  # 向右旋转元素
q
# deque([2, 3, 4, 0, 1])
q.rotate(-1)
q
# deque([3, 4, 0, 1, 2])
```

双端队列支持在左侧高效地附加和弹出元素，而列表却不支持。还可以高效得旋转元素（将元素左移或右移）。

双端队列对象还包含方法extend和extendleft，其中extend类似于相应的列表方法，而extendleft类似于
appendleft。请注意，用于extendleft的可迭代对象中的元素将按相反的顺序出现在双端队列中。

```python
q
# deque([3, 4, 0, 1, 2])
q.extend([7, 8, 9])
q
# deque([3, 4, 0, 1, 2, 7, 8, 9])

# 用于extendleft的可迭代对象中的元素将按相反的顺序出现在双端队列中。
q.extendleft([5, 6, 7])
q
# deque([7, 6, 5, 3, 4, 0, 1, 2, 7, 8, 9])
```


### 10.3.5 time

模块time包含由于获取当前时间、操作时间和日期、从字符串中读取日期、将日期格式化为字符串的函数。  
日期可以表示为实数（UNIX里就是从1970年1月1日0时开始到现在的秒数），也可以表示为包含9个整数的元组。  
例如，元组(2008, 1, 21, 12, 2, 56, 0, 21, 0)
表示2008年1月21日12时2分56秒。这一天是星期一2008年的第21天（不考虑夏令时）

|索引|字段|值|
|---|---|---|
|0|年|如2000、2021等|
|1|月|范围1~12|
|2|日|范围1~31|
|3|时|范围0~23|
|4|分|范围0~59|
|5|秒|范围0~61|
|6|星期几|范围0~6，0代表星期一|
|7|儒略日|范围1~366|
|8|夏令时|0、1或-1|

秒的取值范围为0~61，这考虑到了闰一秒和闰两秒的情况。夏令时数字是一个布尔值(True 或False)
，但如果你使用-1，那么mktime[将时间元组转换为时间戳(从新纪元开始后的秒数) 的函数]可能得到正确的值。

模块time中一些重要的函数

|函数|描述|
|---|---|
|asctime([tuple])|将时间元组转换为字符串|
|localtime([secs])|将秒数转换为表示当地时间的日期元组|
|mktime(tuple)|将时间元组转换为当地时间|
|sleep(secs)|休眠secs秒|
|strptime(string[, format])|将字符串转换为时间元组|
|time()|当前时间（从新纪元开始后的秒数）|

函数time.asctime()将当前时间转换为字符串

```shell
import time
time.asctime()
'Sat Jul  3 10:11:40 2021'
```

如果不想使用当前时间，也可向它提供一个日期元组(如localtime创建的日期元组)。要设置更复杂的格式，可使用函数strftime。

函数time.localtime将一个实数转换为日期元组（本地时间）。如果要转换为国际标准时间，应使用函数gmtime

函数time.mktime将日期元组转换为从新纪元后的秒数，这与localtime的功能相反。

函数time.sleep让解释器等待指定的秒数。

函数time.strptime将一个字符串(其格式与asctime所返回字符串的格式相同)转换为日期元组。(
可选参数format遵循的规则与strftime相同，详情请参阅标准文档。)

函数time.time返回当前的国际标准时间，以从新纪元开始的秒数表示。可以通过两次调用time函数的差值来计时。

另外，还有两个较新的与时间相关的模块:datetime和timeit。前者提供了日期和时间算术 支持，而后者可帮助你计算代码段的执行时间。

### 10.3.6 random

模块random包含生成伪随机数的函数。虽然看起来生成出来的是随机的，但是背后其实是可预测的。如果需要真正的随机（如用于加密或实现与安全相关的功能），应该
考虑使用模块os里面的urandom。模块random里的SystemRandom类基于的功能与urandom类似，可提供接近于真正随机的数据。

模块random中一些重要的函数

|函数|描述|
|---|---|
|random()|返回一个[0.0,1.0)的随机实数|
|getrandbits(n)|以长整数方式返回n个随机的二进制位|
|uniform(a, b)|返回一个随机浮点数 N ，当 a <= b 时 a <= N <= b ，当 b < a 时 b <= N <= a 。|
|randrange([start], stop, [step])|从range(start, stop, step)中随机地选择一个数|
|choice(seq)|从序列seq中随机地选择一个元素|
|shuffle(seq[, random])|就地打乱序列seq| 
|sample(seq, n)|从序列seq中随机地选择n个值不同的元素|

函数random.random是最基本的随机函数之一，它返回一个[0.0,1.0)的伪随机数。除非这正是你需要的，否则可能应使用其他提供了额外功能的函数。

函数random.getrandbits以一个整数的方式返回指定数量的二进制位。

向函数random.uniform提供了两个数字参数a和b时，它返回一个a~b(含)的随机(均匀分布的)
实数。例如，如果你需要一个随机角度，可使用uniform(0, 360)。

函数random.randrange是生成随机整数的标准函数。为指定这个随机整数所在的范围，你可像调用range那样给这个函数提供参数。例如，要生成一个1~
10(含)的随机整数，可 使用randrange(1, 11)或randrange(10) + 1。要生成一个小于20的随机正奇数，可使用randrange(
1, 20, 2)。

函数random.choice从给定序列中随机(均匀)地选择一个元素。

函数random.shuffle随机地打乱一个可变序列中的元素，并确保每种可能的排列顺序出现的概率相同。

函数random.sample从给定序列中随机(均匀)地选择指定数量的元素，并确保所选择元素的值各不相同。

> 编写与统计相关的程序时，可使用其他类似于uniform的函数，它们返回按各种分布随机
> 采集的数字，如贝塔分布、指数分布、高斯分布等。

使用random的例子

```python
# 随机生成指定日期直接的时间
from random import *
from time import *

# 定义时间下限
date1 = (2021, 1, 1, 0, 0, 0, -1, -1, -1)
# 元组转为秒数
time1 = mktime(date1)
date2 = (2022, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)

random_time = uniform(time1, time2)

# 秒数转为当地时间元组，再转换为字符串
print(asctime(localtime(random_time)))
```

```python
# 扔骰子
from random import randrange

num = int(input('有多少个骰子?'))
sides = int(input('骰子有多少个面?'))
sum = 0
for i in range(num):
    sum += randrange(sides) + 1
print('结果是：', sum)
```

### 10.3.7 shelve和json
模块shelve可以将Python中的任意对象持久化。以一种类似字典的形式存储起来。

但是在使用的时候不同于字典，它的键必须是str
```shell
import shelve
s = shelve.open('test.dat')
s['x']=['a', 'b', 'c']
s['x'].append('d') # 此处是获取了存储的副本，但是并没有保存修改
s['x']
['a', 'b', 'c']
```
正确做法：将获取的副本赋给一个临时变量，并在修改这个副本后再次存储：
```shell
s['x']
['a', 'b', 'c']
temp = s['x']
temp.append('d')
s['x'] = temp
s['x']
['a', 'b', 'c', 'd']
```
还有另一种避免这个问题的办法：将函数open的参数writeback设置为True。这样，从shelf
对象读取或赋给它的所有数据结构都将保存到内存（缓存）中，并等到你关闭shelf对象时才将
它们写入磁盘中。


一个简单的数据库程序
```shell
import sys, shelve

def store_person(db):
    """
    让用户输入数据并将其存储到shelve对象
    :param db:
    :return:
    """
    pid = input('Enter unique ID number: ')
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age: ')
    person['phone'] = input('Enter phone number: ')
    db[pid] = person

def lookup_person(db):
    pid = input('Enter ID number: ')
    field = input('What would you like to know? (name, age, phone) ')
    #删除字符串开头和结尾的空格，并转为小写
    field = field.strip().lower()
    print(field.capitalize() + ':', db[pid][field])

def print_help():
    print('The available commands are:')
    print('store : Stores information about a person')
    print('lookup : Looks up a person from ID number')
    print('quit : Save changes and exit')
    print('? : Prints this message')

def enter_command():
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('aaa.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == '__main__':
    main()
```


### 10.3.8 re

re模块提供了对正则表达式的支持

1. 正则表达式相关知识

正则表达式是可匹配文本片段的模式。

+ 通配符 通配符包括`. `等。`.`匹配除换行符以外的所有字符。

+ 对特殊字符进行转义 对于一些在正则表达式中有特殊意义的字符，如果要将其作为普通字符，就需要进行转义比如要匹配`python.org`,就需要加`反斜线`对`.`进行转义。

```python
#但是在Python里，如果要在str里写反斜杠的话需要写成
pat = 'python\\.org'
#可以使用原始字符串
pat = r'python\.org'
```

+ 字符集 可以用方括号将一个子串括起来，创建一个所谓的字符集。这样的字符集与其包含的字符都匹配。**注意字符集只能匹配一个字符**

```python
'[pj]ython'  # 匹配 python 和 jython
'[a-z]'  # 匹配a到z的任何小写字母
'[a-zA-Z0-9]'  # 匹配大写字母，小写字母和数字

#可以使用^来排除字符集
'[^abc]'  # 匹配除a、b和c之外的任何字符
```

> 脱字符(^)位于字符集开头时，除非要将其用作排除运算符，否则必须对其进行转 义。换而言之，除非有意为之，否则不要将其放在字符集开头。
>
> 同样，对于右方括号(])和连字符(-)，要么将其放在字符集开头，要么使用反斜 杠对其进行转义。实际上，如果你愿意，也可将连字符放在字符集末尾。

+ 二选一和子模式

使用管道符`|`可以实现二选一，比如`python|perl`匹配字符串python和perl  
子模式表示模式的一部分，比如上面的示例可以写成`p(ython|erl)`，注意，单个字符也可称为子模式

+ 可选模式和重复模式

通过在子模式后面加上问号`?`，可将其指定为可选的，就是可以包含也可以不包含。

```python
pat = r'(http://)?(www\.)?python\.org'
# 可以匹配以下字符串
# http://www.python.org
# http://python.org
# www.python.org
# python.org
```

+ 字符串的开头和末尾

要匹配指定开头或结尾的字符串就要使用到锚点。^ 指定开头，$ 指定结尾。

^ 用来检查匹配的字符串是否在所匹配字符串的开头。

> "(T|t)he" => **The** car is parked in the garage.

$ 用来检查匹配的字符串是否在所匹配的字符串的结尾。

> "(at\.)$" => The fat cat. sat. on the m**at.**

2. 模块re的内容

re模块的函数

|函数|描述|
|---|---|
|compile(pattern[,flags])|根据包含正则表达式的字符串创建模式对象|
|search(pattern,string[, flags])|在字符串中查找模式|
|match(pattern, string[, flags])|在字符串开头匹配模式|
|split(pattern, string[,flags])|根据模式来分割字符串|
|findall(pattern, string)|返回一个列表，包含所有匹配的子串|
|sub(pat, repl, string[, count=0])|将字符串中与模式pat匹配的子串都替换成repl|
|escape(string)|对字符串中所有的正则表达式特殊字符都进行转义|

函数re.compile将字符串形式的正则表达式编译成模式对象，来提高匹配效率。re.search(pat, string)等价于pat.search(string),编译后的pat对象也可以用在re的普通函数中。

函数re.search在给定字符集中查找第一个与指定模式匹配的子串。如果找到，返回MatchObject(结果为真)，否则返回None（结果为假）。

```python
if re.search(pat, string):
    print('Found it')
```

函数re.match尝试在字符串开头查找与正则表达式匹配的子串，因此

```python
import re

re.match('p', 'python')  # 返回真
re.match('p', 'www.python.org')  # 返回假
```

```python
import re

string = 'like at. mat. hat.'
pat = re.compile(r'at\.')
print(pat.match(string))  # None
print(pat.search(string))  # <re.Match object; span=(5, 8), match='at.'>
```

> 看了看资料，发现其实re.search和re.match要区分情况使用，如果你想从字符串开头匹配，就用match，这样还可以不用在表达式里添加`^`，如果是在一文本内进行匹配，就用search

函数re.split根据与模式匹配的子串来分割字符串。这类似于字符串方法split，但使用正则表达式来指定分隔符，而不是指定固定的分隔符。

```python
some_text = 'alpha, beta,,,,gamma       delta'
pat = re.compile(r'[, ]+')
print(pat.split(some_text))  # ['alpha', 'beta', 'gamma', 'delta']
# maxsplit参数可以指定最多分割多少次
print(pat.split(some_text, maxsplit=2))  # ['alpha', 'beta', 'gamma       delta']
print(pat.split(some_text, maxsplit=1))  # ['alpha', 'beta,,,,gamma       delta']
```

> 注意 如果模式包含圆括号，将在分割得到的子串之间插入括号中的内容。例如，re.split('o(o)',
'foobar')的结果为['f', 'o', 'bar']。
> ```python
>some_text = 'at. mat. hat.'
>pat = re.compile(r'a(t.)')
>print(pat.split(some_text))
> # 本来分割出来的子串是['', ' m', ' h', '']  
> # 由于正则表达式里有括号，所以将括号里的内容，也就是t.插入到分割出的子串里
> # 最终结果就是 ['', 't.', ' m', 't.', ' h', 't.', '']
>```
函数re.findall返回一个列表，其中包含所有与给定模式匹配的子串。
```python
import re
pat = '[a-zA-Z]+'
text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
print(re.findall(pat, text))  
# ['Hm', 'Err', 'are', 'you', 'sure', 'he', 'said', 'sounding', 'insecure']
```
函数re.sub从左往右将与模式匹配的子串替换为指定内容。
```python
pat = re.compile('{name}')
text = 'Dear {name}...'
print(pat.sub('吉祥',text))  # Dear 吉祥...
```
re.escape是一个工具函数，用于对字符串中所有可能被视为正则表达式运算符的字符进行转义。
比如在你想将用户输入的一部分作为正则表达式的时候可以用它。
```python
print(re.escape('www.python.org'))  # www\.python\.org
```


3. 匹配对象和编组

在re模块中，查找与模式匹配的函数都在找到时返回MatchObject对象。这种对象包含与模式匹配的子串的信息，还包含模式的哪部分与子串的哪部分匹配的信息。 
这些子串部分称为**编组(group)**

编组就是放在圆括号里面的子模式，是根据左边的括号数编号的，编组0指的是整个模式。
```
'There (was a (wee) (cooper)) who (lived in Fyfe)'
# 包含以下编组
# 0：There was a wee cooper who lived in Fyfe
# 1：was a wee cooper
# 2：wee
# 3：cooper
# 4：lived in Fyfe
```
通过编组，可以获取到子模式匹配出来的内容。  
下表描述了re匹配对象的一些重要方法

|函数|描述|
|---|---|
|group([group1, ...])|获取与给定子模式（编组）匹配的子串|
|start([group])|返回与给定编组匹配的子串的起始位置|
|end([group])|返回与给定编组匹配的子串的终止位置（与切片一样，不包含终止位置）|
|span([group])|返回与给定编组匹配的子串的起始和终止位置|

方法group返回与模式中给定编组匹配的子串。如果没有指定编组号，则默认为0。如果只指
定了一个编组号（或使用默认值0），将只返回一个字符串；否则返回一个元组，其中包含与给定
编组匹配的子串。
```python
some_string = 'There was a wee cooper who lived in Fyfe'
pat = re.compile('There (was a (wee) (cooper)) who (lived in Fyfe)')
print(pat.match(some_string).group()) # There was a wee cooper who lived in Fyfe
print(pat.match(some_string).group(1, 2)) # ('was a wee cooper', 'wee')
```
> 注意 除整个模式（编组0）外，最多还可以有99个编组，编号为1~99。

方法start返回与给定编组（默认为0，即整个模式）匹配的子串的起始索引。  

方法end类似于start，但返回终止索引加1  

方法span返回一个元组，其中包含与给定编组（默认为0，即整个模式）匹配的子串的起始索引和终止索引。  

示例
```shell
>>> m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
>>> m.group(1)
'python'
>>> m.start(1)
4
>>> m.end(1)
10
>>> m.span(1)
(4, 10)
```

4. 替换中的组号和函数
   
利用re.sub的强大功能，可以在替换字符串中使用组号。在替换字符串中，任何类似于'\\n'的转义序列都将被替换为与模式中编组n匹配的字符串。

举例
```python

emphasis_pattern = re.compile(r'\*([^/*]+)\*')
# 其中里面的\1将变成模式匹配的编号为1的编组匹配的字符串
print(emphasis_pattern.sub(r'<em>\1</em>', 'Hello, *World*!')) # Hello, <em>World</em>!
```   
通过将函数用作替换内容，可执行更复杂的替换。这个函数将MatchObject作为唯一 的参数，
它返回的字符串将用作替换内容。换而言之，你可以对匹配的字符串做任何处理，并通过细致的处理来生成替换内容。

> 贪婪和非贪婪模式  
> 重复运算符默认是贪婪的，它们将匹配尽可能多的内容。  
> 对于所有的重复运算符，都可在后面加上问号来将其指定为非贪婪的。

5. 示例：找出发件人

比如有这样一组虚构的邮件头
```text
From foo@bar.baz Thu Dec 20 01:22:50 2008
Return-Path: <foo@bar.baz>
Received: from xyzzy42.bar.com (xyzzy.bar.baz [123.456.789.42])
by frozz.bozz.floop (8.9.3/8.9.3) with ESMTP id BAA25436
for <magnus@bozz.floop>; Thu, 20 Dec 2004 01:22:50 +0100 (MET) Received: from [43.253.124.23] by bar.baz
(InterMail vM.4.01.03.27 201-229-121-127-20010626) with ESMTP
id <20041220002242.ADASD123.bar.baz@[43.253.124.23]>; Thu, 20 Dec 2004 00:22:42 +0000 User-Agent: Microsoft-Outlook-Express-Macintosh-Edition/5.02.2022
Date: Wed, 19 Dec 2008 17:22:42 -0700
Subject: Re: Spam
From: Foo Fie <foo@bar.baz>
To: Magnus Lie Hetland <magnus@bozz.floop>
CC: <Mr.Gumby@bar.baz>
Message-ID: <B8467D62.84F%foo@baz.com>
In-Reply-To: <20041219013308.A2655@bozz.floop> Mime- version: 1.0 Content-type: text/plain; charset="US-ASCII" Content-transfer-encoding: 7bit Status: RO
Content-Length: 55
Lines: 6
So long, and thanks for all the spam!
Yours, Foo Fie
```
我们来尝试找出这封邮件的发件人。
可以发现发件人都是以From：开头的那一行，所以可以通过正则表达式加fileinput模块处理
```python
# 找出所有发件人
import fileinput, re

pat = re.compile(r'From: (.*) <.*?>$')
for line in fileinput.input():
    m = pat.match(line)
    if m:
        print(m.group(1))

# 找出所有邮件地址
pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE) 
addresses = set()
for line in fileinput.input():
    for address in pat.findall(line):
        addresses.add(address) 
for address in sorted(addresses):
    print(address)
```

6. 模板系统示例

模板（template）是一种文件，可在其中插入具体的值来得到最终的文本。

比如下面的模板
```text
[x = 2]
[y = 3]
The sum of [x] and [y] is [x + y].
```
执行后应该输出
```text
The sum of 2 and 3 is 5.
```
实现逻辑的Python脚本
```python
import fileinput, re
# 与使用方括号括起的字段匹配
field_pat = re.compile(r'\[(.+?)\]')
# 我们将把变量收集到这里：
scope = {}
# 用于re.sub函数的一个入参，用来指定如何处理匹配的编组
def replacement(match):
    code = match.group(1)
    try:
        # 如果字段为表达式（比如x+y），就返回其结果：
        return str(eval(code, scope))
    except SyntaxError:
        # 否则在当前作用域内执行该赋值语句
        exec(code, scope)
        # 并返回一个空字符串
        return ''
# 获取所有文本并合并成一个字符串：
#（还可采用其他办法来完成这项任务，详情请参见第11章）
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)
# 替换所有与字段模式匹配的内容：
print(field_pat.sub(replacement, text))
```
运行
```shell
$ python BeginningPython/chapter10/templates.py BeginningPython/chapter10/test_template.txt

The sum of 2 and 3 is 5.
```

### 10.3.9 其他有趣的标准模块
+ argparse：在UNIX中，运行命令行程序时常常需要指定各种选项（开关）， Python解释器
就是这样的典范。这些选项都包含在sys.argv中，但要正确地处理它们绝非容易。模块
argparse使得提供功能齐备的命令行界面易如反掌。
+ cmd：这个模块让你能够编写类似于Python交互式解释器的命令行解释器。你可定义命令，
让用户能够在提示符下执行它们。或许可使用这个模块为你编写的程序提供用户界面？
+ csv： CSV指的是逗号分隔的值（comma-seperated values），很多应用程序（如很多电子表
格程序和数据库程序）都使用这种简单格式来存储表格数据。这种格式主要用于在不同
的程序之间交换数据。模块csv让你能够轻松地读写CSV文件，它还以非常透明的方式处
理CSV格式的一些棘手部分。
+ datetime：如果模块time不能满足你的时间跟踪需求，模块datetime很可能能够满足。
datetime支持特殊的日期和时间对象，并让你能够以各种方式创建和合并这些对象。相比
于模块time，模块datetime的接口在很多方面都更加直观。
+ difflib：这个库让你能够确定两个序列的相似程度，还让你能够从很多序列中找出与指
定序列最为相似的序列。例如，可使用difflib来创建简单的搜索程序。
+ enum：枚举类型是一种只有少数几个可能取值的类型。很多语言都内置了这样的类型，如
果你在使用Python时需要这样的类型，模块enum可提供极大的帮助。
+ functools：这个模块提供的功能是，让你能够在调用函数时只提供部分参数（部分求值，
partial evaluation），以后再填充其他的参数。在Python 3.0中，这个模块包含filter和reduce。
+ hashlib：使用这个模块可计算字符串的小型“签名”（数）。计算两个不同字符串的签名
时，几乎可以肯定得到的两个签名是不同的。你可使用它来计算大型文本文件的签名，
这个模块在加密和安全领域有很多用途①。
+ itertools：包含大量用于创建和合并迭代器（或其他可迭代对象）的工具，其中包括可
以串接可迭代对象、创建返回无限连续整数的迭代器（类似于range，但没有上限）、反复
遍历可迭代对象以及具有其他作用的函数。
+ logging：使用print语句来确定程序中发生的情况很有用。要避免跟踪时出现大量调试输
出，可将这些信息写入日志文件中。这个模块提供了一系列标准工具，可用于管理一个
或多个中央日志，它还支持多种优先级不同的日志消息。
+ statistics：计算一组数的平均值并不那么难，但是要正确地获得中位数，以确定总体标
准偏差和样本标准偏差之间的差别，即便对于偶数个元素来说，也需要费点心思。在这
种情况下，不要手工计算，而应使用模块statistics！
+ timeit、 profile和trace：模块timeit（和配套的命令行脚本）是一个测量代码段执行时
间的工具。这个模块暗藏玄机，度量性能时你可能应该使用它而不是模块time。模块
profile（和配套模块pstats）可用于对代码段的效率进行更全面的分析。模块trace可帮
助你进行覆盖率分析（即代码的哪些部分执行了，哪些部分没有执行），这在编写测试代
码时很有用。