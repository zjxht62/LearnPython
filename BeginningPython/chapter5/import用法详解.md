# import用法详解

Python中的import主要有两种写法。

1. `import 模块名1 [as 别名], 模块名2 [as 别名2], ...`：这种方式会导入指定模块中的所有成员（包括变量、函数、类等）。在使用模块里面的成员时，需要使用`模块名/别名.成员名`进行使用。
2. `from 模块名 import 成员名1 [as 别名1], 成员名2 [as 别名2], ...`：这种方式只会导入模块里的指定成员，而不是全部成员。可以直接通过`成员名/别名`进行调用。

第二种方式，可以通过`from 模块名 import *`来导入所有的成员，但是并不推荐，很容易造成命名冲突。

## import 模块名 as 别名

```python
# 导入整个sys模块
import sys
print(sys.argv[0])

# 导入sys模块并命别名
import sys as s
print(s.argv[0])

# 同时导入两个模块
import sys, os
print(sys.argv[0])
print(os.sep)

# 同时导入两个模块，分别命别名
import sys as s, os as o
print(s.argv[0])
print(o.sep)
```

## from 模块名 import 成员名 as 别名

```python
# 导入sys模块的argv成员
from sys import argv
# 使用导入成员的语法，直接使用成员名访问
print(argv[0])

# 导入sys模块的argv成员，并为其指定别名v
from sys import argv as v
# 使用导入成员（并指定别名）的语法，直接使用成员的别名访问
print(v[0])

# 导入sys模块的argv,winver成员
from sys import argv, winver
# 使用导入成员的语法，直接使用成员名访问
print(argv[0])
print(winver)

# 导入sys模块的argv,winver成员，并为其指定别名v、wv
from sys import argv as v, winver as wv
# 使用导入成员（并指定别名）的语法，直接使用成员的别名访问
print(v[0])
print(wv)
```