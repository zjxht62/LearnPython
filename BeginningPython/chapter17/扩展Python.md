# 扩展Python

Python的优点是易于开发，但是缺点是性能不佳。对于一般的情况下，Python的速度已经够用，
但是如果需要一定的程序运行速度，C、C++、Java等语言通常要快好几个数量级。

## 17.1 鱼和熊掌兼得

如果速度要求很高，也不是很推荐只用C语言开发，因为虽然开发出来的软件执行速度快，但是会降低编程速度。就是要考虑：
是快速编写好程序，还是很久之后写出了速度极快的程序。（除非必须使用C语言，比如程序在嵌入式设备中运行）。  
对于Python编写的程序，要想提高运行速度，可以采取下面的方法：

1. 使用Python开发原型
2. 对程序进行性能分析，找出瓶颈
3. 使用C（或C++、C#、Java等）扩展重写瓶颈部分

这样的架构兼具两种语言的优点。既能获得Python的简洁灵活，又能获得低级语言的运行速度。
> 注意  
> 还有其他要选择使用C语言的原因，比如要编写与怪异硬件交互的低级代码。

如果写代码之前就知道了哪里可能是性能瓶颈，那么可以按照下面的提示来处理：
> 提示：将潜在的瓶颈封装起来

当代码写完的时候，可能发现并不需要使用C语言编写扩展来替换它（可能因为硬件的速度足够）。但是这样做的好处就是给你留下了选择的空间。  
扩展的另一个使用场景是遗留代码。你可能想重用一些代码，但这些代码是使用其他语言(如C)编写的。在这种情况下， 可将这些代码“包装”起来(
编写一个提供合适接口的小型C语言库)，并使用这个包装器来创建Python扩展。  
接下来将介绍如何扩展Python的经典C语言实现（可以手工编写所有代码，也可以使用工具SWIG），以及如何扩展其他两种Python实现：Jython和IronPython。

**反过来**  
反过来说，也可以在其他低级语言中嵌入Python解释器来执行少量的脚本和扩展。在这种情况下，嵌入Python追求的不是速度而是灵活性。  
现实中有很多这样的例子，例如，很多计算机游戏(它们几乎都是使用编译型语言编写的，其代码库几乎都是为最大限度提高速度而开发的)，
都使用诸如Python等动态语言来描述高级行为(如游戏中角色的“智力”)，而主代码引擎负责图形等方面。

## 17.2 简单易行的方式：Jython和IronPython

Jython和IronPython可以轻松得使用对应的原生语言来扩展Python，因为Jython和IronPython能够让你访问底层语言中的模块和类
（对于Jython来说，底层语言是Java，而IronPython则是C#和其他.Net语言），所以不用像扩展CPython那样遵循特定的API。
例如，在Jython中，可直接访问Java标准库。  
比如我们准备一个简单的Java类

```java
public class JythonTest {
    public void greeting() {
        System.out.println("Hello, world");
    }
}
```

可使用Java编译器（如javac）来编译这个类

```shell
javac JythonTest.java
```

> 提示  
> 如果使用Java进行开发，也可以使用命令jythonc 将Python类编译成Java类，然后就可以将它导入到Java程序中。

编译这个类后，启动Jython（并将.class文件放到当前目录或Java CLASSPATH包含的目录中）。

```shell
$ CLASSPATH=JythonTest.class jython
```

然后，就可以直接导入这个类了

```shell
>>> import JythonTest
>>> test = JythonTest()
>>> test.greeting()
Hello, world!
```

> Jython属性魔法  
> Jython在和Java交互方面确实有几把刷子。其中最有用的功能是，能够想访问普通属性一样访问JavaBean属性。
> 在Java中，只能通过getter/setter来读取或修改这些属性，比如Java实例foo包含方法setBar，
> 那就可以使用foo.bar = baz，而不是foo.setBar(baz)。同理，如果foo实例包含一个返回布尔型变量的方法isBar,
> 就可以使用foo.bar来获取相应属性的值。
> ```python
>   # 不用像下面这样做：
>   b = awt.Button()
>   b.setEnabled(False)
>   # 而可这样做：
>   b = awt.Button()
>   b.enabled = False
>```
> 实际上，所有属性也可以在构造函数中通过关键字参数来设置。因此可以像下面这样：  
> `b = awt.Button(enabled=False)`  
> 这适用于表示多个参数的元组，也适用于Java成例（如事件监听器）的函数参数。
> ```python
>   def exit(event):
>       java.lang.System.exit(0)
>   b = awt.Button("Close Me!", actionPerformed=exit)
>```
> 在Java中，必须实现一个包含方法actionPerformed的类，再使用b.addActionListener来 添加这个类的实例。

