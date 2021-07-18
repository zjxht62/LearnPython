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
一是结合使用程序Tidy(一个Python库)和XHTML解析;  
二是使用专为屏幕抓取而设计的Beautiful Soup库。