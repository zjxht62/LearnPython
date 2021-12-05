import os.path

# 返回路绝对路径的标准化版本，在大多数平台上，相当于用如下形式调用函数 normpath() ： normpath(join(os.getcwd(), path))。
print(os.path.abspath('.'))  # /Users/zjx/PycharmProjects/LearnPython/PythonBuildinModules/ospath

# 返回path最后的文件名。如果path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素。
print(os.path.basename('/foo/bar'))  # bar
print(os.path.basename('/foo/bar/'))  # ''

# 返回路径序列中每个路径的最长公共子路径，如果路径既包含绝对路径也包含相对路径，路径位于不同的驱动器上或者路径为空，则引发 ValueError。与 commonprefix() 不同，它返回一个有效路径。
path_1 = '/Users/zjx/PycharmProjects/LearnPython/PythonBuildinModules/ospath'
path_2 = '/Users/zjx/PycharmProjects/LearnPython/Playground'
print(os.path.commonpath((path_1, path_2)))  # /Users/zjx/PycharmProjects/LearnPython

# 返回最长路径前缀（逐个字符取），它是列表中所有路径的前缀。如果列表为空，则返回空字符串 ('')。
print(os.path.commonprefix(['/usr/lib', '/usr/local/lib']))  # /usr/l

# 返回路径名路径的目录名。这是通过将路径传递给函数 split() 返回的元素对的第一个元素。
print(os.path.dirname('/foo/bar/zar'))  # /foo/bar
print(os.path.dirname('/foo/bar/zar/'))  # /foo/bar/zar

# 如果路径引用现有路径或打开的文件描述符，则返回 True。对于损坏的符号链接，返回 False。在某些平台上，如果未授予对请求的文件执行 os.stat() 的权限，则此函数可能会返回 False，即使该路径实际存在。
print(os.path.exists('/Users/zjx/PycharmProjects/LearnPython/PythonBuildinModules/ospath'))  # True
print(os.path.exists('/Users/zjx/PycharmProjects/LearnPython/PythonBuildinModules/ospath/'))  # True
print(os.path.exists('/Users/zjx/PycharmProjects/LearnPython/PythonBuildinModules/ospath/note.md'))  # True

# 在 Unix 和 Windows 上，返回参数，其中 ~ 或 ~user 的初始组件被该用户的主目录替换。
# 其中各个平台的具体逻辑可以参考：https://docs.python.org/3/library/os.path.html#os.path.expanduser
print(os.path.expanduser('~/PycharmProjects'))  # /Users/zjx/PycharmProjects

# 获取路径相关的时间 返回值是一个浮点数，给出自纪元以来的秒数（参见时间模块）。如果文件不存在或无法访问，则引发 OSError。
print(os.path.getatime('/Users/zjx/PycharmProjects/LearnPython/PythonBuildinModules/ospath/'))  # 访问时间
print(os.path.getmtime('/Users/zjx/PycharmProjects/LearnPython/PythonBuildinModules/ospath/'))  # 修改时间
print(os.path.getctime('/Users/zjx/PycharmProjects/LearnPython/PythonBuildinModules/ospath/'))  # 创建时间

# 获取size，返回路径的大小（以字节为单位）。如果文件不存在或无法访问，则引发 OSError。
print(os.path.getsize('.'))  # 160
print(os.path.getsize('./path_demo.py'))  # 3003

# 如果路径是绝对路径名，则返回 True。在 Unix 上，这意味着它以斜杠开头，在 Windows 上，它在切掉潜在的驱动器号后以（反）斜杠开头。
print(os.path.isabs('/Users/zjx/PycharmProjects/LearnPython/PythonBuildinModules/ospath/'))  # True
print(os.path.isabs('../ospath'))  # False

# 如果路径是现有的常规文件，则返回 True。这遵循符号链接，因此 islink() 和 isfile() 对于同一路径都可以为真。
print(os.path.isfile('.'))  # False
print(os.path.isfile('./note.md'))  # True

# 如果路径是现有目录，则返回 True。这遵循符号链接，因此 islink() 和 isdir() 对于同一路径都可以为真。
print(os.path.isdir('.'))  # True
print(os.path.isdir('./note.md'))  # False

# os.path.join  https://docs.python.org/3/library/os.path.html#os.path.join
# 智能地链接一个或多个路径组件。返回值是 path 和 *paths 的任何成员的串联，每个非空部分后面只有一个目录分隔符，除了最后一部分，这意味着如果最后一部分为空，结果只会以分隔符结尾。
print(os.path.join('/Users', 'zjx', 'PycharmProjects'))  # /Users/zjx/PycharmProjects
print(os.path.join('/Users', 'zjx', 'PycharmProjects/'))  # /Users/zjx/PycharmProjects/
print(os.path.join('/Users/', 'zjx/PycharmProjects'))  # /Users/zjx/PycharmProjects
# 如果一个组件是绝对路径，则所有之前的组件都将被丢弃，并从绝对路径组件继续连接。
print(os.path.join('/Users', '/zjx/PycharmProjects'))  # /zjx/PycharmProjects
print(os.path.join('/Users', '/zjx/PycharmProjects', '/haha'))  # /haha