IronPython相关demo暂时不写了，可以参考Python基础教程PDF的p289

## 17.3 编写C语言扩展

其实使用最广泛的版本是Python官方的基于C语言实现的CPython。  
C语言的动态性不如Java和C#，而且对于Python来说，编译后的C语言代码也不是那么容易理解。所以，在用C语言编写Python扩展的时候，必须遵循严格的API。
有几个项目力图简化C语言扩展的编写过程，其中一个比较有名的是SWIG。

### 17.3.1 SWIG

SWIG指的是简单包装器和接口生成器（simple wrapper and interface generator），是一个适用于多种语言的工具。
一方面，它让你能够使用C或C++编写扩展代码；另一方面，它将自动包装这些代码，以便在Tcl、Python、Perl和Java等高级语言中使用。
这意味着你编写的C语言扩展可能不光能在Python中使用，也可以供众多其他语言使用。  
SWIG的安装步骤与其他Python工具相同。

+ 可从官网http://www.swig.org下载SWIG。
+ 很多UNIX/Linux发布版都包含SWIG；很多包管理器都能够让你直接安装它。
+ 有用于Windows的二进制安装程序。
+ 自己编译源代码也很简单，只需调用configure和make install即可。


1. 用法  
   SWIG使用起来很简单，前提是编写一些C语言代码。  
   (1) 为代码编写一个接口文件。这很像C语言头文件（在比较简单的情况下，可直接使用现有 的头文件）。  
   (2) 对接口文件运行SWIG，以自动生成一些额外的C语言代码（包装器代码）。  
   (3) 将原来的C语言代码和生成的包装器代码一起编译，以生成共享库。

2. 回文  
   回文（palindrome)是忽略空格、标点等后，正着读和反着读一样的句子。假设要检测的回文长度极长。 所以考虑编写一段C语言代码来处理。
   ```c
   #include <string.h>
   int is_palindrome(char *text) {
        int i, n=strlen(text);
        for (i = 0; I <= n/2; ++i) {
            if (text[i] != text[n-i-1]) return 0;
        }
        return 1;
   }
   ```

3. 接口文件  
   假设将上面的代码存储到palindrome.c中，接下来应该在palindrome.i中添加接口描述。
   在很多情况下，如果定义一个头文件（这里为palindrome.h）， SWIG可能能够 从中获取所需的信息。  
   补充一下：`头文件作为一种包含功能函数、数据接口声明的载体文件，主要用于保存程序的声明`  
   因此，如果有头文件，可尝试使用它。显式地编写接口文件的原因之一是，这样可微调SWIG包装代码的方式，
   其中最重要的微调是将某些东西排除在外。例如，包装巨大的C语言库时，你可能只想将几个函数导出到Python。
   在这种情况下，可只将要导出的函数放在接口文件中。  
   在接口文件中，你只是声明要导出的函数（和变量），就像在头文件中做的一样。在接口文件中，
   有一个由%{和%}界定的部分，可在其中指定要包含的头文件（这里为string.h）。
   在这个部分的前面，还有一个%module声明，用于指定模块名。（这里介绍的有些选项是可选的，
   同时使用接口文件可以做的事情还有很多；可以参考SWIG文档），下面是这里要编写的接口文件。    
   `回文检测库的接口（palindrome.i）`
   ```text
   %module palindrome
   
   %{
   #include <string.h>
   %}
   
   extern int is_palindrome(char *text);
   ```

4. 运行SWIG  
   运行SWIG比较简单，虽然有很多命令行开关（可以用swig
   -help查看），但是只要使用-python就可以让SWIG对C语言进行包装，以便在Python中使用。
   另一个可能很有用的开关是-c++，可用于包装C++库。运行SWIG时，需要将接口文件（也可以是头文件）作为参数，如下所示：  
   `$ swig -python palindrome.i`  
   这将生成两个新文件，分别是palindrome_wrap.c和palindrome.py。

