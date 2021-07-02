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
sys.exit() # Process finished with exit code 0

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

变量sys.path在本章前面讨论过，它是一个字符串列表，其中的每个字符串都是一个目录名，
执行import语句时将在这些目录中查找模块
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

变量sys.stdin、 sys.stdout和sys.stderr是类似于文件的流对象，表示标准的UNIX概念：
标准输入、标准输出和标准错误。简单地说， Python从sys.stdin获取输入（例如，用于input中），
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
模块os让你能够访问多个操作系统服务。除此之外，os和它的子模块os.path还包含多个查看、创建和删除目录及文件的函数，以及一些操作路径的函数（例如， os.path.split和os.path.join让你在大多数情况下都可
忽略os.pathsep）

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
者退出Python解释器，并将控制权交给被执行的程序，而后者创建一个到程序的连接（这个连接
类似于文件）。
> 提示 请参阅模块subprocess，它融合了模块os.system以及函数execv和popen的功能

变量os.sep是用于路径名中的分隔符。
在UNIX（以及macOS的命令行Python版本）中，标准
分隔符为/。在Windows中，标准分隔符为\\（这种Python语法表示单个反斜杠）。
（在有些平台中， os.altsep包含替代路径分隔符，如Windows中的/。）
```python
print(repr(os.sep))  # '\\'
```

可使用os.pathsep来组合多条路径， 就像PYTHONPATH中那样。 pathsep用于分隔不同的路径名：
在UNIX/macOS中为:，而在Windows中为;。

变量os.linesep是用于文本文件中的行分隔符：在UNIX/OS X中为单个换行符（\n），在
Windows中为回车和换行符（\r\n）。

函数urandom使用随系统而异的“真正”（至少是强加密）随机源。如果平台没有提供这样的
随机源，将引发NotImplementedError异常。

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
需打印出替代内容，这些内容将被写回到当前输入文件中。就地进行处理时，可选参数backup用
于给从原始文件创建的备份文件指定扩展名。

函数fileinput.filename返回当前文件（即当前处理的行所属文件）的文件名。

函数fileinput.lineno返回当前行的编号。这个值是累计的，因此处理完一个文件并接着处
理下一个文件时，不会重置行号，而是从前一个文件最后一行的行号加1开始。

函数fileinput.filelineno返回当前行在当前文件中的行号。每次处理完一个文件并接着处
理下一个文件时，将重置这个行号并从1重新开始。

函数fileinput.isfirstline在当前行为当前文件中的第一行时返回True，否则返回False。

函数fileinput.isstdin在当前文件为sys.stdin时返回True，否则返回False。

函数fileinput.nextfile关闭当前文件并跳到下一个文件，且计数时忽略跳过的行。这在你
知道无需继续处理当前文件时很有用。

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
集合是可变的，因此不能用作字典中的键。另一个问题是，集合只能包含不可变(可散列) 的值，因此不能包含其他集合。由于在现实世界中经常会遇到集合的集合，因此这可能是个问题。 所幸还有frozenset类型，它表示不可变(可散列)的集合。
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
   
Python没有独立的堆类型，而只有一个包含一些堆操作函数的模块。这个模块名为 heapq(其中的q表示队列)，它包含6个函数(如表10-5所示)，其中前4个与堆操作直接相关。必须使用列表来表示堆对象本身。

|函数|描述|
|---|---|
|heappush(heap, x)|将x压入堆中|
|heappop(heap)|从堆中弹出最小的元素|
|heapify(heap)|让列表具备堆特征|
|heapreplace(heap, x)|弹出最小的元素，并将x压入堆中|
|nlargest(n, iter)|返回iter中n个最大的元素|
|nsmallest(n, iter)|返回iter中n个最小的元素|

函数heappush用于在堆中添加一个元素。请注意，不能将它用于普通列表，而只能用于使用各种堆函数创建的列表。原因是元素的顺序很重要(虽然元素的排列顺序看起来有点随意，并没有严格地排序)。
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
元素的排列顺序并不像看起来那么随意。它们虽然不是严格排序的，但必须保证一点:位置i处的元素总是大于位置i // 2处的元素(反过来说就是小于位置2 * i和2 * i + 1处的元素)。这是底层堆算法的基础，称为**堆特征(heap property)**。

函数heappop弹出最小的元素(总是位于索引0处)，并确保剩余元素中最小的那个位于索引0 处(保持堆特征)。虽然弹出列表中第一个元素的效率通常不是很高，但这不是问题，因为heappop 会在幕后做些巧妙的移位操作。
```shell
heappop(heap)
0

heappop(heap)
0.5

heap
[1, 3, 2, 7, 4, 5, 6, 9, 8]
```
函数heapify通过执行尽可能少的移位操作将列表变成合法的堆(即具备堆特征)。如果你的 堆并不是使用heappush创建的，应在使用heappush和heappop之前使用这个函数。
```shell
>>> heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2] >>> heapify(heap)
>>> heap
[0, 1, 5, 3, 2, 7, 9, 8, 4, 6]
```

函数heapreplace用得没有其他函数那么多。它从堆中弹出最小的元素，再压入一个新元素。 相比于依次执行函数heappop和heappush，这个函数的效率更高。
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

nlargest(n, iter)和nsmallest(n, iter)，:分别用于找出可迭代对象iter中最大和最小的n个元素。这种任务也可通过先排序(如使用函数sorted)再切片来完成，但堆算法的速度更快，使用的内存更少(而且使用起来也更容易)。

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
q.rotate(3) # 向右旋转元素
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