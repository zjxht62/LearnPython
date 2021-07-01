import sys
#导入这个模块时，执行了其中的代码。但如果再次导入它，什么事情都不会发生。
# 因为模块并不是用来执行操作的，而是用于定义变量、函数、类等。由于定义只需要一次，所以导入模块多次和导入一次效果相同
import hello
import re
import os

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
# ['Error', 'copy', 'deepcopy', 'dispatch_table', 'error']
#变量__all__
#它告诉解释器从这个模块导入所有的名称意味着什么
print(copy.__all__)
# ['Error', 'copy', 'deepcopy']

#10.2.2 使用help获取帮助
print(help(copy.copy))

#10.2.3 文档
print(range.__doc__)

#使用源代码
print(copy.__file__)

print(sys.modules)
# {'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, '_imp': <module '_imp' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'nt': <module 'nt' (built-in)>, '_thread': <module '_thread' (built-in)>, '_weakref': <module '_weakref' (built-in)>, 'winreg': <module 'winreg' (built-in)>, 'time': <module 'time' (built-in)>, 'zipimport': <module 'zipimport' (frozen)>, '_codecs': <module '_codecs' (built-in)>, 'codecs': <module 'codecs' from 'E:\\Programs\\Python\\Python38-32\\lib\\codecs.py'>, 'encodings.aliases': <module 'encodings.aliases' from 'E:\\Programs\\Python\\Python38-32\\lib\\encodings\\aliases.py'>, 'encodings': <module 'encodings' from 'E:\\Programs\\Python\\Python38-32\\lib\\encodings\\__init__.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from 'E:\\Programs\\Python\\Python38-32\\lib\\encodings\\utf_8.py'>, '_signal': <module '_signal' (built-in)>, '__main__': <module '__main__' from 'E:/zjx/PycharmProjects/LearnPython/BeginningPython/chapter10/chapter10.py'>, 'encodings.latin_1': <module 'encodings.latin_1' from 'E:\\Programs\\Python\\Python38-32\\lib\\encodings\\latin_1.py'>, '_abc': <module '_abc' (built-in)>, 'abc': <module 'abc' from 'E:\\Programs\\Python\\Python38-32\\lib\\abc.py'>, 'io': <module 'io' from 'E:\\Programs\\Python\\Python38-32\\lib\\io.py'>, '_stat': <module '_stat' (built-in)>, 'stat': <module 'stat' from 'E:\\Programs\\Python\\Python38-32\\lib\\stat.py'>, 'genericpath': <module 'genericpath' from 'E:\\Programs\\Python\\Python38-32\\lib\\genericpath.py'>, 'ntpath': <module 'ntpath' from 'E:\\Programs\\Python\\Python38-32\\lib\\ntpath.py'>, 'os.path': <module 'ntpath' from 'E:\\Programs\\Python\\Python38-32\\lib\\ntpath.py'>, '_collections_abc': <module '_collections_abc' from 'E:\\Programs\\Python\\Python38-32\\lib\\_collections_abc.py'>, 'os': <module 'os' from 'E:\\Programs\\Python\\Python38-32\\lib\\os.py'>, '_sitebuiltins': <module '_sitebuiltins' from 'E:\\Programs\\Python\\Python38-32\\lib\\_sitebuiltins.py'>, '_locale': <module '_locale' (built-in)>, '_bootlocale': <module '_bootlocale' from 'E:\\Programs\\Python\\Python38-32\\lib\\_bootlocale.py'>, '_codecs_cn': <module '_codecs_cn' (built-in)>, '_multibytecodec': <module '_multibytecodec' (built-in)>, 'encodings.gbk': <module 'encodings.gbk' from 'E:\\Programs\\Python\\Python38-32\\lib\\encodings\\gbk.py'>, 'types': <module 'types' from 'E:\\Programs\\Python\\Python38-32\\lib\\types.py'>, 'importlib._bootstrap': <module 'importlib._bootstrap' (frozen)>, 'importlib._bootstrap_external': <module 'importlib._bootstrap_external' (frozen)>, 'warnings': <module 'warnings' from 'E:\\Programs\\Python\\Python38-32\\lib\\warnings.py'>, 'importlib': <module 'importlib' from 'E:\\Programs\\Python\\Python38-32\\lib\\importlib\\__init__.py'>, 'importlib.machinery': <module 'importlib.machinery' from 'E:\\Programs\\Python\\Python38-32\\lib\\importlib\\machinery.py'>, 'importlib.abc': <module 'importlib.abc' from 'E:\\Programs\\Python\\Python38-32\\lib\\importlib\\abc.py'>, '_operator': <module '_operator' (built-in)>, 'operator': <module 'operator' from 'E:\\Programs\\Python\\Python38-32\\lib\\operator.py'>, 'keyword': <module 'keyword' from 'E:\\Programs\\Python\\Python38-32\\lib\\keyword.py'>, '_heapq': <module '_heapq' (built-in)>, 'heapq': <module 'heapq' from 'E:\\Programs\\Python\\Python38-32\\lib\\heapq.py'>, 'itertools': <module 'itertools' (built-in)>, 'reprlib': <module 'reprlib' from 'E:\\Programs\\Python\\Python38-32\\lib\\reprlib.py'>, '_collections': <module '_collections' (built-in)>, 'collections': <module 'collections' from 'E:\\Programs\\Python\\Python38-32\\lib\\collections\\__init__.py'>, '_functools': <module '_functools' (built-in)>, 'functools': <module 'functools' from 'E:\\Programs\\Python\\Python38-32\\lib\\functools.py'>, 'contextlib': <module 'contextlib' from 'E:\\Programs\\Python\\Python38-32\\lib\\contextlib.py'>, 'importlib.util': <module 'importlib.util' from 'E:\\Programs\\Python\\Python38-32\\lib\\importlib\\util.py'>, 'zope': <module 'zope' (namespace)>, 'enum': <module 'enum' from 'E:\\Programs\\Python\\Python38-32\\lib\\enum.py'>, '_sre': <module '_sre' (built-in)>, 'sre_constants': <module 'sre_constants' from 'E:\\Programs\\Python\\Python38-32\\lib\\sre_constants.py'>, 'sre_parse': <module 'sre_parse' from 'E:\\Programs\\Python\\Python38-32\\lib\\sre_parse.py'>, 'sre_compile': <module 'sre_compile' from 'E:\\Programs\\Python\\Python38-32\\lib\\sre_compile.py'>, 'copyreg': <module 'copyreg' from 'E:\\Programs\\Python\\Python38-32\\lib\\copyreg.py'>, 're': <module 're' from 'E:\\Programs\\Python\\Python38-32\\lib\\re.py'>, 'token': <module 'token' from 'E:\\Programs\\Python\\Python38-32\\lib\\token.py'>, 'tokenize': <module 'tokenize' from 'E:\\Programs\\Python\\Python38-32\\lib\\tokenize.py'>, 'linecache': <module 'linecache' from 'E:\\Programs\\Python\\Python38-32\\lib\\linecache.py'>, 'traceback': <module 'traceback' from 'E:\\Programs\\Python\\Python38-32\\lib\\traceback.py'>, 'sitecustomize': <module 'sitecustomize' from 'E:\\Program Files\\JetBrains\\PyCharm 2021.1.2\\plugins\\python\\helpers\\pycharm_matplotlib_backend\\sitecustomize.py'>, 'site': <module 'site' from 'E:\\Programs\\Python\\Python38-32\\lib\\site.py'>, 'hello': <module 'hello' from 'E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10\\hello.py'>, 'hello2': <module 'hello2' from 'E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10\\hello2.py'>, 'hello3': <module 'hello3' from 'E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10\\hello3.py'>, 'pprint': <module 'pprint' from 'E:\\Programs\\Python\\Python38-32\\lib\\pprint.py'>, 'constants': <module 'constants' from 'E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10\\constants\\__init__.py'>, 'constants.haha': <module 'constants.haha' from 'E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10\\constants\\haha.py'>, 'constants.heihei': <module 'constants.heihei' from 'E:\\zjx\\PycharmProjects\\LearnPython\\BeginningPython\\chapter10\\constants\\heihei.py'>, '_weakrefset': <module '_weakrefset' from 'E:\\Programs\\Python\\Python38-32\\lib\\_weakrefset.py'>, 'weakref': <module 'weakref' from 'E:\\Programs\\Python\\Python38-32\\lib\\weakref.py'>, 'copy': <module 'copy' from 'E:\\Programs\\Python\\Python38-32\\lib\\copy.py'>, '_opcode': <module '_opcode' (built-in)>, 'opcode': <module 'opcode' from 'E:\\Programs\\Python\\Python38-32\\lib\\opcode.py'>, 'dis': <module 'dis' from 'E:\\Programs\\Python\\Python38-32\\lib\\dis.py'>, 'collections.abc': <module 'collections.abc' from 'E:\\Programs\\Python\\Python38-32\\lib\\collections\\abc.py'>, 'inspect': <module 'inspect' from 'E:\\Programs\\Python\\Python38-32\\lib\\inspect.py'>, 'pkgutil': <module 'pkgutil' from 'E:\\Programs\\Python\\Python38-32\\lib\\pkgutil.py'>, 'platform': <module 'platform' from 'E:\\Programs\\Python\\Python38-32\\lib\\platform.py'>, 'urllib': <module 'urllib' from 'E:\\Programs\\Python\\Python38-32\\lib\\urllib\\__init__.py'>, 'urllib.parse': <module 'urllib.parse' from 'E:\\Programs\\Python\\Python38-32\\lib\\urllib\\parse.py'>, 'pydoc': <module 'pydoc' from 'E:\\Programs\\Python\\Python38-32\\lib\\pydoc.py'>}

