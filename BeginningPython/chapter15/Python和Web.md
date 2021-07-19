# Python和Web
## 15.1 屏幕抓取
屏幕抓取，其实就类似爬虫，把网页保存下来，并通过一定手段提取需要的信息。  
概念上说，这种技术非常简单：下载数据并对其进行分析。例如使用`urllib`来获取网页的HTML代码，之后用`re`
正则表达式来匹配有用的信息。  
举例：要从Python Job Board(http://python.org/jobs) 提取招聘单位的名称和网站。通过查看该网页的源代码，你发现可在类似于下面的链接中找到名称和URL:
```text
<a href="/jobs/1970/">Python Engineer</a>
```
可以使用下面的代码来获取有用的信息
```python
from urllib.request import urlopen
import re
p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text = urlopen('https://www.python.org/jobs/').read().decode()
# findall返回一个列表，里面每个元素是元组，表示每一个group的内容
for url, name in p.findall(text):
    print('{} ({})'.format(name, url))
```
但是上面的代码也有一些缺点：
1. 正则表达式不好理解。如果HTML较为复杂，还需要编写更加复杂的正则表达式
2. 处理不了独特的HTML内容，如CDATA部分和字符实体(如&amp;)。遇到这样的东西时，这个程序很可能束手无策。

正则表达式依赖HTML代码的细节，而不是其抽象结构。如果结构细微改变，可能就会运行失败。
基于上面提到的使用正则表达式的问题，接下来讨论两种可能的解决方案。  
一是结合使用程序Tidy(一个Python库)和XHTML解析;二是使用专为屏幕抓取而设计的Beautiful Soup库。

### 15.1.1 Tidy和XHTML解析
Python标准库提供了解析HTML和XML等结构化格式的支持。XHTML是HTML5规范描述的两种具体语法之一，
也是一种XML格式。  
如果HTML是规范的，那么解析就会比较简单。但是浏览器对那些不太严谨的HTML也可以尽力渲染出来。
但是，对于解析HTML来说就不那么友好了。  
标准库提供的通用HTML解析方法是基于事件的：用户编写事件处理程序，供解析程序处理数据时调用。
但是对于不严谨的HTML，无法基于文档结构来提取数据。这时可以使用Tidy。
1. Tidy是什么  
    Tidy是用来修复不严谨的HTML的工具。它还提供极大的配置空间，可以灵活开关各种校正。  
    虽然， Tidy并不能修复HTML文件存在的所有问题，但确实能够确保文件是格式良好的（即
    所有元素都嵌套正确），这让解析工作容易得多。
   
2. 获取Tidy  
    可以使用Tidy包装器`pip install pytidylib`  
    也可以通过Tidy官网获取可执行的二进制版本(下载链接：https://github.com/htacg/tidy-html5/releases/download/5.8.0/tidy-5.8.0-win64.zip 下载之后解压将bin文件夹里的tidy.exe和Python脚本放在同一目录下），通过模块subprocess来运行Tidy程序。
   
```python
from subprocess import Popen, PIPE
text = open('messy.html').read()
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)

tidy.stdin.write(text.encode())
tidy.stdin.close()

print(tidy.stdout.read().decode())
```
3. 为何使用XHTML  
    XHTML非常严格，要求显示得结束所有元素。另一个优点是，他是一种XML方言，可以使用各种出色的工具（如XPath）来处理，
   
4. 使用HTMLParser  
    使用HTMLParser意味着要继承它，并重写各种事件处理方法，如handle_starttag和handle_data。
    下表概述了相关的方法以及解析器什么时候自动调用他们

|回调方法|何时被使用|
|---|---|
|handle_starttag(tag, attrs)|遇到开始标签时调用。 attrs是一个由形如(name, value)的元组组成的序列|
|handle_startendtag(tag, attrs)|遇到空标签时调用。默认分别处理开始标签和结束标签|
|handle_endtag(tag)|遇到结束标签时调用|
|handle_data(data)|遇到文本数据时调用|
|handle_charref(ref)|遇到形如&#ref;的字符引用时调用|
|handle_entityref(name)|遇到形如&name;的实体引用时调用|
|handle_comment(data)|遇到注释时；只对注释内容调用|
|handle_decl(decl)|遇到形如<!...>的声明时调用|
|handle_pi(data)|用于处理指令|
|unknown_decl(data)|遇到未知声明时调用|

通常无需实现所有的解析器回调方法，也可能无需创建整个文档的抽象表示就能找到内容。只需跟踪找到目标内容所需的信息就可以了。  
下面的代码演示了使用HTMLParser提取网页信息的过程
```python

```