5. 编译、链接和使用  
   要正确地编译，需要知道Python源代码（至少是头文件pyconfig.h和Python.h）的存储位置（它们可能分别位于Python安装目录和子目录Include中）。
   你还需根据选择的C语言编译器，使用正确的开关将代码编译成共享库。  
   下面是在Linux中使用编译器gcc的示例：
   ```text
   $ gcc -c palindrome.c
   $ gcc -I$PYTHON_HOME -I$PYTHON_HOME/Include -c palindrome_wrap.c
   $ gcc -shared palindrome.o palindrome_wrap.o -o _palindrome.so
   ```
   可能所有必要的包含文件都在一个地方，如/usr/include/python3.5（版本号随具体情况而异）。 在这种情况下，像下面这样做就行：
   ```text
   $ gcc -c palindrome.c
   $ gcc -I/usr/include/python3.5 -c palindrome_wrap.c
   $ gcc -shared palindrome.o palindrome_wrap.o -o _palindrome.so
   ```
   在Windows中（这里也假设从命令行运行编译器gcc），可使用如下命令来创建共享库：
   ```text
   $ gcc -shared palindrome.o palindrome_wrap.o C:/Python25/libs/libpython25.a -o_palindrome.dll
   ```
   在macOS中，可像下面这样做（如果你使用的是Python官方安装，PYTHON_HOME将为
   `/Library/Frameworks/Python.framework/Versions/Current`）：
   ```text
   $ gcc -dynamic -I$PYTHON_HOME/include/python3.5 -c palindrome.c
   $ gcc -dynamic -I$PYTHON_HOME/include/python3.5 -c palindrome_wrap.c
   $ gcc -dynamiclib palindrome_wrap.o palindrome.o -o _palindrome.so -Wl, -undefined, dynamic_lookup
   ```
   执行完上面那些像咒语一样的命令之后，将得到一个很有用的文件`_palindrome.so`。它就是共享库，可直接导入到Python中
   （条件是它位于PYTHONPATH包含的目录中，如当前目录中）：
   ```text
   >>> import _palindrome
   >>> dir(_palindrome)
   ['__doc__', '__file__', '__name__', 'is_palindrome']
   >>> _palindrome.is_palindrome('ipreferpi')
   1
   >>> _palindrome.is_palindrome('notlob')
   0
   ```       
   如果使用的是老版本的SWIG，那上面的就是全部内容了。然而，较新版本的SWIG版本还会生成一些Python包装代码（文件`palindrome.py`
   ）， 它导入模块_palindrome并执行一些检查工作。如果你不想使用文件palindrome.py，只需将其删除并将库链接为palindrome.so即可。  
   使用包装代码的效果与使用共享库相同。
   ```text
   >>> import palindrome
   >>> from palindrome import is_palindrome
   >>> if is_palindrome('abba'):
   ... print('Wow -- that never occurred to me ...')
   ...
   Wow -- that never occurred to me ...
   ```
   
6. 穿越编译器“魔法森林”的捷径  
很多人认为编译过程晦涩难懂。如果想自动化编译过程【如使用生成文件（makefile）】，就需要进行配置：指定Python安装位置、要使用的编译器和选项等。
   通过使用Setuptools可优雅地避免这样做。实际上，它直接支持SWIG，让你无需手工运行SWIG：只需编写代码和接口文件，再运行安装脚本。
   
### 17.3.2 手工编写扩展
并非必须使用SWIG，也可以自己编写包装代码，也可以在C语言代码中直接使用Python C API  
Python C API有专门的参考手册，即“Python/C API参考手册”(https://docs.python.org/3/c-api)。  
1. 引用计数  
在Python中，内存管理是自动完成的。你只需要创建对象，当你不在使用它的时候，它们就会消失。但是在C语言中，必须显式地释放不再使用的对象，
   否则程序占用的内存越来越大，这被称为内存泄露（memory leaking）。  
   编写Python扩展时，可以使用Python在幕后使用的内存管理工具，其中之一就是引用计数。它的基本理念是，一个对象只要被代码引用，就不应该将它释放。
   然而，指向对象的引用数为0后，引用数就不可能再增大--没办法创建指向相应对象的新引用。因此对象在内存中是自由浮动的。此时，可以安全地释放它。
   引用计数自动完成这个过程。所以，我们需要遵守一系列规则，这些规则指定了在各种情况下应将对象的引用计数加1或减1；而引用计数变为0后，对象将被自动释放。
   这意味着Python里没有专门负责管理对象的代码，因为你知道当对象不再被需要的时候，就会自动被释放。