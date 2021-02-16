import sys
#导入这个模块时，执行了其中的代码。但如果再次导入它，什么事情都不会发生。
# 因为模块并不是用来执行操作的，而是用于定义变量、函数、类等。由于定义只需要一次，所以导入模块多次和导入一次效果相同
import hello

#可以告诉解释器去哪里能查找到这个模块
sys.path.append('C:/python')

#10.1.2 模块是用来下定义的
#模块像类一样，有自己的作用域。意味着在模块中定义的类和函数以及对其进行赋值的变量都将成为模块的属性

#1.在模块中定义函数
import hello2
hello2.hello()

#2.在模块中添加测试代码
import hello3
hello3.hello()

# 10.1.3 让模块可用
#1.将模块放在正确的位置
# 打印所有能找到模块的路径
# 虽然放在这里显示
# 的任何一个位置中都可行，但目录site-packages是最佳的选择，因为它就是用来放置模块的
import pprint
pprint.pprint(sys.path)

#2. 告诉解释器到哪里去找
# 这么做的原因
# 不希望Python解释器的目录中充斥着你编写的模块。
# 没有必要的权限，无法将文件保存到Python解释器的目录中。
# 想将模块放在其他地方。

#要告诉解释器到哪里去查找模块，办法之一是直接修改sys.path，但这种做法不常见。标准做法是将模块所在的目录包含在环境变量PYTHONPATH中

#10.1.4 包
#可以通过包来组织模块
#要让Python视为包，目录中需要包含文件__init__.py,文件__init__.py的内容就是包的内容
import constants
constants.packageFunction()
#constants.haha.say() # 非法，因为__init__.py里面没有haha这个属性

#引用包里的模块
import constants.haha
from constants import heihei
constants.haha.say()
heihei.say()

# 10.2探索模块
# 10.2.1模块包含什么
import copy
#使用dir，列出对象的所有属性，通过列表推导式可以过滤掉非外部使用的
print([n for n in dir(copy) if not n.startswith("_")])

#变量__all__
#它告诉解释器从这个模块导入所有的名称意味着什么
print(copy.__all__)

#10.2.2 使用help获取帮助
print(help(copy.copy))

#10.2.3 文档
print(range.__doc__)

#使用源代码
print(copy.__file__)