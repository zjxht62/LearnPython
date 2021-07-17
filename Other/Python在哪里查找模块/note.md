# Python在哪里查找模块

## sys.path

Python在变量`sys.path`中查找模块，它是一个`list`，Python会在`list`内的路径下查找可用的模块

```python
import sys

print(type(sys.path))  # <class 'list'>
for p in sys.path:
    print(p)

# 输出
# /Users/zjx/PycharmProjects/LearnPython/Other/Python在哪里查找模块
# /Users/zjx/PycharmProjects/LearnPython
# /Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display
# /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python38.zip
# /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8
# /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/lib-dynload
# /Users/zjx/PycharmProjects/LearnPython/venv/lib/python3.8/site-packages
# /Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend
```

其中第一个路径是当前路径，表示你当前运行的Python脚本所在的路径。所以你在同目录和同目录的子目录中写的模块都能找到。

既然`sys.path`是一个`list`那么我们可以使用`append`方法增加我们需要查找的路径  
比如我有一个放在桌面的模块，hello。

```python
def hello():
    print('hello from 桌面')
```

我要在/Users/zjx/PycharmProjects/LearnPython/Other/Python在哪里查找模块/demo.py中import桌面上的hello

```python
# 直接import会出现ModuleNotFoundError
import sys
import hello

# Traceback (most recent call last):
#  File "/Users/zjx/PycharmProjects/LearnPython/Other/Python在哪里查找模块/demo.py", line 2, in <module>
#    import hello
# ModuleNotFoundError: No module named 'hello'
```

```python
import sys, pprint

sys.path.append('/Users/zjx/Desktop')
import hello

hello.hello()  # hello from 桌面
```

## PYTHONPATH环境变量

既然Python总是在`sys.path`中的路径查找模块，那我们还可以通过`PYTHONPATH`环境变量，来将路径添加到`sys.path`中

还是以import桌面上的hello模块为例：

```python
import hello

hello.hello()
```

直接import肯定还是ModuleNotFoundError

```shell
% python demo.py
Traceback (most recent call last):
  File "/Users/zjx/PycharmProjects/LearnPython/Other/Python在哪里查找模块/demo.py", line 2, in <module>
    import hello

```

通过export命令可以设置此次会话的环境变量

```shell
% export PYTHONPATH=/Users/zjx/Desktop
% python demo.py 
hello from 桌面
```

改一下脚本，打印一下`sys.path`

```shell
% python demo.py
['/Users/zjx/PycharmProjects/LearnPython/Other/Python在哪里查找模块',
 '/Users/zjx/Desktop',     # 这里就是从PYTHONPATH中读取的路径
 '/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip',
 '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9',
 '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload',
 '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages']
hello from 桌面
```

如果想让`PYTHONPATH`环境变量更加永久性地生效，可以配置用户或系统级别的环境变量。 比如Mac上的`.bash_profile`

## .pth文件

Python有一个`site`模块，这个模块会在初始化的时候自动导入。它会在4个路径下查找`.pth`文件，如果查找到了，就会将文件中记录的路径加入到`sys.path`变量中。  
其中的四个路径由头部和尾部组成。头部是`sys.prefix`变量和`sys.exec_prefix`变量，尾部是空字符串然后是 lib/site-packages (在 Windows 上) 或
lib/pythonX.Y/site-packages (在 Unix 和 Macintosh 上)。

```python
import sys

# 路径头部
prefix_list = [sys.prefix, sys.exec_prefix]
# 这里路径的结尾以Mac系统为例
suffix_list = ['', 'lib/python3.9/site-packages']

for p in prefix_list:
    for s in suffix_list:
        print(p + '/' + s)
```

运行结果如下，Python的site模块会在下面这四个路径下查找.pth文件

```text
/Library/Frameworks/Python.framework/Versions/3.9/
/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages
/Library/Frameworks/Python.framework/Versions/3.9/
/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages
```

接下来我们开始试验：  
要运行的demo.py
```python
# demo.py
import hello
hello.hello()
```

直接运行demo.py肯定还是找不到模块
```shell
% python demo.py         
Traceback (most recent call last):
  File "/Users/zjx/PycharmProjects/LearnPython/Other/Python在哪里查找模块/demo.py", line 1, in <module>
    import hello
```
所以，我在`/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages`目录下创建一个`findhello.pth`文件，内容如下:
```text
/Users/zjx/Desktop
```
再次运行demo.py
```shell
 % python demo.py
hello from 桌面
```

## 总结
Python查找模块的路径都是在sys.path变量中存储着。可以通过多种方式来维护。
1. 直接append，可以在程序运行时动态增加可import的模块
2. 配置PYTHONPATH环境变量，可以将目录设置到环境变量，从而不用修改代码。  
   比如在Jenkins中要运行某个位置的脚本。而且脚本还引用了同目录下其他的脚本。可以使用export命令  
   把脚本根目录加到`sys.path`中
3. 添加.pth文件  
    添加.pth文件是永久生效的，相比配置环境变量更加简单和灵活。