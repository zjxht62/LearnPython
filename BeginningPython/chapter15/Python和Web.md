# Python和Web

## 15.1 屏幕抓取

屏幕抓取，其实就类似爬虫，把网页保存下来，并通过一定手段提取需要的信息。  
概念上说，这种技术非常简单：下载数据并对其进行分析。例如使用`urllib`来获取网页的HTML代码，之后用`re`
正则表达式来匹配有用的信息。  
举例：要从Python Job Board(http://python.org/jobs)
提取招聘单位的名称和网站。通过查看该网页的源代码，你发现可在类似于下面的链接中找到名称和URL:

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

Python标准库提供了解析HTML和XML等结构化格式的支持。XHTML是HTML5规范描述的两种具体语法之一， 也是一种XML格式。  
如果HTML是规范的，那么解析就会比较简单。但是浏览器对那些不太严谨的HTML也可以尽力渲染出来。 但是，对于解析HTML来说就不那么友好了。  
标准库提供的通用HTML解析方法是基于事件的：用户编写事件处理程序，供解析程序处理数据时调用。
但是对于不严谨的HTML，无法基于文档结构来提取数据。这时可以使用Tidy。

1. Tidy是什么  
   Tidy是用来修复不严谨的HTML的工具。它还提供极大的配置空间，可以灵活开关各种校正。  
   虽然， Tidy并不能修复HTML文件存在的所有问题，但确实能够确保文件是格式良好的（即 所有元素都嵌套正确），这让解析工作容易得多。

2. 获取Tidy  
   可以使用Tidy包装器`pip install pytidylib`  
   也可以通过Tidy官网获取可执行的二进制版本(
   下载链接：https://github.com/htacg/tidy-html5/releases/download/5.8.0/tidy-5.8.0-win64.zip
   下载之后解压将bin文件夹里的tidy.exe和Python脚本放在同一目录下），通过模块subprocess来运行Tidy程序。

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
from urllib.request import urlopen
from html.parser import HTMLParser


# 判断是否是工作，href属性的值
def isjob(url):
    try:
        a, b, c, d = url.split('/')
    except ValueError:
        return False
    return a == d == '' and b == 'jobs' and c.isdigit()


class Scraper(HTMLParser):
    # 跟踪是否处于一个链接中
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        url = attrs.get('href', '')
        if tag == 'a' and isjob(url):
            self.url = url
            self.in_link = True
            self.chunks = []

    # 不是假定通过调用handle_data一次就能获得所需的所有文本，而是假定这些文本分成多个块，需要多次调用handle_data才能获得。
    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self.in_link:
            print('{} ({})'.format(''.join(self.chunks), self.url))
            self.in_link = False


text = urlopen('https://www.python.org/jobs/').read().decode()
parser = Scraper()
parser.feed(text)
parser.close()
```

与正则表达式相比，它的健壮性更强，但是代码逻辑更为复杂。

### 15.1.2 BeautifulSoup

BeautifulSoup模块可以帮你解析不那么严谨的HTML。  
可以通过`pip install beautifulsoup4`安装

```python
# 使用Beautiful Soup的屏幕抓取程序
from urllib.request import urlopen
from bs4 import BeautifulSoup

text = urlopen('http://python.org/jobs').read()
soup = BeautifulSoup(text, 'html.parser')

# 使用soup.body来获取文档体，再访问其中的第一个section。使用参数'h2' 调用返回的对象，这与使用其方法find_all等效——返回其中的所有h2元素。
jobs = set()
for job in soup.body.section('h2'):
    # 每个h2元素都表示 一个职位，而我感兴趣的是它包含的第一个链接job.a。属性string是链接的文本内容，而a['href'] 为属性href。
    jobs.add('{} ({})'.format(job.a.string, job.a['href']))

print('\n'.join(sorted(jobs, key=str.lower)))
```

## 15.2 使用CGI创建动态网页

CGI代表通用网关接口（Common Gateway
Interface），它是一种标准机制。Web服务器可通过它将查询交给专门的程序（比如自己编写的Python程序）， 并以网页的方式显示查询结果。  
Python CGI编程的关键工具是模块cgi，另一个对开发CGI脚本很有帮助的模块是cgitb。  
要让CGI脚本能够通过Web进行访问（和运行），必须将其放在Web服务器能够访问的地方、添加!#行并设置合适的文件权限。

### 15.2.1 第一步：准备Web服务器

一般来说，要想将内容发布到Web服务器，只需要将网页，图片等资源放到特定的目录下（如tomcat的webapp）  
这里我们只是想尝试使用CGI，所有使用模块http.server运行一个临时的Web服务器。可通过向Python可执行文件提供开关-m来导入并运行这个模块。如果同时
指定了--cgi，启动的服务器将支持CGI。这个服务器将提供它运行时所在目录中的文件，因此要保证目录中不要有敏感内容。

```shell
python -m http.server --cgi
```

CGI程序也必须放在可通过Web访问的目录中。另外，**必须将它标识为CGI脚本**，以免Web服务器以网页的方式提供其源代码。 为此，有两种常见的方式：

+ 将脚本放在子目录cgi-bin中
+ 将脚本文件的扩展名指定为.cgi

### 15.2.2 第二步：添加!#行

将文件放到正确的位置之后，还需要添加!#行。通过添加!#行，无需显式的执行Python解释器就可以执行脚本。 这对CGI至关重要，因为如果没有!#行，
Web服务器将不知道如何执行脚本。  
举例：linux

```python
#!/usr/bin/env python
```

举例：windows

```python
#!E:\Programs\Python\Python38-32\python.exe
```

### 15.2.3 第三步：设置文件权限

最后一件事是设置合适的文件权限。必须确保任何人都可以读取和执行你的脚本文件，同时只有你才能写入。  
在UNIX中，修改文件权限（或文件模式）的命令为chmod。要修改文件权限，只需通过普通用户账户或专为完成Web任务而建立的账户执行下面的命令

```shell
chmod 755 somescript.cgi
```

通常，CGI脚本不能修改计算机上的任何文件。要让它能够修改文件，必须显式地赋予它权限。  
为此，有两种选择：如果有root（系统管理员）权限，可为脚本专门创建一个用户账户，
并调整需要修改的文件的所有者；如果没有root权限，可设置该文件的文件权限，
让系统中的所有用户（包括Web服务器用来运行CGI脚本的账户）都能写入这个文件。要设置这样的文件权限， 可使用如下命令：

```shell
chomd 666 editable_file.txt
```

### 15.2.4 CGI安全风险

使用CGI程序存在一些安全风险。如果允许CGI脚本写入文件，那么可能被人利用来破坏数据。  
同样， 如果直接将用户提供的数据作为Python代码（如使用exec或eval）或shell代码（如使用os.system或subprocess）执行，
就可能执行恶意命令，进而面临极大风险。  
即便在SQL查询中使用用户提供的字符串也很危险，除非你预先仔细审查这些字符串。 SQL注入是一种常见的攻击系统的方式。

### 15.2.5简单的CGI脚本

将下列脚本放在cgi-bin目录下

```python
#!E:\Programs\Python\Python38-32\python.exe

print('Content-type: text/plain')
print()  # 打印一个空行，以结束首部

print('Hello, world')
```

访问网页`http://127.0.0.1:8000/cgi-bin/simple1.py` 可以看到输出的Hello, world。  
这个程序写入到标准输出的内容都将出现在网页中。首先打印的是HTTP首部，包含有关网页的信息。 这里使用`Content-type: text/plain`
指定网页是纯文本的。打印完首部之后，打印了一个空行， 接下来为文档本身，这里只包含字符串`'Hello, world'`。

### 15.2.6 使用cgitb进行调试

如果CGI程序出错，可能导致Web服务器显示毫无帮助的错误信息。如果能查看服务器日志的话，可能还能找到些线索。
其实，标准库为了帮助调试CGI脚本，提供了一个有用的模块`cgitb`（用于CGI栈跟踪）。通过导入这个模块，并调用其中的函数`enable`，
可显示一个很有用的网页，其中包含有关什么地方出了问题的信息。

```python
#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9


import cgitb;

cgitb.enable()
print('Content-type:text/html\n')
print(1 / 0)
print('Hello, world!')
```

### 15.2.7 使用模块cgi

之前的demo都只是输出。输入是通过HTML表单以键值对的方式提供给CGI脚本的。可以使用模块cgi中的FieldStorage类来获取这些字段。
当你创建FiledStorage实例（应该只创建一个）时，他将从请求中取回输入变量，并通过类似字典的接口将它们提供给脚本。 要访问
FieldStorage中的值，可通过普通的键查找，但出于一些技术原因(与文件上传相关，这里不讨 论)，FieldStorage的元素并不是你要的值。
例如，即便你知道请求包含一个名为name的值，也不能像下面这样做:

```python
form = cgi.FieldStorage()
name = form['name']
```

而必须这样：

```python
form = cgi.FieldStorage()
name = form['name'].value
```

更简单的获取值的方式是使用方法getvalue。它类似于字典的方法get，但返回项目的value属性的值，如下所示:

```python
form = cgi.FieldStorage()
name = form.getvalue('name', 'Unknown')
```

举例：从FieldStorage中获取单个值的CGI脚本

```python
#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9

import cgi

form = cgi.FieldStorage()

name = form.getvalue('name', 'world')
print('Content-type:text/html\n')

print('Hello, {}!'.format(name))

```

通过浏览器访问`http://127.0.0.1:8000/cgi-bin/simple2.py?name=zjx`输出结果`Hello, zjx!`

### 15.2.8 简单的表单

> 从CGI脚本中获取信息主要有两种方式：GET和POST。大致上，GET用于获取信息并在URL中进行查询编码，而POST可用于任何类型的查询，
> 但对查询进行编码的方式稍有不同。

示例：包含HTML表单的问候脚本

```python
#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9

import cgi

form = cgi.FieldStorage()

name = form.getvalue('name', 'world')
print("""Content-type: text/html

<html> <head>
<title>Greeting Page</title> </head>
<body>
<h1>Hello, {}!</h1>
<p>下面这行意味着提交表单，将再次执行simple3.py脚本</p>
<form action='simple3.py'>
Change name <input type='text' name='name' /> <input type='submit' />
</form>
</body> </html>
""".format(name))
```

## 15.3 使用Web框架

Python中有很多Web框架，像Flask，Django等。下面用Flask做个示例。  
首先安装`pip install flask`  
假设有一个计算幂的函数。

```python
def powers(n=10):
    return ', '.join(str(2 ** i) for i in range(n))
```

使用Flask

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def powers(n=10):
    return ', '.join(str(2 ** i) for i in range(n))
```

运行Flask

```shell
$ export FLASK_APP=powers.py
$ flask run
```

可以通过下面的形式传值

```python
# 默认获取的是str类型，可以在获取时执行转换
@app.route('/<int:n>')
def powers2(n=10):
    return ', '.join(str(2 ** i) for i in range(n))


# http://127.0.0.1:5000/5
# 1, 2, 4, 8, 16

@app.route('/input/<s>')
def getInput(s='hello'):
    return "获取到的输入是:{}".format(s)

# http://127.0.0.1:5000/input/hahd
# 获取到的输入是:hahd
```

#### 其他Web框架

还有很多其他的Web框架。下面是几个比较流行的框架。

|名称|网站|
|---|---|
|Django|https://djangoproject.com|
|TurboGears| http://turbogears.org|
|web2py|http://web2py.com|
|Grok|https://pypi.python.org/pypi/grok|
|Zope2|https://pypi.python.org/pypi/Zope2|
|Pyramid|https://trypyramid.com|

## 15.4 Web服务：更高级的抓取
Web服务相比网页更加抽象。它将HTTP作为底层协议，使用更为面向内容的协议（如XML，Json）来对请求和响应进行编码。
