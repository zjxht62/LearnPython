# 文件
## 11.1 打开文件
可以使用函数open打开文件，open在自动导入的模块io中，所以不用import。
其中唯一必不可少的参数是文件名，open函数返回一个文件对象。
```python
f = open('some_file.txt')
```
如果文件不存在会抛异常
```text
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'
```
如果要通过写入文本来创建文件，这种调用函数open的方式并不能满足需求。为解决这种问
题，可使用函数open的第二个参数
### 文件模式
调用open的时候如果只传文件名，默认文件模式是`rt`文本读取，返回的是一个可读取的文件对象。
如果要写入，需要指定文件模式。函数open的mode参数就是这个用途。可以见下表

|值|描述|
|---|---|
|'r'|读取模式（默认值）|
|'w'|写入模式|
|'x'|独占写入模式|
|'a'|附加模式|
|'b'|二进制模式（与其他模式结合使用）|
|'t'|文本模式（默认值，与其他模式结合使用）|
|'+'|读写模式（与其他模式结合使用）|

写入模式让你能够写入文件，并在文件不存在时创建它。 独占写入模式更进一步，在文件已存在时引发FileExistsError异常。在写入模
式下打开文件时，既有内容将被删除（截断），并从文件开头处开始写入；如果要在既有文件末尾继续写入，可使用附加模式。  
'+'可与其他任何模式结合起来使用，表示既可读取也可写入。  
下面的例子说明了r+和w+的区别：  
对于文件somefile.txt 原始内容如下:
```text
我是原有的文件内容，哇哈哈哈
```
```python
# 这里总结一下w+和r+的不同，w+会删除文件原有的内容，并从头开始写
f = open('somefile.txt', 'w+',encoding='utf-8')
f.write("我是w+写入的")
f.close()
# somefile.txt 的内容变成了：我是w+写入的

# r+也是从头开始写，但是会保留原文件未被覆盖的内容
f = open('somefile.txt', 'r+',encoding='utf-8')
f.write("我是r+写入的")
f.close()
# somefile.txt 的内容变成了：我是r+写入的�件内容，哇哈哈哈
```
默认模式为'rt'，这意味着将把文件视为经过编码的Unicode文本，因此将自动执行解码和编码，
且默认使用UTF-8编码。要指定其他编码和Unicode错误处理策略，
可使用关键字参数`encoding`和`errors`。这还将自动转换换行字符。默认情况下， 
行以`'\n'`结尾。读取时将自动替换其他行尾字符（`'\r'`或`'\r\n'`）；写入时将`'\n'`替换为
系统的默认行尾字符（os.linesep）。

通常， Python使用通用换行模式。在这种模式下，后面将讨论的readlines等方法能够识别所
有合法的换行符（`'\n'`、 `'\r'`和`'\r\n'`）。如果要使用这种模式，同时禁止自动转换，
可将关键字参数`newline`设置为空字符串，如`open(name, newline='')`。如果要指定只将`'\r'`或`'\r\n'`视为合
法的行尾字符，可将参数newline设置为相应的行尾字符。这样，读取时不会对行尾字符进行转换，
但写入时将把'\n'替换为指定的行尾字符。

如果文件包含非文本的二进制数据，如声音剪辑片段或图像，你肯定不希望执行上述自动转换。
为此，只需使用二进制模式（如'rb'）来禁用与文本相关的功能。

## 11.2 文件的基本方法
本节介绍文件对象的一些基本
方法以及其他类似于文件的对象（有时称为流）。类似于文件的对象支持文件对象的一些方法，
如支持read或write，或者两者都支持。 urlopen（参见第14章）返回的对象就是典型的类似于文
件的对象，它们支持方法read和readline，但不支持方法write和isatty。