print(sys.platform)  # win32

print(os.environ)
# environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'ANDROID_HOME': 'E:\\android-sdk-windows', 'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming', 'CATALINA_BASE': 'E:\\apache-tomcat-9.0.2', 'CATALINA_HOME': 'E:\\apache-tomcat-9.0.2', 'CHOCOLATEYINSTALL': 'C:\\ProgramData\\chocolatey', 'CHOCOLATEYLASTPATHUPDATE': '132560301740133164', 'CIRRUS_UNINSTALL_EXE': 'E:\\Program Files\\DLP\\dlp3.0\\unins000.exe', 'CLASSPATH': '.;C:\\Program Files\\Java\\jdk1.8.0_241\\lib\\dt.jar;C:\\Program Files\\Java\\jdk1.8.0_241\\lib\\tools.jar;', 'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-RMO2H0L', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'ERLANG_HOME': 'E:\\Program Files\\erl10.3', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Administrator', 'IDEA_INITIAL_DIRECTORY': 'E:\\Program Files\\JetBrains\\PyCharm 2021.1.2\\bin', 'INTELLIJ IDEA': 'E:\\Program Files\\JetBrains\\IntelliJ IDEA 2020.2.4\\bin;', 'ITEST_HOME': 'E:\\itestInstalDir\\itest', 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk1.8.0_241', 'JMETER_HOME': 'E:\\zjx\\Jmeter\\Jmeter', 'LANG': 'zh_CN', 'LOCALAPPDATA': 'C:\\Users\\Administrator\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-RMO2H0L', 'MAVEN_HOME': 'E:\\apache-maven-3.0.5', 'MOZ_PLUGIN_PATH': 'E:\\PROGRAM FILES (X86)\\FOXIT SOFTWARE\\FOXIT READER\\plugins\\', 'NUMBER_OF_PROCESSORS': '4', 'NVM_HOME': 'C:\\Users\\Administrator\\AppData\\Roaming\\nvm', 'NVM_SYMLINK': 'E:\\Program Files\\nodejs', 'ONEDRIVE': 'C:\\Users\\Administrator\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;E:\\Program Files\\Git\\bin;E:\\Program Files\\TortoiseGit\\bin;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;E:\\apache-maven-3.0.5\\bin\\;E:\\android-sdk-windows\\platform-tools;E:\\android-sdk-windows\\tools;E:\\MinGW\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\npm;E:\\Program Files\\erl10.3\\bin;E:\\aliyun;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Java\\jdk1.8.0_241\\bin;C:\\Program Files\\Java\\jdk1.8.0_241\\jre\\bin;C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin;E:\\zjx\\Jmeter\\Jmeter\\bin;C:\\ProgramData\\chocolatey\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\nvm;E:\\Program Files\\nodejs;E:\\allure-2.13.8\\bin;C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\;C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\;E:\\Programs\\Python\\Python38-32\\Scripts\\;E:\\Programs\\Python\\Python38-32\\;C:\\Program Files\\MySQL\\MySQL Shell 8.0\\bin\\;C:\\Users\\Administrator\\AppData\\Local\\Microsoft\\WindowsApps;E:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Users\\Administrator\\AppData\\Local\\Programs\\Fiddler;E:\\Program Files (x86)\\Atmel\\Flip 3.4.7\\bin;C:\\Users\\Administrator\\AppData\\Local\\Microsoft\\WindowsApps;E:\\Program Files\\JetBrains\\IntelliJ IDEA 2020.2.4\\bin;;C:\\Users\\Administrator\\AppData\\Roaming\\nvm;E:\\Program Files\\nodejs;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW', 'PROCESSOR_ARCHITECTURE': 'x86', 'PROCESSOR_ARCHITEW6432': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 142 Stepping 9, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '8e09', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files (x86)', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules\\;C:\\Program Files\\Intel\\;C:\\Program Files\\Intel\\Wired Networking\\', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'E:\\zjx\\PycharmProjects\\LearnPython;E:\\Program Files\\JetBrains\\PyCharm 2021.1.2\\plugins\\python\\helpers\\pycharm_matplotlib_backend;E:\\Program Files\\JetBrains\\PyCharm 2021.1.2\\plugins\\python\\helpers\\pycharm_display', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'ULTRAMON_LANGDIR': 'C:\\Program Files\\UltraMon\\Resources\\cn', 'USERDOMAIN': 'DESKTOP-RMO2H0L', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-RMO2H0L', 'USERNAME': 'Administrator', 'USERPROFILE': 'C:\\Users\\Administrator', 'VS140COMNTOOLS': 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\Common7\\Tools\\', 'WINDIR': 'C:\\WINDOWS'})

# 获取名为JAVA_HOME的环境变量
print(os.environ['JAVA_HOME'])
# C:\Program Files\Java\jdk1.8.0_241

print(repr(os.sep))  # '\\'
