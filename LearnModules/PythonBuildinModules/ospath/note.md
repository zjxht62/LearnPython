# os.path -- 常见的路径名操作
参考链接：https://docs.python.org/3/library/os.path.html  

这个模块实现了一些关于路径的有用的方法。path参数可以通过string或bytes传递。通常文件名表示为（Unicode）字符串。
不幸的是，某些文件名在Unix上可能无法表示为字符串。所以需要在Unix上支持任意文件名的应用程序应该使用字节对象来表示路径名。
反之亦然，使用字节对象不能代表 Windows 上的所有文件名（以标准 mbcs 编码），因此 Windows 应用程序应该使用字符串对象来访问所有文件。
> 注意所有这些函数都只接受字节或只接受字符串对象作为它们的参数。如果返回路径或文件名，则结果是相同类型的对象。

_在 3.8 版更改：exists()、lexists()、isdir()、isfile()、islink() 和 ismount() 现在返回 False 而不是对包含在操作系统级别无法表示的字符或字节的路径引发异常。_