> 三个标准流  
> 一个标准数据输入源是sys.stdin。当程序从标准输入读取时，可以通过输入来提供文本，也可使用管道将标准输入关联到其他程序的标准输出。
> 
> 你提供给print的文本出现在sys.stdout中，向input提供的提示信息也出现在这里。写入到sys.stdout的数据通常出现在屏幕上，但可使用管道将其重定向到另一个程序的标准输入。
> 
> 错误消息（如栈跟踪）被写入到sys.stderr，但与写入到sys.stdout的内容一样，可对其进行重定向。

### 11.2.1 读取和写入
如果有一个名为f的类似于文件的对象，可使用f.write来写入数据，还可以使用f.read来读取数据。
在哪些东西可以用作数据方面，也存在一定的灵活性，但在文本和二进制模式下，基本上分别将str和bytes类用作数据。
```text
f = open('somefile.txt', 'w')
f.write('Hello, ')
f.write('World!')
f.close()

f = open('somefile.txt', 'r')
print(f.read(4))  # 读取四个字符
print(f.read())  # 读取剩余所有
```

### 使用管道重定向输出
通过管道符`|`可以将一个命令的标准输出链接到下一个命令的标准输入。
```shell
$ cat somefile.txt | python somescript.py | sort
```
计算sys.stdin中包含多少个单词的简单脚本
```python
#可以通过管道将内容写到python的标准输入sys.stdin
# cat somefile.txt | python somescript.py | sort
# somescript.py
import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('Wordcount:', wordcount)
```
对于随机存取，可使用文件对象的两个方法：seek和tell  
方法 seek(offset[, whence])将当前位置（执行读取或写入的位置）移到 offset 和 whence 指定的地方。
参数 offset 指定了字节（字符）数，而参数 whence 默认为 io.SEEK_SET（ 0）， 
这意味着偏移量是相对于文件开头的（偏移量不能为负数）。参数 whence 还可设置为io.SEEK_CUR（1） 
或 io.SEEK_END（2）， 其中前者表示相对于当前位置进行移动（偏移量可以为负），而后者表示相对于文件末尾进行移动。
```python
# 使用seek和tell可以实现在文件中的光标移动，以及获取当前位置
f = open('somefile.txt', 'w')
f.write("01234567890123456789")
# 移动光标到5
print(f.seek(5))  # 5 
f.write('Hello, World!')
f.close()

# 可以发现在光标5的地方进行了写入
f = open('somefile.txt')
print(f.read())  # 01234Hello, World!89

f = open('somefile.txt')
f.seek(3)
# 返回当前位于文件的什么位置
print(f.tell()) # 3
```
### 11.2.3 读取和写入行
要读取一行（从当前位置到下一个分行符的文本），可以使用方法readline。默认什么参数都不加将读取一行并返回它；
也可以提供一个非负整数，指定readline最多可读取多少个字符。要读取文件中的所有行，并以列表的方式返回它们，
可使用方法readlines。
```python
# 比如有下面这几行文本，存储在somefile1.txt里面
First line
Second line
Third line
Fourth and final line

# readline()和readline(limit)的区别
f = open('somefile1.txt')
print(repr(f.readline(5)))  # 'First' 读取5个字符
print(repr(f.readline(5)))  # ' line' 读取5个字符
print(repr(f.readline(5)))  # '\n' 读取5个字符，到了换行符
print(repr(f.readline(5)))  # 'Secon'
print(repr(f.readline(5)))  # 'd lin'
print(repr(f.readline(5)))  # 'e\n'
print(repr(f.readline()))  # 'Third line\n' 读取一行，有换行符
```
方法writelines与readlines相反：接受一个字符串列表（实际上，可以是任何序列或可迭代
对象），并将这些字符串都写入到文件（或流）中。请注意，写入时不会添加换行符，因此你必
须自行添加。另外，没有方法writeline，因为可以使用write。
```python
lines = ['娃哈哈', '爱呵呵', '诶嘿嘿']
f = open('demofile.txt', 'w+')
f.writelines(lines)

# 文件demofile.txt的内容如下
# 娃哈哈爱呵呵诶嘿嘿
```
